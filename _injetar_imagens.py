"""
Injeta imagens nos arquivos osce_materiais (MD + HTML de topico) e flashcards.
Uso: python _injetar_imagens.py
"""
import os, re

BASE  = r"D:/Arquivos/Documentos/Faculdade/OSEC/Github/OSCes"
IPED  = "../../Complementos/imagens"   # relativo de osce_materiais/Pediatria/
IFLSH = "../../Complementos/imagens"   # relativo de osce_materiais/flashcards/
IROOT = "Complementos/imagens"         # relativo da raiz

def fig(fname, alt, caption, rel=IPED):
    return (
        f'\n<figure style="margin:22px 0;text-align:center">'
        f'<img src="{rel}/{fname}" alt="{alt}" '
        f'style="max-width:100%;border-radius:8px;border:1px solid #ddd;'
        f'box-shadow:0 2px 10px rgba(0,0,0,.1)">'
        f'<figcaption style="font-size:11px;color:#888;margin-top:6px;'
        f'font-family:system-ui,sans-serif;font-style:italic">{caption}</figcaption>'
        f'</figure>\n'
    )

def patch(path, replacements):
    """replacements: list of (anchor, insertion_html, after=True)"""
    with open(path, encoding="utf-8") as f:
        txt = f.read()
    changed = 0
    for item in replacements:
        anchor, html = item[0], item[1]
        after = item[2] if len(item) > 2 else True
        if anchor not in txt:
            print(f"  [MISS] {os.path.basename(path)}: '{anchor[:60]}'")
            continue
        if after:
            txt = txt.replace(anchor, anchor + html, 1)
        else:
            txt = txt.replace(anchor, html + anchor, 1)
        changed += 1
    with open(path, "w", encoding="utf-8") as f:
        f.write(txt)
    print(f"  [OK] {os.path.basename(path)}: {changed}/{len(replacements)} injecoes")

# ═══════════════════════════════════════════════════════════════
# DOENCAS EXANTEMATICAS
# ═══════════════════════════════════════════════════════════════
print("\n── Doenças Exantemáticas ──")
EX_IMGS = [
    # (anchor_in_both_md_and_html, fig_html)
    (
        "## TABELA-MESTRE — Diagnóstico Diferencial dos Exantemas",
        fig("playbook_cl_nico_de_exantemas_pg06.png",
            "Exantema eritematoso morbiliforme",
            "Exantema morbiliforme: maculopápulas confluentes avermelhadas (Playbook Clínico, OSEC 2026)")
        + fig("playbook_cl_nico_de_exantemas_pg08.png",
              "Bebê com exantema papulovesicular",
              "Exantema pápulo-vesicular em lactente — polimorfismo lesional característico da varicela")
    ),
    (
        "## CLASSIFICAÇÃO DOS TIPOS DE EXANTEMA",
        fig("playbook_cl_nico_de_exantemas_pg11.png",
            "Mapeamento anatômico dos exantemas",
            "Mapeamento anatômico: distribuição de Escarlatina (Sinal de Filatov, Pastia) × Eritema Infeccioso (face esbofeteada, rendilhado)")
    ),
    (
        "## ESTAÇÃO 3 — Caso: Escarlatina (Playbook)",
        fig("playbook_cl_nico_de_exantemas_pg12.png",
            "Cinética febre vs exantema",
            "Cinética febre × exantema: Escarlatina (exantema junto à febre) × Eritema Infeccioso (exantema após melhora febril)")
        + fig("playbook_cl_nico_de_exantemas_pg13.png",
              "Arvore de raciocinio clinico exantemas",
              "Árvore de raciocínio clínico: toxemia + odinofagia → Escarlatina | bom estado geral + fácies → Eritema Infeccioso")
        + fig("playbook_cl_nico_de_exantemas_pg14.png",
              "Matriz diagnostica diferencial Escarlatina vs Eritema Infeccioso",
              "Matriz DDx: Escarlatina (S. pyogenes, penicilina) × Eritema Infeccioso (Parvovírus B19, sintomático)")
    ),
]

