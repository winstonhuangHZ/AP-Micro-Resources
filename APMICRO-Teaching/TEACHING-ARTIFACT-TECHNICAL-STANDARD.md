# AP Microeconomics Teaching Artifact Technical Standard

This document defines the reusable production rules for the AP Microeconomics
lesson plans, handouts, slides, visual assets, and generated PDFs in this
repository. It is intended to make a new session reproducible by another
person without reconstructing design decisions from an earlier session.

## 1. Source-of-truth architecture

Each session has four connected layers:

1. **Lesson plan** — the session objective map, timing, activity sequence, and
   official CED references.
2. **Handout shared source** — the student task sequence and teacher answer
   content. Student and teacher editions must be generated from the same
   `shared.tex` file.
3. **Slide source** — the teacher-facing presentation that follows the handout
   sequence and reveals prompts, diagrams, evidence, and answers in order.
4. **Visual source and manifest** — original charts, diagrams, downloaded
   images, source URLs, licenses, and intended session use.

For a new session, use this structure:

```text
APMICRO-Teaching/
├── Lesson-Plans/
├── Handouts/
│   └── session-XX/
│       ├── README.md
│       ├── SESSION-XX-HANDOUT-PLAN.md
│       ├── manifest.csv
│       └── en/
│           ├── shared.tex
│           ├── handout.tex
│           ├── answer-key.tex
│           ├── handout.pdf
│           └── answer-key.pdf
├── Slides/
│   └── session-XX/
│       ├── README.md
│       ├── manifest.csv
│       ├── Session-XX-Topic.tex
│       └── Session-XX-Topic.pdf
└── Visual-Plan/
    ├── visual-plan-36-sessions.md
    └── assets/
        └── source/
            └── sources.csv
```

The lesson plan owns the learning sequence. The handout owns student work.
The slide deck mirrors the handout but may split one activity into several
overlay pages for live teaching.

## 2. Alignment hierarchy

Use this hierarchy whenever sources use different wording:

1. **College Board CED** — controls required AP content, labels, and scope.
2. **Official AP Question Bank or Progress Check language** — controls the
   expected task form and scoring vocabulary.
3. **Open textbooks and university materials** — provide clear explanations,
   examples, and short source phrases.
4. **Original repository wording** — used for scenarios, prompts, and visual
   explanations when they do not alter the underlying concept.

The CED code must be recorded in the lesson plan and visible in the handout or
slide README. A concept may be student-friendly in the main body, but its
technical meaning must remain traceable to the CED or an indexed source.

### Session alignment example

For Unit 1, Session 01:

| Concept | Official anchor | Teaching wording | Artifact location |
|---|---|---|---|
| Scarcity and trade-offs | `MKT-1.A.1` | Resources are insufficient to satisfy all wants and needs | Slides causal chain; handout model box |
| Factors of production | `MKT-1.A.2` | Land, labor, and capital; established knowledge may be non-rival | Slides factors frame; handout H02/H01 |
| Allocation questions | `MKT-1.B.1` | What, how, and for whom | H03 and allocation slide overlays |
| Economic systems | `MKT-1.B.2` | Market, command, and mixed coordinating mechanisms | P01 and systems slide overlays |
| Opportunity cost | Bridge to `MKT-1.C` and cost-benefit work | Benefit of the next-best alternative forgone | G01 and causal-chain overlays |
| PPC | `MKT-1.C.1` | Preview only: movement along a boundary shows a trade-off | G01 PPC preview; full model begins in Session 02 |

### Source wording policy

Use short quotations when the exact textbook phrasing teaches a distinction.
Keep the quote on the same slide or page as a concise source label. Prefer a
paraphrase when the original wording would make the slide crowded. Do not copy
long textbook passages into student materials.

Approved short source phrases for this session include:

- “Economic trade-offs arise from the lack of sufficient resources to meet
  society's wants and needs.” — College Board CED, `MKT-1.A.1`.
- “the next best alternative action” and “the net benefit of the foregone
  alternative” — CORE Econ, Unit 3.3.
