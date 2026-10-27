# Session 01 Handout Plan — Scarcity and Resource Allocation

## Research basis

- **Official objectives:** `MKT-1.A` and `MKT-1.B`.
- **CED pages:** 41–42 in the local College Board *AP Microeconomics Course and Exam Description, Effective Fall 2026*.
- **Official boundary:** students define resources and the causes of scarcity; then explain the three resource-allocation questions and how a command, market, or mixed economic system coordinates scarce resources.
- **Course schedule product:** use a PPF-style choice to explain one trade-off. The PPF is used here as a short bridge to Session 2, where `MKT-1.C` is taught in full.
- **Local practice alignment:** `TB_11Scarcityandchoice.pdf` emphasizes scarce resources, factors of production, trade-offs, and nonrival knowledge; `TB_12economicsystem.pdf` emphasizes private ownership, price signals, government direction, and the three allocation questions. The prototype uses original prompts that exercise the same concepts without reproducing the bank.

## Learning-objective mapping

| Handout block | Component ID | Evidence students produce | Official link |
|---|---|---|---|
| Retrieval and prediction | `H02` | A distinction between a scarce and a non-scarce resource | `MKT-1.A` |
| Vocabulary and model | `H01` | Definitions of resource, scarcity, trade-off, and factor of production | `MKT-1.A` |
| Resource-allocation table | `H03` | Answers to what, how, and for whom to produce | `MKT-1.B`, `MKT-1.B.1` |
| Economic-system comparison | `P01` | A comparison of command, market, and mixed coordination mechanisms | `MKT-1.B`, `MKT-1.B.2` |
| Choice visual and bridge graph | `G01` | One complete because → therefore → result explanation of a trade-off | `MKT-1.A`; bridge to `MKT-1.C` |
| AP transfer | `T01` | Original MCQ and short-response reasoning | `MKT-1.A`, `MKT-1.B` |
| Exit ticket | `E01` | A one-sentence causal explanation and one uncertainty | `MKT-1.A` or `MKT-1.B` |

## 90-minute production and classroom plan

| Minutes | Handout activity | Slide / teacher move | Student evidence |
|---:|---|---|---|
| 0–8 | `H02` retrieval and prediction | Display one choice prompt; collect the first answer | Scarcity prediction |
| 8–15 | `H01` objectives and vocabulary | Define resource, scarcity, trade-off, and factors of production | Annotated terms |
| 15–30 | `H03` allocation questions | Reveal a constrained community-resource scenario | Three allocation decisions |
| 30–45 | `P01` economic systems | Compare coordinating mechanisms and private/public ownership | Completed comparison |
| 45–60 | `G01` choice card and simple PPF bridge | Model one foregone alternative; connect a move along a PPF to a trade-off | Labeled choice and causal sentence |
| 60–75 | Guided practice | Pair students and ask them to classify the resource and allocation mechanism | Short explanations |
| 75–86 | `T01` AP transfer | Individual attempt, then evidence-based discussion | MCQ reasons and short response |
| 86–90 | `E01` exit ticket | Collect the smallest useful evidence | One causal sentence |

## Visual choices

1. `G01` uses `Visual-Plan/assets/diagrams/session-01-choice-opportunity-cost-card.png`. It is original repository work and makes the foregone alternative visible without introducing a second graph model.
2. `H03` uses `Visual-Plan/assets/exports/figures/session-01-three-resource-scarcity-panel.png`. It is an original illustrative allocation table; the handout places the classroom question beside the figure rather than adding a long caption inside the asset.
3. The plan keeps `Visual-Plan/assets/source/rice-planting-bhutan.jpg` available as an optional slide opener. The prototype does not embed the photograph, so the student handout stays focused and the classroom can use the image without making it evidence for a general economic claim.

## LaTeX and page design

- Use `article` with the repository's Libertine/Libertinus visual language, rather than the `acmart` class. The class is suited to a one-column classroom handout with writing space; the font family preserves the user's preferred ACM-like serif appearance.
- Compile English editions with XeLaTeX. The source uses `libertinus` and `unicode-math` where available, with the local TeX distribution providing the font files.
- Use letter paper, approximately 0.68–0.72 inch margins, 10.5–11 pt body text, restrained dark blue/teal/orange fills, and high-contrast labels that also work in grayscale.
- Keep reusable visual assets free of editorial titles and put the classroom prompt and caption in LaTeX. Keep student writing lines at least 0.28 inch apart.
- The student edition is seven pages after the prototype's writing space and visual checks: retrieval and objectives; core model; allocation systems; choice/PPF bridge; AP transfer and exit ticket. The teacher edition follows the same page order and reveals answers in muted answer boxes across nine pages.

## Student and teacher versions

- `en/handout.tex` produces the student edition with blank response lines and unfilled prompts.
- `en/answer-key.tex` sets the same shared content source to teacher mode. It shows expected answers, a model causal sentence, and instructional notes beneath the same prompts.
- The shared `en/shared.tex` source is the single content source for both editions. This prevents drift in question numbering, figures, and numerical examples.

## Content boundaries and cautions

- Do not treat scarcity as the same thing as shortage, poverty, or an unfair outcome. Scarcity is the persistent condition that wants exceed available resources.
- Do not call money a factor of production in this lesson. Capital means produced physical inputs such as tools, machinery, or buildings; financial capital is not the same classroom category.
- Established knowledge can be nonrival in the CED example. The handout therefore asks students to distinguish a scarce machine from knowledge that can be used by multiple producers at the same time.
- A market economy is not defined as automatically fair or perfectly efficient. A command economy is not defined as eliminating scarcity. A mixed economy combines coordination mechanisms.
- The PPF bridge asks only for a trade-off explanation. Efficiency, underutilization, growth, curvature, and opportunity-cost calculations belong to Session 2 and later Unit 1 work.
- The handout does not use macroeconomic indicators, unemployment, inflation, banking, or government objectives. Those are outside this Session 1 prototype.

## Review and release checklist

- [x] Official IDs and CED pages recorded.
- [x] Original prompts used instead of copying the local question bank.
- [x] Shared component IDs included in source and manifest.
- [x] Existing local visuals reused with source paths recorded.
- [x] Compile student and teacher PDFs with XeLaTeX.
- [x] Render PDF pages to PNG and inspect for clipping, overflow, missing glyphs, and writing-space adequacy.
- [x] Check that the teacher key has the same page order and prompt numbering.
