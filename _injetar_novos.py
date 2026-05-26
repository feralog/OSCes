"""
Injeta imagens selecionadas (clinicamente uteis) nos HTMLs de:
  Pediatria: meningite, itu, ictericia_neonatal
  GO: imagem_mama, larcs_planejamento_familiar
  Cirurgia: suturas, sonda_nasogastrica, dreno_torax
As imagens ja estao copiadas para dentro de cada subpasta.
"""
import os

BASE = r"D:/Arquivos/Documentos/Faculdade/OSEC/Github/OSCes"
PED  = f"{BASE}/osce_materiais/Pediatria"
GO   = f"{BASE}/osce_materiais/GO"
CIR  = f"{BASE}/osce_materiais/Cirurgia"

def fig(fname, alt, caption):
    return (
        f'\n<figure style="margin:22px 0;text-align:center">'
        f'<img src="{fname}" alt="{alt}" '
        f'style="max-width:100%;border-radius:8px;border:1px solid #ddd;'
        f'box-shadow:0 2px 10px rgba(0,0,0,.1)">'
        f'<figcaption style="font-size:11px;color:#888;margin-top:6px;'
        f'font-family:system-ui,sans-serif;font-style:italic">{caption}</figcaption>'
        f'</figure>\n'
    )

def h2(text):
    return f'<h2 class="section-heading">{text}</h2>'

def h3(text):
    return f'<h3 class="section-heading">{text}</h3>'

def patch(path, items):
    with open(path, encoding="utf-8") as f:
        txt = f.read()
    ok = 0
    for anchor, html in items:
        if anchor not in txt:
            print(f"  [MISS] {os.path.basename(path)}: '{anchor[:80]}'")
            continue
        txt = txt.replace(anchor, anchor + html, 1)
        ok += 1
    with open(path, "w", encoding="utf-8") as f:
        f.write(txt)
    print(f"  [OK]  {os.path.basename(path)}: {ok}/{len(items)}")


# ── Meningite Pediátrica ──────────────────────────────────────────────────────
print("\n── meningite.html ──")
patch(f"{PED}/meningite.html", [
    (
        h2("Agentes Etiológicos por Faixa Etária"),
        fig("meningite_pdf_aula_06_meningites_bacterianas_pg2_img1.png",
            "Fisiopatologia meningite bacteriana lesao cerebral",
            "Fisiopatologia: ativação de leucócitos → edema vasogênico + citotóxico + intersticial → ↑ PIC → lesão cerebral")
    ),
    (
        h3("Duração do Tratamento"),
        fig("meningite_pdf_aula_06_meningites_bacterianas_pg5_img1.png",
            "Tabela duracao tratamento por agente bacteriano",
            "Duração do tratamento: N. meningitidis 5–7 d | H. influenzae 7–10 d | S. pneumoniae 10–14 d | Listeria/SGB/BGN 14–21 d")
    ),
])

# ── ITU Pediátrica ────────────────────────────────────────────────────────────
print("\n── itu.html ──")
patch(f"{PED}/itu.html", [
    (
        h3("Coleta de Urina — Método Correto"),
        fig("itu_pdf_aula_11_infecc_a_o_do_trato_urina_rio_pg3_img1.png",
            "Tabela metodos coleta urina crianca",
            "Coleta: Jato médio (controle miccional) | Saco coletor (troca a cada 30 min) | Punção suprapúbica (< 2 anos sem controle ou diarreia/dermatite) | Cateterismo (sem controle miccional)")
    ),
])

# ── Icterícia Neonatal ────────────────────────────────────────────────────────
print("\n── ictericia_neonatal.html ──")
patch(f"{PED}/ictericia_neonatal.html", [
    (
        h2("Zonas de Kramer — Estimativa Clínica da BT"),
        fig("ictericia_neo_pdf_aula_12_icteri_cia_neonatal_pg4_img1.png",
            "Zonas de Kramer progressao cefalocaudal bilirrubina",
            "Zonas de Kramer: Zona 1 (cabeça) BT 4–8 | Zona 2 (tronco até umbigo) 5–12 | Zona 3 (umbigo–joelhos) 8–16 | Zona 4 (extremidades) 11–18 | Zona 5 (palmas/plantas) ≥15 mg/dL")
    ),
    (
        h2("Nomograma de Bhutani — Quando Fototerapia?"),
        fig("ictericia_neo_pdf_aula_12_icteri_cia_neonatal_pg5_img1.png",
            "Fluxograma decisao fototerapia 72 horas",
            "Fluxo ≥35 sem: icterícia <24–36h → dosar BT + etiologia | BT >P95 → fototerapia imediata | BT P75–95 → considerar conforme IG | BT <P75 → reavaliar fatores de risco")
        + fig("ictericia_neo_pdf_aula_12_icteri_cia_neonatal_pg5_img2.png",
              "Grafico nomograma Bhutani zonas risco bilirrubina",
              "Nomograma de Bhutani: zona alto risco (>P95), risco intermediário alto (P75–95), baixo risco (<P40) — indicação de fototerapia baseada na zona e idade gestacional")
    ),
])

