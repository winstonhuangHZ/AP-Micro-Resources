# Visual Asset Completeness Audit

**Audit date:** 2026-10-27  
**Scope:** `visual-plan-36-sessions.md`, `assets/source/`, `assets/diagrams/`, and their manifests.

## Result

The external visual source collection is complete for the current 36-session visual plan.

- **42 source images** are stored in `assets/source/`.
- All 42 images have rows in [`source/sources.csv`](source/sources.csv).
- Every source row has a local file, Commons file page, download URL, author, license or terms, byte count, and SHA-256 hash.
- All 42 local files passed the SHA-256 check against the index.
- **32 photo or photo-group entries** in the lesson visual plan are marked `completed`.
- **28 original concept diagrams** are available as PNG, SVG, and PDF, with [`diagrams/diagram-manifest.csv`](diagrams/diagram-manifest.csv).
- The source folder contains no unindexed JPG files.

## Remaining planned entries

The only remaining `planned` entries in the visual plan are review and lesson-production aids:

- Session 15: profit-rectangle sequence
- Session 34: graph-label checklist card
- Session 35: MCQ error-analysis card
- Session 36: final-week exam-readiness plan

These are locally designed classroom aids rather than missing Wikimedia Commons source images. They can be produced during handout and slide layout work without extending the external image collection.

## Verification commands

```bash
python - <<'PY'
import csv, hashlib
from pathlib import Path

with open("APMICRO-Teaching/Visual-Plan/assets/source/sources.csv", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

for row in rows:
    path = Path(row["local_path"])
    assert path.exists(), path
    assert hashlib.sha256(path.read_bytes()).hexdigest() == row["sha256"], path

print(f"verified {len(rows)} source images")
PY
```
