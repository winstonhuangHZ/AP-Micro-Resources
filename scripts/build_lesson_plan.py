#!/usr/bin/env python3
from __future__ import annotations
import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / 'APMICRO-Teaching/Lesson-Plans'
LATEX = LESSON / 'latex'
OBJ_CSV = LESSON / 'official-learning-objectives.csv'
SESSION_CSV = LESSON / 'session-learning-objectives.csv'

PLANS = [
('Unit 1','Scarcity and resource allocation','Use a PPF to explain one choice','Unit 1 HW: basic concepts'),
('Unit 1','Production possibilities curve','Complete a PPF and opportunity-cost explanation','Trade-off calculation practice'),
('Unit 1','Comparative advantage and trade','Complete a specialization and exchange table','Comparative-advantage calculations'),
('Unit 1','Cost-benefit and marginal consumer choice','Use MB and MC to justify a decision','MCQ rationale log'),
('Unit 2','Demand and supply','Draw the initial market equilibrium','Unit 2 HW: equilibrium'),
('Unit 2','Price elasticity of demand and supply','Calculate elasticity and classify the result','Elasticity practice'),
('Unit 2','Other elasticities and total revenue','Use elasticity to predict total-revenue changes','MCQ plus calculation'),
('Unit 2','Market equilibrium and surplus','Calculate consumer, producer, and total surplus','Surplus practice'),
('Unit 2','Market disequilibrium and equilibrium changes','Classify shortage, surplus, and the new equilibrium','Shift-and-equilibrium diagrams'),
('Unit 2','Government intervention','Graph a price control, tax, or subsidy','FRQ subpart'),
('Unit 2','International trade and public policy','Complete a timed mixed Unit 2 FRQ','Error review'),
('Unit 3','The production function','Complete a production table and identify MP','Unit 3 HW: production'),
('Unit 3','Short-run production costs','Calculate and graph the cost curves','Cost-table calculations'),
('Unit 3','Long-run costs and types of profit','Interpret long-run costs and profit types','Profit comparison practice'),
('Unit 3','Profit maximization','Use P = MR and MC to choose output','Profit-maximization questions'),
('Unit 3','Produce, shut down, enter, or exit','Apply shutdown and entry/exit conditions','Decision classification'),
('Unit 3','Perfect competition and review','Complete a cost/profit synthesis graph','Unit 3 quiz and error review'),
('Unit 4','Introduction to imperfect competition','Identify barriers to entry and market power','Unit 4 HW: market structures'),
('Unit 4','Monopoly','Graph monopoly output, price, and profit','Monopoly graph practice'),
('Unit 4','Price discrimination','Explain how price discrimination changes surplus','Case analysis and MCQ'),
('Unit 4','Monopolistic competition','Compare short-run and long-run outcomes','FRQ subpart'),
('Unit 4','Oligopoly and game theory','Complete a payoff table and equilibrium explanation','Unit 4 quiz'),
('Unit 4','Market structure review','Compare imperfect market structures','Mixed market-structure review'),
('Unit 5','Introduction to factor markets','Derive MRP from the product market','Unit 5 HW'),
('Unit 5','Changes in factor demand and factor supply','Graph a factor-market shift','Wage and employment calculations'),
('Unit 5','Competitive factor markets','Use MRP and factor price to choose input use','Factor-market FRQ'),
('Unit 5','Monopsony and review','Compare monopsony and competitive outcomes','Unit 5 synthesis'),
('Unit 6','Socially efficient and inefficient market outcomes','Identify the efficient quantity and DWL','Unit 6 HW'),
('Unit 6','Externalities','Graph private and social costs or benefits','Policy comparison'),
('Unit 6','Public and private goods','Classify goods and explain free riding','Classification practice'),
('Unit 6','Government intervention in different market structures','Evaluate a policy in a market-structure case','MCQ practice'),
('Unit 6','Inequality','Explain an inequality measure and its causes','FRQ subpart'),
('Unit 6','Market failure FRQ synthesis','Complete a timed market-failure FRQ','Unit 6 quiz and error review'),
('Review','Core graphs','Draw and interpret six core AP Micro graphs','Graph error table'),
('Review','Timed MCQ and error analysis','Complete and classify a timed MCQ set','Targeted follow-up practice'),
('Review','Timed FRQ and exam readiness','Complete a full or half FRQ set','Exam-readiness plan'),
]


def esc_md(s): return str(s).replace('|','\\|').replace('\n',' ')
def esc_tex(s):
    s = str(s)
    repl = {'\\':r'\\textbackslash{}','&':r'\\&','%':r'\\%','$':r'\\$','#':r'\\#','_':r'\\_','{':r'\\{','}':r'\\}','~':r'\\textasciitilde{}','^':r'\\textasciicircum{}'}
    return ''.join(repl.get(c,c) for c in s)

