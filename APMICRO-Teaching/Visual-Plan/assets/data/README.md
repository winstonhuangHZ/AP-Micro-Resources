# Visual data assets

This directory contains the data inputs for the AP Microeconomics visual plan.

## Source policy

The current batch uses official FRED CSV snapshots for public indicators and locally generated illustrative tables for textbook models. Kaggle is not required for these lessons. Kaggle may be considered later for a specific, well documented industry or household dataset, but it should not replace BLS, BEA, NBER, Census, or Federal Reserve sources when an official series exists.

## Folders

- `raw/` — unchanged FRED CSV snapshots.
- `derived/` — locally calculated inflation, growth, recession joins, and aligned dashboards.
- `illustrative/` — synthetic tables for PPC, supply and demand, elasticity, costs, market structures, factor markets, externalities, and review templates. These are models, not measured real-world observations.
- `manifest.csv` — source URL, retrieval date, byte count, SHA-256, and licensing notes for every CSV.

## Rebuild

From the repository root:

```bash
python3 scripts/download_visual_data.py
python3 scripts/build_visual_plan.py
python3 scripts/update_indexes.py
```

The generated charts should cite the relevant manifest row on the figure itself.
