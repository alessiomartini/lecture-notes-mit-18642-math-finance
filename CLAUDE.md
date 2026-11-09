# Instructions for Claude

@~/.claude/templates/lecture-notes/RULES.md

LaTeX lecture notes for MIT 18.642 (2024) / 18.S096 (2013) in `lecture-notes/` (see its README), plus a
generated study HTML in `study/` (see `study/README.md`). Course material in `18.642-fall-2024/`,
`18.s096-fall-2013/` and the transcript folders is read-only source.

- Alessio annotates the PDF: before rebuilding, run `python -I E:\Alessio\Projects_Git\pdf-annotations.py` and act on the annotations (workflow in RULES.md). Old `\note{` markers in `lecture-notes/chapters/*.tex` and `main.tex` keep their meaning (the example in `main.tex`, "Your annotations", stays). Conventions: `lecture-notes/chapters/ch00-requests.tex` (top), macro reference: comments in `lecture-notes/preamble.tex`.
- Structural notes are moved verbatim to `ch00-requests.tex` as `\request{...}`; content doubts become `answer` boxes in place.
- Build: `cd lecture-notes && python build.py` (full build, refreshes `build/book.pdf`); VS Code setup archived in `lecture-notes/archive/vscode/`. Page is 31.5×18 cm: keep figures/tables < ~15 cm. Render pages with `pdftoppm` to check layout.
- Bash heredocs here eat backslashes: write Python helper scripts to the scratchpad with the Write tool.
- Chapter files are CRLF: scripts should read in text mode and write with `newline='\r\n'`.
- Long exercises verbatim → `appendices/appD-exam.tex` (core kept inline); removed passages → `\section*{Set aside}` at the chapter end.
- Pending pilot extensions (Try first, Key concepts, Labs, inline course notes, exercise placement) are
  listed in `ROADMAP.md`.

## Public A4 version (2026-11-06)

`python build.py public` -> `lecture-notes/build/book-a4.pdf` (flag `\publicmode`, block at the end of `preamble.tex`, wrapper `main-a4.tex`). Anything personal must disappear there: new personal macros/environments (notes, answers, feedback, own solutions, requests) need an empty definition in that block; new right-column environments need an inline box. Check it builds with no undefined references and that `pdftotext` shows no personal text. The workflow `.github/workflows/public-pdf.yml` publishes ONLY this PDF as release `latest-pdf`; never publish the study PDF (annotations, personal notes). Use `\inmargin{}` instead of writing "in the margin" in the text.

## Scroll book

`build/book.pdf` is the continuous-scroll book; chapter PDFs are in `lecture-notes/build/scroll/`. `python build.py` recompiles only the chapters whose .tex changed and reassembles; `python build.py ch05` forces a chapter; `python build.py all` = full latexmk build + all chapters; `python build.py pages` = paged book (`build/book-pages.pdf`, use it to check Overfull boxes). Longer chapters are split into several PDF pages. Links between chapters are not kept.
