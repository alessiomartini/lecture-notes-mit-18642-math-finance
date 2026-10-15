# Instructions for Claude

LaTeX lecture notes for MIT 18.642 (2024) / 18.S096 (2013) in `lecture-notes/` (see its README), plus a
generated study HTML in `study/` (see `study/README.md`). Course material in `18.642-fall-2024/`,
`18.s096-fall-2013/` and the transcript folders is read-only source.

- Alessio reads the PDF while Claude edits: work directly on `main`, commit + push after each verified chunk.
- "Leggi le note" = only plain `\note{` in `lecture-notes/chapters/*.tex` and `main.tex` (the example in
  `main.tex`, "Your annotations", stays). Conventions: `lecture-notes/chapters/ch00-requests.tex` (top),
  macro reference: comments in `lecture-notes/preamble.tex`.
- Structural notes are moved verbatim to `ch00-requests.tex` as `\request{...}`; content doubts become
  `answer` boxes in place. Never delete a note, never edit his `mysolution` boxes.
- Build: saving a chapter runs `.vscode/build.py` (one chapter); `python lecture-notes/.vscode/build.py full`
  for the whole book (refreshes `build/book.pdf`). Render pages with `pdftoppm` to check layout.
- Bash heredocs here eat backslashes: write Python helper scripts to the scratchpad with the Write tool.
- Chapter files are CRLF: scripts should read in text mode and write with `newline='\r\n'`.
- Keep the pace: repetitions → `recall` box; long exercises verbatim → `appendices/appD-exam.tex` (core kept
  inline); nothing deleted (removed passages → `\section*{Set aside}` at the chapter end).
- Pending pilot extensions (Try first, Key concepts, Labs, inline course notes, exercise placement) are
  listed in `FUTURE-ARCHITECTURE.md`.

## Roadmap e progressi

Questo progetto è tracciato in https://alessiomartini.github.io/projects-overview/ tramite il file `ROADMAP.md`
nella root del repo. Mantienilo aggiornato:

- Alla fine di ogni sessione di lavoro (prima del commit finale), aggiorna `ROADMAP.md`:
  - spunta (`- [x]`) i punti completati in questa sessione;
  - aggiungi come `- [ ]` i nuovi compiti emersi, nella fase giusta (titoli `##`);
  - aggiungi in cima alla sezione `## Log` una riga `- AAAA-MM-GG: <cosa è stato fatto, in una frase>`
    (se esiste già una riga con la data di oggi, estendila invece di crearne un'altra).
- Non riscrivere né riordinare le voci esistenti senza motivo; non cancellare le voci completate.
- Se `ROADMAP.md` non esiste, crealo con le fasi `## ...`, le checkbox e una sezione `## Log`.
- Includi l'aggiornamento di `ROADMAP.md` nello stesso commit del lavoro.
