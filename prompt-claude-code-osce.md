# PROMPT — Claude Code: Gerador de Material OSCE

\---

## CONTEXTO

Você é um assistente de estudos para um estudante de medicina que tem provas práticas (OSCE) nos dias 26, 27 e 28 de maio. O estudante forneceu seus materiais de referência (PDFs, slides, anotações). Sua tarefa é ler esses materiais e gerar automaticamente, para cada tema listado, o tipo de material de estudo correspondente.

\---

## INSTRUÇÕES GERAIS

1. **Leia todos os arquivos de referência fornecidos antes de gerar qualquer material.**
2. Todo conteúdo gerado deve ser **baseado nos materiais fornecidos** — não invente informações, não preencha lacunas com conhecimento genérico sem indicar que o material não cobriu aquele ponto.
3. Se um tema não estiver coberto em nenhum arquivo, sinalize: `⚠️ Tema não encontrado nos materiais fornecidos.`
4. Gere os arquivos de saída dentro de uma pasta chamada `osce\_materiais/`, organizada por especialidade.
5. Use **Markdown** para todos os arquivos de texto. Use **HTML** para os flashcards interativos.

\---

## ESTRUTURA DE PASTAS DE SAÍDA

```
osce\_materiais/
├── GO/
│   ├── partograma.md
│   ├── sifilis.md
│   ├── papanicolau.md
│   ├── larcs\_planejamento\_familiar.md
│   └── imagem\_mama.md
├── Pediatria/
│   ├── atendimento\_rn\_normal.md
│   ├── reanimacao\_neonatal.md
│   ├── sifilis\_hiv\_torchs.md
│   ├── ictericia\_neonatal.md
│   ├── bronquiolite\_asma\_lactente\_sibilante.md
│   ├── pneumonia.md
│   ├── meningite.md
│   ├── itu.md
│   ├── diarreia\_aguda.md
│   └── doencas\_exantematicas.md
├── Clinica\_Medica/
│   ├── Nefro/
│   │   ├── drc.md
│   │   ├── nefrolitiase.md
│   │   └── sindrome\_nefrotica.md
│   ├── Endocrino/
│   │   ├── sindrome\_cushing.md
│   │   └── hipertireoidismo.md
│   ├── Gastro/
│   │   ├── drge.md
│   │   ├── diarreia\_aguda.md
│   │   ├── diarreia\_cronica.md
│   │   ├── ictericia.md
│   │   ├── colestase.md
│   │   └── obstipacao.md
│   ├── Hemato/
│   │   ├── anemias\_hemoliticas.md
│   │   ├── anemias\_microciticas.md
│   │   └── anemias\_macrociticas.md
│   └── Infecto/
│       ├── leptospirose.md
│       ├── meningites.md
│       └── sindrome\_mononucleose.md
├── Cirurgia/
│   ├── sonda\_vesical.md
│   ├── dreno\_torax.md
│   ├── sonda\_nasogastrica.md
│   └── suturas.md
└── flashcards/
    └── \[um arquivo HTML por especialidade]
```

\---

## TIPOS DE MATERIAL — TEMPLATES

### 1\. RESUMO CLÍNICO (para temas de anamnese/diagnóstico)

Use este template para: DRC, Nefrolitíase, Síndrome Nefrótica, Cushing, Hipertireoidismo, DRGE, Diarreias, Icterícia, Colestase, Obstipação, Leptospirose, Meningites, Mononucleose, Pneumonia, ITU, Bronquiolite×Asma, Sífilis (GO e Peds), Papanicolau, Imagem de Mama, Icterícia Neonatal, TORCHS.

```markdown
# \[NOME DO TEMA]
> Especialidade | Método: Resumo

## Definição
\[1-2 frases do material]

## Epidemiologia / Fatores de Risco
- \[bullet points]

## Fisiopatologia (se relevante para OSCE)
- \[bullet points curtos]

## Quadro Clínico
| Sintoma/Sinal | Detalhe |
|---|---|
| | |

## Diagnóstico
- Critérios: \[...]
- Exames-chave: \[...]
- Valores de referência importantes: \[...]

## Diagnóstico Diferencial
| Condição | Como diferenciar |
|---|---|
| | |

## Conduta / Tratamento
1. \[Passo 1]
2. \[Passo 2]

## Perguntas que o professor provavelmente vai fazer
1. \[Pergunta] → \[Resposta esperada curta]
2. \[Pergunta] → \[Resposta esperada curta]
3. \[Pergunta] → \[Resposta esperada curta]

## Alertas OSCE ⚠️
- \[Erros comuns ou pontos críticos de avaliação]
```

