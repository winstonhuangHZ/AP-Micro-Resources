# AP Microeconomics LaTeX Lesson Plans

The LaTeX lesson plan is maintained as two isolated editions:

- [English edition](en/): [`main.tex`](en/main.tex) and [`AP-Microeconomics-Lesson-Plan-en.pdf`](en/AP-Microeconomics-Lesson-Plan-en.pdf).
- [中文版本](zh/): [`main.tex`](zh/main.tex) and [`AP-Microeconomics-Lesson-Plan-zh.pdf`](zh/AP-Microeconomics-Lesson-Plan-zh.pdf).

Both editions contain the same 36-session structure. Each session shows an official objective ID, an English or Chinese teaching objective, and the relevant College Board CED PDF page.

## Build

Run from the repository root:

```bash
python3 scripts/build_lesson_plan.py
python3 /Users/huangwenqin/.codex/plugins/cache/openai-bundled/latex/0.2.8/scripts/compile_latex.py \
  "$PWD/APMICRO-Teaching/Lesson-Plans/latex/en/main.tex" --compiler texlive --engine xelatex \
  --output-directory "$PWD/APMICRO-Teaching/Lesson-Plans/latex/en/build"
python3 /Users/huangwenqin/.codex/plugins/cache/openai-bundled/latex/0.2.8/scripts/compile_latex.py \
  "$PWD/APMICRO-Teaching/Lesson-Plans/latex/zh/main.tex" --compiler texlive --engine xelatex \
  --output-directory "$PWD/APMICRO-Teaching/Lesson-Plans/latex/zh/build"
```

Copy each `build/main.pdf` to its edition directory using the edition-specific PDF filename. Temporary build directories are ignored by Git.

## Source of truth

- [`official-learning-objectives.csv`](../official-learning-objectives.csv): topic-level official objective IDs and CED pages.
- [`session-learning-objectives.csv`](../session-learning-objectives.csv): 36 session-level objectives.
- [`OFFICIAL-LEARNING-OBJECTIVES.md`](../OFFICIAL-LEARNING-OBJECTIVES.md): source and paraphrase notes.
- [`course-schedule-36-sessions.md`](../course-schedule-36-sessions.md): generated Markdown schedule.
- [`../../../scripts/build_lesson_plan.py`](../../../scripts/build_lesson_plan.py): regenerates the Markdown schedule and both TeX sources.
