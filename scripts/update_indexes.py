from pathlib import Path
import csv, hashlib
from collections import Counter, defaultdict

root = Path(__file__).resolve().parents[1]


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


# MCQ local manifest and external-resource catalog.
mcq = root / 'APMICRO-MCQ-Practice'
mcq_files = [p for p in sorted(mcq.iterdir()) if p.is_file() and p.suffix.lower() == '.pdf']
with (mcq / 'manifest.csv').open('w', newline='') as f:
    fields = ['name', 'kind', 'local_path', 'source_url', 'bytes', 'sha256']
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    for path in mcq_files:
        official = path.name.startswith('college-board')
        writer.writerow({
            'name': path.name,
            'kind': 'College Board official sample/course material' if official else 'Independent practice exam',
            'local_path': str(path.relative_to(root)),
            'source_url': 'https://apcentral.collegeboard.org/media/pdf/ap-microeconomics-course-and-exam-description.pdf' if official else 'https://examtex.com/free-exams/ap-microeconomics-practice-exam.pdf',
            'bytes': path.stat().st_size,
            'sha256': sha(path),
        })

external = [
    {'name': '2012 Public Practice Exam', 'kind': 'Official full practice exam with MCQ and answer key', 'access': 'Direct public PDF link; do not mirror or electronically redistribute', 'url': 'https://apcentral.collegeboard.org/media/pdf/ap-microeconomics-practice-exam-2012.pdf', 'notes': 'The College Board PDF explicitly restricts posting on personal websites and electronic redistribution.'},
    {'name': 'AP Classroom / Bluebook practice', 'kind': 'Official authorized practice and test previews', 'access': 'Requires College Board class/account access', 'url': 'https://apstudents.collegeboard.org/courses/ap-microeconomics/assessment', 'notes': 'Use teacher-assigned AP Classroom question banks and Bluebook previews.'},
    {'name': 'Fiveable AP Micro', 'kind': 'Online practice and review questions', 'access': 'Online', 'url': 'https://fiveable.me/ap-micro', 'notes': 'Independent study resource; not an annual official MCQ archive.'},
    {'name': 'Varsity Tutors AP Microeconomics practice', 'kind': 'Online practice questions', 'access': 'Online', 'url': 'https://www.varsitytutors.com/practice/subjects/ap-microeconomics', 'notes': 'Independent practice bank.'},
    {'name': 'Albert AP Microeconomics', 'kind': 'Online practice question bank', 'access': 'Online; some content may require account/subscription', 'url': 'https://www.albert.io/ap-microeconomics', 'notes': 'Independent practice bank.'},
    {'name': 'Tikonote AP Economics resources', 'kind': 'Online practice and review resources', 'access': 'Online', 'url': 'https://www.tpock.com/pages/ap-economics-resources', 'notes': 'Resource index linking to AP Micro practice materials and official resources.'},
    {'name': 'ExamTeX AP Micro practice generator', 'kind': 'Generated online practice exams', 'access': 'Online', 'url': 'https://examtex.com/practice/ap-microeconomics', 'notes': 'Generates independent MCQ and FRQ-style practice.'},
    {'name': 'Perfection Learning AP Microeconomics teacher sampler', 'kind': 'Publisher sample with practice questions', 'access': 'Public link when available', 'url': 'https://new.perfectionlearning.com/common/series/ap-micro-tr-sampler.pdf', 'notes': 'Publisher sample; check redistribution terms before mirroring.'},
    {'name': 'Test Papers AP past papers', 'kind': 'Paid MCQ archive lead', 'access': 'Paid email delivery', 'url': 'https://a.testpapers.net/?post=10', 'notes': 'Page lists AP Micro years 2000, 2005, 2008, 2010, 2012–2019, 2021–2025; not downloaded.'},
    {'name': 'Public Padlet Unit 1 MC upload', 'kind': 'Publicly reachable unit practice upload', 'access': 'Direct PDF link; provenance unclear', 'url': 'https://padletuploads.blob.core.windows.net/prod/135439946/74d77306521c78f916a342b1513570a0/Unit_1_MC___Mort.pdf', 'notes': 'Recorded as a lead only; not mirrored because the file does not state a clear redistribution license.'},
]
with (mcq / 'resources.csv').open('w', newline='') as f:
    fields = ['name', 'kind', 'access', 'url', 'notes']
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(external)

