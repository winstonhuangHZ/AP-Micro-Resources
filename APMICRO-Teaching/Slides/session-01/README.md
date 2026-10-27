# Session 01 Slides — Scarcity and Resource Allocation

## Metadata

- Unit: Unit 1
- Session: Session 01
- Duration: 90 minutes
- Official objectives: `MKT-1.A`, `MKT-1.B`
- Language: English primary edition
- Status: prototype compiled and visually checked (11 slides)

## Files

- Editable source: [`Session-01-Scarcity.tex`](Session-01-Scarcity.tex)
- PDF deck: [`Session-01-Scarcity.pdf`](Session-01-Scarcity.pdf)
- Manifest: [`manifest.csv`](manifest.csv)

The deck follows the handout sequence while keeping each slide to one classroom
job. The handout remains the full student record; the deck supplies prompts,
definitions, visual reveals, transfer practice, and the exit ticket.

## Build

From this directory:

```bash
latexmk -cd -xelatex -interaction=nonstopmode -halt-on-error -outdir=build Session-01-Scarcity.tex
cp build/Session-01-Scarcity.pdf Session-01-Scarcity.pdf
```

The source uses XeLaTeX with Libertinus and a 16:9 Beamer canvas. Build
auxiliary files remain in the ignored `build/` directory.

Final verification on 2026-10-27 produced an 11-page PDF with no fatal errors,
overfull boxes, or LaTeX warnings in the build log.

## Shared component order

| Slide | Component | Handout connection |
|---:|---|---|
| 1 | Opening | Lesson identity |
| 2 | `H02` | Retrieval and prediction |
| 3 | `H01` | Official targets |
| 4 | `H01` | Scarcity and trade-offs |
| 5 | `H03` | What, how, and for whom |
| 6 | `P01` | Economic systems |
| 7 | `G02` | Resource bundle visual |
| 8 | `G01` | Choice and opportunity cost |
| 9 | `G01` | PPF bridge |
| 10 | `T01` | AP transfer |
| 11 | `E01` | Exit ticket |

## Visual assets and licensing

The deck embeds only existing repository assets:

- `../../Visual-Plan/assets/exports/figures/session-01-three-resource-scarcity-panel.png` — original illustrative figure generated in this repository; repository license applies.
- `../../Visual-Plan/assets/diagrams/session-01-choice-opportunity-cost-card.png` — original concept diagram generated in this repository; repository license applies.

The optional Wikimedia Commons image `rice-planting-bhutan.jpg` is indexed for
Session 01 but is not embedded in this prototype. Its source and CC BY-SA 4.0
terms remain recorded in `Visual-Plan/assets/source/sources.csv`.

The PPF bridge is an editable TikZ diagram using the same qualitative sketch as
the accepted Session 01 handout. It is intentionally limited to movement along
the boundary and does not introduce Session 2's full PPC model.

## Visual QA

The PDF was rendered to PNG at 160 dpi and reviewed as individual pages and as
a contact sheet on 2026-10-27. The release check covers title and body fit,
image proportions, asset clipping, readable labels, consistent margins, and
slide-level whitespace. No visible clipping, overlap, or distracting empty
space remained in the final prototype.
