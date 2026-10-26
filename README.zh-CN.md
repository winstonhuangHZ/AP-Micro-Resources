# AP Microeconomics 资料库

[English README / 英文主文档](README.md)

这是一个用于 AP Microeconomics 学习、备课、练习和课程规划的资料库。仓库整理了历年公开 FRQ、可合法保存的练习资料、Unit 1–6 HW、开放教材、MIT OpenCourseWare 资料，以及可打印的 LaTeX 教案。

## 快速入口

- [总索引](INDEX.md)
- [历年 FRQ Archive](APMICRO-FRQ-Archive/)
- [MCQ 练习资料](APMICRO-MCQ-Practice/)
- [Unit 1–6 HW](APMICRO-Unit-HW/)
- [College Board 官方课程文件](APMICRO-Official-Docs/)
- [开放教材与大学课程资料](APMICRO-Open-Resources/)
- [教学资料总目录](APMICRO-Teaching/)
- [教案与课时设计](APMICRO-Teaching/Lesson-Plans/)
- [讲义](APMICRO-Teaching/Handouts/)
- [PPT / Slides](APMICRO-Teaching/Slides/)
- [36 课时配图设计](APMICRO-Teaching/Visual-Plan/)
- [研究来源、论坛和后续整理入口](AP-Microeconomics-Research-Sources.md)

## 资料内容

| 目录 | 内容 |
|---|---|
| `APMICRO-FRQ-Archive/` | 2003–2026 的公开 FRQ、评分标准、学生答案和 Reader materials；2020 年目前没有配套文件 |
| `APMICRO-MCQ-Practice/` | CED、独立练习和外部题库目录；受限官方 MCQ 只保留官方入口 |
| `APMICRO-Unit-HW/` | Unit 1–6 HW、自制练习和逐文件索引 |
| `APMICRO-Official-Docs/` | College Board 官方课程概览、课程海报和 CED 澄清文件 |
| `APMICRO-Open-Resources/` | OpenStax、CORE Econ EPUB/PDF、MIT OCW 讲义、习题和答案 |
| `APMICRO-Teaching/` | 教案、讲义、PPT 文件夹，以及每节课的配图设计和素材目录 |
| `APMICRO-Teaching/Lesson-Plans/` | 教案框架、官方 CED Learning Objectives、36 课时安排、资料映射、双语 LaTeX 源文件和 PDF |

## LaTeX 教案

LaTeX 版本默认按 18 周、每周 2 次课、每次 90 分钟设计，包含：

- 课程目标和教学原则；
- 标准课堂流程；
- Unit 1–6 的 36 课时安排；
- MCQ、FRQ、图像、计算和错题训练；
- 测验和模拟考试节点；
- 每个课时对应的官方 objective ID、Learning Objective 和 CED 页码；
- 分离的英文版和中文版 XeLaTeX 源文件及 PDF。

入口：

- [LaTeX README](APMICRO-Teaching/Lesson-Plans/latex/README.md)
- [英文 LaTeX 源文件](APMICRO-Teaching/Lesson-Plans/latex/en/main.tex)
- [英文打印版 PDF](APMICRO-Teaching/Lesson-Plans/latex/en/AP-Microeconomics-Lesson-Plan-en.pdf)
- [中文 LaTeX 源文件](APMICRO-Teaching/Lesson-Plans/latex/zh/main.tex)
- [中文打印版 PDF](APMICRO-Teaching/Lesson-Plans/latex/zh/AP-Microeconomics-Lesson-Plan-zh.pdf)
- [官方目标说明](APMICRO-Teaching/Lesson-Plans/OFFICIAL-LEARNING-OBJECTIVES.md)
- [LaTeX 备忘录](APMICRO-Teaching/Lesson-Plans/LATEX-MEMO.md)

配图设计入口：[36 课时配图计划](APMICRO-Teaching/Visual-Plan/visual-plan-36-sessions.md)。每节课按 2–5 项弹性设计：至少保留一张核心数据图和一张概念图，需要时再加入更多图表、流程图、历史图片或现实案例；后续再按来源、许可证和数据快照逐项制作。

可视化数据入口：[Visual-Plan/assets/data](APMICRO-Teaching/Visual-Plan/assets/data/)。当前批次包含 FRED 原始快照、派生指标表、课堂模型合成数据和 SHA-256 清单；Kaggle 暂不需要，未来只有在寻找特定行业或家庭微观数据时再考虑。

## 索引和更新

资料目录中的 `manifest.csv` 记录本地路径、来源、文件大小和 SHA-256。MCQ 目录另有 `resources.csv`，记录没有镜像进仓库的在线题库和官方入口。

在仓库根目录运行：

```bash
python3 scripts/update_indexes.py
```

## 资料使用边界

- 公开可访问不等于可以自由再分发。
- College Board 明确限制电子再分发的资料只保留官方链接和说明。
- 付费题库不绕过付款、登录或访问控制。
- 来源和授权不清的扫描件只作为线索记录。
- 使用 OpenStax、CORE Econ 和 MIT OCW 资料时保留原始署名和许可证说明。

英文 README 是项目主文档；本文件作为中文辅助说明，项目结构和更新流程以英文 README 为准。
