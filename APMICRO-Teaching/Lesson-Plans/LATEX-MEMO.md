# LaTeX Lesson Plan Memo

The lesson plan is maintained as two isolated editions:

- English: [`latex/en/main.tex`](latex/en/main.tex) and [`latex/en/AP-Microeconomics-Lesson-Plan-en.pdf`](latex/en/AP-Microeconomics-Lesson-Plan-en.pdf)
- 中文: [`latex/zh/main.tex`](latex/zh/main.tex) and [`latex/zh/AP-Microeconomics-Lesson-Plan-zh.pdf`](latex/zh/AP-Microeconomics-Lesson-Plan-zh.pdf)

Each of the 36 sessions includes an official College Board objective ID, an English or Chinese Learning Objective, and a CED PDF page reference. The mapping is documented in [`OFFICIAL-LEARNING-OBJECTIVES.md`](OFFICIAL-LEARNING-OBJECTIVES.md).

## Regeneration

From the repository root:

```bash
python3 scripts/build_lesson_plan.py
```

This regenerates the official objective overview, the Markdown schedule, and both TeX sources from the CSV files. Then compile each edition with XeLaTeX as described in [`latex/README.md`](latex/README.md), and run `python3 scripts/update_indexes.py` to refresh manifests and indexes.
