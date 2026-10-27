# AP Microeconomics One-Lesson Handout Design Specification

**Status:** Canonical production reference  
**Audience:** Lesson-plan authors, handout authors, slide authors, and teachers  
**Primary language:** English  
**Chinese edition:** Use the same structure and asset IDs; translate the instructional text in a separate source tree.  
**Applies to:** One 50–90 minute AP Microeconomics lesson

This document defines the standard design for one complete lesson package. A package contains a student handout, a teacher answer edition, a matching slide deck, shared visual assets, and a short production manifest. The handout is the durable student reference; the slides are the paced classroom layer.

## 1. Design goals

Every lesson package should help a student move through the same chain:

> **objective → model → graph or table → calculation → economic explanation → AP transfer**

The handout should make that chain visible. A student should be able to use it during class, finish it after class, and later review the same lesson without needing to reconstruct the teacher's slide deck.

The design has six goals:

1. **Traceability:** every learning target is linked to an official objective ID and to at least one student task.
2. **Economic coherence:** definitions, graphs, numbers, and written explanations describe the same model.
3. **Active use:** most pages contain something to complete, annotate, calculate, compare, or explain.
4. **AP transfer:** the lesson ends with a small MCQ/FRQ task that uses the same concept in a new context.
5. **Visual consistency:** the handout and slides use the same graph files, labels, colors, notation, and asset IDs.
6. **Revision safety:** source files, answer keys, data, licenses, and generated PDFs can be rebuilt and audited.

## 2. Where this specification fits in the repository

The production chain is:

```text
APMICRO-Teaching/Lesson-Plans/
    official-learning-objectives.csv
    session-learning-objectives.csv
    course-schedule-36-sessions.md
            │
            ▼
APMICRO-Teaching/Visual-Plan/
    visual-plan-36-sessions.md
    assets/exports/figures/
            │
            ├──────────────┐
            ▼              ▼
APMICRO-Teaching/Handouts/  APMICRO-Teaching/Slides/
    student handout          English and Chinese decks
    teacher key
    source manifest
```

The authoritative upstream files are:

- [`Lesson-Plans/session-learning-objectives.csv`](../Lesson-Plans/session-learning-objectives.csv)
- [`Lesson-Plans/OFFICIAL-LEARNING-OBJECTIVES.md`](../Lesson-Plans/OFFICIAL-LEARNING-OBJECTIVES.md)
- [`Lesson-Plans/course-schedule-36-sessions.md`](../Lesson-Plans/course-schedule-36-sessions.md)
- [`Visual-Plan/visual-plan-36-sessions.md`](../Visual-Plan/visual-plan-36-sessions.md)
- [`Visual-Plan/assets/exports/figures/`](../Visual-Plan/assets/exports/figures/)

The handout must not invent a new learning objective wording when an official objective is available. It may add a student-facing success criterion that makes the objective observable.

## 3. Standard package structure

Use one folder per lesson. The English tree is the primary production tree; the Chinese tree mirrors it.

```text
Handouts/
└── Unit-2/
    └── Session-05-Demand-Supply/
        ├── README.md
        ├── manifest.csv
        ├── en/
        │   ├── main.tex
        │   ├── handout.pdf
        │   └── answer-key.pdf
        ├── zh/
        │   ├── main.tex
        │   ├── handout.pdf
        │   └── answer-key.pdf
        ├── assets/
        │   ├── figures/
        │   └── source-notes.md
        └── data/
            └── illustrative-schedule.csv
```

The corresponding slide package uses the same session slug:

```text
Slides/
└── Unit-2/
    └── Session-05-Demand-Supply/
        ├── README.md
        ├── en/
        │   └── Session-05-Demand-Supply.pptx
        └── zh/
            └── Session-05-Demand-Supply.pptx
```

### Required package metadata

Every `README.md` or `manifest.csv` must record:

| Field | Required content |
|---|---|
| Session | `Session-05` and the unit number |
| Slug | One stable lowercase or title-case folder slug |
| Official objective IDs | Exact IDs from the lesson-plan objective map |
| Student objectives | Two to four observable outcomes |
| Duration | 50, 75, or 90 minutes |
| Handout source | Relative path to `en/main.tex` and `zh/main.tex` |
| Slide source | Relative path to English and Chinese decks |
| Figure IDs | Session figure filenames used in the package |
| Data sources | CSV or official series used in calculations or charts |
| Answer-key status | Draft, checked, or released |
| License notes | Attribution and reuse conditions for every external asset |
| Last visual QA | Date and reviewer initials |

## 4. Complete structure of one student handout