(mcq / 'README.md').write_text('''# AP Microeconomics MCQ Practice

本目录只保存公开下载、适合放入仓库的 MCQ 练习文件；完整的官方年度 MCQ 原卷通常需要 AP Classroom/Bluebook 权限，或者 College Board 明确限制电子再分发。

## 已保存到仓库

| 文件 | 类型 | 说明 |
|---|---|---|
| [college-board-ap-microeconomics-course-and-exam-description.pdf](college-board-ap-microeconomics-course-and-exam-description.pdf) | College Board 官方 | 包含课程框架、考试说明、样题和相关答案材料。 |
| [examtex-ap-microeconomics-practice-exam.pdf](examtex-ap-microeconomics-practice-exam.pdf) | 独立练习 | 公开下载的整套练习卷，含 MCQ 和 FRQ-style 内容；网站的 worked answer key 通过其自己的流程提供，因此没有复制进仓库。 |

## 外部资源

完整的在线题库、官方授权入口、公开但不适合镜像的 PDF，以及付费题库线索见 [`resources.csv`](resources.csv) 和仓库根目录的 [`MCQ-Mirror-Notes.md`](../MCQ-Mirror-Notes.md)。

其中 College Board 2012 Public Practice Exam 的官方链接保留在外部资源表中。该 PDF 自身写明不得发布到个人网站或进行电子再分发，所以这里只做链接索引，不保存副本。

本地文件的来源、大小和 SHA-256 校验值见 [`manifest.csv`](manifest.csv)。
''')

# Detailed Unit HW index from its manifest.
hw = root / 'APMICRO-Unit-HW'
rows = list(csv.DictReader((hw / 'manifest.csv').open()))
by = defaultdict(list)
for row in rows:
    by[row['unit']].append(row)
lines = ['# AP Microeconomics Unit 1–6 HW Index', '', 'This index is generated from `manifest.csv`. The source folder on the Desktop is preserved separately; these are organized copies.', '']
for unit in [f'Unit {i}' for i in range(1, 7)] + ['Custom']:
    lines += [f'## {unit}', '', '| Kind | Organized file | Original source |', '|---|---|---|']
    for row in sorted(by.get(unit, []), key=lambda x: (x['kind'], x['destination'])):
        dest = Path(row['destination'].replace('APMICRO-Unit-HW/', ''))
        link = dest.as_posix().replace(' ', '%20')
        lines.append(f"| {row['kind']} | [{link}]({link}) | `{row['source']}` |")
    lines.append('')
(hw / 'INDEX.md').write_text('\n'.join(lines))

# FRQ year index.
frq = root / 'APMICRO-FRQ-Archive'
frq_rows = list(csv.DictReader((frq / 'manifest.csv').open()))
byyear = defaultdict(list)
for row in frq_rows:
    byyear[row['year']].append(row)
lines = ['# AP Microeconomics FRQ Archive Index', '', 'This index is generated from `manifest.csv`. Each year links to the local year directory and reports the available resource types.', '', '| Year | Files | Questions | Scoring / answers | Commentary / reports |', '|---|---:|---:|---:|---:|']
for year in sorted(byyear):
    year_rows = byyear[year]
    def count(*words):
        return sum(any(word in row['local_path'] for word in words) for row in year_rows)
    lines.append(f"| [{year}]({year}/) | {len(year_rows)} | {count('question-paper')} | {count('scoring-guidelines', 'sample-responses')} | {count('commentary', 'reader-report', 'statistics', 'distribution')} |")
