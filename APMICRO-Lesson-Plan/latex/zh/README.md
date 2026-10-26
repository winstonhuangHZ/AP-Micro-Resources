# 中文 LaTeX 教案

- [`main.tex`](main.tex)：中文版源文件。
- [`AP-Microeconomics-Lesson-Plan-zh.pdf`](AP-Microeconomics-Lesson-Plan-zh.pdf)：编译后的中文版 PDF。

在仓库根目录运行：

```bash
python3 /Users/huangwenqin/.codex/plugins/cache/openai-bundled/latex/0.2.8/scripts/compile_latex.py \
  "$PWD/APMICRO-Lesson-Plan/latex/zh/main.tex" \
  --compiler texlive --engine xelatex \
  --output-directory "$PWD/APMICRO-Lesson-Plan/latex/zh/build"
```

课时目标来自 [`../../session-learning-objectives.csv`](../../session-learning-objectives.csv)。正文使用中文，但保留 AP Microeconomics、Learning Objective、FRQ、MCQ、PPC、MRP 等标准术语。