The default 90-minute handout is **five to seven pages**, excluding the answer key. A 50-minute version should usually be **three to five pages**. The page count is a pacing limit, not a reason to shrink type or remove writing space.

### Page 1 — Lesson identity and retrieval

Include:

- Unit and session number;
- short lesson title;
- official objective ID(s);
- two to four student-friendly learning objectives;
- success criteria;
- estimated lesson time;
- three to five retrieval questions from earlier sessions;
- one short diagnostic graph, table, or prediction.

The retrieval section should be answerable without opening the new lesson. It is for activating prior knowledge, not for introducing a second topic.

Recommended student-facing objective wording:

```text
By the end of this lesson, I can:

□ identify the variables on the graph and label both axes;
□ calculate the market equilibrium from a schedule or graph;
□ explain how a change in a determinant shifts demand or supply;
□ use a complete because → therefore → result explanation.
```

### Page 2 — Core model and vocabulary

Use a compact concept block rather than a page of prose. Each term should have:

| Item | Required form |
|---|---|
| Term | Bold term or short heading |
| Meaning | One or two sentences |
| Condition | When the term applies |
| Representation | Graph, equation, table, or example |
| Common error | One short warning |

Limit this page to the terms needed for the lesson's main task. A handout is not a textbook chapter.

### Page 3 — Teacher model / worked example

The model section should contain one fully specified example that the teacher can demonstrate in the slides and that the student can annotate in the handout.

Required components:

1. the initial data or situation;
2. the decision rule or economic relationship;
3. one graph or table;
4. one calculation with units;
5. one complete causal explanation;
6. a small “watch for” box with the most likely error.

The worked example must use the same numbers in the slide deck, answer key, and any generated chart. Do not make a slide example with one dataset and a handout example with another dataset unless the difference is intentional and explicitly labelled.

### Page 4 — Graph lab

The graph lab is the central AP Microeconomics page. Give students enough space to draw and label the graph themselves.

Every graph task should provide or ask for:

- `Price` or the appropriate vertical variable;
- `Quantity` or the appropriate horizontal variable;
- all required curve names, such as `Demand`, `Supply`, `ATC`, `AVC`, `MC`, `MR`, `MRP`, or `MFC`;
- an initial and final equilibrium where relevant;
- dotted projection lines from the key point to both axes;
- labels for quantities and prices, including `Q*`, `Q_M`, `P*`, or policy-specific labels;
- an arrow for a curve shift or a price/quantity change when the prompt asks for a change;
- units whenever a numerical scale is provided.

For a supplied figure, use it as a reference or annotation target. For a blank graph, keep the axes and scale visible unless the task specifically tests whether students can construct them.

### Page 5 — Calculation and guided practice

Use a repeatable three-row scaffold:

```text
Relationship / formula: __________________________________________
Substitution with units: _________________________________________
Answer and economic meaning: ____________________________________
```

The standard calculation sequence is:

1. identify the requested variable;
2. write the relationship;
3. substitute values with units;
4. calculate and round only at the end;
5. state what the result means in the model.

Include two or three tasks that increase in independence:

- **Guided:** formula and relevant values are supplied;
- **Supported:** students select the relationship from a formula bank;
- **Independent:** students interpret the prompt and produce the full response.

### Page 6 — AP transfer task

The transfer section should contain either:

- four to eight MCQs with a short rationale field; or
- one FRQ-style prompt with two to four subparts; or
- a mixed set with two to four MCQs and one short FRQ subpart.

The task must change the context while preserving the same economic relationship. If the lesson teaches a demand shift using coffee, the transfer task may use concert tickets or rental housing, but it should not silently introduce a new model.

For MCQs, provide:

```text
Answer: ______
Evidence from the graph/table/prompt: ____________________________
Why the tempting alternative is wrong: ___________________________
```

For FRQ subparts, provide separate space for:

- graph;
- calculation;
- explanation;
- final conclusion or policy judgment.

### Page 7 — Error analysis and exit ticket

Use the project's error categories:

- **Concept** — misunderstood the economic relationship;
- **Graph** — wrong curve, shift, label, intersection, or projection;
- **Calculation** — wrong formula, arithmetic, sign, or unit;
- **Reading** — missed a condition, scale, or requested variable;
- **Expression** — answer was not stated clearly enough to earn the point.

The exit ticket should take two to four minutes:

```text
The key relationship from today is: _______________________________

If __________________ changes, then __________________ because ____.

One point I still need to check: __________________________________
```

## 5. Teacher answer edition

The teacher key is a separate PDF and should not be hidden in the student handout. It follows the same page order so that a teacher can compare pages quickly.