\---

### 2\. CHECKLIST DE PROCEDIMENTO (para temas cirúrgicos e de execução)

Use este template para: Sonda Vesical, Dreno de Tórax, SNG, Suturas, Atendimento ao RN, Reanimação Neonatal.

```markdown
# \[NOME DO PROCEDIMENTO] — Checklist OSCE
> Especialidade | Método: Checklist

## Indicações
- \[...]

## Contraindicações
- \[...]

## Material necessário
- \[ ] Item 1
- \[ ] Item 2
- \[ ] ...

## Passo a Passo
- \[ ] \*\*1.\*\* \[Ação]
- \[ ] \*\*2.\*\* \[Ação]
- \[ ] \*\*3.\*\* \[Ação]
- \[ ] ...

## Erros Clássicos em OSCE (o que costuma estar errado na estação)
1. \[Erro 1] — Por que é errado: \[...]
2. \[Erro 2] — Por que é errado: \[...]

## Pontos críticos de avaliação
- \[O que o examinador vai observar especificamente]

## Perguntas teóricas associadas
1. \[Pergunta] → \[Resposta]
```

**Instruções específicas para SUTURAS:**

* Gere uma tabela de indicações por tipo de sutura (simples, colchoeiro horizontal, colchoeiro vertical, chuleio simples, chuleio ancorado, Donati)
* Inclua: indicação clínica, camadas adequadas, material recomendado, vantagem principal
* Adicione um bloco "Como descrever ao professor durante a execução" com frases-modelo

**Instruções específicas para SNG (estação de erros):**

* Liste os 10 erros mais comuns na passagem de SNG em formato de tabela: \[Erro] | \[Consequência] | \[Correto seria...]

\---

### 3\. SIMULAÇÃO OSCE (para temas com alta probabilidade de avaliação clínica ativa)

Use este template para: Partograma, Reanimação Neonatal, LARCs/Planejamento Familiar, Doenças Exantemáticas, Anemias (DDx), Meningites (DDx), Bronquiolite×Asma×Lactente Sibilante.

```markdown
# \[TEMA] — Simulação de Estação OSCE
> Especialidade | Método: Simulação

---

## ESTAÇÃO 1: \[título do cenário]

\*\*\[PROFESSOR]:\*\* \[Apresentação do caso clínico em 3-5 linhas: paciente, queixa, dados objetivos]

\*\*Pergunta 1:\*\* \[Pergunta direta do professor]
> \*\*Resposta esperada:\*\* \[Resposta objetiva]

\*\*Pergunta 2:\*\* \[Pergunta de conduta ou diagnóstico]
> \*\*Resposta esperada:\*\* \[Resposta objetiva]

\*\*Pergunta 3:\*\* \[Pergunta de complicação ou dado adicional]
> \*\*Resposta esperada:\*\* \[Resposta objetiva]

---

## ESTAÇÃO 2: \[segundo cenário — variação do tema]
\[repetir estrutura]

---

## ESTAÇÃO 3: \[terceiro cenário]
\[repetir estrutura]

---

## Pontos que o professor vai checar
- \[ ] \[Critério 1]
- \[ ] \[Critério 2]
- \[ ] \[Critério 3]
```

**Instrução específica para PARTOGRAMA:**

* Gere pelo menos 3 cenários distintos com dados de partograma (DU, BCF, plano de De Lee, apagamento, dilatação, variedade de posição)
* Cada cenário deve ter: leitura do partograma → diagnóstico → conduta
* Inclua pelo menos: 1 caso de fase ativa normal, 1 caso de parada de progressão, 1 caso de sofrimento fetal

**Instrução específica para DOENÇAS EXANTEMÁTICAS:**

* Gere uma tabela-mestre com: Doença | Agente | Período de incubação | Tipo de exantema | Distribuição | Enantema | Sinal patognomônico | Tratamento | Notificação compulsória?
* Cubra: Sarampo, Rubéola, Varicela, Escarlatina, Eritema infeccioso, Exantema súbito, Mononucleose (se exantema)

**Instrução específica para ANEMIAS:**

* Gere tabela DDx: Tipo | VCM | HCM | Reticulócitos | Achado-chave | Causa principal | Tratamento
* Cubra: Ferropriva, Talassemia minor, Doença crônica, B12, Folato, Hemolítica autoimune, Hereditária (esferocitose)

\---