def load_rows():
    with SESSION_CSV.open(newline='', encoding='utf-8') as f: rows = list(csv.DictReader(f))
    if len(rows) != 36: raise SystemExit(f'Expected 36 sessions, got {len(rows)}')
    for i,(r,p) in enumerate(zip(rows,PLANS),1):
        r.update(session=str(i), unit_label=p[0], plan_topic=p[1], output=p[2], homework=p[3])
    return rows

def build_objective_doc():
    grouped = defaultdict(list)
    with OBJ_CSV.open(newline='', encoding='utf-8') as f:
        for r in csv.DictReader(f): grouped[r['unit']].append(r)
    out = ['# Official Learning Objectives and CED Mapping','',
      'This document records the AP Microeconomics learning-objective map used by the lesson-plan package.','',
      '## Source and method','',
      '- Source: [College Board AP Microeconomics Course and Exam Description](../../APMICRO-MCQ-Practice/college-board-ap-microeconomics-course-and-exam-description.pdf).',
      '- The local CED is marked **Effective Fall 2026**; page references below are PDF page numbers.',
      '- Objective IDs are retained from the CED. The English and Chinese sentences here are concise teaching paraphrases aligned to those IDs, not a replacement for the official wording.',
      '- Session assignments are maintained in [`session-learning-objectives.csv`](session-learning-objectives.csv).','', '## Unit map','']
    for unit in map(str,range(1,7)):
        out += [f'### Unit {unit}','','| CED topic | Objective ID | English teaching paraphrase | 中文教学改写 | CED PDF pages |','|---|---|---|---|---|']
        for r in grouped[unit]: out.append(f"| {esc_md(r['topic'])} {esc_md(r['topic_name'])} | {esc_md(r['official_objective_ids'])} | {esc_md(r['learning_objective_en'])} | {esc_md(r['learning_objective_zh'])} | {esc_md(r['ced_pdf_pages'])} |")
        out.append('')
    out += ['## Use in the lesson plan','','Each of the 36 sessions carries objective IDs, English and Chinese teaching objectives, and a CED page reference. The last three sessions synthesize the course skills and graphing references across Units 1–6.','']
    (LESSON/'OFFICIAL-LEARNING-OBJECTIVES.md').write_text('\n'.join(out),encoding='utf-8')

def build_schedule(rows):
    out = ['# AP Microeconomics 36-Session Schedule','', 'Default format: 18 weeks, two 90-minute meetings per week. Every session has a student-visible product and an objective mapped to the College Board CED.','',
      '## Session map','', '| Session | Unit / topic | Official objective ID | English Learning Objective | 中文 Learning Objective | CED pages | Student product | Homework |','|---:|---|---|---|---|---|---|---|']
    for r in rows:
        out.append(f"| {r['session']} | {esc_md(r['unit_label'])} / {esc_md(r['plan_topic'])} | {esc_md(r['official_objective_ids'])} | {esc_md(r['learning_objective_en'])} | {esc_md(r['learning_objective_zh'])} | {esc_md(r['ced_pdf_pages'])} | {esc_md(r['output'])} | {esc_md(r['homework'])} |")
    out += ['', '## Fixed Unit cycle','', '1. Preview terms and one core graph.','2. Teach the model and its assumptions.','3. Practice numerical, graphing, and written-response forms.','4. Use a mixed quiz or a timed FRQ subpart.','5. Compare work with scoring guidance and record the error type.','6. Reattempt a similar item one week later.','', '## Source files','', '- [`official-learning-objectives.csv`](official-learning-objectives.csv)', '- [`session-learning-objectives.csv`](session-learning-objectives.csv)', '- [`OFFICIAL-LEARNING-OBJECTIVES.md`](OFFICIAL-LEARNING-OBJECTIVES.md)','']
    (LESSON/'course-schedule-36-sessions.md').write_text('\n'.join(out),encoding='utf-8')