- Constrained choice, trade-offs, and opportunity cost — MIT OpenCourseWare,
  14.01 Lecture 1.

## 3. Reusable handout standard

### Document format

- Engine: XeLaTeX through `latexmk`.
- Class: `article`.
- Paper: US Letter, `11pt`.
- Geometry: `0.70in` margins with `includeheadfoot`.
- Main font: Libertinus through `\usepackage{libertinus}`.
- Paragraphs: no first-line indent, short paragraph spacing.
- Tables: `booktabs`, `tabularx`, and `array`.
- Response areas: bordered lines or boxes with enough height for handwritten
  answers.
- Graphics: repository-relative paths through `\graphicspath`; never use a
  machine-specific absolute path in a source file.

### Shared-source rule

`shared.tex` contains the complete document preamble, macros, and content.
The wrappers stay minimal:

```tex
% handout.tex
\input{shared.tex}
```

```tex
% answer-key.tex
\def\teacheredition{1}
\input{shared.tex}
```

Teacher-only material must be inside `\ifteacher ... \fi`, using the existing
answer and teacher-note macros. The student edition must never require a second
copy of the content to stay synchronized.

### Handout component IDs

Use stable component IDs so the handout, slide deck, lesson plan, and manifest
can refer to the same classroom object:

| Prefix | Meaning | Typical job |
|---|---|---|
| `H` | Handout core | objectives, retrieval, vocabulary, allocation table |
| `G` | Graph or visual | diagrams, graph interpretation, model bridge |
| `P` | Practice | comparison table or structured practice |
| `T` | Transfer | new context using the same model |
| `E` | Exit ticket | final causal explanation or uncertainty check |

Each component should record its time range, objective, student action, expected
evidence, and teacher answer in the session plan.

### Handout layout checks

Check every generated edition for:

- no clipped text, figures, or response boxes;
- no response box split across pages unless deliberately designed;
- no isolated concept box on an otherwise empty page;
- student edition contains only prompts and working space;
- teacher edition preserves the same page order and reveals answers in place;
- page count is recorded in the session README;
- the last page has a usable exit ticket and teacher note area.

## 4. Reusable slide standard

### Document format

- Engine: XeLaTeX through `latexmk`.
- Class: `beamer` with `aspectratio=169,11pt`.
- Theme: classic `Madrid` unless a session-specific decision is recorded.
- Font: Computer Modern style through `lmodern`.
- Canvas: 16:9, with `0.72cm` left and right text margins.
- Main slide title: 14pt / 17pt line height.
- Cover title: 17pt / 21pt line height.
- Subtitle: 12pt / 15pt line height.
- Body text: 15pt / 19pt line height.
- Block title: 14pt / 17pt line height.
- Navigation symbols: disabled.
- Grid lines: disabled unless a graph explicitly needs them.

### Color system

Use the shared AP palette:

| Name | Hex | Use |
|---|---|---|
| `APBlue` | `#17395C` | title bars, primary structure, axes |
| `APBlueDark` | `#102B45` | footer and secondary bars |
| `APTeal` | `#168C87` | positive or secondary concept |
| `APOrange` | `#C96B32` | opportunity cost, warning, answer emphasis |
| `Ink` | `#1E2F40` | primary body text |
| `Muted` | `#5E7185` | source notes and secondary text |
| `PaleBlue` | `#EEF4F9` | light block backgrounds |

### Slide composition rules

Each frame should have one classroom job. Use this order when appropriate:

1. question or prediction;
2. visual or evidence;
3. labels and mechanism;
4. conclusion or model answer.

Use one composition rather than a dashboard of repeated cards. Keep the main
visual on the left and the prompt or explanation on the right when the image is
the object of discussion. Use a full-width block only for a definition,
sentence stem, or final synthesis.

### Overlay rules

Overlays are teaching states, not decorative animation:

```tex
\begin{frame}<1-3>{Scarcity and choice}
  \only<1>{Question before explanation.}
  \only<2>{Evidence before labels.}
  \only<3>{Conclusion or model answer.}
\end{frame}
```

The PDF page count includes every overlay state. Record the mapping in the
session README. Never reveal an answer before the student prompt unless the
frame is explicitly a teacher model.