lines += ['', 'See [README.md](README.md) for coverage notes and source policy.', '']
(frq / 'INDEX.md').write_text('\n'.join(lines))

# Official document and open resource manifests are maintained separately from
# the generated indexes so that source/licence notes are not overwritten.
official = root / 'APMICRO-Official-Docs'
official_files = sorted([p for p in official.iterdir() if p.is_file() and p.suffix.lower() == '.pdf']) if official.exists() else []
if official.exists():
    with (official / 'manifest.csv').open('w', newline='') as f:
        fields = ['name', 'kind', 'local_path', 'source_url', 'bytes', 'sha256', 'use_notes']
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        official_urls = {
            'official-ced-clarifications.pdf': 'https://apcentral.collegeboard.org/media/pdf/ap-microeconomics-course-and-exam-description-clarifications.pdf',
            'official-course-overview.pdf': 'https://apcentral.collegeboard.org/media/pdf/ap-microeconomics-course-overview.pdf',
            'official-course-at-a-glance.pdf': 'https://apcentral.collegeboard.org/media/pdf/ap-microeconomics-course-at-a-glance.pdf',
            'official-course-at-a-glance-printable-poster.pdf': 'https://apcentral.collegeboard.org/media/pdf/ap-microeconomics-course-at-a-glance-printable-poster.pdf',
        }
        for path in official_files:
            writer.writerow({'name': path.name, 'kind': 'College Board official course support', 'local_path': str(path.relative_to(root)), 'source_url': official_urls.get(path.name, ''), 'bytes': path.stat().st_size, 'sha256': sha(path), 'use_notes': 'Official source; follow College Board terms for redistribution.'})

open_root = root / 'APMICRO-Open-Resources'
open_files = sorted([p for p in open_root.rglob('*') if p.is_file() and p.suffix.lower() in {'.pdf', '.epub'}]) if open_root.exists() else []
if open_root.exists():
    with (open_root / 'manifest.csv').open('w', newline='') as f:
        fields = ['name', 'kind', 'local_path', 'source_url', 'bytes', 'sha256', 'license_or_terms']
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for path in open_files:
            rel = path.relative_to(root).as_posix()
            if 'OpenStax' in rel:
                source = 'https://openstax.org/details/books/principles-microeconomics-3e' if '3e' in path.name else 'https://openstax.org/details/books/principles-microeconomics-ap-courses-2e'
                kind = 'OpenStax open textbook'
                terms = 'Creative Commons Attribution 4.0 International (CC BY 4.0); verify front matter for edition-specific notices.'
            elif 'CORE-Econ' in rel:
                source = 'https://www.core-econ.org/project/core-the-economy/'
                kind = 'CORE Econ open textbook / local EPUB conversion'
                terms = 'CORE Econ open access resource; retain attribution and check current CORE Econ terms before redistribution.'
            else:
                source = 'https://ocw.mit.edu/courses/14-01-principles-of-microeconomics-fall-2023/'
                kind = 'MIT OpenCourseWare course material'
                terms = 'MIT OpenCourseWare materials are generally CC BY-NC-SA 4.0; retain notices and verify the page terms.'
            writer.writerow({'name': path.name, 'kind': kind, 'local_path': rel, 'source_url': source, 'bytes': path.stat().st_size, 'sha256': sha(path), 'license_or_terms': terms})