def tex_header(lang):
    if lang == 'en':
        doc = r'\documentclass[11pt,a4paper]{article}'; title='AP Microeconomics Lesson Plan'; subtitle='36-session course framework and session design'; note='English edition'
    else:
        doc = r'\documentclass[11pt,a4paper]{ctexart}'; title='AP Microeconomics 教案框架'; subtitle='36 课时课程框架与课时设计'; note='中文版（保留 AP 专业术语与英文缩写）'
    return f'''{doc}
\\usepackage[a4paper,margin=2.0cm]{{geometry}}
\\usepackage{{longtable,booktabs,tabularx,array}}
\\usepackage{{enumitem,xcolor,hyperref,fancyhdr,lastpage,titlesec,parskip}}
\\definecolor{{apblue}}{{HTML}}{{17365D}}
\\definecolor{{aplight}}{{HTML}}{{EAF2F8}}
\\hypersetup{{colorlinks=true,linkcolor=apblue,urlcolor=apblue,pdftitle={{{title}}},pdfauthor={{AP-Micro-Resources}}}}
\\pagestyle{{fancy}}\\setlength{{\\headheight}}{{14pt}}\\fancyhf{{}}
\\lhead{{{title}}}\\rhead{{APMICRO-Teaching/Lesson-Plans}}\\cfoot{{\\thepage/\\pageref{{LastPage}}}}
\\titleformat{{\\section}}{{\\Large\\bfseries\\color{{apblue}}}}{{\\thesection}}{{0.7em}}{{}}
\\titleformat{{\\subsection}}{{\\large\\bfseries\\color{{apblue}}}}{{\\thesubsection}}{{0.7em}}{{}}
\\newcolumntype{{Y}}{{>{{\\raggedright\\arraybackslash}}X}}
\\newcommand{{\\objectivebox}}[1]{{\\noindent\\colorbox{{aplight}}{{\\parbox{{0.96\\textwidth}}{{#1}}}}}}
\\newcommand{{\\codepath}}[1]{{\\texttt{{\\small #1}}}}
\\begin{{document}}
\\begin{{titlepage}}\\centering\\vspace*{{2cm}}
{{\\Huge\\bfseries {title}\\par}}\\vspace{{0.5cm}}{{\\LARGE {subtitle}\\par}}
\\vspace{{1cm}}{{\\large 18 weeks \\textperiodcentered 2 meetings per week \\textperiodcentered 90 minutes per meeting\\par}}
\\vspace{{0.5cm}}{{\\large {note}\\par}}\\vfill
\\begin{{tabular}}{{ll}}Scope: & Units 1--6\\\\Core outputs: & concepts, graphs, calculations, explanations, FRQ writing\\\\Official map: & CED objective IDs and PDF page references\\\\Repository: & \\codepath{{APMICRO-Teaching/Lesson-Plans/}}\\\\\\end{{tabular}}
\\vfill{{\\large \\today\\par}}\\end{{titlepage}}
\\tableofcontents\\newpage
'''