For every answer, include the minimum evidence needed to verify it:

- MCQ answer plus a one-sentence reason;
- graph with all required labels and projections;
- calculation with formula, substitution, unit, and final interpretation;
- FRQ response organized by subpart;
- a note on common wrong answers where the error is instructional.

The answer key should not simply repeat the prompt in a different color. It should show what makes the response complete and what would lose a point.

### Graph answer-key standard

The answer graph must be checked at full size and at the expected print size. Confirm:

1. the vertical axis and horizontal axis are named;
2. every curve has a clear name;
3. the curve shift direction is correct;
4. the relevant intersection is calculated from the data;
5. dotted projections reach the correct axes;
6. `Q` and `P` labels do not overlap or sit farther out than the axis title;
7. no line or annotation hides another curve;
8. the figure has no accidental grid or decorative text;
9. the same figure appears in the matching slide deck;
10. the explanation below the graph matches the graph.

## 6. Recommended LaTeX architecture

### 6.1 Class choice

Use `article` or `extarticle` as the handout class. Do **not** use the `acmart` class itself for a classroom handout: its publication metadata, front matter, review modes, and conference-oriented layout create unnecessary constraints.

Use the **Libertine/Libertinus family** for the visual language that the user prefers from ACM materials. This preserves the familiar serif text and math appearance while allowing ordinary one-column teaching layouts, wider writing areas, bilingual editions, and controlled margins.

Recommended engine:

- English: XeLaTeX or LuaLaTeX;
- Chinese: XeLaTeX with `xeCJK` or LuaLaTeX with a CJK font setup;
- use the same engine for the English and Chinese package when possible.

The font policy is:

```latex
\usepackage{fontspec}
\setmainfont{Libertinus Serif}
\setsansfont{Libertinus Sans}
\setmonofont{Libertinus Mono}

\usepackage{unicode-math}
\setmathfont{Libertinus Math}
```

If the installed TeX distribution exposes the older package names instead, use the corresponding Libertine package consistently. Do not mix Computer Modern body text with Libertine headings or use a different math font for only one language edition.

Chinese editions should add a CJK family that is available on the build machine, for example:

```latex
\usepackage{xeCJK}
\setCJKmainfont{Noto Serif CJK SC}
\setCJKsansfont{Noto Sans CJK SC}
```

The exact installed CJK font should be recorded in the package README if it affects reproducibility.

### 6.2 Core packages

The baseline preamble should include:

```latex
\usepackage[letterpaper,margin=0.72in,includeheadfoot]{geometry}
\usepackage{microtype}
\usepackage{mathtools,amssymb}
\usepackage{graphicx}
\usepackage{booktabs,tabularx,array,longtable}
\usepackage{enumitem}
\usepackage[most]{tcolorbox}
\usepackage{tikz}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
\usepackage{caption}
\usepackage{fancyhdr,lastpage}
\usepackage{hyperref}
\usepackage[nameinlink,noabbrev]{cleveref}
```

Use `tcolorbox` for learning objectives, formulas, misconceptions, and exit tickets. Use `booktabs` for data tables. Use `pgfplots` only for figures that must be generated inside TeX; prefer the repository's validated PNG/SVG/PDF assets for the publication-quality AP graphs.

### 6.3 Page and typography defaults

| Element | Default |
|---|---:|
| Body text | 10.5–11 pt |
| Main title | 18–22 pt |
| Section heading | 13–15 pt |
| Figure caption | 8.5–9 pt |
| Margin | 0.68–0.75 in |
| Paragraph spacing | 3–5 pt |
| Body line spacing | about 1.05–1.12 |
| Student writing lines | at least 0.28 in apart |
| Graph minimum print width | 3.0 in for a single graph |

Do not solve an overflow problem by shrinking the whole document below 10 pt. Shorten prose, split a crowded table, or move the answer key to its own page.

### 6.4 Reusable component names

Keep the component vocabulary stable across lessons:

```latex
\newtcolorbox{objectivebox}{...}
\newtcolorbox{successbox}{...}
\newtcolorbox{modelbox}{...}
\newtcolorbox{warningbox}{...}
\newtcolorbox{exitbox}{...}

\newcommand{\answerline}[1][0.96\linewidth]{\rule{#1}{0.4pt}}
\newcommand{\formula}[1]{\[\boxed{#1}\]}
\newcommand{\asset}[2][]{\includegraphics[#1]{#2}}
```

The visual style should use the existing AP Micro palette sparingly: dark blue for structure, teal for a positive or selected outcome, orange/red for a cost, policy, or warning, and pale fills for boxes. Color must never be the only way to distinguish two curves or two answer states.

