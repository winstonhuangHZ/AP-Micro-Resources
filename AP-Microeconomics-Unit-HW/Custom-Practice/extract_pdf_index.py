from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parent
OUT_DIR = ROOT / "_analysis"
TEXT_DIR = OUT_DIR / "texts"


UNIT_PATTERNS = [
    (1, re.compile(r"(11Scarcity|12economicsystem|13PPC|14comparativeadvantage|15costandbenefit|16consumerchoice|UNIT1)", re.I)),
    (2, re.compile(r"(21demand|22supply|23PED|2425otherelasticities|26csandps|27equilibrium|28governmentintervention|29internationaltrade|utilityFRQ|Unit2)", re.I)),
    (3, re.compile(r"(31productionfunction|32shortruncosts|33longruncosts|34profit|35profitmax|36firmentryandexit|37perfectcompetition|Unit3)", re.I)),
    (4, re.compile(r"(41imperfectcompetition|42monopoly|43pricediscrimination|44monopolisticcompetition|45oligopoly|Unit4)", re.I)),
    (5, re.compile(r"(51introtofactormarket|52changeinfactordemandandsupply|53perfectcompetitivefactormarket|54monopsony)", re.I)),
    (6, re.compile(r"(62externalities|63publicgood|6164governmentpolicies|65inequality)", re.I)),
]


def detect_unit(name: str) -> int | None:
    for unit, pattern in UNIT_PATTERNS:
        if pattern.search(name):
            return unit
    return None


def clean_text(text: str) -> str:
    text = text.replace("\x00", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def main() -> None:
    OUT_DIR.mkdir(exist_ok=True)
    TEXT_DIR.mkdir(exist_ok=True)

    records = []
    by_unit = defaultdict(list)

    for pdf_path in sorted(ROOT.glob("*.pdf")):
        reader = PdfReader(str(pdf_path))
        texts = []
        for page in reader.pages:
            try:
                texts.append(page.extract_text() or "")
            except Exception as exc:  # pragma: no cover
                texts.append(f"[EXTRACTION_ERROR: {exc}]")

        full_text = clean_text("\n\n".join(texts))
        unit = detect_unit(pdf_path.name)
        out_text_path = TEXT_DIR / f"{pdf_path.stem}.txt"
        out_text_path.write_text(full_text, encoding="utf-8")

        record = {
            "file": pdf_path.name,
            "stem": pdf_path.stem,
            "unit": unit,
            "pages": len(reader.pages),
            "chars": len(full_text),
            "sample": full_text[:1000],
            "text_file": str(out_text_path.relative_to(ROOT)),
        }
        records.append(record)
        by_unit[str(unit)].append(record)

    (OUT_DIR / "pdf_index.json").write_text(
        json.dumps(records, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (OUT_DIR / "pdf_index_by_unit.json").write_text(
        json.dumps(by_unit, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    lines = []
    for unit in range(1, 7):
        items = by_unit.get(str(unit), [])
        lines.append(f"Unit {unit}: {len(items)} files")
        for item in items:
            lines.append(
                f"- {item['file']} | {item['pages']} pages | {item['chars']} chars | {item['text_file']}"
            )
        lines.append("")
    unassigned = [r for r in records if r["unit"] is None]
    if unassigned:
        lines.append("Unassigned:")
        for item in unassigned:
            lines.append(f"- {item['file']}")
    (OUT_DIR / "pdf_index_summary.txt").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
