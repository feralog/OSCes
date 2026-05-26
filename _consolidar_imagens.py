"""
1. Copia imagens usadas nos HTMLs de Pediatria/flashcards para dentro das subpastas
   e simplifica os src (remove prefixo de path).
2. Extrai imagens (>15KB) dos JSONs do Code para as subpastas corretas de osce_materiais,
   nomeando como <topico>_pg<N>_img<N>.png para facilitar visualizacao posterior.
"""
import os, json, base64, re, shutil

PYTHON = r"C:/Users/Fernando/AppData/Local/Programs/Python/Python314/python.exe"
OSCES  = r"D:/Arquivos/Documentos/Faculdade/OSEC/Github/OSCes"
COMP   = f"{OSCES}/Complementos/imagens"
MAT    = f"{OSCES}/osce_materiais"
CODE   = r"D:/Arquivos/Documentos/Faculdade/OSEC/Code"
MIN_KB = 15

# ─── 1. Copiar imagens existentes para as subpastas e simplificar paths ────────
print("=== 1. Copiando imagens existentes para subpastas ===")

MOVES = {
    # (subpasta_destino, prefixo_src_atual)
    f"{MAT}/Pediatria":   "../../Complementos/imagens/",
    f"{MAT}/flashcards":  "../../Complementos/imagens/",
}

for dest_dir, src_prefix in MOVES.items():
    # Coletar todos os arquivos HTML na subpasta
    htmls = [f for f in os.listdir(dest_dir) if f.endswith(".html")]
    copied = set()
    for html in htmls:
        path = os.path.join(dest_dir, html)
        with open(path, encoding="utf-8") as f:
            txt = f.read()
        # Encontrar todos os filenames referenciados
        fnames = re.findall(re.escape(src_prefix) + r'([^\'"]+)', txt)
        for fname in fnames:
            src = os.path.join(COMP, fname)
            dst = os.path.join(dest_dir, fname)
            if os.path.exists(src) and not os.path.exists(dst):
                shutil.copy2(src, dst)
                copied.add(fname)
                print(f"  cp → {os.path.basename(dest_dir)}/{fname}")
        # Simplificar paths no HTML
        new_txt = txt.replace(src_prefix, "")
        if new_txt != txt:
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_txt)
    if copied:
        print(f"  [{os.path.basename(dest_dir)}] {len(copied)} imagens copiadas, paths simplificados")
    else:
        print(f"  [{os.path.basename(dest_dir)}] ja atualizado ou sem imagens")

# osce-plano.html usa "Complementos/imagens/" (raiz) — copiar para raiz do projeto
plano = f"{OSCES}/osce-plano.html"
with open(plano, encoding="utf-8") as f:
    ptxt = f.read()
fnames = re.findall(r'Complementos/imagens/([^\'"]+)', ptxt)
for fname in set(fnames):
    src = os.path.join(COMP, fname)
    dst = os.path.join(OSCES, fname)
    if os.path.exists(src) and not os.path.exists(dst):
        shutil.copy2(src, dst)
        print(f"  cp → raiz/{fname}")
new_ptxt = ptxt.replace("Complementos/imagens/", "")
if new_ptxt != ptxt:
    with open(plano, "w", encoding="utf-8") as f:
        f.write(new_ptxt)
    print("  osce-plano.html: paths simplificados")

# ─── 2. Extrair imagens dos JSONs do Code ─────────────────────────────────────
print("\n=== 2. Extraindo imagens dos JSONs do Code ===")

