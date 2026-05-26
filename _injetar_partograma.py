"""
Injeta imagens do partograma nos arquivos GO/partograma.md e .html
"""
import os

BASE = r"D:/Arquivos/Documentos/Faculdade/OSEC/Github/OSCes"
REL_GO   = "../../../Complementos/imagens"   # de osce_materiais/GO/
REL_FLASH = "../../Complementos/imagens"      # de osce_materiais/flashcards/

def fig(fname, alt, caption, rel=REL_GO):
    return (
        f'\n<figure style="margin:22px 0;text-align:center">'
        f'<img src="{rel}/{fname}" alt="{alt}" '
        f'style="max-width:100%;border-radius:8px;border:1px solid #ddd;'
        f'box-shadow:0 2px 10px rgba(0,0,0,.1)">'
        f'<figcaption style="font-size:11px;color:#888;margin-top:6px;'
        f'font-family:system-ui,sans-serif;font-style:italic">{caption}</figcaption>'
        f'</figure>\n'
    )

def h2(text):
    return f'<h2 class="section-heading">{text}</h2>'

def patch(path, items):
    with open(path, encoding="utf-8") as f:
        txt = f.read()
    ok = 0
    for anchor, html in items:
        if anchor not in txt:
            print(f"  [MISS] {os.path.basename(path)}: '{anchor[:70]}'")
            continue
        txt = txt.replace(anchor, anchor + html, 1)
        ok += 1
    with open(path, "w", encoding="utf-8") as f:
        f.write(txt)
    print(f"  [OK]  {os.path.basename(path)}: {ok}/{len(items)}")

GO = f"{BASE}/osce_materiais/GO"

# ── Âncoras compartilhadas (mesmas no MD e no HTML) ──────────────
# No MD: "## ESTAÇÃO 1: ..."   No HTML: "<h2 class="section-heading">ESTAÇÃO 1: ..."

INTRO_IMGS = (
    fig("parto_pdf_aula_04_partograma_pg5_img1.png",
        "Curva de Friedman fase latencia vs ativa",
        "Curva de Friedman: Fase de Latência (até 4 cm) → Fase Ativa (aceleração → dilatação máxima → desaceleração → 2º período)")
    + fig("parto_pdf_aula_04_partograma_pg4_img1.png",
          "Partograma de Philpott linha de alerta e acao",
          "Partograma de Philpott: Linha de Alerta (traçado cruzando os quadrados diagonalmente) e Linha de Ação (4h à direita da linha de alerta)")
    + fig("parto_pdf_aula_04_partograma_pg3_img1.png",
          "Plano de De Lee escala pelve feto",
          "Plano de De Lee: espinha isquiática = plano 0. Acima: −1, −2, −3 (móvel). Abaixo: +1, +2, +3 (encravado). Vulva = +4")
    + fig("parto_pdf_aula_04_partograma_pg3_img2.png",
          "Variedades de posicao cefalica OA OT OP",
          "Variedades de posição: OA (occipito-anterior), OT (transversa), OP (posterior), com variantes direita (D) e esquerda (E)")
)

EST1_IMGS = (
    fig("parto_pdf_aula_04_partograma_pg5_img3.png",
        "Partograma preenchido caso fase ativa normal",
        "Partograma: caso de fase ativa normal — dilatação progressiva seguindo a linha de alerta, FCF estável, contrações regulares")
)

EST2_IMGS = (
    fig("parto_pdf_aula_04_partograma_pg6_img1.png",
        "Partograma parada secundaria de dilatacao DPC",
        "Partograma: parada de progressão — dilatação cruza linha de alerta e atinge linha de ação → indicação de conduta ativa (amniotomia/ocitocina/cesárea)")
)

EST3_IMGS = (
    fig("parto_pdf_aula_04_partograma_pg6_img2.png",
        "Partograma sofrimento fetal taquissistolia",
        "Partograma: taquissistolia e alteração de FCF — contrações >5 em 10 min + BCF alterado → conduta imediata (decúbito lateral, O₂, suspender ocitocina, cesárea de urgência)")
    + fig("parto_pdf_aula_04_partograma_pg7_img1.png",
          "Partograma caso parada com recuperacao",
          "Partograma adicional: progressão que cruza linha de alerta, com recuperação após intervenção — aprendizado de leitura dinâmica")
)

# ── MD ────────────────────────────────────────────────────────────
print("\n── partograma.md ──")
patch(f"{GO}/partograma.md", [
    ("## ESTAÇÃO 1: Fase Ativa Normal — Parto Eutócico", INTRO_IMGS + EST1_IMGS),
    ("## ESTAÇÃO 2: Parada Secundária de Dilatação — DPC", EST2_IMGS),
    ("## ESTAÇÃO 3: Sofrimento Fetal Agudo + Taquissistolia", EST3_IMGS),
])

