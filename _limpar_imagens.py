"""
Deleta PNGs das subpastas de osce_materiais que nao estao
referenciados em nenhum HTML da mesma pasta.
Tambem limpa Complementos/imagens/ (pasta de trabalho intermediaria).
"""
import os, re, shutil

BASE   = r"D:/Arquivos/Documentos/Faculdade/OSEC/Github/OSCes"
MAT    = f"{BASE}/osce_materiais"
COMP_IMGS = f"{BASE}/Complementos/imagens"

total_del = 0
total_kept = 0

# ── 1. osce_materiais: deletar PNGs nao referenciados ────────────────────────
for root, dirs, files in os.walk(MAT):
    pngs = [f for f in files if f.lower().endswith(".png")]
    if not pngs:
        continue

    # Coletar todos os src referenciados pelos HTMLs desta pasta
    htmls = [f for f in files if f.lower().endswith(".html")]
    referenced = set()
    for html in htmls:
        with open(os.path.join(root, html), encoding="utf-8") as f:
            txt = f.read()
        # src="FILENAME.png" — captura qualquer filename referenciado
        referenced.update(re.findall(r'src="([^"]+\.png)"', txt))

    # Deletar PNGs nao referenciados
    for png in pngs:
        if png not in referenced:
            os.remove(os.path.join(root, png))
            total_del += 1
        else:
            total_kept += 1

print(f"osce_materiais: {total_kept} mantidos, {total_del} deletados")

# ── 2. Complementos/imagens/ — pasta de trabalho, remover inteira ────────────
if os.path.isdir(COMP_IMGS):
    count = len([f for f in os.listdir(COMP_IMGS) if os.path.isfile(os.path.join(COMP_IMGS, f))])
    shutil.rmtree(COMP_IMGS)
    os.makedirs(COMP_IMGS)  # recriar vazia para nao quebrar estrutura
    print(f"Complementos/imagens/: {count} arquivos removidos (pasta recriada vazia)")

# ── 3. PNGs soltos na raiz do projeto ────────────────────────────────────────
root_pngs = [f for f in os.listdir(BASE) if f.lower().endswith(".png")]
plano_path = f"{BASE}/osce-plano.html"
plano_refs = set()
if os.path.exists(plano_path):
    with open(plano_path, encoding="utf-8") as f:
        plano_refs.update(re.findall(r'src="([^"]+\.png)"', f.read()))

root_del = 0
for png in root_pngs:
    if png not in plano_refs:
        os.remove(os.path.join(BASE, png))
        root_del += 1

print(f"Raiz: {len(root_pngs) - root_del} mantidos, {root_del} deletados")
print("\nConcluido.")
