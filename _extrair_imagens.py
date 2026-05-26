"""
Extrai todas as páginas dos PDFs em OSCes/Complementos como PNG
e também copia as imagens WhatsApp/pagina de Code/Complementos.
Saída: OSCes/Complementos/imagens/
"""
import os, shutil, re

PYTHON = r"C:/Users/Fernando/AppData/Local/Programs/Python/Python314/python.exe"

COMPLEMENTOS_OSCE = r"D:/Arquivos/Documentos/Faculdade/OSEC/Github/OSCes/Complementos"
COMPLEMENTOS_CODE = r"D:/Arquivos/Documentos/Faculdade/OSEC/Code/Complementos"
TEMP_CODE         = r"D:/Arquivos/Documentos/Faculdade/OSEC/Code/.temp"
OUT_DIR           = os.path.join(COMPLEMENTOS_OSCE, "imagens")

os.makedirs(OUT_DIR, exist_ok=True)

# ── 1. Renderizar PDFs como PNG ───────────────────────────────────────────────
try:
    import fitz  # PyMuPDF
    pdfs = [f for f in os.listdir(COMPLEMENTOS_OSCE) if f.lower().endswith(".pdf")]
    for pdf_name in sorted(pdfs):
        slug = re.sub(r'[^a-z0-9]+', '_', os.path.splitext(pdf_name)[0].lower()).strip('_')
        pdf_path = os.path.join(COMPLEMENTOS_OSCE, pdf_name)
        doc = fitz.open(pdf_path)
        print(f"PDF: {pdf_name} ({len(doc)} paginas)")
        for i, page in enumerate(doc, 1):
            out_path = os.path.join(OUT_DIR, f"{slug}_pg{i:02d}.png")
            if os.path.exists(out_path):
                print(f"  já existe: {os.path.basename(out_path)}, pulando")
                continue
            pixmap = page.get_pixmap(dpi=120)
            pixmap.save(out_path)
            print(f"  salvo: {os.path.basename(out_path)}")
        doc.close()
except ImportError:
    print("ERRO: PyMuPDF (fitz) não encontrado — instale: pip install pymupdf")

# ── 2. Copiar imagens de Code/Complementos ────────────────────────────────────
img_exts = {'.jpg', '.jpeg', '.png', '.webp'}
if os.path.isdir(COMPLEMENTOS_CODE):
    files = [f for f in os.listdir(COMPLEMENTOS_CODE)
             if os.path.splitext(f)[1].lower() in img_exts]
    print(f"\nCode/Complementos: {len(files)} imagens")
    for f in sorted(files):
        src = os.path.join(COMPLEMENTOS_CODE, f)
        # normalizar nome: remover espaços e caracteres especiais
        slug = re.sub(r'[^a-z0-9_.\-]+', '_', f.lower())
        dst = os.path.join(OUT_DIR, "whatsapp_" + slug if "whatsapp" in f.lower() else slug)
        shutil.copy2(src, dst)
        print(f"  copiado: {os.path.basename(dst)}")

# ── 3. Copiar PNGs já extraídos do .temp ─────────────────────────────────────
if os.path.isdir(TEMP_CODE):
    osce_pngs = [f for f in os.listdir(TEMP_CODE)
                 if f.startswith("osce_pg_") and f.endswith(".png")]
    print(f"\n.temp: {len(osce_pngs)} PNGs do OSCE")
    for f in sorted(osce_pngs):
        src = os.path.join(TEMP_CODE, f)
        dst = os.path.join(OUT_DIR, f)
        shutil.copy2(src, dst)
        print(f"  copiado: {f}")

# ── Resumo ────────────────────────────────────────────────────────────────────
all_imgs = os.listdir(OUT_DIR)
print(f"\nTotal em imagens/: {len(all_imgs)} arquivos")
for f in sorted(all_imgs):
    size_kb = os.path.getsize(os.path.join(OUT_DIR, f)) / 1024
    print(f"  {f} ({size_kb:.0f} KB)")
