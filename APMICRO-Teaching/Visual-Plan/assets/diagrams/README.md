# Original Concept Diagrams

This folder contains locally generated teaching diagrams for the 36-session AP Microeconomics visual plan.

- Every diagram has PNG, SVG, and PDF exports.
- `diagram-manifest.csv` records the session, intended use, and original-work status.
- The diagrams keep only the labels needed for reading the visual. Long titles, captions, source notes, and classroom directions belong in the LaTeX handout or slide deck.
- The PNG exports are suitable for slides and quick previews; SVG and PDF preserve vector quality for LaTeX and print.

Regenerate the set from the repository root with:

```bash
python APMICRO-Teaching/Visual-Plan/assets/python/build_concept_diagrams.py
```

The diagrams are original repository work. External photographs and other third-party materials are kept under `../source/` with attribution records in `../source/sources.csv`.
