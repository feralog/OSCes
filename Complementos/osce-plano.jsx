import { useState } from "react";

const plan = [
  {
    day: "25/05 — Domingo",
    label: "HOJE",
    color: "#e63946",
    provas: ["GO (amanhã)", "Pediatria (amanhã)"],
    blocos: [
      {
        hora: "Agora",
        specialty: "GO",
        temas: [
          { id: "go-partograma", nome: "Partograma", metodo: "Simulação OSCE", prioridade: "🔴" },
          { id: "go-sifilis", nome: "Sífilis", metodo: "Resumo", prioridade: "🔴" },
          { id: "go-papanicolau", nome: "Papanicolau", metodo: "Flashcards", prioridade: "🟡" },
          { id: "go-larcs", nome: "LARCs + Planejamento Familiar", metodo: "Resumo", prioridade: "🟡" },
          { id: "go-mama", nome: "Imagem de Mama", metodo: "Flashcards", prioridade: "🟡" },
        ],
      },
      {
        hora: "Noite",
        specialty: "Pediatria",
        temas: [
          { id: "ped-rn", nome: "Atendimento ao RN Normal", metodo: "Checklist", prioridade: "🔴" },
          { id: "ped-reanimacao", nome: "Reanimação Neonatal — Minuto de Ouro", metodo: "Checklist + Simulação", prioridade: "🔴" },
          { id: "ped-sifilis", nome: "Sífilis e HIV (TORCHS)", metodo: "Resumo", prioridade: "🔴" },
          { id: "ped-ictero", nome: "Icterícia Neonatal", metodo: "Resumo + Flashcards", prioridade: "🟡" },
        ],
      },
    ],
  },
  {
    day: "26/05 — Segunda",
    label: "PROVA GO + PEDS",
    color: "#e63946",
    provas: ["🏥 OSCE Ginecologia e Obstetrícia", "🏥 OSCE Pediatria"],
    blocos: [
      {
        hora: "Manhã cedo — Revisão",
        specialty: "Pediatria",
        temas: [
          { id: "ped-bronquiolite", nome: "Bronquiolite × Asma × Lactente Sibilante", metodo: "Resumo DDx", prioridade: "🔴" },
          { id: "ped-pneumonia", nome: "Pneumonia", metodo: "Flashcards", prioridade: "🟡" },
          { id: "ped-meningite", nome: "Meningite", metodo: "Flashcards", prioridade: "🟡" },
          { id: "ped-itu", nome: "ITU", metodo: "Resumo", prioridade: "🟡" },
          { id: "ped-diarreia", nome: "Diarreia Aguda", metodo: "Flashcards", prioridade: "🟡" },
          { id: "ped-exantema", nome: "Doenças Exantemáticas", metodo: "Tabela rápida", prioridade: "🟢" },
        ],
      },
      {
        hora: "À noite — Preparo Clínica Médica",
        specialty: "Clínica Médica",
        temas: [
          { id: "cm-drc", nome: "DRC", metodo: "Resumo", prioridade: "🟡" },
          { id: "cm-nefrolit", nome: "Nefrolitíase", metodo: "Flashcards", prioridade: "🟡" },
          { id: "cm-nefrotica", nome: "Síndrome Nefrótica", metodo: "Resumo", prioridade: "🟡" },
          { id: "cm-cushing", nome: "Síndrome de Cushing", metodo: "Flashcards", prioridade: "🟡" },
          { id: "cm-hiper", nome: "Hipertireoidismo", metodo: "Flashcards", prioridade: "🟡" },
          { id: "cm-drge", nome: "DRGE", metodo: "Resumo", prioridade: "🟢" },
          { id: "cm-diarreia-a", nome: "Diarreia Aguda", metodo: "Resumo", prioridade: "🟢" },
          { id: "cm-diarreia-c", nome: "Diarreia Crônica", metodo: "Resumo", prioridade: "🟢" },
          { id: "cm-ict", nome: "Icterícia", metodo: "Resumo DDx", prioridade: "🟡" },
          { id: "cm-colestase", nome: "Colestase", metodo: "Flashcards", prioridade: "🟡" },
          { id: "cm-obstip", nome: "Obstipação", metodo: "Flashcards", prioridade: "🟢" },
          { id: "cm-hemol", nome: "Anemias Hemolíticas", metodo: "Tabela", prioridade: "🟡" },
          { id: "cm-microcit", nome: "Anemias Microcíticas", metodo: "Tabela", prioridade: "🟡" },
          { id: "cm-macrocit", nome: "Anemias Macrocíticas", metodo: "Flashcards", prioridade: "🟡" },
          { id: "cm-lepto", nome: "Leptospirose", metodo: "Resumo", prioridade: "🟡" },
          { id: "cm-mening", nome: "Meningites", metodo: "Resumo DDx", prioridade: "🔴" },
          { id: "cm-mono", nome: "Síndrome da Mononucleose", metodo: "Flashcards", prioridade: "🟢" },
        ],
      },
    ],
  },
  {
    day: "27/05 — Terça",
    label: "PROVA CLÍNICA MÉDICA",
    color: "#457b9d",
    provas: ["🏥 OSCE Clínica Médica"],
    blocos: [
      {
        hora: "Manhã cedo — Revisão rápida",
        specialty: "Clínica Médica",
        temas: [
          { id: "cm-rev1", nome: "Revisão Nefro (DRC + Nefrótica + Nefrolitíase)", metodo: "Simulação OSCE", prioridade: "🔴" },
          { id: "cm-rev2", nome: "Revisão Gastro (Icterícia + Colestase + DRGE)", metodo: "Simulação OSCE", prioridade: "🔴" },
          { id: "cm-rev3", nome: "Revisão Anemias (tabela DDx)", metodo: "Flashcards", prioridade: "🟡" },
          { id: "cm-rev4", nome: "Revisão Infecto (Meningites + Lepto + Mono)", metodo: "Flashcards", prioridade: "🟡" },
        ],
      },
      {
        hora: "À noite — Preparo Cirurgia",
        specialty: "Cirurgia",
        temas: [
          { id: "cir-sonda", nome: "Sonda Vesical — Checklist completo", metodo: "Checklist", prioridade: "🔴" },
          { id: "cir-dreno", nome: "Dreno de Tórax — Checklist completo", metodo: "Checklist", prioridade: "🔴" },
          { id: "cir-sng", nome: "SNG — o que está errado?", metodo: "Checklist + Erros comuns", prioridade: "🔴" },
          { id: "cir-sutura", nome: "Sutura — indicações + execução", metodo: "Checklist + Simulação", prioridade: "🔴" },
        ],
      },
    ],
  },
  {
    day: "28/05 — Quarta",
    label: "PROVA CIRURGIA",
    color: "#2d6a4f",
    provas: ["🏥 OSCE Técnicas Cirúrgicas"],
    blocos: [
      {
        hora: "Manhã cedo — Revisão final",
        specialty: "Cirurgia",
        temas: [
          { id: "cir-rev1", nome: "Revisão sonda vesical — mental walkthrough", metodo: "Checklist", prioridade: "🔴" },
          { id: "cir-rev2", nome: "Revisão dreno de tórax — indicações + passos", metodo: "Checklist", prioridade: "🔴" },
          { id: "cir-rev3", nome: "Revisão SNG — erros clássicos", metodo: "Checklist", prioridade: "🔴" },
          { id: "cir-rev4", nome: "Revisão suturas — pontos simples, colchoeiro, etc.", metodo: "Checklist", prioridade: "🔴" },
        ],
      },
    ],
  },
];