# ── HTML ──────────────────────────────────────────────────────────
print("\n── partograma.html ──")
patch(f"{GO}/partograma.html", [
    (h2("ESTAÇÃO 1: Fase Ativa Normal — Parto Eutócico"), INTRO_IMGS + EST1_IMGS),
    (h2("ESTAÇÃO 2: Parada Secundária de Dilatação — DPC"), EST2_IMGS),
    (h2("ESTAÇÃO 3: Sofrimento Fetal Agudo + Taquissistolia"), EST3_IMGS),
])

# ── Flashcard GO — adicionar cards visuais do partograma ──────────
print("\n── Flashcard GO.html ──")
FC_PATH = f"{BASE}/osce_materiais/flashcards/GO.html"

with open(FC_PATH, encoding="utf-8") as f:
    fc = f.read()

# CSS para card-img (só adicionar se ainda não tiver)
if ".card-img" not in fc:
    IMG_CSS = "\n  .card-img { max-width: 100%; max-height: 200px; border-radius: 6px; margin-bottom: 10px; object-fit: contain; }\n"
    fc = fc.replace("  @media (max-width: 480px) {", IMG_CSS + "  @media (max-width: 480px) {", 1)

# Altura variável
fc = fc.replace(
    ".scene { width: 100%; max-width: 640px; height: 380px;",
    ".scene { width: 100%; max-width: 640px; min-height: 380px; height: auto;", 1
)

# Renderer com img (só adicionar se ainda não tiver)
OLD_RENDER = "  document.getElementById('cardQ').innerHTML = c.q;"
NEW_RENDER = """  const imgHtml = c.img ? `<img src="${c.img}" class="card-img" alt="">` : '';
  document.getElementById('cardQ').innerHTML = imgHtml + c.q;"""
if OLD_RENDER in fc:
    fc = fc.replace(OLD_RENDER, NEW_RENDER, 1)

# Novos cards visuais de partograma
NEW_CARDS = f"""
  // ── Cards Visuais — Partograma ──
  {{ tag: "Partograma", img: "{REL_FLASH}/parto_pdf_aula_04_partograma_pg3_img1.png", q: "O que é o Plano de De Lee e qual é o plano 0?", a: "Escala de descida da apresentação fetal.<br><strong>Plano 0</strong> = nível das espinhas isquiáticas.<br>Acima: −1, −2, −3 (apresentação móvel).<br>Abaixo: +1, +2, +3 (encravada). <span class='ok'>+4 = na vulva.</span>" }},
  {{ tag: "Partograma", img: "{REL_FLASH}/parto_pdf_aula_04_partograma_pg3_img2.png", q: "Identifique as variedades de posição cefálica neste esquema", a: "<strong>OA</strong>: occipito-anterior (mais favorável) | <strong>OT</strong>: transversa | <strong>OP</strong>: posterior (mais prolongado).<br>Variantes: D = direita, E = esquerda (ex: OEA = occipito-esquerda-anterior)." }},
  {{ tag: "Partograma", img: "{REL_FLASH}/parto_pdf_aula_04_partograma_pg5_img1.png", q: "Descreva as fases do trabalho de parto pela curva de Friedman", a: "<strong>Fase de latência:</strong> até 4 cm, progressão lenta.<br><strong>Fase ativa:</strong> aceleração → dilatação máxima → desaceleração.<br><span class='alert'>Normalidade: fase ativa progride ≥1 cm/h na primigesta.</span>" }},
  {{ tag: "Partograma", img: "{REL_FLASH}/parto_pdf_aula_04_partograma_pg4_img1.png", q: "O que são a Linha de Alerta e a Linha de Ação no partograma?", a: "<strong>Linha de Alerta:</strong> dilatação cruzando os quadrados na diagonal — sinaliza desvio do esperado.<br><strong>Linha de Ação:</strong> 4 horas à direita da linha de alerta — indica necessidade de conduta ativa (amniotomia, ocitocina ou cesárea)." }},
  {{ tag: "Partograma", img: "{REL_FLASH}/parto_pdf_aula_04_partograma_pg6_img1.png", q: "Leia este partograma: qual é o diagnóstico e a conduta?", a: "Dilatação que <strong>cruza a linha de alerta e atinge a linha de ação</strong> → <span class='alert'>Parada Secundária de Dilatação</span>.<br>Causas: DPC, variedade desfavorável, hipodinia.<br>Conduta: amniotomia → ocitocina → reavaliação → cesárea se sem progressão." }},
"""

fc = fc.replace("const ALL_CARDS = [", "const ALL_CARDS = [" + NEW_CARDS, 1)

with open(FC_PATH, "w", encoding="utf-8") as f:
    f.write(fc)
print(f"  [OK]  GO.html: 5 novos cards visuais do partograma")

print("\nConcluido.")
