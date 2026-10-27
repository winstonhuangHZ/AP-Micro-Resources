#!/usr/bin/env python3
"""Render and crop selected AP Micro graph pages for internal visual reference.

These are reference-only crops from existing PDFs. The metadata intentionally
preserves the original file, page, purpose, and redistribution warning.
"""
from __future__ import annotations

import csv
from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "APMICRO-Teaching" / "Visual-Plan" / "assets" / "source" / "ap-reference-crops"

# Coordinates are PDF points in a letter-size page (612 x 792), origin at the
# top left. They cover the graph itself plus enough labels to study AP layout.
CROPS = [
    ("government-intervention-ticket-market", "APMICRO-Unit-HW/Unit-2/Question Banks / Prompts/TB_28governmentinterventionFRQ.pdf", 1, (70, 105, 370, 285), "Unit 2 price ceiling and quantity labels"),
    ("government-intervention-widget-market", "APMICRO-Unit-HW/Unit-2/Question Banks / Prompts/TB_28governmentinterventionFRQ.pdf", 6, (55, 125, 560, 340), "Unit 2 equilibrium, price control, and axis mapping"),
    ("short-run-cost-curves", "APMICRO-Unit-HW/Unit-3/Question Banks / Prompts/TB_32shortruncosts.pdf", 14, (75, 155, 390, 375), "Unit 3 MC, ATC, and AVC intersection layout"),
    ("monopoly-cost-revenue-curves", "APMICRO-Unit-HW/Unit-4/Question Banks / Prompts/TB_42monopoly.pdf", 1, (65, 80, 485, 300), "Unit 4 monopoly D, MR, MC, ATC graph"),
    ("monopoly-profit-graph", "APMICRO-Unit-HW/Unit-4/Question Banks / Prompts/TB_42monopoly.pdf", 13, (55, 90, 560, 340), "Unit 4 monopoly price, output, and profit labels"),
    ("monopoly-mcq-graph", "APMICRO-Unit-HW/Unit-4/Question Banks / Prompts/TB_42monopoly.pdf", 26, (70, 95, 535, 365), "Unit 4 MCQ graph with projections"),
    ("negative-externality-graph", "APMICRO-Unit-HW/Unit-6/Question Banks / Prompts/TB_62externalities.pdf", 3, (65, 95, 490, 330), "Unit 6 MSC, MPC, MSB, and Q projections"),
    ("externality-policy-graph", "APMICRO-Unit-HW/Unit-6/Question Banks / Prompts/TB_62externalities.pdf", 10, (70, 285, 525, 565), "Unit 6 corrective policy and marginal external cost"),
    ("official-perfect-competition-panel", "APMICRO-MCQ-Practice/college-board-ap-microeconomics-course-and-exam-description.pdf", 176, (70, 55, 555, 285), "Official CED reference panel for perfect competition"),
    ("official-externality-panels", "APMICRO-MCQ-Practice/college-board-ap-microeconomics-course-and-exam-description.pdf", 179, (70, 55, 555, 315), "Official CED reference panels for externalities"),
]


def crop_page(pdf_path: Path, page_number: int, box: tuple[float, float, float, float], output: Path) -> None:
    doc = fitz.open(pdf_path)
    page = doc.load_page(page_number - 1)
    pix = page.get_pixmap(matrix=fitz.Matrix(4, 4), alpha=False)
    x0, y0, x1, y1 = [int(v * 4) for v in box]
    image = pix.pil_image() if hasattr(pix, "pil_image") else None
    if image is None:
        from PIL import Image
        image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    image.crop((x0, y0, x1, y1)).save(output, quality=95)
    doc.close()


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    for slug, rel, page, box, purpose in CROPS:
        source = ROOT / rel
        output = OUT / f"{slug}.png"
        crop_page(source, page, box, output)
        rows.append({
            "name": output.name,
            "source_pdf": rel,
            "page": page,
            "crop_box_points": ",".join(str(v) for v in box),
            "purpose": purpose,
            "status": "reference-only",
            "redistribution": "Do not redistribute as an original asset; consult the source PDF terms.",
        })
    with (OUT / "metadata.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0])
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} reference crops to {OUT}")


if __name__ == "__main__":
    main()
