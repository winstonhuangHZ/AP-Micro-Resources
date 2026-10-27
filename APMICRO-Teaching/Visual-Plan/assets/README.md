# Visual Assets

Reserved layout for future asset production:

- `source/` — original downloaded source images and their metadata; keep these files unchanged
- `source/ap-reference-crops/` — reference-only graph crops from existing AP PDFs, with source-page metadata and reuse warnings
- `data/` — public CSV snapshots and retrieval dates
- `python/` — chart-generation scripts
- `diagrams/` — original SVG/PDF/PNG diagrams
- `wikimedia/` — optional compatibility area for source files that need a separate Wikimedia-specific grouping
- `exports/` — slide-ready and handout-ready versions

Add every downloaded image to `source/sources.csv` with its individual source page, direct file URL, author, license, intended session, retrieval date, byte count, and SHA-256. Keep PDF-derived reference crops in their separate folder and record their source PDF, page, crop box, purpose, and redistribution status in `source/ap-reference-crops/metadata.csv`.