# Mapeamento: caminho_json → (subpasta_destino, prefixo_slug)
EXTRACTIONS = [
    # Pediatria — sem cobertura
    (f"{CODE}/Ped/Infectologia Pediatrica/Meningites/imagens_meningites.json",
     f"{MAT}/Pediatria", "meningite"),
    (f"{CODE}/Ped/Infectologia Pediatrica/ITU/imagens_itu.json",
     f"{MAT}/Pediatria", "itu"),
    (f"{CODE}/Ped/Neonatologia/Ictericia/imagens_ictericia.json",
     f"{MAT}/Pediatria", "ictericia_neo"),
    (f"{CODE}/Ped/Infectologia Pediatrica/GECA/imagens_geca.json",
     f"{MAT}/Pediatria", "diarreia_aguda"),

    # GO — sem cobertura
    (f"{CODE}/GO/Masto/Mamografia/imagens_mamografia.json",
     f"{MAT}/GO", "mamografia"),
    (f"{CODE}/GO/Masto/USG Mamas/imagens_usg_mamas.json",
     f"{MAT}/GO", "usg_mamas"),
    (f"{CODE}/GO/Obstetricia/Planejamento familiar/imagens_planejamento_familiar.json",
     f"{MAT}/GO", "larcs"),
    (f"{CODE}/GO/Obstetricia/Assistencia ao parto/imagens_assistencia_ao_parto.json",
     f"{MAT}/GO", "assistencia_parto"),

    # Clinica Medica — Gastro
    (f"{CODE}/SAI/Gastro/DRGE/imagens_drge.json",
     f"{MAT}/Clinica_Medica/Gastro", "drge"),
    (f"{CODE}/SAI/Gastro/Diarreia aguda/imagens_diarreia_aguda.json",
     f"{MAT}/Clinica_Medica/Gastro", "diarreia_aguda"),
    (f"{CODE}/SAI/Gastro/Diarreia cronica/imagens_diarreia_cronica.json",
     f"{MAT}/Clinica_Medica/Gastro", "diarreia_cronica"),
    (f"{CODE}/SAI/Gastro/Ictericia e colestase/imagens_ictericia_e_colestase.json",
     f"{MAT}/Clinica_Medica/Gastro", "ictericia_colestase"),
    (f"{CODE}/SAI/Gastro/Obstipacao/imagens_obstipacao.json",
     f"{MAT}/Clinica_Medica/Gastro", "obstipacao"),

    # Clinica Medica — Hemato
    (f"{CODE}/SAI/Hemato/Anemias hemoliticas/imagens_anemias_hemoliticas.json",
     f"{MAT}/Clinica_Medica/Hemato", "anemias_hemoliticas"),
    (f"{CODE}/SAI/Hemato/Anemias macrociticas/imagens_anemias_macrociticas.json",
     f"{MAT}/Clinica_Medica/Hemato", "anemias_macrociticas"),
    (f"{CODE}/SAI/Hemato/Anemias microciticas/imagens_anemias_microciticas.json",
     f"{MAT}/Clinica_Medica/Hemato", "anemias_microciticas"),

    # Clinica Medica — Infecto
    (f"{CODE}/SAI/Infecto/Meningites/imagens_meningites.json",
     f"{MAT}/Clinica_Medica/Infecto", "meningites"),
    (f"{CODE}/SAI/Infecto/Leptospirose/imagens_leptospirose.json",
     f"{MAT}/Clinica_Medica/Infecto", "leptospirose"),
    (f"{CODE}/SAI/Infecto/Sindrome da Mononucleose/imagens_sindrome_da_mononucleose.json",
     f"{MAT}/Clinica_Medica/Infecto", "mononucleose"),

    # Clinica Medica — Endocrino
    (f"{CODE}/SAI/Endocrino/Sindrome de Cushing/imagens_sindrome_de_cushing.json",
     f"{MAT}/Clinica_Medica/Endocrino", "cushing"),
    (f"{CODE}/SAI/Endocrino/Hipertireoidismo/imagens_hipertireoidismo.json",
     f"{MAT}/Clinica_Medica/Endocrino", "hipertireoidismo"),

    # Clinica Medica — Nefro
    (f"{CODE}/SAI/Hemato/Anemias microciticas/imagens_anemias_microciticas.json",  # reutilizar
     f"{MAT}/Clinica_Medica/Nefro", "nefro_ref"),  # placeholder, sem JSON específico

    # Cirurgia
    (f"{CODE}/Cirurgia/Principios da cirurgia/Drenos e Sondas/imagens_drenos_e_sondas.json",
     f"{MAT}/Cirurgia", "drenos_sondas"),
    (f"{CODE}/Cirurgia/Principios da cirurgia/Feridas cirurgicas/imagens_feridas_cirurgicas.json",
     f"{MAT}/Cirurgia", "feridas"),
    (f"{CODE}/Cirurgia/Principios da cirurgia/Fios e agulhas/imagens_fios_e_agulhas.json",
     f"{MAT}/Cirurgia", "fios_agulhas"),
    (f"{CODE}/Cirurgia/Principios da cirurgia/Instrumentais cirurgicos/imagens_instrumentais_cirurgicos.json",
     f"{MAT}/Cirurgia", "instrumentais"),
]

for json_path, dest_dir, slug in EXTRACTIONS:
    if not os.path.exists(json_path):
        print(f"  [SKIP] nao encontrado: {os.path.basename(json_path)}")
        continue
    os.makedirs(dest_dir, exist_ok=True)
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)

    saved = 0
    skipped = 0
    for key, b64 in data.items():
        size_kb = len(b64) * 3 / 4 / 1024
        if size_kb < MIN_KB:
            skipped += 1
            continue
        # Nome de arquivo legível
        out_name = f"{slug}_{key}.png"
        out_path = os.path.join(dest_dir, out_name)
        if not os.path.exists(out_path):
            with open(out_path, "wb") as f:
                f.write(base64.b64decode(b64))
        saved += 1

    print(f"  [{slug}] → {os.path.basename(dest_dir)}: {saved} imgs (ignoradas {skipped} <{MIN_KB}KB)")

print("\nConcluido. Proximos passos: visualizar e injetar as novas imagens.")