### 4\. FLASHCARDS INTERATIVOS (HTML)

Para cada especialidade, gere um arquivo HTML com flashcards interativos cobrindo todos os temas daquela especialidade.

**Especificações técnicas:**

* HTML, CSS e JavaScript em arquivo único
* Layout: cartão com frente/verso, virar com clique
* Navegação: botões "Anterior" e "Próximo"
* Contador de progresso (ex: "Card 3 de 24")
* Botões de avaliação: "Sabia ✓" e "Rever ✗" — ao final, mostra quais precisa revisar
* Design simples, legível em tela de celular (responsivo)
* Cada card: **Frente** = pergunta ou termo; **Verso** = resposta objetiva (máximo 5 linhas)

**Quantidade mínima de flashcards por especialidade:**

* GO: 20 cards
* Pediatria: 30 cards
* Clínica Médica: 50 cards (subdividir por área se necessário)
* Cirurgia: 20 cards

\---

## LISTA COMPLETA DE TEMAS E MÉTODO

|Especialidade|Tema|Template a usar|
|-|-|-|
|GO|Partograma|Simulação OSCE|
|GO|Sífilis|Resumo Clínico|
|GO|Papanicolau|Resumo Clínico|
|GO|LARCs + Planejamento Familiar|Simulação OSCE|
|GO|Imagem de Mama|Resumo Clínico|
|Pediatria|Atendimento ao RN Normal|Checklist|
|Pediatria|Reanimação Neonatal — Minuto de Ouro|Checklist + Simulação|
|Pediatria|Sífilis e HIV — TORCHS|Resumo Clínico|
|Pediatria|Icterícia Neonatal|Resumo Clínico|
|Pediatria|Bronquiolite × Asma × Lactente Sibilante|Simulação OSCE|
|Pediatria|Pneumonia|Resumo Clínico|
|Pediatria|Meningite|Resumo Clínico|
|Pediatria|ITU|Resumo Clínico|
|Pediatria|Diarreia Aguda|Resumo Clínico|
|Pediatria|Doenças Exantemáticas|Simulação OSCE (tabela-mestre)|
|CM — Nefro|DRC|Resumo Clínico|
|CM — Nefro|Nefrolitíase|Resumo Clínico|
|CM — Nefro|Síndrome Nefrótica|Resumo Clínico|
|CM — Endocrino|Síndrome de Cushing|Resumo Clínico|
|CM — Endocrino|Hipertireoidismo|Resumo Clínico|
|CM — Gastro|DRGE|Resumo Clínico|
|CM — Gastro|Diarreia Aguda|Resumo Clínico|
|CM — Gastro|Diarreia Crônica|Resumo Clínico|
|CM — Gastro|Icterícia|Resumo Clínico|
|CM — Gastro|Colestase|Resumo Clínico|
|CM — Gastro|Obstipação|Resumo Clínico|
|CM — Hemato|Anemias Hemolíticas|Simulação OSCE (tabela DDx)|
|CM — Hemato|Anemias Microcíticas|Simulação OSCE (tabela DDx)|
|CM — Hemato|Anemias Macrocíticas|Resumo Clínico|
|CM — Infecto|Leptospirose|Resumo Clínico|
|CM — Infecto|Meningites|Simulação OSCE|
|CM — Infecto|Síndrome da Mononucleose|Resumo Clínico|
|Cirurgia|Sonda Vesical|Checklist|
|Cirurgia|Dreno de Tórax|Checklist|
|Cirurgia|SNG — erros na execução|Checklist (foco em erros)|
|Cirurgia|Suturas|Checklist + Tabela de indicações|

\---

## ORDEM DE EXECUÇÃO RECOMENDADA

Execute nesta ordem (por urgência das provas):

```
1. GO/ — todos os temas (prova em 26/05)
2. Pediatria/ — todos os temas (prova em 26/05)
3. flashcards/GO.html
4. flashcards/Pediatria.html
5. Clinica\_Medica/ — todos os temas (prova em 27/05)
6. flashcards/Clinica\_Medica.html
7. Cirurgia/ — todos os temas (prova em 28/05)
8. flashcards/Cirurgia.html
```

\---

## CONTROLE DE QUALIDADE

Ao final de cada arquivo gerado, adicione um bloco:

```markdown
---
## Fonte
- Gerado a partir de: \[nome do arquivo de referência usado]
- Seções consultadas: \[página ou seção específica]
- Gaps identificados: \[tópicos não cobertos pelo material]
```

\---

## 

