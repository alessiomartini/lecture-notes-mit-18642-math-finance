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

## Versione pubblica A4
- [x] `python build.py public` -> `build/book-a4.pdf`: A4, una colonna, senza note personali (flag `\publicmode`)
- [x] Attribuzione e licenza CC BY-NC-SA 4.0 (MIT OCW) nella pagina iniziale
- [x] GitHub Action: a ogni push su main compila solo la versione A4 e la pubblica nella release `latest-pdf`
- [ ] Rivedere a occhio i 3 Overfull (pagine ~61, 409, 513) e le figure larghe
- [x] Appendice A (mappa dei file OCW): una riga "planned" da togliere o chiarire

## Idee
- [ ] Più figure come nelle slide (TikZ/pgfplots)
- [ ] Formato pagina 16:9: le note le leggo sempre da computer (oggi 25 × 29,7 cm; vale anche per il template `~/.claude/templates/lecture-notes/preamble.tex` e le altre note) (da Google Tasks, 2026-11-04)

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

### Versione pubblica (2026-11-06)

Scelta (a) della inbox di projects-overview: release pubblica, ma solo della versione A4 (il PDF di studio contiene annotazioni personali e non viene mai pubblicato). Gli stessi sorgenti, un flag `\publicmode`; i box che stavano a destra diventano box normali nel testo (i riferimenti "recalled in the margin" usano `\inmargin{}`). Le risposte (`answer`) alle mie domande non sono nella versione pubblica, anche se sono contenuto: se servono, trasformarle in `coursenote`/`remark`.

### Tried and reverted / decided against

- Links from a one-chapter PDF to another chapter's PDF (LaTeX Workshop viewer cannot follow them).
- One endless page per chapter (TeX/PDF page height limits).
- Hiding solutions in the PDF with optional-content layers: not attempted, the VS Code viewer support is
  uncertain; solutions go to the chapter end instead.

## Log
- 2026-11-07: 🤖 Appendice A: la riga "planned" (`21m383-...-lecture-28_transcript.pdf`) chiarita come trascrizione di un altro corso OCW (21M.383, dal nome del file), segnata "--"; non compilato (niente LaTeX nel sandbox).
- 2026-11-06: versione pubblica A4 di tutte le note (`python build.py public`, release `latest-pdf` aggiornata da GitHub Action ad ogni push su main); fuori note, answer, feedback, mysolution, richieste; box della colonna destra messi nel testo; template `~/.claude/templates/lecture-notes` aggiornato col flag `public`.
- 2026-11-05: tight margins and 12pt: geometry 31.5x18 cm with 0.9 left, 0.4+header top, 1.5 bottom, columns 18.8 + 10 cm, page number in the one-line header (no footer). Rebuilt; content that ran below the page edge fixed (history boxes moved or `\Needspace`, `\clearpage`, `\allowdisplaybreaks`).
- 2026-11-05: layout 16:9 (32x18 cm, PC screen), VS Code setup archived in `lecture-notes/archive/vscode/`, single build `python build.py`. Annotations read with `pdf-annotations.py` before the rebuild: none open in the current PDFs (n/a for this book). Checked the full build: no content running off the page.
- 2026-10-18: 🤖 study HTML: liste dentro `answer`, tabelle (`table`/`tabular`, `\multicolumn`), `lstlisting`, `\texorpdfstring`, `\hyperref` e `\subsubsection` ora convertiti; 0 residui grezzi su tutti i capitoli
- 2026-10-18: FUTURE-ARCHITECTURE.md unito in ROADMAP.md (protocollo unico)
- 2026-10-16: box RECALL in 8 capitoli (ripetizioni di capitoli precedenti), 71 esercizi lunghi spostati nell'Appendice D con il nucleo breve nel testo
- 2026-10-15: creata la roadmap per Projects Overview