# Root index.
frq_pdf = list(frq.rglob('*.pdf'))
hw_pdf = list(hw.rglob('*.pdf'))
mcq_pdf = list(mcq.rglob('*.pdf'))
teaching = root / 'APMICRO-Teaching'
lesson_files = [p for p in (teaching / 'Lesson-Plans').rglob('*') if p.is_file() and 'latex/build' not in p.as_posix()] if (teaching / 'Lesson-Plans').exists() else []
handout_files = [p for p in (teaching / 'Handouts').rglob('*') if p.is_file()] if (teaching / 'Handouts').exists() else []
slide_files = [p for p in (teaching / 'Slides').rglob('*') if p.is_file()] if (teaching / 'Slides').exists() else []
visual_files = [p for p in (teaching / 'Visual-Plan').rglob('*') if p.is_file()] if (teaching / 'Visual-Plan').exists() else []
unit_counts = Counter(row['unit'] for row in rows)
frq_counts = Counter(row['year'] for row in frq_rows)
(root / 'INDEX.md').write_text(f'''# AP Microeconomics Resources

本仓库集中整理 AP Microeconomics 的 FRQ、MCQ 练习资料，以及 Unit 1–6 homework。

项目说明： [English README](README.md) · [中文说明](README.zh-CN.md)

## 快速入口

| 材料 | 入口 | 数量 |
|---|---|---:|
| 历年 FRQ、评分标准、学生答案和 Reader Report | [APMICRO-FRQ-Archive/](APMICRO-FRQ-Archive/) · [详细索引](APMICRO-FRQ-Archive/INDEX.md) | {len(frq_pdf)} PDFs |
| MCQ 练习资料 | [APMICRO-MCQ-Practice/](APMICRO-MCQ-Practice/) · [详细说明](APMICRO-MCQ-Practice/README.md) | {len(mcq_pdf)} PDFs |
| Unit 1–6 HW | [APMICRO-Unit-HW/](APMICRO-Unit-HW/) · [详细索引](APMICRO-Unit-HW/INDEX.md) | {len(hw_pdf)} PDFs |
| 官方课程文件 | [APMICRO-Official-Docs/](APMICRO-Official-Docs/) | {len(official_files)} PDFs |
| 开放教材与课程资料 | [APMICRO-Open-Resources/](APMICRO-Open-Resources/) | {len(open_files)} PDF/EPUB |
| 教学资料总目录 | [APMICRO-Teaching/](APMICRO-Teaching/) | {len(lesson_files) + len(handout_files) + len(slide_files) + len(visual_files)} files |
| 教案与课时设计 | [APMICRO-Teaching/Lesson-Plans/](APMICRO-Teaching/Lesson-Plans/) · [官方目标说明](APMICRO-Teaching/Lesson-Plans/OFFICIAL-LEARNING-OBJECTIVES.md) · [LaTeX README](APMICRO-Teaching/Lesson-Plans/latex/README.md) | {len(lesson_files)} files |
| 讲义 | [APMICRO-Teaching/Handouts/](APMICRO-Teaching/Handouts/) | {len(handout_files)} files |
| PPT / Slides | [APMICRO-Teaching/Slides/](APMICRO-Teaching/Slides/) | {len(slide_files)} files |
| 配图设计与素材目录 | [APMICRO-Teaching/Visual-Plan/](APMICRO-Teaching/Visual-Plan/) | {len(visual_files)} files |
| 研究来源与论坛入口 | [AP-Microeconomics-Research-Sources.md](AP-Microeconomics-Research-Sources.md) | — |
| MCQ 镜像和在线题库线索 | [MCQ-Mirror-Notes.md](MCQ-Mirror-Notes.md) | — |

## Unit HW 数量

| Unit | 文件数 |
|---|---:|
'''+''.join(f'| Unit {i} | {unit_counts.get(f"Unit {i}", 0)} |\n' for i in range(1, 7))+f'''| 自制练习 / Custom | {unit_counts.get('Custom', 0)} |

## FRQ 年份覆盖

已收录年份：{', '.join(sorted(frq_counts))}。2020 年在当前公开资料中没有配套文件；详细说明和每年文件数见 [FRQ 索引](APMICRO-FRQ-Archive/INDEX.md)。

## 索引和校验

每个资料区都有自己的 `manifest.csv`，记录本地路径、来源、文件大小和 SHA-256。MCQ 目录另有 `resources.csv`，记录已发现但没有镜像进仓库的官方入口、在线题库和付费线索。修改或补充资料后，从仓库根目录运行 `python3 scripts/update_indexes.py` 即可重建索引。
''')
print('wrote root and sub-indexes')
