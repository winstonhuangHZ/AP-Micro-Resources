# Visual Assets

Reserved layout for future asset production:

- `source/` — 42 downloaded source images and their metadata; keep these files unchanged
- `source/ap-reference-crops/` — reference-only graph crops from existing AP PDFs, with source-page metadata and reuse warnings
- `data/` — public CSV snapshots and retrieval dates
- `python/` — chart-generation scripts, including the reproducible concept-diagram builder
- `diagrams/` — 28 original SVG/PDF/PNG concept diagrams with `diagram-manifest.csv`
- `wikimedia/` — optional compatibility area for source files that need a separate Wikimedia-specific grouping
- `exports/` — slide-ready and handout-ready versions

Add every downloaded image to `source/sources.csv` with its individual source page, direct file URL, author, license, intended session, retrieval date, byte count, and SHA-256. Keep PDF-derived reference crops in their separate folder and record their source PDF, page, crop box, purpose, and redistribution status in `source/ap-reference-crops/metadata.csv`.
