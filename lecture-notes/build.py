r"""Build the book. Run from lecture-notes/.

  python build.py           # scroll book: recompile only the chapters whose .tex changed, reassemble build/book.pdf
  python build.py ch05      # scroll book: recompile only chapter(s) matching ch05, reassemble
  python build.py all       # full latexmk build (cross-references) + every chapter + reassemble
  python build.py pages     # only the normal paged book: latexmk -> build/main.pdf, copied to build/book-pages.pdf
  python build.py public    # PUBLIC A4 book (one column, nothing personal): build/public/ -> build/book-a4.pdf

build/book.pdf is the continuous-scroll book (one long page per chapter, bookmarks): what sync-pdfs.ps1 copies.
The first time (or after adding labels/chapters) run "python build.py all". See scroll.py.
Check overfull boxes in the paged build:  grep "Overfull" build/main.log
"""
import os, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
args = sys.argv[1:]


def pages():
    code = subprocess.call(['latexmk', '-pdf', '-outdir=build', '-interaction=nonstopmode', '-file-line-error', 'main.tex'])
    if code == 0:
        try:
            shutil.copyfile('build/main.pdf', 'build/book-pages.pdf')
        except OSError as e:
            print(f'Could not update build/book-pages.pdf: {e}')
    return code


def public():
    # own output folder: the \include d chapters write their .aux next to the output, the study build must not see them
    for d in ('', 'chapters', 'appendices'):
        os.makedirs(os.path.join('build', 'public', d), exist_ok=True)
    code = subprocess.call(['latexmk', '-pdf', '-outdir=build/public', '-interaction=nonstopmode', '-file-line-error', 'main-a4.tex'])
    if code == 0:
        shutil.copyfile('build/public/main-a4.pdf', 'build/book-a4.pdf')
        print('-> build/book-a4.pdf')
    return code


if args == ['public']:
    sys.exit(public())
if args == ['pages']:
    sys.exit(pages())
if args == ['all'] or not os.path.exists('build/main.aux'):
    if pages():
        sys.exit(1)
    args = ['all']
sys.exit(subprocess.call([sys.executable, 'scroll.py', *args]))