def build_tex(rows,lang):
    en = lang=='en'; L = tex_header(lang)
    (LATEX/lang).mkdir(parents=True, exist_ok=True)
    if en:
        L += r'''\section{Course design}
This course treats AP Microeconomics as model-based reasoning. Students connect definitions to graphs, calculations, and causal explanations, then transfer those skills to MCQ and FRQ formats.

The default plan is 18 weeks with two 90-minute meetings per week. Every session has a visible student product and an objective mapped to the College Board CED.

\section{Course outcomes}
By the end of the course, students should be able to:
\begin{itemize}[leftmargin=2em]
\item explain scarcity, opportunity cost, comparative advantage, and the production possibilities curve;
\item use demand, supply, elasticity, surplus, trade, taxes, subsidies, and price controls to explain market outcomes;
\item calculate production, costs, revenue, profit, and profit-maximizing output;
\item compare perfect competition, monopoly, monopolistic competition, and oligopoly;
\item analyze factor markets using marginal revenue product, factor price, and monopsony models;
\item evaluate externalities, public goods, common resources, inequality, efficiency, and government policy;
\item produce AP-style graphs, calculations, and written explanations with correct labels, units, and causal logic.
\end{itemize}
\section{Standard 90-minute lesson}
\begin{tabularx}{\textwidth}{p{1.5cm}YY}\toprule Time & Phase & Student product \\ \midrule
0--8 & Retrieval warm-up & 3--5 retrieval questions or an unlabeled core graph \\
8--20 & Context and objective & A prediction and a question to answer \\
20--42 & Mini-lesson and model & Structured notes, formula, or teacher model \\
42--62 & Guided practice & Graph, calculation, or causal explanation \\
62--78 & AP-style transfer & 4--8 MCQs or one FRQ subpart \\
78--86 & Review and error code & Concept, graph, calculation, reading, or expression error \\
86--90 & Exit ticket & One conclusion and one unresolved question \\ \bottomrule\end{tabularx}
\section{Graphing and response routines}
For every graph, students identify both axes and units, name the curve that moves, mark old and new outcomes, and state the change in price, quantity, revenue, cost, surplus, or efficiency. For every calculation, they write the relationship, substitute values with units, and state the economic meaning. For every FRQ explanation, they use a because--therefore--result chain.
'''
    else:
        L += r'''\section{课程设计}
本课程把 AP Microeconomics 组织为一门以模型推理为核心的课程。学生需要把定义连接到图像、计算和因果解释，再把这些能力迁移到 MCQ 与 FRQ 题型中。

默认方案为 18 周、每周 2 次课、每次 90 分钟。每个课时都有可检查的学生产出，并且对应 College Board CED 中的目标 ID。

\section{课程学习成果}
完成课程后，学生应能够：
\begin{itemize}[leftmargin=2em]
\item 解释稀缺性、机会成本、比较优势和 PPC；
\item 使用需求、供给、弹性、剩余、贸易、税收、补贴和价格管制解释市场结果；
\item 计算生产、成本、收益、利润和利润最大化产量；
\item 比较完全竞争、垄断、垄断竞争和寡头；
\item 使用 MRP、要素价格和买方垄断模型分析要素市场；
\item 评价外部性、公共物品、共有资源、不平等、效率和政府政策；
\item 绘制 AP 风格图像，完成计算，并用准确标注、单位和因果逻辑写出解释。
\end{itemize}
\section{标准 90 分钟课堂流程}
\begin{tabularx}{\textwidth}{p{1.5cm}YY}\toprule 时间 & 环节 & 学生产出 \\ \midrule
0--8 & Retrieval warm-up & 3--5 道回忆题或一张无标注核心图 \\
8--20 & 情境与目标 & 写出预测和本节要回答的问题 \\
20--42 & 小讲授与示范 & 结构化笔记、公式或教师示范模型 \\
42--62 & 引导练习 & 图像、计算或因果解释 \\
62--78 & AP 风格迁移 & 4--8 道 MCQ 或一个 FRQ 小问 \\
78--86 & 讲评与错因编码 & 概念、图像、计算、读题或表达错误 \\
86--90 & Exit ticket & 一句结论和一个仍未解决的问题 \\ \bottomrule\end{tabularx}
\section{图像与作答常规}
每次画图都要写出坐标轴和单位，指出移动的曲线，标出新旧结果，并说明价格、数量、收益、成本、剩余或效率的变化。每道计算题写出关系式、带单位的代入过程和经济含义。每个 FRQ 解释都使用“因为—所以—结果”的因果链。
'''
    L += '\\section{'+('Session-by-session design' if en else '逐课时设计')+'}\n'
    for r in rows:
        heading = f"Session {r['session']}: {r['unit_label']} -- {r['plan_topic']}" if en else f"课时 {r['session']}：{r['unit_label']} -- {r['plan_topic']}"
        obj = r['learning_objective_en'] if en else r['learning_objective_zh']
        label = 'Official Learning Objective' if en else '官方 Learning Objective'
        page = 'CED PDF pages' if en else 'CED PDF 页码'; outlab='Student product' if en else '学生产出'; hwlab='Homework' if en else '课后任务'
        L += f"\\subsection{{{esc_tex(heading)}}}\n\\objectivebox{{\\textbf{{{label}:}} {esc_tex(obj)}\\\\\\textbf{{Objective ID:}} {esc_tex(r['official_objective_ids'])}\\\\\\textbf{{{page}:}} {esc_tex(r['ced_pdf_pages'])}}}\\par\\vspace{{0.4em}}\n"
        L += '\\begin{tabularx}{\\textwidth}{p{3.0cm}Y}\n\\toprule\n'
        L += f"{('Focus' if en else '课堂重点')} & {esc_tex(r['plan_topic'])}\\\\\n{outlab} & {esc_tex(r['output'])}\\\\\n{hwlab} & {esc_tex(r['homework'])}\\\\\n\\bottomrule\n\\end{{tabularx}}\n"
        if int(r['session']) in (6,12,18,24,30): L += '\\newpage\n'
    L += r'''\section{Materials and assessment loop}
Use the official CED and course documents to set the content boundary, the local FRQ archive for scored writing practice, the local Unit HW collection for repetition, and the open resources for supplementary explanations and problem sets. Restricted College Board MCQ stays in AP Classroom or Bluebook and is accessed through the official route.

The recurring assessment loop is retrieval, graph or calculation practice, one AP-style transfer item, error coding, and a delayed reattempt. The error log distinguishes concept, graph, calculation, reading, and expression errors.

\section{Source and synchronization note}
The objective IDs and CED pages come from \codepath{official-learning-objectives.csv} and \codepath{session-learning-objectives.csv}. The Markdown schedule is generated from the same session table. The source CED is stored at \codepath{APMICRO-MCQ-Practice/college-board-ap-microeconomics-course-and-exam-description.pdf}.

\end{document}
'''
    (LATEX/lang/'main.tex').write_text(L,encoding='utf-8')

def main():
    rows=load_rows(); build_objective_doc(); build_schedule(rows); build_tex(rows,'en'); build_tex(rows,'zh'); print('Generated lesson-plan artifacts.')
if __name__=='__main__': main()
