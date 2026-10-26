# AP Microeconomics Lesson Plan

This package provides an 18-week, 36-session AP Microeconomics course design for two 90-minute meetings per week.

## Files

- [`framework.md`](framework.md): course framework, teaching routines, assessment loop, and differentiation.
- [`course-schedule-36-sessions.md`](course-schedule-36-sessions.md): generated session schedule with official objective IDs, English Learning Objectives, 中文 Learning Objectives, CED pages, products, and homework.
- [`OFFICIAL-LEARNING-OBJECTIVES.md`](OFFICIAL-LEARNING-OBJECTIVES.md): College Board CED mapping and teaching-paraphrase notes.
- [`official-learning-objectives.csv`](official-learning-objectives.csv): topic-level objective map.
- [`session-learning-objectives.csv`](session-learning-objectives.csv): 36 session-level objective map.
- [`unit-lesson-template.md`](unit-lesson-template.md): reusable lesson template.
- [`materials-map.csv`](materials-map.csv): Unit-to-resource map.
- [`LATEX-MEMO.md`](LATEX-MEMO.md): LaTeX maintenance memo.
- [`latex/`](latex/): isolated English and Chinese LaTeX editions.

## Regeneration

From the repository root:

```bash
python3 scripts/build_lesson_plan.py
python3 scripts/update_indexes.py
```

The English and Chinese LaTeX files are generated from the same session CSV, so objective IDs and CED pages stay aligned across Markdown and PDF outputs.

## Course model

The default design is 18 weeks, two meetings per week, and 90 minutes per meeting. Every session includes a student-visible product: a graph, calculation, explanation, MCQ error record, or FRQ subpart. The plan can be compressed to 18 meetings or expanded to 45 meetings by splitting graphing and FRQ practice.
