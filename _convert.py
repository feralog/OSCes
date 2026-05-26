#!/usr/bin/env python3
import re, os, glob as globmod

BASE = "D:/Arquivos/Documentos/Faculdade/OSEC/Github/OSCes/osce_materiais"
TEMPLATE_PATH = "D:/Arquivos/Documentos/Faculdade/OSEC/Github/OSCes/_template.html"

def inline(text):
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*([^*\n]+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    return text

def render_table(rows):
    if not rows: return ''
    out = ['<div class="table-wrap"><table>']
    header_done = False
    for row in rows:
        if re.match(r'^\|[\s\-|:]+\|$', row.strip()):
            continue
        cells = [c.strip() for c in row.strip().strip('|').split('|')]
        if not header_done:
            out.append('<thead><tr>' + ''.join('<th>' + inline(c) + '</th>' for c in cells) + '</tr></thead><tbody>')
            header_done = True
        else:
            out.append('<tr>' + ''.join('<td>' + inline(c) + '</td>' for c in cells) + '</tr>')
    out.append('</tbody></table></div>')
    return '\n'.join(out)

def md_to_html(text):
    lines = text.split('\n')
    out = []
    i = 0
    n = len(lines)
    list_buf = []
    list_kind = None
    table_buf = []
    in_table = False

    def flush_list():
        nonlocal list_buf, list_kind
        if not list_buf: return
        if list_kind == 'check':
            total = len([x for x in list_buf if '<input' in x])
            prog = ('<div class="check-progress"><span class="prog-text">0/' +
                    str(total) + ' marcados</span></div>') if total else ''
            out.append('<div class="checklist">' + ''.join(list_buf) + prog + '</div>')
        elif list_kind == 'ul':
            out.append('<ul>' + ''.join(list_buf) + '</ul>')
        elif list_kind == 'ol':
            out.append('<ol>' + ''.join(list_buf) + '</ol>')
        list_buf.clear()
        list_kind = None

    def flush_table():
        nonlocal table_buf, in_table
        if table_buf:
            out.append(render_table(table_buf))
        table_buf.clear()
        in_table = False

    while i < n:
        raw = lines[i]
        s = raw.strip()

        if not s:
            flush_list()
            flush_table()
            i += 1
            continue

        if s.startswith('|'):
            flush_list()
            in_table = True
            table_buf.append(s)
            i += 1
            continue
        if in_table:
            flush_table()

        if re.match(r'^-{3,}$', s) or re.match(r'^\*{3,}$', s):
            flush_list()
            out.append('<hr>')
            i += 1
            continue

        m = re.match(r'^(#{1,6})\s+(.+)$', s)
        if m:
            flush_list()
            lvl = len(m.group(1))
            content = inline(m.group(2))
            cls = 'section-heading'
            if lvl == 1:
                cls = 'page-h1'
            out.append('<h' + str(lvl) + ' class="' + cls + '">' + content + '</h' + str(lvl) + '>')
            i += 1
            continue

        if s.startswith('>'):
            flush_list()
            content = s[1:].strip()
            if re.search(r'[Rr]esposta\s+esperada', content):
                out.append('<div class="answer-block">' + inline(content) + '</div>')
            elif re.search(r'(Especialidade|Método)', content):
                out.append('<p class="eyebrow-meta">' + inline(content) + '</p>')
            else:
                out.append('<blockquote>' + inline(content) + '</blockquote>')
            i += 1
            continue

        m = re.match(r'^[-*]\s+\[([ xX])\]\s+(.+)$', s)
        if m:
            if list_kind != 'check':
                flush_list()
                list_kind = 'check'
            chk = ' checked' if m.group(1).lower() == 'x' else ''
            content = m.group(2)
            subs = []
            while i+1 < n and (lines[i+1].startswith('  ') or lines[i+1].startswith('\t')):
                i += 1
                sub = lines[i].strip()
                if re.match(r'^[-*]\s+', sub):
                    subs.append('<li>' + inline(sub[2:]) + '</li>')
                else:
                    subs.append('<span class="check-note">' + inline(sub) + '</span>')
            sub_html = ('<ul class="check-sub">' + ''.join(subs) + '</ul>') if subs else ''
            list_buf.append('<label class="check-item"><input type="checkbox"' + chk + '><span>' + inline(content) + sub_html + '</span></label>')
            i += 1
            continue

        m = re.match(r'^[-*]\s+(.+)$', s)
        if m:
            if list_kind != 'ul':
                flush_list()
                list_kind = 'ul'
            list_buf.append('<li>' + inline(m.group(1)) + '</li>')
            i += 1
            continue

        m = re.match(r'^(\d+)[.)]\s+(.+)$', s)
        if m:
            if list_kind != 'ol':
                flush_list()
                list_kind = 'ol'
            list_buf.append('<li>' + inline(m.group(2)) + '</li>')
            i += 1
            continue

        flush_list()
        para = [s]
        while i+1 < n:
            nxt = lines[i+1].strip()
            if (not nxt or nxt.startswith('#') or nxt.startswith('>') or
                    nxt.startswith('|') or re.match(r'^[-*\d]', nxt) or
                    re.match(r'^-{3,}$', nxt)):
                break
            i += 1
            para.append(lines[i].strip())
        content = ' '.join(para)
        fmt = inline(content)

        if re.match(r'.*\*\*\[PROFESSOR\]', content):
            out.append('<div class="professor-block">' + fmt + '</div>')
        elif re.match(r'^\*\*(Pergunta|Question)\s*\d*', content):
            out.append('<div class="question-label">' + fmt + '</div>')
        else:
            out.append('<p>' + fmt + '</p>')
        i += 1

    flush_list()
    flush_table()
    return '\n'.join(out)

with open(TEMPLATE_PATH, encoding='utf-8') as f:
    TEMPLATE = f.read()

def get_eyebrow(text, filepath):
    m = re.search(r'^>\s*(.+?)\s*\|\s*Método', text, re.MULTILINE)
    if m: return m.group(1).strip()
    path = filepath.replace('\\', '/')
    if '/GO/' in path: return 'GO · Ginecologia e Obstetrícia'
    if '/Pediatria/' in path: return 'Pediatria'
    if '/Nefro/' in path: return 'Clínica Médica · Nefrologia'
    if '/Endocrino/' in path: return 'Clínica Médica · Endocrinologia'
    if '/Gastro/' in path: return 'Clínica Médica · Gastroenterologia'
    if '/Hemato/' in path: return 'Clínica Médica · Hematologia'
    if '/Infecto/' in path: return 'Clínica Médica · Infectologia'
    if '/Cirurgia/' in path: return 'Cirurgia'
    return 'OSCE 2026'

def get_title(text):
    m = re.search(r'^#\s+(.+?)(?:\s*[—–-]+.*)?$', text, re.MULTILINE)
    if m: return m.group(1).strip()
    return 'Material OSCE'

def get_back(filepath):
    fp = filepath.replace('\\', '/').replace('D:/', 'D:/')
    base = "D:/Arquivos/Documentos/Faculdade/OSEC/Github/OSCes/osce_materiais"
    rel = fp[len(base):].lstrip('/')
    depth = rel.count('/')
    return '../' * depth + '../osce-plano.html'

def convert_file(md_path):
    with open(md_path, encoding='utf-8') as f:
        text = f.read()
    title = get_title(text)
    eyebrow = get_eyebrow(text, md_path)
    back = get_back(md_path)
    body = md_to_html(text)
    html = (TEMPLATE
            .replace('{{TITLE}}', title)
            .replace('{{EYEBROW}}', eyebrow)
            .replace('{{BACK}}', back)
            .replace('{{BODY}}', body))
    out_path = md_path.replace('.md', '.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print('OK  ' + os.path.basename(out_path))

md_files = globmod.glob(BASE + '/**/*.md', recursive=True)
print('Found ' + str(len(md_files)) + ' .md files...')
for f in md_files:
    try:
        convert_file(f)
    except Exception as e:
        print('ERR ' + f + ': ' + str(e))

print('\nDone: ' + str(len(md_files)) + ' files converted.')