for fname in ["doencas_exantematicas.md", "doencas_exantematicas.html"]:
    patch(f"{BASE}/osce_materiais/Pediatria/{fname}", EX_IMGS)

# ═══════════════════════════════════════════════════════════════
# SIFILIS / HIV / TORCHS
# ═══════════════════════════════════════════════════════════════
print("\n── Sífilis / HIV / TORCHS ──")
SIF_IMGS = [
    (
        "## Toxoplasmose Congênita",
        fig("protocolo_s_filis_e_hiv_neonatal_pg09.png",
            "Fluxograma triagem sifilis congenita",
            "Triagem Sífilis Congênita: Regra de Ouro — NUNCA usar sangue do cordão umbilical. Fluxo investigação/tratamento")
        + fig("protocolo_s_filis_e_hiv_neonatal_pg11.png",
              "Criterios diagnosticos LCR sifilis",
              "Fator neurológico: VDRL liquórico reagente OU >25 céls/mm³ OU proteínas >150 mg/dL → internação 10 dias")
    ),
    (
        "## CMV Congênito",
        fig("protocolo_s_filis_e_hiv_neonatal_pg04.png",
            "Nascimento e biosseguranca HIV",
            "Nascimento: FAZER (parto empelicado, clampeamento imediato, banho) × NÃO FAZER (ordenha do cordão, aspiração de rotina)")
        + fig("protocolo_s_filis_e_hiv_neonatal_pg05.png",
              "Decisao via de parto pela carga viral",
              "Via de parto: CV <1.000 cópias/mL na 34ª semana → parto vaginal | CV ≥1.000 ou desconhecida → cesárea eletiva ≥38 sem")
        + fig("protocolo_s_filis_e_hiv_neonatal_pg07.png",
              "Conduta HIV alojamento conjunto",
              "HIV no alojamento conjunto: AZT neonatal precoce + amamentação CONTRAINDICADA + fórmula láctea até 6 meses")
        + fig("protocolo_s_filis_e_hiv_neonatal_pg13.png",
              "Seguimento HIV timeline alta",
              "Seguimento HIV pós-alta: 2 semanas → 4–6 semanas → 12 semanas | Alta do serviço: 18 meses ou 2 CV indetectáveis")
    ),
]

for fname in ["sifilis_hiv_torchs.md", "sifilis_hiv_torchs.html"]:
    patch(f"{BASE}/osce_materiais/Pediatria/{fname}", SIF_IMGS)

# ═══════════════════════════════════════════════════════════════
# REANIMACAO NEONATAL
# ═══════════════════════════════════════════════════════════════
print("\n── Reanimação Neonatal ──")
REAM_IMGS = [
    (
        "## Fluxograma de Decisão — ≥ 34 Semanas",
        fig("atendimento_ao_rece_m_nascido_2026_1_pg06.png",
            "Fluxograma 3 perguntas vitais nascimento",
            "3 Perguntas Vitais: todas SIM → pele-a-pele com mãe | qualquer NÃO → mesa de reanimação")
        + fig("atendimento_ao_rece_m_nascido_2026_1_pg07.png",
              "Minuto de Ouro reanimacao neonatal",
              "Minuto de Ouro: VPP deve ser iniciada no 1º minuto de vida. Objetivo: restabelecer FC e respiração espontânea")
        + fig("atendimento_ao_rece_m_nascido_2026_1_pg08.png",
              "Passos iniciais 30 segundos reanimacao",
              "Passos iniciais (≤30 s): 1. Aquecer → 2. Secar → 3. Posicionar → 4. Aspirar (só se obstrução visível)")
    ),
    (
        "## Ventilação com Pressão Positiva (VPP)",
        fig("atendimento_ao_rece_m_nascido_2026_1_pg09.png",
            "Avaliacao vitalidade fluxograma VPP",
            "Avaliação de vitalidade: FC <100 bpm OU apneia → iniciar VPP imediatamente")
        + fig("atendimento_ao_rece_m_nascido_2026_1_pg11.png",
              "Alvos de saturacao O2 pre-ductal por minuto",
              "Alvos de SatO₂ pré-ductal: 1 min=70-80% | 5 min=80-90% | 10 min=85-95%. Não suplementar O₂ dentro dos alvos")
        + fig("atendimento_ao_rece_m_nascido_2026_1_pg13.png",
              "Algoritmo SBP 2022 reanimacao neonatal completo",
              "Algoritmo SBP 2022: fluxo completo nascimento → passos iniciais → VPP → massagem cardíaca → adrenalina")
    ),
]

