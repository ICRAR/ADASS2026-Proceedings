<!--
Title this pull request "YOURPID: Your paper title", with your own PID.
Tick each box by changing [ ] to [x]. The editors review your paper here.
-->

**PID:** <!-- your PID, from the list of papers in the README -->

### One paper, from my fork

- [ ] This pull request comes from a branch on **my own fork** of this repository.
- [ ] It is for **one paper only**. (Two papers means two pull requests.)
- [ ] It changes files in **my own folder only**, `papers/YOURPID/`: the *Files changed*
      tab lists nothing outside it.

### Only the files that are needed

- [ ] The only files I added or changed are:
  - `YOURPID.tex`: my paper
  - `YOURPID.bib`: my references, with only the ones my paper cites
  - my figures, named `YOURPID_f1.png`, `YOURPID_f2.jpg`, …
  - `makedefs`, with my surname and email
- [ ] I deleted the template's `example.*` figures, and my paper no longer uses them.
- [ ] I didn't change the `Makefile`, the style files (`asp20*.sty`/`.bst`) or the
      Python scripts, and I didn't commit a PDF or other build output.

### Tested locally

In `papers/YOURPID/`:

- [ ] `make pdf` builds my paper with **no LaTeX errors or warnings** (in particular no
      overfull `\hbox`es or undefined references).
- [ ] `make check` (PaperCheck) passes, or I explain what it still reports below.
- [ ] `make fix` finds no unprintable (non-ASCII) characters, or I've applied its fixes.

### The paper

- [ ] It is within the page limit, references included: **10 pages** for an invited
      talk, **4 pages** for everything else.
- [ ] The first author is the person who presented it at the conference.
- [ ] I've followed the author instructions in `docs/README_2026.md` (the checklist at
      the top of my `YOURPID.tex` is a good summary).
- [ ] I've emailed my signed copyright form, `copyrightForm_YOURPID_Surname.pdf`, to
      **EDITORS_EMAIL**. It is not in this pull request: it carries my signature.

### Anything the editors should know

<!-- e.g. PaperCheck warnings you think are fine, an extra package you need, figures that
gave you trouble. Leave empty if there's nothing. -->
