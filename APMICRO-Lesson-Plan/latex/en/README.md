# English LaTeX Lesson Plan

- [`main.tex`](main.tex): English source.
- [`AP-Microeconomics-Lesson-Plan-en.pdf`](AP-Microeconomics-Lesson-Plan-en.pdf): compiled English PDF.

Compile from the repository root with:

```bash
python3 /Users/huangwenqin/.codex/plugins/cache/openai-bundled/latex/0.2.8/scripts/compile_latex.py \
  "$PWD/APMICRO-Lesson-Plan/latex/en/main.tex" \
  --compiler texlive --engine xelatex \
  --output-directory "$PWD/APMICRO-Lesson-Plan/latex/en/build"
```

The session objectives come from [`../../session-learning-objectives.csv`](../../session-learning-objectives.csv).