for fname in ["reanimacao_neonatal.md", "reanimacao_neonatal.html"]:
    patch(f"{BASE}/osce_materiais/Pediatria/{fname}", REAM_IMGS)

# ═══════════════════════════════════════════════════════════════
# ATENDIMENTO AO RN NORMAL
# ═══════════════════════════════════════════════════════════════
print("\n── Atendimento ao RN Normal ──")
RN_IMGS = [
    (
        "## Checklist — Recepção do RN ≥ 34 Semanas",
        fig("atendimento_ao_rece_m_nascido_2026_1_pg06.png",
            "Fluxograma 3 perguntas avaliacao RN",
            "Fluxo de decisão no nascimento: 3 perguntas vitais definem se o RN vai para o colo da mãe ou para a mesa")
        + fig("atendimento_ao_rece_m_nascido_2026_1_pg08.png",
              "Passos iniciais primeiros 30 segundos",
              "Primeiros 30 segundos: aquecer → secar → posicionar → aspirar (condicional). Reavaliação imediata em seguida")
    ),
]

for fname in ["atendimento_rn_normal.md", "atendimento_rn_normal.html"]:
    patch(f"{BASE}/osce_materiais/Pediatria/{fname}", RN_IMGS)

# ═══════════════════════════════════════════════════════════════
# BRONQUIOLITE × LACTENTE SIBILANTE × ASMA
# ═══════════════════════════════════════════════════════════════
print("\n── Bronquiolite × Asma ──")
BRQ_IMGS = [
    (
        "## ESTAÇÃO 1 — Caso Clínico: 4 Meses, Primeiro Episódio de Sibilância",
        fig("bronquiolite_x_lactente_sibilnate_x_asma_pg13.png",
            "Bronquiolite Viral Aguda fatores de risco clinicos",
            "Bronquiolite Viral Aguda: diagnóstico clínico (coriza→febre→tosse→sibilância). Radiografia NÃO indicada de rotina")
        + fig("bronquiolite_x_lactente_sibilnate_x_asma_pg09.png",
              "Comparacao exame fisico bronquiolite vs lactente sibilante",
              "Exame físico comparativo: Caso Azul (BVA) — sibilos difusos, grave/descompensado × Caso Laranja (LS) — expiração prolongada, compensado")
    ),
    (
        "## ESTAÇÃO 2 — Caso Clínico: 9 Meses, Sibilância Recorrente",
        fig("bronquiolite_x_lactente_sibilnate_x_asma_pg11.png",
            "Tabela comparativa bronquiolite aguda vs lactente sibilante",
            "DDx fundamental: Bronquiolite Aguda (1º episódio, VSR, grave) × Lactente Sibilante (recorrente, atopia, compensado)")
    ),
    (
        "## ESTAÇÃO 3 — Diagnóstico Diferencial: Asma",
        fig("bronquiolite_x_lactente_sibilnate_x_asma_pg16.png",
            "4 fenotipos da sibilancia PRACTALL Martinez",
            "4 Fenótipos PRACTALL/Martínez: Transitória (VSR, <2-3 anos) | Não-Atópica (viral) | Atópica Persistente (asma) | Intermitente Grave")
        + fig("bronquiolite_x_lactente_sibilnate_x_asma_pg19.png",
              "Terapia de manutencao asma via atopica vs nao atopica",
              "Manutenção: Via Atópica → CI + β2 longa + montelucaste | Via Viral/Não-Atópica → macrolídeos controversos, azitromicina promissora")
    ),
]

