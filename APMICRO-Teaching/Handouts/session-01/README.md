# Session 01 — Scarcity and Resource Allocation

## Metadata

- Unit: Unit 1
- Duration: 90 minutes
- Official objectives: `MKT-1.A`, `MKT-1.B`
- CED pages: 41–42
- Student product: a resource-allocation comparison and one PPF-style trade-off explanation
- Status: prototype; source compiled and visually checked on 2026-10-27

## Files

- Plan: [`SESSION-01-HANDOUT-PLAN.md`](SESSION-01-HANDOUT-PLAN.md)
- Student source: [`en/handout.tex`](en/handout.tex)
- Teacher source: [`en/answer-key.tex`](en/answer-key.tex)
- Shared source: [`en/shared.tex`](en/shared.tex)
- Student PDF: [`en/handout.pdf`](en/handout.pdf)
- Teacher PDF: [`en/answer-key.pdf`](en/answer-key.pdf)
- Manifest: [`manifest.csv`](manifest.csv)

The student and teacher sources share `en/shared.tex`. The teacher edition is selected by a wrapper flag, so the prompt numbering and figures remain synchronized.

## Shared components

| ID | Component | Intended use |
|---|---|---|
| `H01` | Objectives and vocabulary | Make the official targets observable |
| `H02` | Retrieval | Activate scarcity and resource distinctions |
| `H03` | Allocation scenario | Practice what/how/for whom |
| `G01` | Choice and PPF bridge | Explain one foregone alternative |
| `P01` | Economic-system comparison | Compare coordination mechanisms |
| `T01` | AP transfer | New context with the same model |
| `E01` | Exit ticket | One causal sentence and one uncertainty |

## Visual assets and licensing

- `../../../Visual-Plan/assets/exports/figures/session-01-three-resource-scarcity-panel.png` — original illustrative figure generated in this repository.
- `../../../Visual-Plan/assets/diagrams/session-01-choice-opportunity-cost-card.png` — original concept diagram generated in this repository.
- Optional slide opener only: `../../../Visual-Plan/assets/source/rice-planting-bhutan.jpg`, recorded in `Visual-Plan/assets/source/sources.csv` as a Wikimedia Commons image by Bernard Gagnon, CC BY-SA 4.0. It is not embedded in this prototype PDF.

No new external asset is introduced by this package.

## Build

From this directory:

```bash
latexmk -cd -xelatex -interaction=nonstopmode -halt-on-error -outdir=build handout.tex
latexmk -cd -xelatex -interaction=nonstopmode -halt-on-error -outdir=build answer-key.tex
cp build/handout.pdf handout.pdf
cp build/answer-key.pdf answer-key.pdf
```

The wrapper sources include `shared.tex`, so the package uses the direct
`latexmk` commands above. The generated PDFs are kept beside their source
files after visual QA; auxiliary files remain in the ignored `en/build/`
directory.

The latest visual check used rendered PNG pages and confirmed that both
editions have no clipping or overlapping response areas. Student edition: 7
pages. Teacher edition: 8 pages.