const specialtyColors = {
  GO: { bg: "#fce4ec", text: "#880e4f", border: "#f48fb1" },
  Pediatria: { bg: "#e8f5e9", text: "#1b5e20", border: "#a5d6a7" },
  "Clínica Médica": { bg: "#e3f2fd", text: "#0d47a1", border: "#90caf9" },
  Cirurgia: { bg: "#fff8e1", text: "#e65100", border: "#ffcc02" },
};

const methodIcons = {
  "Simulação OSCE": "🎭",
  "Resumo": "📋",
  "Flashcards": "🃏",
  "Checklist": "✅",
  "Resumo DDx": "🔍",
  "Tabela": "📊",
  "Tabela rápida": "📊",
  "Checklist + Simulação": "✅🎭",
  "Checklist + Erros comuns": "✅⚠️",
  "Resumo + Flashcards": "📋🃏",
  "Simulação OSCE": "🎭",
};

export default function OSCEPlanner() {
  const [checked, setChecked] = useState({});
  const [activeDay, setActiveDay] = useState(0);

  const toggle = (id) => setChecked((prev) => ({ ...prev, [id]: !prev[id] }));

  const totalAll = plan.flatMap(d => d.blocos.flatMap(b => b.temas)).length;
  const doneAll = Object.values(checked).filter(Boolean).length;
  const pct = Math.round((doneAll / totalAll) * 100);

  const dayData = plan[activeDay];

  const dayTotal = dayData.blocos.flatMap(b => b.temas).length;
  const dayDone = dayData.blocos.flatMap(b => b.temas).filter(t => checked[t.id]).length;

  return (
    <div style={{
      fontFamily: "'Georgia', 'Times New Roman', serif",
      background: "#fafaf8",
      minHeight: "100vh",
      padding: "0 0 60px 0",
      color: "#1a1a1a",
    }}>
      {/* Header */}
      <div style={{
        background: "#1a1a1a",
        color: "#f5f0e8",
        padding: "28px 24px 20px",
        position: "sticky",
        top: 0,
        zIndex: 100,
        boxShadow: "0 2px 20px rgba(0,0,0,0.3)",
      }}>
        <div style={{ maxWidth: 720, margin: "0 auto" }}>
          <div style={{ fontSize: 11, letterSpacing: 3, color: "#a89f8c", textTransform: "uppercase", marginBottom: 4 }}>
            OSCE 2026
          </div>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-end" }}>
            <div>
              <h1 style={{ margin: 0, fontSize: 22, fontWeight: "normal", letterSpacing: "-0.5px" }}>
                Plano de Estudos
              </h1>
              <div style={{ fontSize: 12, color: "#a89f8c", marginTop: 2 }}>26–28 de maio • 4 provas práticas</div>
            </div>
            <div style={{ textAlign: "right" }}>
              <div style={{ fontSize: 28, fontWeight: "bold", color: pct > 60 ? "#7ecf8a" : "#f4c842" }}>{pct}%</div>
              <div style={{ fontSize: 11, color: "#a89f8c" }}>{doneAll}/{totalAll} temas</div>
            </div>
          </div>
          {/* Progress bar */}
          <div style={{ height: 3, background: "#333", marginTop: 16, borderRadius: 2, overflow: "hidden" }}>
            <div style={{ height: "100%", width: `${pct}%`, background: "linear-gradient(90deg, #f4c842, #7ecf8a)", transition: "width 0.4s ease", borderRadius: 2 }} />
          </div>
        </div>
      </div>

      <div style={{ maxWidth: 720, margin: "0 auto", padding: "0 16px" }}>
        {/* Day tabs */}
        <div style={{ display: "flex", gap: 8, marginTop: 20, marginBottom: 4, overflowX: "auto", paddingBottom: 4 }}>
          {plan.map((d, i) => {
            const dt = d.blocos.flatMap(b => b.temas).length;
            const dd = d.blocos.flatMap(b => b.temas).filter(t => checked[t.id]).length;
            const isActive = activeDay === i;
            return (
              <button
                key={i}
                onClick={() => setActiveDay(i)}
                style={{
                  border: isActive ? `2px solid ${d.color}` : "2px solid #ddd",
                  background: isActive ? d.color : "#fff",
                  color: isActive ? "#fff" : "#555",
                  borderRadius: 8,
                  padding: "8px 14px",
                  cursor: "pointer",
                  whiteSpace: "nowrap",
                  fontSize: 12,
                  fontFamily: "inherit",
                  transition: "all 0.2s",
                }}
              >
                <div style={{ fontWeight: "bold", fontSize: 13 }}>{d.day.split(" — ")[0]}</div>
                <div style={{ fontSize: 10, opacity: 0.85, marginTop: 2 }}>{dd}/{dt}</div>
              </button>
            );
          })}
        </div>

        {/* Day header */}
        <div style={{
          background: "#fff",
          border: `1px solid #e8e3da`,
          borderLeft: `4px solid ${dayData.color}`,
          borderRadius: "0 8px 8px 0",
          padding: "16px 20px",
          marginBottom: 16,
          marginTop: 8,
        }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
            <div>
              <div style={{ fontSize: 11, letterSpacing: 2, color: dayData.color, textTransform: "uppercase", fontWeight: "bold" }}>
                {dayData.label}
              </div>
              <div style={{ fontSize: 17, marginTop: 2, fontStyle: "italic" }}>{dayData.day}</div>
            </div>
            <div style={{
              background: dayData.color,
              color: "#fff",
              borderRadius: 20,
              padding: "4px 12px",
              fontSize: 13,
              fontWeight: "bold",
            }}>
              {dayDone}/{dayTotal}
            </div>
          </div>
          {dayData.provas.map((p, i) => (
            <div key={i} style={{ marginTop: 6, fontSize: 13, color: "#444" }}>{p}</div>
          ))}
        </div>

        {/* Blocos */}
        {dayData.blocos.map((bloco, bi) => {
          const sc = specialtyColors[bloco.specialty] || { bg: "#f5f5f5", text: "#333", border: "#ccc" };
          const bTotal = bloco.temas.length;
          const bDone = bloco.temas.filter(t => checked[t.id]).length;
          return (
            <div key={bi} style={{ marginBottom: 20 }}>
              {/* Bloco header */}
              <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 10 }}>
                <div style={{
                  background: sc.bg,
                  color: sc.text,
                  border: `1px solid ${sc.border}`,
                  borderRadius: 6,
                  padding: "3px 10px",
                  fontSize: 11,
                  fontWeight: "bold",
                  letterSpacing: 1,
                  textTransform: "uppercase",
                }}>
                  {bloco.specialty}
                </div>
                <div style={{ fontSize: 12, color: "#888", fontStyle: "italic" }}>{bloco.hora}</div>
                <div style={{ marginLeft: "auto", fontSize: 11, color: "#aaa" }}>{bDone}/{bTotal}</div>
              </div>

              {/* Temas */}
              <div style={{ display: "flex", flexDirection: "column", gap: 6 }}>
                {bloco.temas.map((tema) => {
                  const done = checked[tema.id];
                  return (
                    <div
                      key={tema.id}
                      onClick={() => toggle(tema.id)}
                      style={{
                        display: "flex",
                        alignItems: "center",
                        gap: 12,
                        background: done ? "#f0faf1" : "#fff",
                        border: `1px solid ${done ? "#b7dfbb" : "#e8e3da"}`,
                        borderRadius: 8,
                        padding: "10px 14px",
                        cursor: "pointer",
                        transition: "all 0.15s",
                        opacity: done ? 0.7 : 1,
                      }}
                    >
                      {/* Checkbox */}
                      <div style={{
                        width: 20,
                        height: 20,
                        borderRadius: 4,
                        border: `2px solid ${done ? "#4caf50" : "#ccc"}`,
                        background: done ? "#4caf50" : "transparent",
                        display: "flex",
                        alignItems: "center",
                        justifyContent: "center",
                        flexShrink: 0,
                        transition: "all 0.15s",
                      }}>
                        {done && <span style={{ color: "#fff", fontSize: 12, lineHeight: 1 }}>✓</span>}
                      </div>

                      {/* Priority */}
                      <span style={{ fontSize: 14, flexShrink: 0 }}>{tema.prioridade}</span>

                      {/* Nome */}
                      <div style={{ flex: 1 }}>
                        <div style={{
                          fontSize: 14,
                          color: done ? "#888" : "#1a1a1a",
                          textDecoration: done ? "line-through" : "none",
                          fontFamily: "inherit",
                        }}>
                          {tema.nome}
                        </div>
                      </div>

                      {/* Método */}
                      <div style={{
                        background: sc.bg,
                        color: sc.text,
                        border: `1px solid ${sc.border}`,
                        borderRadius: 20,
                        padding: "2px 10px",
                        fontSize: 10,
                        whiteSpace: "nowrap",
                        flexShrink: 0,
                      }}>
                        {methodIcons[tema.metodo] || "📚"} {tema.metodo}
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>
          );
        })}

        {/* Legenda prioridade */}
        <div style={{
          background: "#fff",
          border: "1px solid #e8e3da",
          borderRadius: 8,
          padding: "14px 16px",
          marginTop: 8,
        }}>
          <div style={{ fontSize: 11, color: "#aaa", letterSpacing: 1, textTransform: "uppercase", marginBottom: 8 }}>
            Legenda de Prioridade
          </div>
          <div style={{ display: "flex", gap: 20, fontSize: 12, color: "#555" }}>
            <span>🔴 Alta — maior chance de cair</span>
            <span>🟡 Média — provável</span>
            <span>🟢 Baixa — bom ter</span>
          </div>
        </div>

        {/* CTA */}
        <div style={{
          background: "#1a1a1a",
          color: "#f5f0e8",
          borderRadius: 10,
          padding: "16px 20px",
          marginTop: 16,
          fontSize: 13,
          lineHeight: 1.7,
        }}>
          <div style={{ fontWeight: "bold", marginBottom: 4, fontSize: 14 }}>💡 Como usar</div>
          <div style={{ color: "#c8c0b0" }}>
            Marque um tema e diga <em style={{ color: "#f4c842" }}>"vamos estudar [tema]"</em> — eu simulo a estação OSCE, faço flashcards ou monto o resumo conforme o método indicado.
          </div>
        </div>
      </div>
    </div>
  );
}