for fname in ["bronquiolite_asma_lactente_sibilante.md", "bronquiolite_asma_lactente_sibilante.html"]:
    patch(f"{BASE}/osce_materiais/Pediatria/{fname}", BRQ_IMGS)

# ═══════════════════════════════════════════════════════════════
# PNEUMONIA
# ═══════════════════════════════════════════════════════════════
print("\n── Pneumonia ──")
PNM_IMGS = [
    (
        "## Diagnóstico Clínico — Tríade Principal",
        fig("aula_pratica_pneumonia_pg06.png",
            "Mapeamento exame fisico toracico pneumonia",
            "Exame físico torácico: Inspeção (tiragem) → Palpação (FTV) → Percussão (macicez) → Ausculta (MV reduzido, broncofonia)")
    ),
    (
        "### Pneumonias Atípicas",
        fig("aula_pratica_pneumonia_pg18.png",
            "Pneumonia necrosante S aureus PVL",
            "Pneumonia Necrosante: consolidação → liquefação → pneumatocele. S. aureus PVL+ (MRSA): fístula broncopleural 17-67%, empiema 63-100%")
    ),
    (
        "## Classificação e Conduta — OMS Simplificada",
        fig("aula_pratica_pneumonia_pg22.png",
            "Guia rapido dosagens IV antibioticos pneumonia",
            "Dosagens IV: Ampicilina 150-200 mg/kg/dia | Pen. Cristalina 200.000-250.000 U/kg/dia | Ceftriaxona 50-100 mg/kg/dia | Oxacilina 200 mg/kg/dia")
    ),
]

for fname in ["pneumonia.md", "pneumonia.html"]:
    patch(f"{BASE}/osce_materiais/Pediatria/{fname}", PNM_IMGS)

# ═══════════════════════════════════════════════════════════════
# FLASHCARD Pediatria.html — adicionar suporte a img e novos cards
# ═══════════════════════════════════════════════════════════════
print("\n── Flashcard Pediatria ──")
FC_PATH = f"{BASE}/osce_materiais/flashcards/Pediatria.html"

# 1. Corrigir altura do card para acomodar imagens
patch(FC_PATH, [
    (
        ".scene { width: 100%; max-width: 640px; height: 380px;",
        ".scene { width: 100%; max-width: 640px; min-height: 380px; height: auto;"
    ),
    (
        ".face { position: absolute; inset: 0; backface-visibility: hidden;",
        ".face { position: absolute; top: 0; left: 0; right: 0; bottom: 0; backface-visibility: hidden;"
    ),
])

# 2. Adicionar suporte a campo `img` no renderer e novos cards visuais
with open(FC_PATH, encoding="utf-8") as f:
    fc = f.read()

# Adicionar CSS para imagem dentro do card
IMG_CSS = """
  .card-img { max-width: 100%; max-height: 200px; border-radius: 6px; margin-bottom: 10px; object-fit: contain; }
"""
fc = fc.replace("  @media (max-width: 480px) {", IMG_CSS + "  @media (max-width: 480px) {", 1)

# Modificar o render para mostrar img se existir
OLD_RENDER = "  document.getElementById('cardQ').innerHTML = c.q;"
NEW_RENDER = """  const imgHtml = c.img ? `<img src="${c.img}" class="card-img" alt="">` : '';
  document.getElementById('cardQ').innerHTML = imgHtml + c.q;"""
fc = fc.replace(OLD_RENDER, NEW_RENDER, 1)