## 7. Handout and PPT correspondence

The slide deck and handout are two views of one lesson model.

| Handout block | Slide role | Classroom action |
|---|---|---|
| Lesson identity and objectives | Opening slide | Students read and paraphrase the target |
| Retrieval | Warm-up slide | Individual response, then pair check |
| Core model | Concept slide | Teacher introduces only the needed vocabulary |
| Worked example | Model slide(s) | Reveal one step at a time |
| Graph lab | Graph build slide | Students draw before the completed graph appears |
| Calculation scaffold | Calculation slide | Reveal formula, substitution, and meaning separately |
| Guided practice | Practice slide | Timer, prompt, and response mode |
| AP transfer | MCQ/FRQ slide | Students commit to an answer before discussion |
| Error analysis | Review slide | Classifies the mistake rather than only showing the answer |
| Exit ticket | Final slide | Students submit or photograph the response |

### Slide pacing rule

One slide should have one classroom job. Avoid putting a full handout page on a slide. The slide should display the prompt, diagram, or reveal step that the teacher is currently using; the handout should preserve the complete record and the space for student work.

### Shared IDs

Use stable IDs in both sources:

```text
H01  handout objective block
H02  retrieval set
H03  worked example
G01  main graph
G02  shifted graph
C01  calculation scaffold
P01  guided practice
T01  AP transfer task
E01  exit ticket
```

Put the ID in the LaTeX source, slide notes, and package manifest. This makes it possible to change the figure or wording without losing the handout-to-slide relationship.

## 8. Standard 90-minute lesson choreography

| Minutes | Handout block | Slides | Teacher move | Student evidence |
|---:|---|---|---|---|
| 0–8 | Retrieval | 1–2 | Set a quiet timer and collect a prediction | Initial answer |
| 8–15 | Objectives | 3 | Connect the prediction to today's question | Paraphrased target |
| 15–28 | Core model | 4–6 | Introduce only essential terms and relationships | Annotated vocabulary |
| 28–42 | Worked example | 7–9 | Reveal graph/calculation in steps | Completed model |
| 42–58 | Graph lab | 10–12 | Pause before each curve, shift, and projection | AP-style graph |
| 58–70 | Guided calculation | 13–14 | Ask for formula before numbers | Completed scaffold |
| 70–82 | AP transfer | 15–17 | Individual attempt, pair justification, class debrief | MCQ rationale or FRQ subpart |
| 82–87 | Error analysis | 18 | Code the error and repair one response | Revised response |
| 87–90 | Exit ticket | 19 | Collect the smallest useful evidence | One causal sentence |

For a 50-minute lesson, use:

```text
0–5 retrieval → 5–10 objective → 10–23 model →
23–38 graph/calculation practice → 38–47 AP transfer → 47–50 exit ticket
```

## 9. Visual and graph production rules

All supplied graphs must follow the repository's AP-style visual rules:

- use `Price` and `Quantity` or the model-specific variable names;
- label every curve in the figure or in an unambiguous legend;
- calculate intersections from the schedule or model data;
- draw `MC` from calculated marginal changes when a cost schedule is used;
- show `MC` declining first and rising later when the model requires a Nike-swoosh shape;
- use dotted projection lines for important prices and quantities;
- offset adjacent labels such as `Q_A`, `Q_B`, `Q_M`, and `Q*`;
- keep price labels between the y-axis and the y-axis title;
- remove grid lines when they reduce the readability of a graph-only asset;
- use a 3:2 landscape canvas by default, while allowing naturally wide maps, dashboards, and timelines to use a wider ratio;
- remove editorial titles and long explanatory paragraphs from reusable graph assets; add those in the handout or slide text layer;
- inspect the exported PNG at print size and inspect the PDF/SVG for clipping.

The current figure generator is:

[`Visual-Plan/assets/python/build_publication_figures.py`](../Visual-Plan/assets/python/build_publication_figures.py)

Do not redraw an existing validated figure inside a handout with a second, slightly different function unless the lesson intentionally needs a different view.

## 10. Accessibility and print requirements

Every handout should remain usable in grayscale and when printed on ordinary letter paper.

- Use text labels, line styles, markers, or patterns in addition to color.
- Keep contrast high between text and fill colors.
- Do not place essential information only in a legend far from the curve.
- Keep writing space clear of decorative backgrounds.
- Use descriptive figure captions in the teacher edition and concise captions in the student edition.
- Include alt text or a text description in the package README for important figures.
- Use real text for equations and labels when possible; avoid flattening all information into a screenshot.
- Check that the Chinese edition does not create line breaks inside formulas or variable labels.

