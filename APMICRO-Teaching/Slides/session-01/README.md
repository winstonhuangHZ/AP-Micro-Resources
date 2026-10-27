# Session 01 Slides — Scarcity and Resource Allocation

## Metadata

- Unit: Unit 1
- Session: Session 01
- Duration: 90 minutes
- Official objectives: `MKT-1.A`, `MKT-1.B`
- Language: English primary edition
- Template: classic Beamer `Madrid`
- Status: revised prototype with teaching overlays
- Final PDF pages: 34

## Files

- Editable source: [`Session-01-Scarcity.tex`](Session-01-Scarcity.tex)
- PDF deck: [`Session-01-Scarcity.pdf`](Session-01-Scarcity.pdf)
- Manifest: [`manifest.csv`](manifest.csv)

The deck follows the accepted Session 01 handout sequence. Each instructional
frame uses Beamer overlays so the PDF presents one teaching step per page:
question before explanation, visual before labels, evidence before answer, and
prompt before model response.

## Build

From this directory:

```bash
latexmk -cd -xelatex -interaction=nonstopmode -halt-on-error -outdir=build Session-01-Scarcity.tex
cp build/Session-01-Scarcity.pdf Session-01-Scarcity.pdf
```

The source uses XeLaTeX, Computer Modern via Latin Modern, a 16:9 canvas, and the classic `Madrid`
Beamer theme. Auxiliary files remain in the ignored `build/` directory.

## Overlay structure

| PDF pages | Group | Teaching sequence |
|---:|---|---|
| 1 | Opening title | Lesson identity |
| 2–3 | `H02` opening | Question → today’s answer |
| 4 | `H01` targets | Official objectives |
| 5–7 | `H01` scarcity visual | Resource image → constraints → conclusion |
| 8–10 | `H01` causal chain | Scarcity → choice → opportunity cost |
| 11–14 | `H03` allocation | What → how → for whom → synthesis |
| 15–18 | `P01` systems | Frame → market → command → mixed/conclusion |
| 19–21 | `G02` resource bundle | Image → labels → trade-off |
| 22–24 | `G01` opportunity cost | Choice → foregone alternative → definition |
| 25–28 | `G01` PPF bridge | Curve → A/B points → projections → conclusion |
| 29–31 | `T01` AP transfer | Question → evidence → answer |
| 32–34 | `E01` exit ticket | Prompt → response space → model answer |

## Visual assets and licensing

The deck embeds only existing repository assets:

- `../../Visual-Plan/assets/exports/figures/session-01-three-resource-scarcity-panel.png` — original illustrative figure generated in this repository; repository license applies.
- `../../Visual-Plan/assets/diagrams/session-01-choice-opportunity-cost-card.png` — original concept diagram generated in this repository; repository license applies.

The optional Wikimedia Commons image `rice-planting-bhutan.jpg` is indexed for
Session 01 but is not embedded. Its source and CC BY-SA 4.0 terms remain
recorded in `Visual-Plan/assets/source/sources.csv`.

## Visual QA

The final 34-page PDF was rendered to PNG at 160 dpi and reviewed page by page
and as a contact sheet on 2026-10-27. The review checked the Madrid title bars,
overlay order, text size, image proportions, TikZ geometry, margins, clipping,
overlap, and whitespace. The final build has no fatal errors, overfull boxes,
or underfull boxes in the XeLaTeX log.
