# AP Microeconomics Resources

[中文说明 / Chinese README](README.zh-CN.md)

A structured repository for AP Microeconomics study, teaching, practice, and course planning. It brings together public FRQ materials, legally accessible practice resources, Unit 1–6 homework, open economics textbooks, MIT OpenCourseWare materials, and a printable LaTeX lesson plan.

## Quick start

- Start with the [master index](INDEX.md).
- Use the [FRQ archive](AP-Microeconomics-FRQ-Archive/) for historical questions, scoring guidelines, sample responses, and reader materials.
- Use [MCQ practice](AP-Microeconomics-MCQ-Practice/) for locally saved practice files and the external-resource catalog.
- Use the [Unit 1–6 HW collection](AP-Microeconomics-Unit-HW/) for organized homework.
- Use [official course documents](AP-Microeconomics-Official-Docs/) for College Board course materials.
- Use [open textbooks and university materials](AP-Microeconomics-Open-Resources/) for additional explanations, problem sets, and solutions.
- Use the [lesson plan package](AP-Microeconomics-Lesson-Plan/) for the 36-session course design and printable PDF.

## Repository contents

| Area | Contents | Entry point |
|---|---|---|
| FRQ archive | 251 PDFs covering public AP Microeconomics FRQ materials from 2003–2026, with a 2020 coverage gap | [FRQ archive](AP-Microeconomics-FRQ-Archive/) |
| MCQ practice | College Board CED, independent practice, external catalog, and mirror notes | [MCQ practice](AP-Microeconomics-MCQ-Practice/) |
| Unit homework | Organized Unit 1–6 homework, custom practice, and per-file manifest | [Unit HW](AP-Microeconomics-Unit-HW/) |
| Official documents | College Board course overview, course-at-a-glance files, and CED clarifications | [Official docs](AP-Microeconomics-Official-Docs/) |
| Open resources | OpenStax, CORE Econ EPUB/PDF, and MIT OCW 14.01 lecture and problem-set materials | [Open resources](AP-Microeconomics-Open-Resources/) |
| Lesson planning | Framework, 36-session schedule, lesson template, materials map, LaTeX source and PDF | [Lesson plan](AP-Microeconomics-Lesson-Plan/) |
| Research sources | Official links, open resources, forums, and follow-up research leads | [Research sources](AP-Microeconomics-Research-Sources.md) |

## Lesson plan and LaTeX edition

The lesson-plan package uses an 18-week model with two 90-minute classes per week. It includes:

- course goals and teaching principles;
- a repeatable 90-minute lesson structure;
- a 36-session Unit 1–6 schedule;
- MCQ, FRQ, graphing, calculation, and error-analysis routines;
- assessment checkpoints and review sessions;
- an XeLaTeX source file and an 8-page printable PDF.

The LaTeX project has its own [README](AP-Microeconomics-Lesson-Plan/latex/README.md) and [compile memo](AP-Microeconomics-Lesson-Plan/LATEX-MEMO.md).

## Index and verification

Each material area maintains a manifest with local path, source URL, file size, and SHA-256 where applicable. The MCQ area also has `resources.csv` for online resources that are indexed but not mirrored.

Regenerate the indexes from the repository root:

```bash
python3 scripts/update_indexes.py
```

The LaTeX lesson plan is compiled with XeLaTeX. See [the LaTeX README](AP-Microeconomics-Lesson-Plan/latex/README.md) for the exact command.

## Resource and licensing policy

This repository prioritizes official and clearly licensed material.

- Publicly available does not automatically mean freely redistributable.
- College Board materials with explicit electronic-redistribution restrictions are indexed by official link and access note rather than mirrored.
- Paid question banks are cataloged only as external resources; payment or access controls are not bypassed.
- Files with unclear provenance or unclear redistribution permission are kept as leads only.
- OpenStax, CORE Econ, and MIT OpenCourseWare materials retain their attribution and license notes in the open-resource README and manifest.
- Verify the current source terms before publishing a derivative collection or using materials commercially.

## Suggested workflow

1. Read the current College Board course documents.
2. Study one Unit using the Unit HW and an open textbook chapter.
3. Practice with graphs and calculations before doing a timed FRQ.
4. Compare FRQ work with the official scoring guidelines.
5. Record MCQ and FRQ errors by concept, graph, calculation, reading, or explanation.
6. Re-run the index script after adding or replacing files.

## Project language

English is the primary project README and navigation language. The Chinese version is maintained as a companion translation and links back here for the canonical project structure and update workflow.