# ── Imagem da Mama (Mamografia + USG) ────────────────────────────────────────
print("\n── imagem_mama.html ──")
patch(f"{GO}/imagem_mama.html", [
    (
        h2("Achados na Mamografia"),
        fig("mamografia_pdf_aula_03_2_pra_tica_mamografia_pg2_img3.png",
            "Mamografia MLO bilateral incidencia padrao",
            "Incidência MLO bilateral: padrão normal — visualização simétrica do tecido fibroglandular, linha da pele e mamilo")
        + fig("mamografia_pdf_aula_03_2_pra_tica_mamografia_pg6_img1.png",
              "Nodulo denso espiculado com microcalcificacoes carcinoma ductal",
              "Nódulo denso e espiculado (palpável, mama E) com microcalcificações associadas → carcinoma ductal invasivo (BI-RADS 5)")
    ),
    (
        h2("Achados no USG"),
        fig("usg_mamas_pdf_aula_pra_tica_usg_mamas_pg23_img1.png",
            "USG mama caracteristicas acusticas posteriores sombra reforco",
            "Características acústicas posteriores: Sombra (lesão sólida calcificada — maligno) | Reforço (cisto simples — benigno) | Padrão combinado (lesão complexa)")
        + fig("usg_mamas_pdf_aula_pra_tica_usg_mamas_pg33_img1.png",
              "USG mama margem nao circunscrita espiculada VPP 86",
              "Margem não circunscrita: VPP maligno 86% | Espiculada (86%) | Microlobulada (50%) | Angulada (60%) | Indefinida → critério BI-RADS 4C/5")
    ),
])

# ── LARCs e Planejamento Familiar ────────────────────────────────────────────
print("\n── larcs_planejamento_familiar.html ──")
patch(f"{GO}/larcs_planejamento_familiar.html", [
    (
        h2("Tabela de LARCs — Referência Rápida"),
        fig("larcs_pdf_aula_planejamento_familiar_pg27_img1.png",
            "Equacao planejamento familiar LARCs eficacia progestagenos seguranca CV",
            "Equação do PF: Eficácia+Rotina (LARCs eliminam erro humano) × Sintonia do Progestágeno (acne/TPM guiam escolha) × Segurança Cardiovascular (Categoria 4 OMS → usar desogestrel/DIU-Cu)")
    ),
])

# ── Suturas ───────────────────────────────────────────────────────────────────
print("\n── suturas.html ──")
patch(f"{CIR}/suturas.html", [
    (
        h3("Quanto à Estrutura"),
        fig("fios_agulhas_pdf_aula_07_fios_e_agulhas_pdf_pg3_img2.png",
            "Estrutura fios sutura mono torcido trancado multifilamentar revestido",
            "Estrutura: Monofilamentar (menor infecção, mais memória) | Torcido | Trançado (maior força de nó) | Revestido multifilamentar (maneabilidade + resistência)")
    ),
    (
        h2("Classificação das Agulhas"),
        fig("fios_agulhas_pdf_aula_7_fios_e_agulhas_pdf_pg21_img1.png",
            "Como ler embalagem fio sutura agulha acido poliglicolico",
            "Leitura da embalagem: tipo do fio | calibre (1=espessura) | cor | comprimento | curvatura (M=meia circunferência) | ponta da agulha (R=romba/Cil=cilíndrica) | comprimento da agulha (4,0 cm)")
    ),
])

# ── Sonda Nasogástrica ────────────────────────────────────────────────────────
print("\n── sonda_nasogastrica.html ──")
patch(f"{CIR}/sonda_nasogastrica.html", [
    (
        h2("Tipos de Sondas"),
        fig("drenos_sondas_pdf_aula_9_drenos_e_sondas_6s_unisa_pdf_pg41_img2.png",
            "Sonda gastrica simples Salem duas luzes radiopaca",
            "Sonda Gástrica Simples (Salem): naso-gástrica radiopaca de plástico claro, duas luzes — usada para descompressão gástrica e manter estômago vazio")
    ),
])

# ── Dreno de Tórax ────────────────────────────────────────────────────────────
print("\n── dreno_torax.html ──")
patch(f"{CIR}/dreno_torax.html", [
    (
        h2("Sistema de Drenagem com Selo D'água"),
        fig("drenos_sondas_pdf_aula_9_drenos_e_sondas_6s_unisa_pdf_pg28_img2.png",
            "Sistema dreno toracico frasco selo dagua",
            "Sistema de drenagem: dreno de tórax conectado a frasco lacrado (selo d'água) com câmara de coleta e válvula unidirecional — impede entrada de ar na pleura")
    ),
])

print("\nConcluido.")