For decks distributed as page-by-page teaching PDFs, the footer must use the
physical presentation page counter (`\insertpagenumber` and
`\insertpresentationendpage`) so the displayed number includes every overlay.
Do not use `\inserttotalframenumber` for this purpose because it counts
logical frames and can undercount the pages that a teacher prints or advances
through in a PDF viewer.

### Source notes

Use a small muted source note when a slide uses official wording, a textbook
definition, or an external visual. Keep the source note short and readable:

```tex
\sourceNote{College Board CED, MKT-1.A.1}
```

The complete citation, license, and URL belong in the relevant README,
manifest, or source database. A source note is not a substitute for a license
record.

### Graph and visual rules

- Label both axes with meaningful economic variables and units when applicable.
- Label every curve directly: `Demand`, `Supply`, `MC`, `AVC`, `ATC`, and so on.
- Use dashed projection lines only when they help map a point to an axis.
- Use arrows for curve shifts or price/quantity changes when the direction is
  part of the learning objective.
- Compute cost curves from a consistent table or production model; do not draw
  unrelated MC, AVC, and ATC functions independently.
- Keep elasticity visually readable and avoid a plot that compresses all curves
  into a horizontal strip.
- Set the y-range to the instructional region and preserve enough vertical
  height for curve separation.
- Inspect the rendered image at the final output size. Code correctness alone
  does not establish visual correctness.

## 5. Reproducible build commands

### Slides

Run from the session slide directory:

```bash
latexmk -cd -xelatex -interaction=nonstopmode -halt-on-error \
  -outdir=build Session-XX-Topic.tex
cp build/Session-XX-Topic.pdf Session-XX-Topic.pdf
```

### Handout

Run from the language directory:

```bash
latexmk -cd -xelatex -interaction=nonstopmode -halt-on-error \
  -outdir=build handout.tex
cp build/handout.pdf handout.pdf

latexmk -cd -xelatex -interaction=nonstopmode -halt-on-error \
  -outdir=build answer-key.tex
cp build/answer-key.pdf answer-key.pdf
```

### Build verification

For each PDF, check page count and paper size:

```bash
pdfinfo output.pdf | rg 'Pages|Page size'
```

Render pages before delivery:

```bash
mkdir -p /tmp/apmicro-review
pdftoppm -png -r 160 output.pdf /tmp/apmicro-review/page
```

Then inspect representative pages and the full page set: cover, first prompt,
first definition, first graph, first answer reveal, and final exit ticket. For a
major layout change, inspect every rendered page.

The final check must include:

```bash
git diff --check
rg -n 'Overfull|Emergency stop|Fatal error|Undefined control sequence' build/*.log
```

Underfull boxes may be accepted only after visual inspection confirms that the
layout is readable and intentional. Any visible overlap, clipping, missing
math, excessive empty space, or unreadable label is a failed check.

## 6. Versioning and delivery

- Keep source, generated PDF, README, and manifest changes together.
- Record page counts and overlay ranges after every meaningful change.
- Do not add generated build auxiliary files to Git; keep them in ignored
  `build/` directories.
- Add every external image to the visual source manifest before embedding it.
- Preserve attribution and license terms in the source record and, when useful,
  a short slide or handout source note.
- Keep English as the primary artifact when an English and Chinese edition both
  exist. Link the Chinese edition from the English README and keep the two
  editions structurally synchronized.
- Commit significant source and generated-output changes together so another
  checkout can reproduce the delivered PDF.

## 7. Session 01 implementation record

The current Session 01 package demonstrates this standard:

- Beamer `Madrid`, 16:9, Computer Modern style, 37 overlay pages;
- shared handout source, 7-page student edition, and 8-page teacher edition;
- CED `MKT-1.A` and `MKT-1.B` alignment;
- factors of production and non-rival established knowledge;
- textbook-aligned scarcity and next-best-alternative wording;
- PPC explicitly limited to a Session 02 preview;
- source notes for CED, MIT OpenCourseWare, and CORE Econ;
- rendered visual checks for both slide and handout outputs.
