# ADASS 2026 author template

Last updated: 2026-10-05

This replaces the `README` of earlier years. Papers are no longer packaged as `.tar` or
`.zip` files and uploaded: each paper has its own ready-made folder in the ADASS 2026
proceedings repository on GitHub, and you submit your paper as a **pull request**.

## Contents

- [Introduction](#introduction)
- [Step 1: Prepare your manuscript](#step-1-prepare-your-manuscript)
- [Step 2: Check your manuscript](#step-2-check-your-manuscript)
- [Step 3: Submit your paper as a pull request](#step-3-submit-your-paper-as-a-pull-request)
- [File index](#file-index)
- [GitHub](#github)
- [LaTeX](#latex)

## Introduction

The Proceedings are typeset for the ASP in print quality, so please follow these steps
carefully: the more problems are solved early on, the more time we all save.

From "too much" to "too little" information, these documents help, in the
proceedings repository's `docs/` folder and your paper's folder:

1. `manual2010.pdf`: the ASP "Instructions for Authors and Editors"
2. `ManuscriptInstructions.pdf`: the guidelines for preparing an ADASS paper, including
   the page limits (10 pages for invited talks, 4 for everything else)
3. this README
4. `<PID>.tex`: your paper, which starts as the ADASS template with its checklist

Where this README and `ManuscriptInstructions.pdf` disagree about how files are named,
packaged or submitted, this README wins: the PDF still describes `.tar` uploads,
`O4-3`-style paper IDs, `asp2014` and EPS-only figures.

### Paper IDs

Each paper has a paper ID, or PID, of the form `XNNN`:

- `X` is the presentation type:
  - `I` invited talk
  - `C` contributed talk
  - `P` poster (including featured posters)
  - `F` focus demo
  - `B` BoF
  - `T` tutorial
- the first digit is the conference track, 1 to 8
- the last two digits number the papers within that track

For example, `C101` is the first contributed talk in track 1. In this README we use
`C101` as the example PID. Find yours in the list of papers in the proceedings
repository's `README.md`.

## Step 1: Prepare your manuscript

Your paper's folder, `papers/<PID>/`, already contains everything you need:

- `<PID>.tex` is the ADASS template with `\bibliography{<PID>}` already set
- `<PID>.bib` holds the template's example references
- `makedefs` has your PID and surname filled in
- the style files, `Makefile` and checking scripts

Read `ManuscriptInstructions.pdf`, then replace the template's example content in
`<PID>.tex` and `<PID>.bib` with your own. For more detail, see the first section of
`manual2010.pdf`, but note that it is some years old and the requirements have changed a
little since. In particular, references **must** be BibTeX entries in `<PID>.bib`.

The paper is built with `pdflatex`, then `bibtex`, then `pdflatex` up to twice more to
resolve all cross-references. `make pdf` does all of this for you. ASP now uses
`pdflatex`, so use **PNG or JPG figures**, named `<PID>_f1.png`, `<PID>_f2.jpg`, and so
on, in your paper's folder (no subdirectories). Delete the template's `example.*`
figures once your paper no longer uses them.

**Overleaf** also works: upload the contents of your `papers/<PID>/` folder (as a ZIP is
easiest) as a new project. It compiles there as it is. Copy your changed files back into
the folder for your pull request.

### Using the provided Makefile

The Makefile builds and checks your paper. Your settings go in `makedefs`, not in the
`Makefile`, which you shouldn't change. Your `makedefs` is already filled in, for example:

```make
# this is where you should define *your* macros, not in the Makefile
P = C101
V = 1
A = Teuben
E = you@example.edu
# your figures, named C101_f1.eps, C101_f2.png, ...
FIGS = $(filter-out C101_inc.tex,$(wildcard C101_*))
```

- `P` is your PID.
- `A` is the surname of the first author. Fix it if it is wrong; it is used by the
  checks and in the name of the copyright form.
- `E` is the email address for questions about your submission. Replace the
  placeholder.
- `FIGS` picks up every `<PID>_*` file, so your figures are found automatically.
- `V` is no longer used: git keeps the history of your paper.

From your paper's folder you can then run:

| Command | What it does |
|---|---|
| `make pdf` | builds `<PID>.pdf` |
| `make check` | checks your paper for common problems (see [Step 2](#step-2-check-your-manuscript)) |
| `make clean` | removes the build products |

You don't need the `tar`, `zip` and `overleaf` targets any more.

### Adding author index entries

The author index needs one commented-out `%\aindex` line per author, just before the
abstract, with the surname first:

```latex
%\aindex{Teuben,~P.~J.}
```

`python3 Aindex.py <PID>` prints them for you from your `\author` list. Check what it
prints: a parser can't always tell which part of a name is the surname. Also add one
`\paperauthor` line per author, as shown in the template; these are used by ADS.

### Adding subject index entries

It helps the editors if you add subject index entries for the important terms in your
paper. They go in your paper as commented-out `\ssindex{}` lines, each on its own line,
for example:

```latex
%\ssindex{observatories!ground-based!VLT}
```

`python3 Index.py <term>` searches the entries used in previous volumes, so you can
reuse them and keep the index consistent. Full details are in an appendix of
`ManuscriptInstructions.pdf`. For a quick word cloud of your paper, to see which terms
are worth indexing:

```
detex C101.tex | grep -o -E '\w+' | sort | uniq -c | sort -n
```

If you don't have `detex`, use `cat`.

### Adding ASCL index entries

It also helps the editors if you add ASCL index entries for the software you mention.
`python3 ascl.py <PID>.tex` suggests them. It gives lots of false positives, so copy
only the correct ones into your paper as LaTeX comments, for example:

```latex
%\ooindex{TOPCAT, ascl:1101.010}
```

Remove the template's example `FOOBAR` index entries.

## Step 2: Check your manuscript

Your paper must typeset without any LaTeX errors or warnings. Overfull `\hbox` warnings
in particular must be fixed; some underfull `\hbox` and `\vbox` warnings can be
tolerated. Make sure your paper is within the page limit.

`make check` runs `PaperCheck.py`, which looks for problems often found in submitted
papers. It is the same check the editors run on every paper, so run it and fix what it
finds before you open your pull request. You can also run it directly:

```
python3 PaperCheck.py C101 Teuben
```

The arguments are your PID and the surname of the first author. PaperCheck doesn't run
LaTeX, or check the length, spelling or grammar of your paper.

PaperCheck also looks for your signed copyright form in your folder and warns if it is
missing. Ignore that warning: you email the form to the editors (Step 3), so it is
never in your folder.

## Step 3: Submit your paper as a pull request

The proceedings repository's own `README.md` walks through every step, with the exact
git commands and GitHub buttons, and a browser-only route if you don't use git. In
short:

1. **Fork** the proceedings repository. Everyone works in their own fork; you don't
   need write access to the proceedings repository.
2. In your fork, make a branch named after your PID.
3. Change **only** files in your own folder, `papers/<PID>/`, and commit only:
   - `<PID>.tex`
   - `<PID>.bib`
   - your figures, `<PID>_f1.png` etc.
   - `makedefs`
4. Don't commit `<PID>.pdf` or other build products; `.gitignore` takes care of that.
   Don't change the `Makefile`, style files or scripts.
   **Email your signed copyright form to the editors; don't commit it.** It carries
   your signature, and the repository and its forks are public. Fill in the whole form
   (`copyrightform.pdf` in your folder), sign and date it, save it as
   `copyrightForm_<PID>_<Surname>.pdf`, with `<Surname>` as `A` in `makedefs`, and
   email it to **EDITORS_EMAIL** with the subject `ADASS 2026 copyright form <PID>`.
5. Push the branch to your fork and open a pull request from it to the proceedings
   repository, titled `<PID>: <your paper title>`. **One paper per pull request.**

Every push to your pull request is built and checked automatically. A LaTeX error fails
the check, with the error lines in the job log. PaperCheck problems fail the
*PaperCheck* check, with the problems in the job log; fix what you can, and say in the
pull request why the rest are fine. The built PDF can be downloaded from the run's
artifacts, so you no longer need to send your own copy.

The editors review your paper in the pull request. To make changes, push more commits
to the **same** pull request: there are no version numbers and no need to resubmit
everything. When your paper is accepted, the editors merge it.

To sum up, a finished folder looks like this:

```
papers/C101/
    C101.tex
    C101.bib
    C101_f1.png
    C101_f2.jpg
    makedefs
    (plus the template files below, unchanged)
```

## File index

Your paper's folder, `papers/<PID>/`, contains:

| File | Purpose |
|---|---|
| `<PID>.tex` | your paper; starts as the ADASS template (`ADASS_template.tex`) |
| `<PID>.bib` | your references; starts as the template's examples (`example.bib`) |
| `makedefs` | your macros (PID, surname, email, figures), included by the Makefile |
| `Makefile` | `make pdf`, `make check` |
| `asp2023.sty` | the required ASP LaTeX style file |
| `asp2021.bst` | the required ASP bibliography style file |
| `example.jpg`, `example.eps` | the template's example figures; delete them when no longer used |
| `copyrightform.pdf` | the blank ASP copyright form; email the signed copy, don't commit it |
| `PaperCheck.py` | checks an ADASS paper (`make check`) |
| `AdassChecks.py` | Python module used by `PaperCheck.py` |
| `TexScanner.py` | Python module used by `AdassChecks.py` |
| `detect_tex.py` | finds your `.tex` file; set `P=` in `makedefs` to resolve conflicts |
| `FixUnprintable.py` | replaces unprintable characters in your `.tex` file |
| `Aindex.py` | generates `%\aindex` author index entries |
| `Index.py` | suggests `%\ssindex` subject index entries |
| `AdassConfig.py` | Python module used by `Index.py` |
| `AdassIndex.py` | Python module used by `Index.py` |
| `ascl.py` | suggests `%\ooindex` ASCL index entries |
| `subjectKeywords.txt` | recent subject index entries, used by `Index.py` and PaperCheck |
| `newKeywords.txt` | additional subject index entries, used by PaperCheck |
| `asclKeywords.txt` | ASCL codes, used by `ascl.py` |

The repository's `docs/` folder contains:

| File | Purpose |
|---|---|
| `README_2026.md` | this file |
| `ManuscriptInstructions.pdf` | the guidelines for preparing an ADASS paper |
| `manual2010.pdf` | the ASP "Instructions for Authors and Editors" |
| `ADASS_template.pdf` | the ADASS template, typeset |

## GitHub

Each year's proceedings package is drawn from the
[ADASSProceedings](https://github.com/astroumd/ADASSProceedings) repository, where every
year develops its release on a branch (`2026` this year) and merges it back to the
master branch for the next year's team.

You don't need to know about that, but you may come across editor-specific comments or
commands in the Makefile or the Python scripts.

Good luck!

## LaTeX

If `pdflatex` isn't installed on your system, install TeX Live with your package
manager. The package names differ between systems; for example:

| System | Command | Packages |
|---|---|---|
| Linux, Ubuntu/Debian | `sudo apt install` | `texlive texlive-base texlive-bibtex-extra texlive-binaries texlive-fonts-recommended texlive-lang-greek texlive-latex-base texlive-latex-extra texlive-latex-recommended texlive-pictures texlive-plain-generic texlive-publishers texlive-science texlive-xetex` |
| Linux, Red Hat | `sudo dnf install` | `@texlive` |
| macOS, Homebrew | `brew install` | `texlive` |
