"""
Injeta imagens nos HTML de topicos (anchors <h2 class="section-heading">).
Executar APOS _injetar_imagens.py (que ja fez os .md).
"""
import os

BASE = r"D:/Arquivos/Documentos/Faculdade/OSEC/Github/OSCes"
REL  = "../../Complementos/imagens"

def fig(fname, alt, caption):
    return (
        f'\n<figure style="margin:22px 0;text-align:center">'
        f'<img src="{REL}/{fname}" alt="{alt}" '
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
            print(f"  [MISS] {os.path.basename(path)}: '{anchor[:70]}'")
            continue
        txt = txt.replace(anchor, anchor + html, 1)
        ok += 1
    with open(path, "w", encoding="utf-8") as f:
        f.write(txt)
    print(f"  [OK]  {os.path.basename(path)}: {ok}/{len(items)}")

PED = f"{BASE}/osce_materiais/Pediatria"

# ── Doenças Exantemáticas ─────────────────────────────────────
print("\n── doencas_exantematicas.html ──")
patch(f"{PED}/doencas_exantematicas.html", [
    (
        h2("TABELA-MESTRE — Diagnóstico Diferencial dos Exantemas"),
        fig("playbook_cl_nico_de_exantemas_pg06.png",
            "Foto exantema eritematoso",
            "Exantema morbiliforme: maculopápulas confluentes avermelhadas")
        + fig("playbook_cl_nico_de_exantemas_pg08.png",
              "Bebe com exantema",
              "Exantema pápulo-vesicular em lactente — polimorfismo lesional típico da varicela")
    ),
    (
        h2("CLASSIFICAÇÃO DOS TIPOS DE EXANTEMA"),
        fig("playbook_cl_nico_de_exantemas_pg11.png",
            "Mapeamento anatomico exantemas",
            "Mapeamento anatômico: Escarlatina (Filatov, Pastia, língua em framboesa) × Eritema Infeccioso (fácies esbofeteada, rendilhado)")
    ),
    (
        h2("ESTAÇÃO 3 — Caso: Escarlatina (Playbook)"),
        fig("playbook_cl_nico_de_exantemas_pg12.png",
            "Cinetica febre vs exantema",
            "Cinética febre × exantema: Escarlatina (junto à febre) × Eritema Infeccioso (surge após queda da febre)")
        + fig("playbook_cl_nico_de_exantemas_pg13.png",
              "Arvore de raciocinio clinico",
              "Raciocínio clínico: toxemia + odinofagia + exantema lixa → Escarlatina | bom estado + fácies → Eritema Infeccioso")
        + fig("playbook_cl_nico_de_exantemas_pg14.png",
              "Matriz DDx Escarlatina vs Eritema Infeccioso",
              "DDx: Escarlatina (S. pyogenes, antibiótico obrigatório) × Eritema Infeccioso (Parvovírus B19, autolimitado)")
    ),
])

# ── Sífilis / HIV / TORCHS ────────────────────────────────────
print("\n── sifilis_hiv_torchs.html ──")
patch(f"{PED}/sifilis_hiv_torchs.html", [
    (
        h2("Sífilis Congênita — Visão Neonatal (ver também <code>sifilis.md</code> em GO)"),
        fig("protocolo_s_filis_e_hiv_neonatal_pg09.png",
            "Fluxograma triagem sifilis congenita",
            "Triagem: NUNCA usar cordão umbilical (falso-reagente). Mãe tratada + RN assintomático + VDRL RN < materno → ambulatório")
        + fig("protocolo_s_filis_e_hiv_neonatal_pg11.png",
              "LCR criterios neurologicos sifilis",
              "Neurossífilis (até 60% dos casos): VDRL liquórico reagente OU >25 céls OU proteínas >150 mg/dL → internação 10 dias")
    ),
    (
        h2("HIV na Gestação e no RN"),
        fig("protocolo_s_filis_e_hiv_neonatal_pg04.png",
            "Nascimento biosseguranca HIV",
            "Parto com HIV: parto empelicado, clampeamento imediato, banho. NUNCA: ordenha do cordão, aspiração de rotina")
        + fig("protocolo_s_filis_e_hiv_neonatal_pg05.png",
              "Via de parto carga viral",
              "Decisão via parto: CV <1.000 cópias/mL → vaginal | CV ≥1.000 ou desconhecida → cesárea ≥38 sem + AZT intraparto")
        + fig("protocolo_s_filis_e_hiv_neonatal_pg07.png",
              "Conduta HIV alojamento conjunto",
              "Alojamento conjunto: AZT neonatal nas primeiras 4h + amamentação CONTRAINDICADA + fórmula até 6 meses")
        + fig("protocolo_s_filis_e_hiv_neonatal_pg13.png",
              "Seguimento HIV pos-alta timeline",
              "Seguimento: nascimento → 2 sem → 4-6 sem → 12 sem. Alta: 18 meses com sorologia negativa ou 2 CV indetectáveis")
    ),
])

# ── Reanimação Neonatal ───────────────────────────────────────
print("\n── reanimacao_neonatal.html ──")
patch(f"{PED}/reanimacao_neonatal.html", [
    (
        h2("Fluxograma de Decisão — ≥ 34 Semanas"),
        fig("atendimento_ao_rece_m_nascido_2026_1_pg06.png",
            "Fluxograma 3 perguntas vitais",
            "3 Perguntas Vitais: todas SIM → pele-a-pele | qualquer NÃO → mesa de reanimação imediatamente")
        + fig("atendimento_ao_rece_m_nascido_2026_1_pg07.png",
              "Minuto de Ouro reanimacao",
              "Minuto de Ouro: VPP iniciada no 1º minuto de vida. Gatilho: qualquer NÃO (prematuridade, apneia, hipotonia)")
        + fig("atendimento_ao_rece_m_nascido_2026_1_pg08.png",
              "Passos iniciais 30 segundos",
              "Primeiros 30s: Aquecer → Secar → Posicionar → Aspirar (só se obstrução visível). Reavaliar FC + respiração")
    ),
    (
        h2("Checklist — VPP (Ventilação com Pressão Positiva)"),
        fig("atendimento_ao_rece_m_nascido_2026_1_pg09.png",
            "Avaliacao vitalidade indicacao VPP",
            "VPP indicada: FC <100 bpm OU apneia/respiração irregular após passos iniciais")
        + fig("atendimento_ao_rece_m_nascido_2026_1_pg11.png",
              "Alvos saturacao O2 pre-ductal",
              "Alvos SatO₂ pré-ductal: 1 min=70-80% | 5 min=80-90% | 10 min=85-95%. Não ofertar O₂ extra dentro dos alvos")
        + fig("atendimento_ao_rece_m_nascido_2026_1_pg13.png",
              "Algoritmo SBP 2022 completo",
              "Algoritmo SBP 2022: fluxo completo — passos iniciais → VPP → massagem 3:1 → adrenalina EV/traqueal")
    ),
])

# ── Atendimento ao RN Normal ──────────────────────────────────
print("\n── atendimento_rn_normal.html ──")
patch(f"{PED}/atendimento_rn_normal.html", [
    (
        h2("Checklist — Recepção do RN ≥ 34 Semanas"),
        fig("atendimento_ao_rece_m_nascido_2026_1_pg06.png",
            "Fluxograma 3 perguntas avaliacao RN",
            "Avaliação ao nascer: A termo? Respirando/chorando? Tônus? — SIM a todas → pele-a-pele com a mãe")
        + fig("atendimento_ao_rece_m_nascido_2026_1_pg08.png",
              "Passos iniciais RN",
              "Primeiros 30s: aquecer → secar → posicionar → aspirar (condicional). Reavaliação imediata em seguida")
    ),
])

# ── Bronquiolite × Asma ───────────────────────────────────────
print("\n── bronquiolite_asma_lactente_sibilante.html ──")
patch(f"{PED}/bronquiolite_asma_lactente_sibilante.html", [
    (
        h2("ESTAÇÃO 1 — Caso Clínico: 4 Meses, Primeiro Episódio de Sibilância"),
        fig("bronquiolite_x_lactente_sibilnate_x_asma_pg13.png",
            "Bronquiolite Viral Aguda fatores de risco",
            "BVA: 1º episódio de sibilância em <24 meses, VSR em 50-70% dos casos. Diagnóstico CLÍNICO — sem RX de rotina")
        + fig("bronquiolite_x_lactente_sibilnate_x_asma_pg09.png",
              "Exame fisico comparativo BVA vs lactente sibilante",
              "Exame físico: Caso Azul (BVA) — tiragem + sibilos difusos + grave | Caso Laranja (LS) — expiração prolongada + compensado")
    ),
    (
        h2("ESTAÇÃO 2 — Caso Clínico: 9 Meses, Episódios Recorrentes"),
        fig("bronquiolite_x_lactente_sibilnate_x_asma_pg11.png",
            "Tabela DDx bronquiolite vs lactente sibilante",
            "DDx fundamental: BVA (1º episódio, VSR, hipóxia, sem histórico familiar) × Lactente Sibilante (recorrente, atopia, compensado)")
    ),
    (
        h2("ESTAÇÃO 3 — Diagnóstico Diferencial: Asma"),
        fig("bronquiolite_x_lactente_sibilnate_x_asma_pg16.png",
            "4 fenotipos sibilancia PRACTALL Martinez",
            "4 Fenótipos: Transitória (resolução <3 anos) | Não-Atópica (viral) | Atópica Persistente (= asma) | Intermitente Grave")
        + fig("bronquiolite_x_lactente_sibilnate_x_asma_pg19.png",
              "Terapia manutencao asma via atopica viral",
              "Manutenção: Via Atópica → CI inalatório + β2 longa | Via Viral → macrolídeos (azitromicina promissora, controversa)")
    ),
])

# ── Pneumonia ─────────────────────────────────────────────────
print("\n── pneumonia.html ──")
patch(f"{PED}/pneumonia.html", [
    (
        h2("Diagnóstico Clínico — Tríade Principal"),
        fig("aula_pratica_pneumonia_pg06.png",
            "Mapeamento exame fisico toracico pneumonia",
            "Exame torácico na pneumonia: Inspeção (tiragem) → Palpação (FTV↓) → Percussão (macicez) → Ausculta (MV↓, broncofonia↓)")
    ),
    (
        h3("Pneumonias Atípicas"),
        fig("aula_pratica_pneumonia_pg18.png",
            "Pneumonia necrosante MRSA PVL",
            "Pneumonia Necrosante: consolidação → liquefação → pneumatocele. S. aureus PVL+ (MRSA): fístula 17-67%, empiema 63-100%")
    ),
    (
        h2("Classificação e Conduta — OMS Simplificada"),
        fig("aula_pratica_pneumonia_pg22.png",
            "Guia dosagens IV antibioticos pneumonia pediatrica",
            "Dosagens IV: Ampicilina 150-200 mg/kg/dia | Pen. Cristalina 200-250 mil U/kg/dia | Ceftriaxona 50-100 mg/kg/dia")
    ),
])

print("\nConcluido.")