# Novos cards visuais — inserir antes do fechamento de ALL_CARDS
NEW_CARDS = f"""
  // ── Cards Visuais com Imagem ──
  {{ tag: "Reanimação", img: "{IFLSH}/atendimento_ao_rece_m_nascido_2026_1_pg06.png", q: "Qual o fluxo de decisão ao nascer (as 3 perguntas)?", a: "Todas SIM → pele-a-pele com mãe.<br><strong class='ok'>A termo? Respirando/chorando? Tônus?</strong><br>Qualquer NÃO → mesa de reanimação imediatamente." }},
  {{ tag: "Reanimação", img: "{IFLSH}/atendimento_ao_rece_m_nascido_2026_1_pg08.png", q: "Quais os passos iniciais nos primeiros 30 segundos?", a: "<strong>1. Aquecer</strong> (calor radiante) → <strong>2. Secar</strong> (corpo + cabeça, desprezar campos) → <strong>3. Posicionar</strong> (leve extensão) → <strong>4. Aspirar</strong> (só se obstrução visível — não é rotina)." }},
  {{ tag: "Reanimação", img: "{IFLSH}/atendimento_ao_rece_m_nascido_2026_1_pg11.png", q: "Quais os alvos de SatO₂ pré-ductal por minuto de vida?", a: "1 min: <strong>70–80%</strong> | 5 min: <strong>80–90%</strong> | 10 min: <strong>85–95%</strong>.<br><span class='alert'>Não suplementar O₂ se dentro dos alvos, mesmo que o bebê pareça cianótico.</span>" }},
  {{ tag: "Exantemas", img: "{IFLSH}/playbook_cl_nico_de_exantemas_pg11.png", q: "Identifique os achados clínicos de Escarlatina × Eritema Infeccioso no mapeamento anatômico", a: "<strong>Escarlatina:</strong> Sinal de Filatov (palidez perioral) + Sinal de Pastia (linhas nas dobras) + língua em framboesa.<br><strong>Eritema Infeccioso:</strong> face esbofeteada (eritema malar) + rendilhado em extremidades, poupa palmas/plantas." }},
  {{ tag: "Exantemas", img: "{IFLSH}/playbook_cl_nico_de_exantemas_pg12.png", q: "Qual a diferença na cinética febre × exantema entre Escarlatina e Eritema Infeccioso?", a: "<strong>Escarlatina:</strong> exantema surge durante a febre alta (juntos).<br><strong>Eritema Infeccioso:</strong> exantema surge <em>após</em> a queda da febre (fácies esbofeteada pós-doença febril)." }},
  {{ tag: "Sífilis/HIV", img: "{IFLSH}/protocolo_s_filis_e_hiv_neonatal_pg05.png", q: "Como a carga viral na 34ª semana define a via de parto no HIV?", a: "<strong class='ok'>CV <1.000 cópias/mL</strong> → parto vaginal (AZT intraparto não obrigatório).<br><strong class='alert'>CV ≥1.000 ou desconhecida</strong> → cesárea eletiva ≥38 semanas + AZT intraparto obrigatório." }},
  {{ tag: "Sífilis/HIV", img: "{IFLSH}/protocolo_s_filis_e_hiv_neonatal_pg09.png", q: "Descreva o fluxo de triagem para sífilis congênita ao nascer", a: "<strong class='alert'>Regra de Ouro: NUNCA usar sangue do cordão</strong> (risco de falso-reagente).<br>Mãe adequadamente tratada + RN assintomático + VDRL RN < materno → seguimento ambulatorial.<br>Qualquer desvio → investigação e tratamento." }},
  {{ tag: "Bronquiolite", img: "{IFLSH}/bronquiolite_x_lactente_sibilnate_x_asma_pg11.png", q: "Compare BVA (Bronquiolite Viral Aguda) × Lactente Sibilante nesta tabela", a: "<strong>BVA:</strong> 1º episódio, pródromo viral, taquipneia grave, SatO₂ ↓, sem atopia familiar.<br><strong>Lactente Sibilante:</strong> recorrente (>3 ep.), mãe asmática, expiração prolongada, SatO₂ preservada → pensar em asma." }},
  {{ tag: "Bronquiolite", img: "{IFLSH}/bronquiolite_x_lactente_sibilnate_x_asma_pg16.png", q: "Quais os 4 fenótipos de sibilância pelo consenso PRACTALL/Martínez?", a: "1. <strong>Transitória</strong> (viral, <2 anos, resolve)<br>2. <strong>Não-Atópica</strong> (exclusivamente viral)<br>3. <strong>Atópica Persistente</strong> (= Asma)<br>4. <strong>Intermitente Grave</strong> (episódios graves, fundo atópico)" }},
  {{ tag: "Pneumonia", img: "{IFLSH}/aula_pratica_pneumonia_pg06.png", q: "Quais os achados do exame físico torácico na pneumonia com derrame?", a: "<strong>Inspeção:</strong> aumento do hemitórax, tiragem intercostal/subcostal.<br><strong>Palpação:</strong> FTV diminuído.<br><strong>Percussão:</strong> macicez na base.<br><strong>Ausculta:</strong> MV reduzido + broncofonia diminuída." }},
"""

