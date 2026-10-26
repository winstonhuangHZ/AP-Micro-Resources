from pathlib import Path
import csv, hashlib
from collections import Counter, defaultdict

root=Path(__file__).resolve().parents[1]

def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()

# MCQ local manifest.
mcq=root/'AP-Microeconomics-MCQ-Practice'
mcq_files=[p for p in sorted(mcq.iterdir()) if p.is_file() and p.suffix.lower()=='.pdf']
with (mcq/'manifest.csv').open('w',newline='') as f:
 fields=['name','kind','local_path','source_url','bytes','sha256']
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
 for p in mcq_files:
  kind='Official course/exam description with sample MCQs' if p.name.startswith('college-board') else 'Independent practice exam'
  source='https://apcentral.collegeboard.org/media/pdf/ap-microeconomics-course-and-exam-description.pdf' if p.name.startswith('college-board') else 'https://examtex.com/free-exams/ap-microeconomics-practice-exam.pdf'
  w.writerow({'name':p.name,'kind':kind,'local_path':str(p.relative_to(root)),'source_url':source,'bytes':p.stat().st_size,'sha256':sha(p)})
(mcq/'README.md').write_text('''# AP Microeconomics MCQ Practice\n\nThis folder contains publicly downloadable MCQ practice material. The files are practice resources, not a complete archive of official annual College Board MCQ forms.\n\n| File | Type | Notes |\n|---|---|---|\n| [college-board-ap-microeconomics-course-and-exam-description.pdf](college-board-ap-microeconomics-course-and-exam-description.pdf) | College Board official | Includes the course framework, exam information, sample questions, and answer material. |\n| [examtex-ap-microeconomics-practice-exam.pdf](examtex-ap-microeconomics-practice-exam.pdf) | Independent practice | Publicly downloadable practice exam with MCQ and FRQ-style material. The matching worked answer key is delivered by the site through its own access flow and is not included here. |\n\nOnline practice banks and mirror leads are listed in [../MCQ-Mirror-Notes.md](../MCQ-Mirror-Notes.md).\n\nThe local file manifest with source URLs, byte sizes, and SHA-256 checksums is [manifest.csv](manifest.csv).\n''')

# Detailed Unit HW index from its manifest.
hw=root/'AP-Microeconomics-Unit-HW'
rows=list(csv.DictReader((hw/'manifest.csv').open()))
by=defaultdict(list)
for r in rows: by[r['unit']].append(r)
lines=['# AP Microeconomics Unit 1–6 HW Index','', 'This index is generated from `manifest.csv`. The source folder on the Desktop is preserved separately; these are organized copies.', '']
for unit in [f'Unit {i}' for i in range(1,7)]+['Custom']:
 lines += [f'## {unit}','', '| Kind | Organized file | Original source |','|---|---|---|']
 for r in sorted(by.get(unit,[]), key=lambda x:(x['kind'],x['destination'])):
  dest=Path(r['destination'].replace('AP-Microeconomics-Unit-HW/',''))
  lines.append(f"| {r['kind']} | [{dest.as_posix()}]({dest.as_posix().replace(' ','%20')}) | `{r['source']}` |")
 lines.append('')
(hw/'INDEX.md').write_text('\n'.join(lines))

# FRQ year index.
frq=root/'AP-Microeconomics-FRQ-Archive'
frq_rows=list(csv.DictReader((frq/'manifest.csv').open()))
byyear=defaultdict(list)
for r in frq_rows: byyear[r['year']].append(r)
lines=['# AP Microeconomics FRQ Archive Index','', 'This index is generated from `manifest.csv`. Each year links to the local year directory and reports the available resource types.', '', '| Year | Files | Questions | Scoring / answers | Commentary / reports |','|---|---:|---:|---:|---:|']
for year in sorted(byyear):
 rs=byyear[year]
 def n(*words): return sum(any(w in r['local_path'] for w in words) for r in rs)
 q=n('question-paper'); s=n('scoring-guidelines','sample-responses'); c=n('commentary','reader-report','statistics','distribution')
 lines.append(f"| [{year}]({year}/) | {len(rs)} | {q} | {s} | {c} |")
lines += ['', 'See [README.md](README.md) for coverage notes and source policy.', '']
(frq/'INDEX.md').write_text('\n'.join(lines))

# Root index.
frq_pdf=list(frq.rglob('*.pdf'))
hw_pdf=list(hw.rglob('*.pdf'))
mcq_pdf=list(mcq.rglob('*.pdf'))
unit_counts=Counter(r['unit'] for r in rows)
frq_counts=Counter(r['year'] for r in frq_rows)
root_index=f'''# AP Microeconomics Resources\n\n本仓库集中整理 AP Microeconomics 的 FRQ、MCQ 练习资料，以及 Unit 1–6 homework。\n\n## 快速入口\n\n| 材料 | 入口 | 数量 |\n|---|---|---:|\n| 历年 FRQ、评分标准、学生答案和 Reader Report | [AP-Microeconomics-FRQ-Archive/](AP-Microeconomics-FRQ-Archive/) · [详细索引](AP-Microeconomics-FRQ-Archive/INDEX.md) | {len(frq_pdf)} PDFs |\n| MCQ 练习资料 | [AP-Microeconomics-MCQ-Practice/](AP-Microeconomics-MCQ-Practice/) · [详细说明](AP-Microeconomics-MCQ-Practice/README.md) | {len(mcq_pdf)} PDFs |\n| Unit 1–6 HW | [AP-Microeconomics-Unit-HW/](AP-Microeconomics-Unit-HW/) · [详细索引](AP-Microeconomics-Unit-HW/INDEX.md) | {len(hw_pdf)} PDFs |\n| MCQ 镜像和在线题库线索 | [MCQ-Mirror-Notes.md](MCQ-Mirror-Notes.md) | — |\n\n## Unit HW 数量\n\n| Unit | 文件数 |\n|---|---:|\n'''+''.join(f'| Unit {i} | {unit_counts.get(f"Unit {i}",0)} |\n' for i in range(1,7))+f'''| 自制练习 / Custom | {unit_counts.get('Custom',0)} |\n\n## FRQ 年份覆盖\n\n已收录年份：{', '.join(sorted(frq_counts))}。2020 年在当前公开资料中没有配套文件；详细说明和每年文件数见 [FRQ 索引](AP-Microeconomics-FRQ-Archive/INDEX.md)。\n\n## 索引和校验\n\n每个资料区都有自己的 `manifest.csv`，记录本地路径、来源、文件大小和 SHA-256。修改或补充资料后，重新运行维护脚本即可重建索引。\n'''
(root/'INDEX.md').write_text(root_index)
print('wrote root and sub-indexes')
