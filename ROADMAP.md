# Roadmap

<!-- Single file for todo, ideas, decisions and log, read by Projects Overview (https://alessiomartini.github.io/projects-overview/). Protocol: templates/ROADMAP.md in projects-overview. -->

## Pilot (chapter 4)
- [x] Pilot on chapter 4: RECALL box, long exercises in an appendix
- [x] Pace extended to all chapters: RECALL, long exercises in Appendix D, Set aside section
- [ ] Review the pilot and extend it to the other chapters (Try first, Key concepts, Labs, inline notes)

## Study HTML
- [x] Cover the missing cases: itemize inside `answer`, tables, `\texorpdfstring`
- [x] Study HTML: `\o` and the two ch03 TikZ figures that did not compile to SVG (to check with pdflatex available)

## Public A4 version
- [x] `python build.py public` -> `build/book-a4.pdf`: A4, one column, no personal notes (flag `\publicmode`)
- [x] Attribution and CC BY-NC-SA 4.0 licence (MIT OCW) on the title page
- [x] GitHub Action: on every push to main it builds only the A4 version and publishes it as the `latest-pdf` release
- [x] Check by eye the 3 Overfull boxes (pages ~61, 409, 513) and the wide figures (one 1.4 pt Overfull remains in ch25, negligible)
- [x] Appendix A (OCW file map): one "planned" row to remove or clarify

## Page layout
- [x] 16:9 page format: the notes are always read on a computer (was 25 x 29.7 cm; should also apply to the template `~/.claude/templates/lecture-notes/preamble.tex` and the other notes) (from Google Tasks, 2026-11-04). Done 2026-11-05 for this book: `lecture-notes/preamble.tex` has `paperwidth=31.5cm,paperheight=18cm` (see Log). The template and the other notes are tracked in their own repos.

## Ideas
- [x] Chapter 3: add a plot in the multivariate normal paragraph (level ellipses) and check whether figures are missing elsewhere (Alessio's note, see ch00)
- [ ] Chapter 3: empirical SML plot with real data (portfolios sorted by beta, e.g. French data library), not invented
- [x] Chapter 3: fix the alignment between the chi-square proof and the coursenote (the proof takes precedence)
- [x] Chapter 3: figures still missing (found by the check): (a) section "Several random variables": scatter/joint density for different correlations; ~~(b) PCA: scatter plot with the first principal component~~ done 2026-11-21 (simulated sample); ~~(c) concave utility and Jensen (risk premium)~~ done 2026-11-21; ~~(d) diversification: portfolio volatility as a function of n~~ done 2026-11-21; (e) moment generating function: graphical example of $M_X(t)$ and its domain; ~~(a) and (e) done 2026-11-21~~ (joint pmf independent vs $Y=X^2$; MGF of $N(1,1)$ and Exp(2) with tangents at 0)
- [ ] Whole book: in every important definition highlight "the idea in one line" (the philosophy of the definition) and add a tag for "important" points (Alessio's requests, see ch00)
- [ ] More figures like the slides (TikZ/pgfplots); also listed in `lecture-notes/README.md` "Future ideas"

## Decisions and things tried

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
  tables without `\midrule` have no header row; `\o` (and other text letters such as `\ae`, `\ss`) and `\inmargin` are now converted. The two ch03 TikZ figures failed because
  the chapter-local `\pgfplotsset` styles (`lawplot`, `retplot`) and the `data/*.dat` tables were not visible to the figure
  compile: now they are (checked with pdflatex 2026-11-21, all 8 ch03 figures build; ch09-fig1 needed `tabularx`).

### Public version (2026-11-06)

Option (a) from the projects-overview inbox: public release, but only of the A4 version (the study PDF contains personal annotations and is never published). Same sources, one `\publicmode` flag; boxes that were on the right become normal boxes in the text ("recalled in the margin" references use `\inmargin{}`). The answers (`answer`) to my questions are not in the public version even though they are content: if needed, turn them into `coursenote`/`remark`.

### Tried and reverted / decided against

- Links from a one-chapter PDF to another chapter's PDF (LaTeX Workshop viewer cannot follow them).
- One endless page per chapter (TeX/PDF page height limits).
- Hiding solutions in the PDF with optional-content layers: not attempted, the VS Code viewer support is
  uncertain; solutions go to the chapter end instead.

## Log
- 2026-11-21: 🤖 Docs cleanup: ROADMAP translated to English, 16:9 item ticked, duplicate figures item merged, CLAUDE.md condensed, root README added. 🤖 Read the chapter 3 notes: 13 notes answered (15 answer boxes), 8 comments marked as seen, 4 requests moved to ch00-requests (open); latexmk build without errors. Study HTML: `\o`, `\inmargin` and the ch03/ch09 TikZ figures now compile to SVG; A4 version: 2 of the 3 Overfull boxes fixed (1.4 pt remains in ch25), wide figures no longer overflow. Chapter 3: figure of the level ellipses of the bivariate normal (rho = 0, +-0.6) with the principal axes; chi-square coursenote moved into the proof (same notation, no content removed); two ch00 requests marked done; the other missing figures listed in Ideas. Added 3 figures to chapter 3: diversification (volatility vs n), PCA with the first component on a simulated sample, concave utility with Jensen, certainty equivalent and risk premium; also (a) joint pmf (independent vs dependent but uncorrelated) and (e) MGF of $N(1,1)$ and Exp(2) with tangent at 0 and pole at $t=\lambda$: chapter 3 figures complete. Study HTML: the "unresolved ref" warnings for ch03:fig-* were not a bug but an artefact, labels are read from the `.aux` files in `build/` and are resolved after a full build (no change to study/build.py). Independent check (clean sandbox): study HTML ch03 = 14 SVG figures out of 14, ch09 ok; `python build.py public` without undefined references, a single Overfull (1.4 pt, ch25). Building also needs `texlive-fonts-extra`, `texlive-plain-generic` and `tex-gyre` (packages `newpx`, `binhex`, TeX Gyre Heros): without them `pdflatex failed` for every figure.
- 2026-11-07: 🤖 Appendix A: the "planned" row (`21m383-...-lecture-28_transcript.pdf`) clarified as a transcript of another OCW course (21M.383, from the file name), marked "--"; not compiled (no LaTeX in the sandbox).
- 2026-11-06: public A4 version of all the notes (`python build.py public`, release `latest-pdf` updated by a GitHub Action on every push to main); notes, answers, feedback, mysolution and requests left out; right-column boxes put in the text; template `~/.claude/templates/lecture-notes` updated with the `public` flag.
- 2026-11-05: tight margins and 12pt: geometry 31.5x18 cm with 0.9 left, 0.4+header top, 1.5 bottom, columns 18.8 + 10 cm, page number in the one-line header (no footer). Rebuilt; content that ran below the page edge fixed (history boxes moved or `\Needspace`, `\clearpage`, `\allowdisplaybreaks`).
- 2026-11-05: layout 16:9 (32x18 cm, PC screen), VS Code setup archived in `lecture-notes/archive/vscode/`, single build `python build.py`. Annotations read with `pdf-annotations.py` before the rebuild: none open in the current PDFs (n/a for this book). Checked the full build: no content running off the page.
- 2026-10-18: 🤖 study HTML: lists inside `answer`, tables (`table`/`tabular`, `\multicolumn`), `lstlisting`, `\texorpdfstring`, `\hyperref` and `\subsubsection` now converted; 0 raw leftovers in all chapters
- 2026-10-18: FUTURE-ARCHITECTURE.md merged into ROADMAP.md (single protocol)
- 2026-10-16: RECALL box in 8 chapters (repetitions of earlier chapters), 71 long exercises moved to Appendix D with the short core kept in the text
- 2026-10-15: created the roadmap for Projects Overview
