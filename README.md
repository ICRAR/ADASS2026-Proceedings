# ADASS 2026 Proceedings — paper submissions

Every accepted contribution has its own ready-made folder in `papers/`, named after its
paper ID (PID). Find **your** PID in the [list of papers](#papers) below; the folder
with that name is the only one you work in. A PID is a letter and three digits: the
letter is the presentation type (I, C, P, F, B, T), the first digit is the track number,
and the last two digits number the papers within that track.

> [!IMPORTANT]
> **Every pull request must come from your own fork of this repository.** Pull requests
> from a branch in this repository are not accepted, even if you have write access.

## For authors

Submit your paper by **forking** this repository; editing **your own paper's
folder** in your fork; and opening a **pull request** (PR) from your fork back to this
repository. The editors review your paper in that pull request and merge it when it is
accepted.

```
 this repository                      your fork
 (ADASS)                              (your-username)
 ┌──────────────────┐   1. Fork      ┌─────────────────────────────────────┐
 │ main             │ ─────────────▶ │ main                                │
 │                  │                │   │ 2. branch YOURPID               │
 │                  │                │   ▼                                 │
 │                  │                │ YOURPID: edit papers/YOURPID/ only  │
 │                  │ 3. pull request│                                     │
 │ main ◀───────────┼────────────────┼─ YOURPID                            │
 └──────────────────┘                └─────────────────────────────────────┘
       4. the editors review and merge
```

A fork is your own copy of this repository under your GitHub account. The pull request
is how you ask for your folder to be copied from your fork into this repository.

> [!IMPORTANT]
> **The three rules**
>
> 1. **Work in your own fork, and open the pull request from it.** Don't push branches
>    to this repository or ask for write access to it; you don't need it. A check on
>    every pull request fails if it doesn't come from a fork.
> 2. **Change only your own folder, `papers/YOURPID/`.** Nothing outside it: not the
>    README, not `.github/`, not anyone else's paper, not the `Makefile`, style files
>    or scripts inside your folder.
> 3. **One paper per pull request.** If you are first author on two papers, open two
>    pull requests, each from its own branch.
>
> A pull request that breaks these rules will be sent back to you to fix.

Throughout these instructions, `YOURPID` stands for **your** PID and `your-username`
for **your** GitHub username: type yours wherever they appear.

### Contents

- [Before you start](#before-you-start)
- [Route A: with git on your computer (recommended)](#route-a-with-git-on-your-computer-recommended)
- [Route B: in the browser only, no git](#route-b-in-the-browser-only-no-git)
- [Optional: writing your paper in Overleaf](#optional-writing-your-paper-in-overleaf)
- [After you open the pull request](#after-you-open-the-pull-request)
- [What to put in your folder](#what-to-put-in-your-folder)
- [Your copyright form: email it, don't commit it](#your-copyright-form-email-it-dont-commit-it)
- [Fixing common mistakes](#fixing-common-mistakes)

### Before you start

You need:

- a [GitHub account](https://github.com/signup);
- your PID, from the [list of papers](#papers) below;
- for route A, [git](https://git-scm.com/downloads) and a TeX Live installation
  (`pdflatex`, `bibtex`, `make` and `python3`). If you'd rather not install LaTeX, you
  can [write the paper in Overleaf](#optional-writing-your-paper-in-overleaf) and use
  route B to submit it.

You also need to sign the ASP copyright form and **email** it to the editors; it never
goes into this repository. See [Your copyright form](#your-copyright-form-email-it-dont-commit-it).

Start with [`docs/README_2026.md`](docs/README_2026.md); that is the README for the
ADASS author template, and explains the `make` targets, index entries, PaperCheck and
what is in your folder.

If necessary, the complete formatting rules are in [`docs/ManuscriptInstructions.pdf`](docs/ManuscriptInstructions.pdf)
(the ADASS guidelines). [`docs/ADASS_template.pdf`](docs/ADASS_template.pdf) shows what
the starting template looks like once built.

### Route A: with git on your computer (recommended)

#### A1. Fork this repository

1. Sign in to GitHub.
2. At the top right of this page, click **Fork**.
3. Leave the owner as your own account and the repository name as it is. Leave
   **Copy the `main` branch only** ticked.
4. Click **Create fork**.

You now have your own copy at `https://github.com/your-username/<this repository's name>`.
Everything you do from here on happens in your fork; this repository is only touched
when the editors merge your pull request.

#### A2. Clone your fork

On **your fork's** page (check that the top left says `your-username/...`, not the
ADASS organisation), click the green **Code** button and copy the URL. Then:

```
git clone <the URL you copied>
cd <this repository's name>
```

#### A3. Create a branch for your paper

Don't work on `main`. Make a branch named after your PID:

```
git switch -c YOURPID
```

(With git older than 2.23, use `git checkout -b YOURPID`.)

#### A4. Write your paper

Everything you need is already in `papers/YOURPID/`, and it builds as it is. Edit only
the files listed in [What to put in your folder](#what-to-put-in-your-folder).

#### A5. Build and check it

```
cd papers/YOURPID
make pdf      # builds YOURPID.pdf
make check    # runs the ADASS PaperCheck
make fix      # replaces non-ASCII characters with LaTeX
              # (keeps the original as YOURPID.tex_1)
cd ../..
```

Fix any LaTeX errors and anything PaperCheck reports, except its warning about the
copyright form: you [email that form](#your-copyright-form-email-it-dont-commit-it) to
the editors, so it is never in your folder. Then check
`YOURPID.pdf` against the page limit: **10 pages** for an invited talk, **4 pages** for
everything else, references included.

#### A6. Check what you changed, then commit

From the top of the repository:

```
git status
```

**Every** path listed must start with `papers/YOURPID/`. If anything else is listed, see
[Fixing common mistakes](#fixing-common-mistakes) before going on. Then add your folder,
and only your folder:

```
git add papers/YOURPID/
git status      # check again: under "Changes to be committed",
                # only papers/YOURPID/ is listed
git commit -m "YOURPID: first draft"
```

Don't use `git add .` or `git add -A` from the top of the repository: they pick up
anything else you touched. Build output (the PDF, `.aux`, `.log` and so on) is ignored
by `.gitignore`, so it isn't added.

#### A7. Push the branch to your fork

```
git push -u origin YOURPID
```

`origin` is your fork. You don't need, and won't have, permission to push to this
repository.

#### A8. Open the pull request

1. Go to **your fork** on GitHub. A yellow banner says *YOURPID had recent pushes*;
   click **Compare & pull request**. (No banner? Click **Contribute** → **Open pull
   request**.)
2. Check the four boxes at the top of the page read:
   - **base repository**: this repository (the ADASS one, not your fork)
   - **base**: `main`
   - **head repository**: `your-username/...` (your fork)
   - **compare**: `YOURPID` (your branch)
3. Title it with your PID and your paper's title: `YOURPID: Your paper title`.
4. Fill in the checklist that appears in the description.
5. Leave **Allow edits and access to secrets by maintainers** ticked, so the editors can
   make small fixes for you.
6. Click the **Files changed** tab before you submit, or right after: every file must
   be inside `papers/YOURPID/`.
7. Click **Create pull request**.

Then go to [After you open the pull request](#after-you-open-the-pull-request).

### Route B: in the browser only, no git

Use this if you don't want to use git. If you're writing in Overleaf, follow
[Optional: writing your paper in Overleaf](#optional-writing-your-paper-in-overleaf)
first; it brings you back here to submit.

#### B1. Fork this repository

As in [A1](#a1-fork-this-repository): **Fork** at the top right of this page, then
**Create fork**.

#### B2. Upload your files into your folder

1. On **your fork**, click into `papers`, then into **your** folder, `YOURPID`. Check
   the path above the file list reads `<repository>/papers/YOURPID/`.
2. Click **Add file** → **Upload files**.
3. Drag in your `YOURPID.tex`, `YOURPID.bib`, figures and `makedefs`. Files with the
   same name replace the template's ones. Upload only the files listed in [What to put
   in your folder](#what-to-put-in-your-folder). **Never upload your signed copyright
   form**: in the browser nothing stops it being committed, and it would be public.
   [Email it](#your-copyright-form-email-it-dont-commit-it) instead.
4. To delete a template file you no longer use (such as the `example.*` figures), open
   it, click **⋯** at the top right → **Delete file**.
5. Under **Commit changes**, choose **Create a new branch for this commit and start a
   pull request**, and name the branch `YOURPID`. Click **Propose changes**.

   (If you've already made the `YOURPID` branch, switch to it with the branch menu at
   the top left before uploading, and commit to it directly.)

#### B3. Open the pull request

GitHub takes you to the *Open a pull request* page. Follow
[A8](#a8-open-the-pull-request) from step 2.

### Optional: writing your paper in Overleaf

Your folder compiles in Overleaf as it is, so you can write and collaborate on the
paper there, and submit it with route B (or route A) at the end. The three rules still
apply: the pull request comes from your fork and changes only `papers/YOURPID/`.

> [!NOTE]
> Don't use Overleaf's **GitHub Sync** or **Import from GitHub** with this repository.
> They copy the whole repository, which has more files than an Overleaf project allows,
> and they only work with the `main` branch. Copying your one folder across, as below,
> is simpler.

#### O1. Put your folder into Overleaf

1. On this page, click the green **Code** button → **Download ZIP**, and unzip it.
2. Find your folder, `papers/YOURPID/`, in the unzipped files, and make a zip of just
   that folder (on macOS, right-click → **Compress "YOURPID"**; on Windows, right-click
   → **Send to** → **Compressed (zipped) folder**).
3. In Overleaf, click **New Project** → **Upload Project**, and choose that zip.

#### O2. Set up the project

Open the project's **Menu** (top left) and set:

- **Compiler**: `pdfLaTeX`
- **TeX Live version**: the newest one offered, which is closest to what the checks use
- **Main document**: `YOURPID.tex`

Click **Recompile**. You should see the ADASS template, as in
[`docs/ADASS_template.pdf`](docs/ADASS_template.pdf).

#### O3. Write the paper

Edit `YOURPID.tex` and `YOURPID.bib`, upload your figures as `YOURPID_f1.png`,
`YOURPID_f2.pdf` and so on, delete the `example.*` figures, and check your surname and
email in `makedefs`. See [What to put in your folder](#what-to-put-in-your-folder).

- Leave the other files (`Makefile`, `asp2023.sty`, the `.bst`, the Python scripts)
  where they are and unchanged. Overleaf needs the style files to compile your paper;
  the rest is harmless.
- Don't add other `.sty` or `.cls` files, or extra packages, without asking the editors:
  the book is built with the ADASS style only.
- Overleaf can't run `make check` or `make fix`. The PaperCheck and *Unprintable
  characters* checks run on your pull request instead, so expect to fix a few things
  there. Watch out for non-ASCII characters pasted into the text (accented letters,
  curly quotes, en dashes, `µ`): write them in LaTeX (`\'e`, ``` `` '' ```, `--`, `$\mu$`).
- Keep an eye on the page count in Overleaf's PDF: **10 pages** for an invited talk,
  **4 pages** for everything else, references included.

#### O4. Get your files out of Overleaf

In Overleaf, open **Menu** → **Download** → **Source**. You get a zip of the project's
files (without the PDF); unzip it.

#### O5. Submit

- **Without git**: follow [route B](#route-b-in-the-browser-only-no-git), and in
  [B2](#b2-upload-your-files-into-your-folder) upload only your `YOURPID.tex`,
  `YOURPID.bib`, figures and `makedefs` from the unzipped download, and delete the
  `example.*` figures.
- **With git**: follow [route A](#route-a-with-git-on-your-computer-recommended) to
  A3, copy the same files from the download into `papers/YOURPID/`, delete the
  `example.*` figures, and carry on from [A5](#a5-build-and-check-it).

#### Changes after you've opened the pull request

Keep editing in Overleaf. When you're ready, download the source again (O4) and upload
the changed files to the **same** `YOURPID` branch of your fork: on your fork, switch to
the `YOURPID` branch with the branch menu at the top left, go to `papers/YOURPID/`, then
**Add file** → **Upload files**, and choose **Commit directly to the `YOURPID` branch**.
The pull request updates by itself. Don't open a new one.

If someone (an editor, or a fix from the *Unprintable characters* check) changes your
files in the pull request, make the same change in Overleaf too. Otherwise your next
upload undoes it.

### After you open the pull request

Within a few minutes, four checks run on your paper, each with its own status at the
bottom of the pull request:

| Check | What it does | When it fails |
|---|---|---|
| *From a fork* | checks the pull request comes from your fork | it comes from a branch in this repository; see [Fixing common mistakes](#fixing-common-mistakes) |
| *Build papers* | builds the PDF with [latex-action](https://github.com/xu-cheng/latex-action) (latexmk with a full TeX Live) | a LaTeX error; the error lines are in the job log |
| *PaperCheck* | the ADASS PaperCheck, as `make check`, including its TexScanner parse of the `.tex` file | PaperCheck reports problems; the job log lists them |
| *Unprintable characters* | FixUnprintable, as `make fix` | non-ASCII characters; the log shows the replacements, and the fixed `.tex` is in the run's artifacts |

Click **Details** next to a check to see its log. A comment on the pull request links the
built PDF: check it looks the way you expect.

The checks on a first pull request may wait for an editor to approve them; that's
normal.

**To make changes**, whether to fix a check or to answer the editors: change the files
in the **same branch** of your fork, and push again (route A: commit, then `git push`;
route B: upload to the `YOURPID` branch). The pull request updates by itself and the
checks run again. **Don't open a new pull request**, and don't close the old one.

When the editors are happy, they merge your pull request. You're done; you can delete
your fork afterwards if you like.

### What to put in your folder

Change these, in `papers/YOURPID/`:

| File | What to do |
|---|---|
| `YOURPID.tex` | your paper. It starts as the standard ADASS template, which also explains the formatting rules; replace its example content with your paper |
| `YOURPID.bib` | your references. It starts as the template's example references; replace them with only the ones your paper cites |
| figures | name them `YOURPID_f1.eps`, `YOURPID_f2.png`, and so on |
| `example.*` | delete the template's example figures once your paper no longer uses them |
| `makedefs` | check your surname and email |

Don't change or add anything else: not the `Makefile`, the style files
(`asp20*.sty`, `.bst`), the Python scripts or the other template files. Don't commit
the PDF or other build output, and **don't commit your signed copyright form**: it
carries your signature, so [email it](#your-copyright-form-email-it-dont-commit-it) to
the editors instead.

### Your copyright form: email it, don't commit it

ASP needs a signed copyright form for every paper. **Email it to the editors. Don't
commit it** to your fork or add it to your pull request: it carries your signature, and
this repository and every fork of it are public.

1. Fill in the whole blank form, `copyrightform.pdf` in your folder, and sign and date
   it.
2. Save it as `copyrightForm_YOURPID_Surname.pdf`, with `Surname` as `A` in your
   `makedefs`.
3. Email it to **EDITORS_EMAIL** with the subject `ADASS 2026 copyright form YOURPID`.

With git, `.gitignore` keeps files named `copyrightForm_*.pdf` out of your commits; in
the browser nothing does. Either way, check the *Files changed* tab of your pull request
doesn't list it. If it does, delete it from your branch and tell the editors in the pull
request.

### Fixing common mistakes

**`git status` or *Files changed* shows files outside `papers/YOURPID/`.** Put each one
back as it is in this repository. With git, first add this repository as a remote called
`upstream` (once; use the URL from the green **Code** button on *this* page, not your
fork's):

```
git remote add upstream <this repository's URL>
git fetch upstream
```

Then, for each file that shouldn't have changed:

```
git restore --source=upstream/main --staged --worktree path/to/the/file
```

A file you added by mistake, which isn't in this repository, is removed with
`git rm --cached path/to/the/file` (add it to your own `.git/info/exclude` if you want
to keep it locally). Commit and push; the pull request updates.

In the browser, open each wrong file on your branch and delete it, or ask the editors in
the pull request to tidy it for you.

**The *From a fork* check fails.** Your pull request comes from a branch in this
repository, not from your fork. Fork the repository ([A1](#a1-fork-this-repository)),
push your branch to the fork (with git: `git remote add fork <your fork's URL>`, then
`git push -u fork YOURPID`), and open a new pull request from it as in
[A8](#a8-open-the-pull-request). Then close the old pull request, with a link to the new
one.

**I committed to `main` instead of a branch.** That's fine as long as only your folder
changed: open the pull request from your fork's `main` (in [A8](#a8-open-the-pull-request),
**compare** is then `main`). Use a separate branch for any second paper.

**My pull request shows other people's papers, or hundreds of changes.** Your fork is
out of date with this repository, or the pull request is the wrong way round. Check the
four boxes in [A8](#a8-open-the-pull-request) step 2. To bring your fork up to date, on
your fork's page click **Sync fork** → **Update branch**; then, with git,
`git switch YOURPID && git pull origin main && git push`.

**A check warns *This PR touches more than one paper*.** You changed files in two
`papers/` folders. Undo the changes to the folder that isn't yours, as above.

**I have two papers.** Make a separate branch for each, named after each PID
(`git switch main`, then `git switch -c` and your second PID), and open a separate pull
request from each.

**Something else.** Ask in your pull request, or contact the editors. Don't worry about
breaking anything: nothing reaches this repository until an editor merges it.

## For editors

- `bash ci/build_papers.sh C101 P203` builds specific papers locally with `make`. With no
  arguments it builds every paper. GitHub Actions uses latex-action instead; it runs the
  same `pdflatex`/`bibtex` passes through latexmk.
- Running any of the three workflows manually runs it on the whole set. They share the
  `find-papers.yml` workflow, which picks the papers a PR changed.
- This repo was generated by `make_author_templates.py` in the main
  ADASSProceedings2026 repo. When all PRs are merged, copy `papers/` back there:
  ```
  git clean -fdX papers/      # drop ignored build products first
  rsync -av papers/ ../ADASSProceedings2026/papers/
  ```
  Then continue with `pmake inc rsync` and `make asp1` / `make book0` as described in its `INGESTION.md`.

## Papers

<!-- papers-table:start -->
### 1. AI as a tool for data discovery and data management

| Authors | Type | Title | PID |
|---------|------|-------|-----|
| Chilingarian, Igor | Featured Poster | How can LLMs help in the data reduction pipeline development in astronomy? | [P104](papers/P104/) |
| Clarke, Alex | Contributed Talk | Unexplainable AI: rats, super recognisers, and multi-modal deep learning for astronomical datasets | [C101](papers/C101/) |
| Danehkar, Ashkbiz | Contributed Talk | AstroAKD: An MCP-Based Agent for Natural-Language Search of Astronomical Archives | [C104](papers/C104/) |
| Derriere, Sebastien; Sharon E. Hunt | Poster | A Unified Astronomy Thesaurus in the era of Large Language Models | [P107](papers/P107/) |
| Felix, Jankowsky | Featured Poster | AI assisted observatory management | [P101](papers/P101/) |
| Gause, Dan | Poster | MANNA: an MCP Architecture for NOIRLab, NRAO, and additional Archives | [P108](papers/P108/) |
| Ibarra Ibaibarriaga, Aitor | Featured Poster | Beyond XMMGPT: Agentic AI for Science Operations Centres, from Proposal Preparation to Catalogue Exploration | [P106](papers/P106/) |
| Iyer, Kartheik | Invited Talk | Using insights from the embedding spaces of large language models for (astronomical) research and discovery | [I101](papers/I101/) |
| Kruk, Sandor | Contributed Talk | ADQL generation using LLMs | [C105](papers/C105/) |
| López-Caniego, Marcos | Contributed Talk | Sustainable AI for Astronomical Archival Data Discovery in the Petabyte Era | [C103](papers/C103/) |
| Lynn, Meca | Contributed Talk | New Tools for Streamlining Data Ingestion at NASA Exoplanet Archive (NEA) | [C102](papers/C102/) |
| McCormick, Kiera; Adele Plunkett; Felix Stoehr | Poster | Toward Natural Language Search in the ALMA Science Archive Using LLM Source Descriptions | [P102](papers/P102/) |
| O'Toole, Simon; Christophe Arviset; MANTELET Gregory; Gilles Landais | BoF | How to cope with the rapidly increasing number of aggressive incoming requests? | [B101](papers/B101/) |
| Sekhar, Srikrishna | Contributed Talk | # LLM-Orchestrated Radio Interferometric Data Reduction | [C106](papers/C106/) |
| Shen, Sharon | Poster | Vector Search for Similarity-Based Discovery of Astronomical Light Curves | [P103](papers/P103/) |
| Zautkin, Serhii | Featured Poster | Bring Your Own Model: Treating AI as a Replaceable Part of the Science Platform | [P105](papers/P105/) |

### 2. AI as tool for scientific discovery

| Authors | Type | Title | PID |
|---------|------|-------|-----|
| Antonio; Ghulam Mustafa | Poster | Machine-Learning-Based Event Classification of Terrestrial Gamma-ray Flashes with a Segmented Scintillator Detector | [P207](papers/P207/) |
| Bait, Omkar | Invited Talk | Learning the Radio Sky: Representation Learning from Visibilities to Data Archives | [I201](papers/I201/) |
| Bisen, Rose Singh | Poster | Diagnosing and Mitigating Simulation-to-Real Failure in Photometric Transient Classification. | [P202](papers/P202/) |
| Gheller, Claudio | Contributed Talk | Scalable Deep-Learning Segmentation of Extended and Diffuse Radio Sources with TUNA | [C202](papers/C202/) |
| Gorchakova, Nika | Poster | Beyond the Light Curve: Exploring Computer Vision Approaches for Exoplanet Transit Detection | [P211](papers/P211/) |
| Gupta, Nikhel | Contributed Talk | From Detection to Discovery: ML Pipelines for the Radio Sky Surveys | [C203](papers/C203/) |
| Harris, Carmen Isabel Martinez | Poster | SpecML: A Self-Supervised Foundational Model for Interpreting Galaxy Spectrum used on predicting High-z Source Classification and Galaxy Property Estimations | [P205](papers/P205/) |
| Ivleva, Anna | Featured Poster | Radio Signatures of Merger Shocks in Galaxy Groups: Predictions from Cosmological Simulations | [P206](papers/P206/) |
| Jagannathan, Preshanth; Arpan | Featured Poster | VROOM-SBI: Amortized Bayesian QU-Fitting for Survey-Scale Faraday Analysis | [P215](papers/P215/) |
| Li, Shanshan | Contributed Talk | Mining Double-line Spectroscopic Candidates in the LAMOST Medium-resolution Spectroscopic Survey Using a Human–AI Hybrid Method | [C201](papers/C201/) |
| Luise, Alberto; Ghulam Mustafa | Poster | Explainable XRF Element Detection with Embedding-Space KNN and Physics-Based Masks for the HARLOCK Lunar Rover | [P216](papers/P216/) |
| McLeod, Alistair | Poster | A robust and scalable deep learning approach for detecting gravitational waves | [P213](papers/P213/) |
| Mustafa, Ghulam | Poster | Machine Learning Models for Predicting the COSI Background for Gamma-Ray Burst Detection | [P210](papers/P210/) |
| Parmiggiani, Nicolò; Ghulam Mustafa | Poster | ARCADIA: AI-based Real-time Analysis for Autonomous Space Systems | [P209](papers/P209/) |
| Riedel, Johanna; Mark Taylor | Poster | Towards Plug-and-Play Machine Learning in Astronomy | [P218](papers/P218/) |
| Rizzo, Alessandro; Ghulam Mustafa | Poster | Quantum Annealing for Gamma-Ray Source Detection and Localization with AGILE Data | [P204](papers/P204/) |
| Roy, Gourab | Featured Poster | AstraQ-VL: Parameter-Efficient Astronomy Vision-Language Modeling with Connector Alignment and LoRA Tuning | [P201](papers/P201/) |
| Saha, Tanumoy | Poster | Pulsar Signal Segmentation and Analysis using Custom Convolutional Filter Stacks | [P208](papers/P208/) |
| Sanvitale, Nicoletta | Contributed Talk | Toward Scalable Neural Fields for Continuous Visibility Modeling in Radio Interferometry | [C204](papers/C204/) |
| Tan, Qitong Anabel | Contributed Talk | TransformerRIM: A Data-Driven Transformer-based Radio Interferometric Imager with Uncertainty Quantification | [C205](papers/C205/) |
| Teuben, Peter | Featured Poster | Teaching AI in Astronomy | [P212](papers/P212/) |
| Wang, Li | Poster | Image-to-Catalogue: End-to-End Source Finding with a 3D large vision model | [P217](papers/P217/) |
| Williams, Peter K. G. | Poster | Pervasive AI as A Second Enclosure Movement | [P214](papers/P214/) |

### 3. AI as tool for software engineering

| Authors | Type | Title | PID |
|---------|------|-------|-----|
| Buchbender, Christof | Invited Talk | Code Is Cheap, Judgement Is Not: Building Software and Systems We Can Trust with Agentic AI | [I301](papers/I301/) |
| Cruz, Kelle | Featured Poster | Teaching the Machines Our Tools: Why we need to be building “Skills”, not just writing docs. | [P306](papers/P306/) |
| Danehkar, Ashkbiz | Poster | xstar-tools: AI-Assisted Modernization of the XSTAR Photoionization Code | [P304](papers/P304/) |
| Glazebrook, Karl | Contributed Talk | Same Source, Three Orders of Magnitude: A 2026 Reprise of Shortridge's Compiler Benchmark, Co-Authored with an LLM | [C302](papers/C302/) |
| Jenness, Tim | Contributed Talk | Using LLMs to Port a Large C Library to Rust | [C303](papers/C303/) |
| Lacopo, Giovanni | Contributed Talk | Multi-Agent Loop Engineering for Radio Astronomy Pipelines: Autonomous Refactoring and Scientific Validation | [C301](papers/C301/) |
| Mosheva, Tatiana | Poster | AI-Assisted PostgreSQL Engineering for NASA’s Near-Earth Object Surveyor Mission | [P305](papers/P305/) |
| Salgado, Jesus | Poster | Use of the AI for SRCNet development | [P301](papers/P301/) |
| Smith, Jeffrey | Featured Poster | Prototyping a Space-Based Observatory Pipeline in Three Weeks with Claude Code | [P302](papers/P302/) |
| Stenborg, Travis | Poster | BIAS (Bias Images As Syntax): An AI Co-designed Esolang with Python and TypeScript Interpreters | [P303](papers/P303/) |

### 4. Building and operating science platforms and workflows in the Petabyte Era

| Authors | Type | Title | PID |
|---------|------|-------|-----|
| (DZA), Elsa Buchholz; Lars Haupt | Contributed Talk | Galactic Plane Imaging and Polarimetry from MeerKAT data on High-performance and Memory-based computing resources | [C402](papers/C402/) |
| (DZA), Elsa Buchholz | Featured Poster | Astronomical Projects with Multiple Repositories: A Portal for Consolidated Information and Kubernetes-Based Operations | [P406](papers/P406/) |
| Arenas, Javier Ballester | Poster | How Should We Build the Next Generation of Science Platforms? | [P408](papers/P408/) |
| Ballester Arenas, Javier; Yan Grange; Marcos López-Caniego; Sandor Kruk; Jesus Salgado; Christophe Arviset; Michele Delli Veneri; Rosie Bolton; William O Mullane; Carmen Toribio; Brian Major | BoF | Science Platforms at Scale: Developing Data Services in the Petabyte Era | [B403](papers/B403/) |
| Barrett, Paul | Featured Poster | AURIS.jl: A High Performance Radio Interferometry Software Suite | [P413](papers/P413/) |
| Borra, Sagar | Contributed Talk | Bridging Kubernetes and Slurm for Transparent HPC Job Offloading | [C403](papers/C403/) |
| Brophy, Keith; Simon O'Toole | BoF | Trust, Identity and Researcher Mobility in Astronomy Infrastructure | [B402](papers/B402/) |
| Casteels, Kevin | Featured Poster | CANFAR Science Portal: Overcoming Challenges to Enable Next-Generation Astronomical Research | [P402](papers/P402/) |
| Comrie, Angus | Poster | A new CARTA controller for scalable deployment across regional centres | [P410](papers/P410/) |
| Coulson, James | Poster | Evolving the Data Central Archive: Scaling and Optimising Archival and Automated Data Reduction Systems | [P404](papers/P404/) |
| Danner, Christopher | Poster | Machine Learning Methods for Imaging with Interferometers | [P405](papers/P405/) |
| Donaldson, Tom | Poster | Exploring Roman Space Telescope Data in the Cloud: Integrating ipyaladin and Jdaviz in the Roman Research Nexus | [P416](papers/P416/) |
| Driver, Simon | Contributed Talk | Data Fusion: What is it and why "bringing compute to the data" may endanger it! | [C408](papers/C408/) |
| Glorioso, John | Contributed Talk | Building a Cloud-Native, Petabyte-Scale Pipeline for the Roman Space Telescope | [C401](papers/C401/) |
| Hoogenberg, Kim | Poster | The SRCNet Federated Execution Framework: Bringing Scientific Workflows to the Data | [P411](papers/P411/) |
| Joshi, Rohini | Contributed Talk | Making the Most of What You Have: Platform Strategy and Science Verification Readiness at the Swiss SRC | [C404](papers/C404/) |
| Kale, Ruta | Contributed Talk | Towards Reliable Batch Data Processing for the SKA Science Data Processor | [C409](papers/C409/) |
| Li, Changhua | Invited Talk | Changhua's talk | [I401](papers/I401/) |
| Mi, Linying | Poster | A Configurable and Reusable Batch-Processing Pipeline for Time-Domain Astronomical Data | [P409](papers/P409/) |
| Murugeshan, Chandra; Jordan Collier | Featured Poster | A reproducible workflow for multi-frequency radio continuum spectral mapping | [P414](papers/P414/) |
| Oliveira, Joaquim | Contributed Talk | From Stars to Storage Engines: Migrating Big Science Workloads Beyond Greenplum | [C405](papers/C405/) |
| Pietrantonio, Cristian Di | Contributed Talk | BLINK and you’ll miss it: a high time resolution imaging pipeline for fast radio burst searches with the Murchison Widefield Array | [C406](papers/C406/) |
| Robotham, Aaron | Poster | MAML: Equality in Metadata for Data Lakes, Humans, and AI | [P412](papers/P412/) |
| Ross, Kat | Featured Poster | A classification schema for Peaked Spectrum Sources in the SKA era | [P407](papers/P407/) |
| Sawyers, Andrew | Contributed Talk | Fornax Science Console: A repeatable, open science platform for compute-near-data | [C407](papers/C407/) |
| Sokolowski, Marcin | Contributed Talk | Visualising Massive Astronomical Datasets with CARTA | [C410](papers/C410/) |
| Stone, Connor | Featured Poster | AstroPhot: fitting everyhting everywhere all at once in astronomical images | [P401](papers/P401/) |
| Tobar, Rodrigo | Featured Poster | The real-time visibility reception pipeline for the SKA observatory | [P415](papers/P415/) |
| verbenajl; Christof Buchbender; Maksym | BoF | Inter-operable Data and Compute for Astronomical Research | [B401](papers/B401/) |

### 5. Usability, accessibility and security in astronomy software

| Authors | Type | Title | PID |
|---------|------|-------|-----|
| Ates, Onur | Contributed Talk | The CTAO Science Data Challenge Portal: A Secure and User-Centric Web Platform for Gamma-ray Astronomy | [C503](papers/C503/) |
| Bianco, Sam | Contributed Talk | Interactive Documentation in the Age of AI: Lessons from MAST Software | [C501](papers/C501/) |
| Davies, Elizabeth | Invited Talk | Elizabeth's talk | [I501](papers/I501/) |
| Gangat, Ameera | Contributed Talk | Building Confidence in the Proposal Submission System with Playwright | [C502](papers/C502/) |
| Grange, Yan | Featured Poster | Towards a unified data infastructure for LOFAR 2.0 | [P504](papers/P504/) |
| Landais, Gilles; MANTELET Gregory; Fernique | Poster | VizieR versus increasing bot scraping | [P503](papers/P503/) |
| Pedamkar, Kalyani | Poster | More Structure, Less Handwork: The New IVOA Document Repository | [P502](papers/P502/) |

### 6. The art of collaboration in astronomy software development

| Authors | Type | Title | PID |
|---------|------|-------|-----|
| Allen, Mark | Featured Poster | Sharing best practices for astronomical software, services and infrastructure. | [P608](papers/P608/) |
| Baláž, Martin | Featured Poster | Pythonic data reduction pipeline framework for ESO software stack | [P605](papers/P605/) |
| Brederode, Ray | Invited Talk | Ray's talk | [I601](papers/I601/) |
| Buttfield-Addison, Mars | Contributed Talk | Interrogating Processes in Australian Radio Astronomy Data Production | [C603](papers/C603/) |
| Grange, Yan; Janneke de Boer; Kim Hoogenberg | BoF | Beyond the grant: keeping astronomical collaborations alive | [B601](papers/B601/) |
| Greiner, Benjamin | Featured Poster | Activities at the SOFIA Data Center: Preserving a rich legacy of observations for the scientific community | [P604](papers/P604/) |
| Holmberg, Conrad | Featured Poster | The Golden Docker Image - A DevOps Approach on How One Environment Can Unfrustrate All. | [P603](papers/P603/) |
| Molinaro, Marco | Poster | Status of the IVOA Technical Standards and Processes as of 2026 | [P602](papers/P602/) |
| O'Toole, Simon; Nuria Lorente | BoF | Diversity, Equity, Inclusion, and Belonging: why do we keep talking about this? | [B602](papers/B602/) |
| Ortega, Antonio; Antonio Siles | Featured Poster | XMM-NEWTON SCIENCE ARCHIVE: Forthcoming Release of the New Angular-Based Portal | [P607](papers/P607/) |
| Peleato, Eduardo Alonso; Dario Oliviero; Francesco Gianotto | Featured Poster | The NEOCC Observations Analysis Tool: Astrometric Residual Diagnostics and Unexplained Systematic Errors | [P609](papers/P609/) |
| Scora, Jennifer | Featured Poster | RAIL: A Community-driven Library to Estimate Photometric Redshifts for LSST and Beyond | [P606](papers/P606/) |
| Stevens, Grant | Contributed Talk | AstronomicAL: A Plugin-Based Workbench for Composable Astronomy Workflows | [C602](papers/C602/) |
| Valame, Snehal | Contributed Talk | Seeing the Same Sky: Visual Thinking as a Collaboration Tool in the SKAO | [C601](papers/C601/) |
| Withers, Tai | Featured Poster | Free your team's knowledge with Cambium - a static site generator for scientific documentation | [P601](papers/P601/) |

### 7. Global data management and lifecycle in the exascale era

| Authors | Type | Title | PID |
|---------|------|-------|-----|
| Dodson, Richard | Contributed Talk | A little can go a long way: Investigations into visibility compression for Radio Interferometry Data Storage | [C702](papers/C702/) |
| O'Mullane, William | Invited Talk | Rubin Data Management: Delivering awe and wonder and weathering organisational upheaval | [I701](papers/I701/) |
| Wicenec, Andreas | Contributed Talk | Astronomers, unfortunately you need to change your hoarder mentality! | [C701](papers/C701/) |

### 8. Topical Computing, Software and Algorithms

| Authors | Type | Title | PID |
|---------|------|-------|-----|
| Allen, Alice | Poster | Results from Improving the Visibility and Citability of Exoplanet Research Software | [P814](papers/P814/) |
| Barrett, Paul | Tutorial | An Introduction to the Julia Programming Language | [T801](papers/T801/) |
| Berriman, G. Bruce | Featured Poster | The Keck Observatory Archive Hurtles Towards the 2030s | [P811](papers/P811/) |
| Bryant, Aaron | Poster | ATRAN_SDC - Modelling Atmospheric Transmission Spectra for Airborne & Ground-Based Infrared Observations | [P809](papers/P809/) |
| Bryant, Aaron | Poster | The FIFI-LS Pipeline at the SOFIA Data Center – Preserving the legacy of Far-Infrared Imaging Spectroscopy | [P816](papers/P816/) |
| Chattopadhyay, Sabyasachi | Contributed Talk | FIBRA: FIber Bundle Reduction of Astronomical spectra — an instrument-agnostic pipeline for fiber-fed integral-field spectroscopy | [C803](papers/C803/) |
| Eigenbrot, Arthur | Contributed Talk | solar-wavelength-calibration: Designing a new tool for computing wavelength solutions of solar spectra | [C805](papers/C805/) |
| Fabbro, Sébastien | Contributed Talk | From FITS archives to differentiable multispectral sky models | [C810](papers/C810/) |
| Gianotto, Francesco | Contributed Talk | Engineering for Requirements: The Evolution of the Aegis Asteroid Impact Monitoring System at ESA | [C804](papers/C804/) |
| Gianotto, Francesco | Poster | Meerkat: An Operational Software System for Automated Imminent Impactor Detection and Community Alerting | [P815](papers/P815/) |
| Gómez, Miguel | Contributed Talk | GOATS: An end-to-end time-domain and multi-messenger astronomy platform | [C807](papers/C807/) |
| Holmberg, Conrad; Sidik | Poster | Obsolescence Management: Rewrite, Port, or Emulate? | [P820](papers/P820/) |
| Ibsen, Amanda | Poster | Improving operational reliability of the Rubin Observatory Control System. | [P801](papers/P801/) |
| Isoe, George | Featured Poster | High precision SOP-Based Optical Delay Measurement Technique for Square Kilometre Array Telescope | [P818](papers/P818/) |
| Jeschke, Eric | Poster | Transitioning Subaru's Remote Observing Software to a Web Site | [P807](papers/P807/) |
| Jiang, Hansen | Poster | A New Method for Visualizing Multiband Astronomical Data in the Hue-Saturation-Value Colour Space | [P802](papers/P802/) |
| Jurjen | Contributed Talk | Pushing LOFAR to its limits: Automated ultra-deep sub-arcsecond radio imaging below 200 MHz | [C809](papers/C809/) |
| Keimpema, Aard | Contributed Talk | SFXGPU: A GPU accelerated correlator for the European VLBI Network. | [C806](papers/C806/) |
| Kettenis, Mark | Contributed Talk | RADIOBLOCKS: Using GPUs for signal processing in the AI era | [C808](papers/C808/) |
| Lagos, Claudia | Poster | Astronomy and Computing: strengthening the link between astronomy, software and computation | [P810](papers/P810/) |
| Lahur, Paulus | Poster | The use of container in ASKAPsoft deployment | [P819](papers/P819/) |
| Lambert, Trystan | Contributed Talk | Nessie: The fastest group-finder in the world; or why rust is the best *high-level* language | [C801](papers/C801/) |
| Muders, Dirk | Poster | ALMA Pipeline Evolution | [P817](papers/P817/) |
| Phillips, Chris | Featured Poster | The Australia Telescope Compact Array "BIGCAT" GPU backend | [P803](papers/P803/) |
| R, Kavin Kumar N | Featured Poster | Disentangling AGN and stellar contributions to the Cosmic Spectral Energy Distribution using GAMA, SWAGX, EMU and eFEDS | [P821](papers/P821/) |
| Smallwood, Jay | Contributed Talk | Spatial Filtering in Practice: A GPU Pipeline for Real-Time RFI Mitigation | [C802](papers/C802/) |
| Stefano, Simona Di; Giovanni Lacopo | Poster | Modeling the sky in VLT/ESPRESSO spectra | [P813](papers/P813/) |
| Steinwender, Lukas | Featured Poster | Visual anomaly detection at scale using ThumP! | [P823](papers/P823/) |
| Stoehr, Felix | Poster | The ALMA spectral line search is now online | [P806](papers/P806/) |
| Tang, Amy | Poster | Astellum: A Morphological Feature Annotation Tool for Astronomy Outreach | [P804](papers/P804/) |
| Tocknell, James | Tutorial | Packaging and Managing Kubernetes Applications with Helm | [T802](papers/T802/) |
| Tocknell, James | Tutorial | Helm Templating and Kubernetes | [T803](papers/T803/) |
| Torres, Simón | Poster | A distributed system for collecting sky brightness data | [P824](papers/P824/) |
| verbenajl | Poster | grex: A Python Pipeline for SOFIA/GREAT Spectral Data Reduction | [P808](papers/P808/) |
| Verkouter, Marjolein | Featured Poster | What does 10M€ EC-funding buy you? (e.g.) RADIOBLOCKS! | [P812](papers/P812/) |
| Wu, Xiuqin | Poster | NED's new API | [P822](papers/P822/) |
| Zhang, Zhen | Featured Poster | XPhotonBank: Enabling Scientific Discoveries through Photon-Level Management of Einstein Probe X-ray Data | [P805](papers/P805/) |
<!-- papers-table:end -->
