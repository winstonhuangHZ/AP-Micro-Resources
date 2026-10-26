# AP Microeconomics LaTeX 教案

这是 AP Microeconomics 教案框架的 LaTeX 版本，适合打印、归档和后续制作正式课程手册。

## 文件

- [`main.tex`](main.tex)：LaTeX 主源文件。
- [`AP-Microeconomics-Lesson-Plan.pdf`](AP-Microeconomics-Lesson-Plan.pdf)：已编译的打印版 PDF。
- `build/`：本地编译产生的临时文件，不纳入 Git。

## 内容

文档包含：

- 课程定位与学习目标；
- 90 分钟课堂流程；
- 18 周、36 课时安排；
- Unit 1–6 教学重点；
- MCQ、FRQ、图像和计算训练安排；
- 测验、错题和模拟考试节奏；
- 18 次课、36 次课、45 次课和自学版本的调整方式；
- 单节课备课模板；
- 仓库资料配合说明。

## 编译

在 repo 根目录执行：

```bash
python3 /Users/huangwenqin/.codex/plugins/cache/openai-bundled/latex/0.2.8/scripts/compile_latex.py \
  "$PWD/AP-Microeconomics-Lesson-Plan/latex/main.tex" \
  --compiler texlive \
  --engine xelatex \
  --output-directory "$PWD/AP-Microeconomics-Lesson-Plan/latex/build"
```

编译成功后，把 `build/main.pdf` 复制为本目录的 `AP-Microeconomics-Lesson-Plan.pdf`。

## 同步规则

- 课时结构和教学原则：同步检查 [`../framework.md`](../framework.md)。
- 36 课时表：同步检查 [`../course-schedule-36-sessions.md`](../course-schedule-36-sessions.md)。
- Unit 资料映射：同步检查 [`../materials-map.csv`](../materials-map.csv)。
- 修改资料后：在 repo 根目录运行 `python3 scripts/update_indexes.py`。
