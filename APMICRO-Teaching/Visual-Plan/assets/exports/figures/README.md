# Publication figures

This folder contains the first rendered batch of AP Microeconomics figures generated with `matplotlib.pyplot`.

## Formats

- `.png` — 320 DPI raster files for slide and handout placement.
- `.svg` — editable vector files for layout and annotation.
- `.pdf` — vector files for print and publication workflows.

## Design system

- Dark navy typography and axes for readable projection and print.
- Blue, teal, orange, purple, and red series with redundant labels where color alone would be ambiguous.
- Direct titles, axis units, restrained gridlines, and source notes on every figure.
- Synthetic classroom models are labelled as illustrative; public indicators cite their local FRED snapshot.
- Figure names use the session number and visual-plan title so they can be mapped back to the lesson plan.

## Rebuild

From the repository root:

```bash
python3 APMICRO-Teaching/Visual-Plan/assets/python/build_publication_figures.py
```

The complete output catalog is [`figure-manifest.csv`](figure-manifest.csv). The current batch covers every `Python chart` and `Python/diagram` item in the 36-session visual plan. Concept diagrams and external source photographs remain separate production tracks.