## 11. Source, licensing, and attribution

Each package must separate three kinds of material:

1. **Original:** generated figures, original prompts, original explanations, and synthetic datasets created for this repository.
2. **Openly reusable:** material used under a compatible open license, with the license and attribution recorded.
3. **Reference-only:** copyrighted or access-controlled examples used for internal analysis; do not redistribute them in the released handout or deck.

For every external image, table, dataset, or adapted diagram, record:

```text
asset_id, title, creator, source, license, attribution_text,
adapted?, local_path, allowed_outputs, checked_on
```

Do not put a third-party image into the handout merely because it is easy to download. Prefer an original Matplotlib figure, an open-license image with clear attribution, or a simple diagram drawn from first principles.

## 12. Production and QA workflow

### Before writing

- Read the session row in `session-learning-objectives.csv`.
- Select no more than two to four main objectives.
- Select the main graph or table from the visual plan.
- Decide whether the lesson's main student product is a graph, calculation, explanation, or comparison.
- Choose one AP transfer task that preserves the same model.

### During writing

- Write the answer key at the same time as the student version.
- Use the same notation in handout, slides, data, and figures.
- Keep prompt numbers and answer-key numbers synchronized.
- Add every figure and source to `manifest.csv`.
- Add `H/G/C/P/T/E` component IDs to both handout and slide source.

### Before release

```bash
# compile English and Chinese editions
xelatex -interaction=nonstopmode -halt-on-error main.tex

# inspect the generated PDFs visually
pdftoppm -png -r 160 handout.pdf /tmp/handout-preview
pdftoppm -png -r 160 answer-key.pdf /tmp/answer-preview

# check source and repository indexes
git diff --check
python3 scripts/update_indexes.py
```

The visual review must check:

- page breaks;
- blank writing space;
- table width;
- figure clipping;
- font consistency;
- equation rendering;
- bilingual line wrapping;
- answer-key alignment;
- slide/handout figure identity;
- attribution and source completeness.

### Release gate

A lesson is ready when:

- the official objective is traceable;
- the student can produce the stated evidence;
- every answer is checked against the same model/data;
- the main graph passes the AP graph checklist;
- the handout and slides share the same asset IDs;
- English and Chinese source trees are structurally parallel;
- PDFs render without clipping or missing fonts;
- source and license records are complete.

## 13. Suggested package README template

```markdown
# Session 05 — Demand and Supply

## Metadata

- Unit: Unit 2
- Duration: 90 minutes
- Official objectives: MKT-3.A, MKT-3.C, MKT-3.D
- Student product: labeled market-equilibrium graph plus causal explanation
- Status: checked

## Files

- English handout: `en/handout.pdf`
- English answer key: `en/answer-key.pdf`
- Chinese handout: `zh/handout.pdf`
- Chinese answer key: `zh/answer-key.pdf`
- English slides: `../../../../Slides/Unit-2/Session-05-Demand-Supply/en/`
- Chinese slides: `../../../../Slides/Unit-2/Session-05-Demand-Supply/zh/`

## Shared component IDs

| ID | Component | Handout page | Slide |
|---|---|---:|---:|
| H01 | Objectives | 1 | 3 |
| H02 | Retrieval | 1 | 1–2 |
| G01 | Market equilibrium graph | 3 | 7–9 |
| C01 | Equilibrium calculation | 4 | 13 |
| T01 | AP transfer | 5 | 15–17 |
| E01 | Exit ticket | 6 | 19 |

## Visual assets

- `session-05-market-equilibrium-chart.png`
- `session-05-market-equilibrium-chart.pdf`

## Sources and license

Record all external sources and licenses in `assets/source-notes.md` and `manifest.csv`.
```

## 14. Recommended first implementation

Use Session 05, **Demand and Supply**, as the pilot template because it exercises the full production chain without requiring a large number of curves:

1. official objective block;
2. retrieval from scarcity and PPC;
3. demand/supply vocabulary;
4. market-equilibrium worked graph;
5. schedule-to-equilibrium calculation;
6. shift-and-new-equilibrium graph lab;
7. MCQ plus one short FRQ explanation;
8. error code and exit ticket;
9. matching slide deck with the same `G01` and `C01` assets.

Once the Session 05 package passes the release gate, copy its folder structure for Sessions 06–36. Change the content and assets, but keep the metadata, component IDs, answer-key structure, and QA process stable.

## 15. Short design principle

The handout should be complete enough to review from later, while the slide deck should be paced enough to teach from now. Both should describe one model, use one notation system, and point to the same evidence.