fc = fc.replace("const ALL_CARDS = [", "const ALL_CARDS = [" + NEW_CARDS, 1)

with open(FC_PATH, "w", encoding="utf-8") as f:
    f.write(fc)
print(f"  [OK] Pediatria.html: CSS img + render + 10 novos cards visuais")

# ═══════════════════════════════════════════════════════════════
# OSCE-PLANO.html — imagens de destaque na visão geral
# ═══════════════════════════════════════════════════════════════
print("\n── osce-plano.html ──")
PLANO_PATH = f"{BASE}/osce-plano.html"

with open(PLANO_PATH, encoding="utf-8") as f:
    plano = f.read()

# Adicionar CSS para o bloco de imagem de referência no plano
PLANO_CSS = """
  .ref-imgs { display: flex; gap: 10px; flex-wrap: wrap; margin: 16px 0; }
  .ref-imgs img { border-radius: 6px; border: 1px solid #ddd; object-fit: cover;
                  flex: 1 1 140px; max-height: 110px; box-shadow: 0 1px 6px rgba(0,0,0,.08); }
"""
plano = plano.replace("</style>", PLANO_CSS + "</style>", 1)

# Inserir galeria de referência visual logo após o header (antes do main)
GALLERY = f"""
<div style="max-width:740px;margin:14px auto 0;padding:0 16px">
  <p style="font-family:system-ui,sans-serif;font-size:10px;letter-spacing:2px;
     text-transform:uppercase;color:#999;margin-bottom:8px">Material de referência</p>
  <div class="ref-imgs">
    <img src="{IROOT}/atendimento_ao_rece_m_nascido_2026_1_pg13.png" alt="Algoritmo SBP Reanimação">
    <img src="{IROOT}/playbook_cl_nico_de_exantemas_pg11.png" alt="Mapeamento Exantemas">
    <img src="{IROOT}/protocolo_s_filis_e_hiv_neonatal_pg05.png" alt="Via de Parto HIV">
    <img src="{IROOT}/bronquiolite_x_lactente_sibilnate_x_asma_pg11.png" alt="BVA vs Lactente Sibilante">
    <img src="{IROOT}/aula_pratica_pneumonia_pg06.png" alt="Exame Fisico Toracico">
  </div>
</div>
"""
plano = plano.replace('<div class="day-tabs"', GALLERY + '<div class="day-tabs"', 1)

with open(PLANO_PATH, "w", encoding="utf-8") as f:
    f.write(plano)
print(f"  [OK] osce-plano.html: galeria de referência adicionada")

print("\nConcluido.")
