# Roadmap

<!--
Unico file per todo, idee, decisioni e diario, letto da Projects Overview
(https://alessiomartini.github.io/projects-overview/). Protocollo: templates/ROADMAP.md di projects-overview.
-->

## Pilota (capitolo 4)
- [x] Pilota sul capitolo 4: box RECALL, esercizi lunghi in appendice
- [x] Ritmo esteso a tutti i capitoli: RECALL, esercizi lunghi nell'Appendice D, sezione Set aside
- [ ] Rivedere il pilota ed estenderlo agli altri capitoli (Try first, Key concepts, Labs, note inline)

## HTML di studio
- [x] Coprire i casi mancanti: itemize dentro `answer`, tabelle, `\texorpdfstring`
- [ ] Study HTML: `\o` e le due figure TikZ di ch03 che non compilano in SVG (da verificare con pdflatex disponibile)

## Idee
- [ ] Più figure come nelle slide (TikZ/pgfplots)

- [ ] More figures like the slides (TikZ/pgfplots).

## Decisioni e cose provate

### Piloted on 2026-10-07, to extend after Alessio has looked at the pilot

Requests in `lecture-notes/chapters/ch00-requests.tex` (Chapter 3 / Introduction, all marked done for the pilot).

| Change | Done in | Remaining |
|---|---|---|
| Worked computational examples -> `tryfirst` + `solution` (printed by `\printsolutions` at chapter end) | ch03 (2 examples) | other chapters: only computations on material he already knows; idea-introducing examples stay |
| `keyformulas` -> `keyconcepts` (retrieval questions, then concepts with formula + `\cref`) | ch03 | 24 chapters still have `keyformulas` |
| `casestudy` -> `lab` (question, data in `data/`, Python steps, course results as solution, script in `labs/`) | ch05 high-yield spread | ~30 case studies |
| Course notes inline, numbered where they refer (`coursenote` inside the paragraph) | ch03 | other chapters: boxes already numbered, markers in text missing |
| Keep the pace (2026-10-15): repetitions in `recall` boxes (cyan); long exercises verbatim to `appendices/appD-exam.tex` (one `\section` per chapter), core kept inline; removed passages to `\section*{Set aside}` | whole book (2026-10-16): recalls in ch04-07, 15, 17, 19, 20; long exercises of ch03-25 in Appendix D (ch01-02 exercises already solved by Alessio, kept) | new chapters; Mehrling and dynamical-systems done too |
| Exercises: short ones after the *paragraph* they practise, long structured ones in a final `\section*{Exercises}` | ch03 | other chapters (the 2026-10-06 pass placed them per *section*) |

Each chapter needs `\printsolutions` at its end once it has a `tryfirst` or `lab`.

### Study HTML (`study/build.py`)

- New envs are rewritten by `newer_envs()` into known ones; solutions are folded `<details>` right after
  the exercise.
- Covered since 2026-10-18: lists, tables (`tabular`/`table`, `\multicolumn` as colspan, rules and `\cmidrule`
  dropped, header = rows before the first `\midrule`), `lstlisting` (as `<pre>`), `\texorpdfstring` (first argument),
  `\hyperref`, `\subsubsection`, answers with blank lines inside a paragraph; environments met inside running text
  (answer, boxes, lists) are passed to `blocks()`. Limits: tables are not numbered from the `.aux` (counted in source order);
  tables without `\midrule` have no header row; `\o` not checked; two ch03 TikZ figures still fail to compile to SVG
  (no pdflatex in this environment, not verified).

### Tried and reverted / decided against

- Links from a one-chapter PDF to another chapter's PDF (LaTeX Workshop viewer cannot follow them).
- One endless page per chapter (TeX/PDF page height limits).
- Hiding solutions in the PDF with optional-content layers: not attempted, the VS Code viewer support is
  uncertain; solutions go to the chapter end instead.

## Log
- 2026-10-18: 🤖 study HTML: liste dentro `answer`, tabelle (`table`/`tabular`, `\multicolumn`), `lstlisting`, `\texorpdfstring`, `\hyperref` e `\subsubsection` ora convertiti; 0 residui grezzi su tutti i capitoli
- 2026-10-18: FUTURE-ARCHITECTURE.md unito in ROADMAP.md (protocollo unico)
- 2026-10-16: box RECALL in 8 capitoli (ripetizioni di capitoli precedenti), 71 esercizi lunghi spostati nell'Appendice D con il nucleo breve nel testo
- 2026-10-15: creata la roadmap per Projects Overview
