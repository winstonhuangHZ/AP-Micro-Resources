# LaTeX 教案备忘录

本目录新增了一份适合打印和归档的 LaTeX 教案文档：

- [`latex/main.tex`](latex/main.tex)：主源文件，使用 `ctexart`，通过 XeLaTeX 编译。
- [`latex/AP-Microeconomics-Lesson-Plan.pdf`](latex/AP-Microeconomics-Lesson-Plan.pdf)：已编译 PDF。
- [`framework.md`](framework.md)：Markdown 版课程框架。
- [`course-schedule-36-sessions.md`](course-schedule-36-sessions.md)：Markdown 版 36 课时表。
- [`materials-map.csv`](materials-map.csv)：Unit 与本地资料的映射。

## 编译

在 repo 根目录执行：

```bash
python3 /Users/huangwenqin/.codex/plugins/cache/openai-bundled/latex/0.2.8/scripts/compile_latex.py \
  "$PWD/AP-Microeconomics-Lesson-Plan/latex/main.tex" \
  --compiler texlive \
  --engine xelatex \
  --output-directory "$PWD/AP-Microeconomics-Lesson-Plan/latex/build"
```

编译成功后，将 `latex/build/main.pdf` 更新为 `latex/AP-Microeconomics-Lesson-Plan.pdf`。`latex/build/` 是临时编译目录，不纳入版本控制。

## 同步规则

修改 36 课时安排时，同时检查 LaTeX 表格、Markdown 课表和 `materials-map.csv`。新增资料后运行根目录的 `python3 scripts/update_indexes.py`，再重新编译 PDF。
