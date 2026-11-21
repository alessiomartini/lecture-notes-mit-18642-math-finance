# MIT 18.642 / 18.S096: lecture notes

Study notes in LaTeX for *Topics in Mathematics with Applications in Finance* (MIT OpenCourseWare, 18.642 Fall 2024
and 18.S096 Fall 2013), plus a generated study HTML.

- `lecture-notes/`: the LaTeX book (25 chapters, appendices). Build, layout and macro reference: [lecture-notes/README.md](lecture-notes/README.md).
- `study/`: local HTML version of a chapter (video synced with the text, notes, exercise solutions). See [study/README.md](study/README.md).
- Course material (`18.642-fall-2024/`, `18.s096-fall-2013/`, transcripts) is kept locally as read-only source and is not part of the repo.

## Public PDF

A public A4, one-column version (no personal notes or annotations) is built by the GitHub Action
`.github/workflows/public-pdf.yml` on every push to `main` and published as the release
`latest-pdf` (see the repository's Releases) (file `lecture-notes-mit-18642-A4.pdf`). The personal study PDF is never published.

## Licence

The notes are shared under CC BY-NC-SA 4.0, like the MIT OpenCourseWare originals (see the licence note in `lecture-notes/README.md`).
