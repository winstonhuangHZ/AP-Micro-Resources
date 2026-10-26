from __future__ import annotations

from pathlib import Path
from textwrap import dedent

from ap_micro_hard_exam_data import UNITS


ROOT = Path(__file__).resolve().parent
EXAM_TEX = ROOT / "ap_micro_hard_exam.tex"
SOLUTIONS_TEX = ROOT / "ap_micro_hard_solutions.tex"


def normalize(text: str) -> str:
    return dedent(text).strip() + "\n"


def validate() -> None:
    total = 0
    for unit in UNITS:
        unit_total = 0
        for block in unit["blocks"]:
            for question in block["questions"]:
                if len(question["choices"]) != 5:
                    raise ValueError(f"{unit['title']} has a question without 5 choices.")
                if question["answer"] not in {"A", "B", "C", "D", "E"}:
                    raise ValueError(f"{unit['title']} has an invalid answer key.")
                unit_total += 1
        if unit_total != 20:
            raise ValueError(f"{unit['title']} has {unit_total} questions instead of 20.")
        total += unit_total
    if total != 120:
        raise ValueError(f"Question bank has {total} questions instead of 120.")


def render_choices(choices: list[str]) -> str:
    lines = ["\\begin{choiceslist}"]
    for choice in choices:
        lines.append(f"\\item {choice}")
    lines.append("\\end{choiceslist}")
    return "\n".join(lines)


def exam_preamble() -> str:
    return normalize(
        r"""
        \documentclass[10pt]{article}
        \usepackage[margin=0.55in,includeheadfoot]{geometry}
        \usepackage[T1]{fontenc}
        \usepackage[utf8]{inputenc}
        \usepackage{lmodern}
        \usepackage{multicol}
        \usepackage{enumitem}
        \usepackage{booktabs}
        \usepackage{array}
        \usepackage{tabularx}
        \usepackage{amsmath,amssymb}
        \usepackage{tikz}
        \usepackage{graphicx}
        \usepackage{eso-pic}
        \usepackage{fancyhdr}
        \usepackage{lastpage}
        \usepackage{xcolor}
        \usepackage[hidelinks]{hyperref}
        \setlength{\columnsep}{0.28in}
        \setlength{\parindent}{0pt}
        \setlength{\parskip}{0.35em}
        \raggedbottom
        \pagestyle{fancy}
        \fancyhf{}
        \fancyhead[L]{\textsf{AP MICROECONOMICS}}
        \fancyhead[C]{\textsf{Hard Unit Review Test Booklet}}
        \fancyhead[R]{\textsf{Page \thepage\ of \pageref*{LastPage}}}
        \fancyfoot[R]{\textsf{GO TO THE NEXT PAGE.}}
        \renewcommand{\headrulewidth}{0.4pt}
        \renewcommand{\footrulewidth}{0pt}
        \newenvironment{choiceslist}
          {\begin{enumerate}[label=(\Alph*), leftmargin=1.6em, itemsep=0.12em, topsep=0.18em, parsep=0pt]}
          {\end{enumerate}}
        \newenvironment{stimulus}
          {\begin{center}\begin{minipage}{0.96\columnwidth}\footnotesize\itshape\setlength{\tabcolsep}{3pt}\renewcommand{\arraystretch}{0.96}}
          {\end{minipage}\end{center}}
        \newcommand{\unitheader}[2]{%
          \vspace{0.35em}
          {\large\bfseries Unit #1. #2\par}
          \vspace{0.2em}
          \hrule
          \vspace{0.45em}
        }
        \newcommand{\sourcebox}[1]{%
          \begingroup
          \small
          \setlength{\tabcolsep}{4pt}
          #1
          \endgroup
        }
        \newcommand{\CodexWatermark}{%
          \AddToShipoutPictureBG{%
            \AtPageCenter{%
              \makebox(0,0){%
                \rotatebox{45}{%
                  \textcolor[gray]{0.92}{\fontsize{22}{22}\selectfont\bfseries Winston Huang-Generated with Codex}%
                }%
              }%
            }%
          }%
        }
        \begin{document}
        \CodexWatermark
        {\centering
        {\LARGE\bfseries AP Microeconomics Intensive Unit 1--6 Review\par}
        \vspace{0.5em}
        {\large Hard Practice Test Booklet\par}
        \vspace{1em}}
        \textbf{Directions:} Choose the best answer for each question. The set is organized by unit, but the question style deliberately mixes calculation, graph interpretation, policy analysis, and multi-step reasoning in the style of difficult AP Microeconomics items. Some tables and figures were newly created for this booklet after synthesizing the recurring themes in the source PDFs from this directory.

        \textbf{Structure:} 6 units, 20 questions per unit, 120 questions total.

        \textbf{Reference base:} The booklet was synthesized from the TB/SG sets, FRQs, and progress checks found in this folder, especially the recurring topics on comparative advantage, elasticity, market intervention, perfect competition, imperfect competition, factor markets, externalities, public goods, and inequality.

        \vspace{0.8em}
        \begin{multicols*}{2}
        """
    )


def exam_postamble() -> str:
    return normalize(
        r"""
        \end{multicols*}
        \label{LastPage}
        \end{document}
        """
    )


def solutions_preamble() -> str:
    return normalize(
        r"""
        \documentclass[10pt]{article}
        \usepackage[margin=0.65in]{geometry}
        \usepackage[T1]{fontenc}
        \usepackage[utf8]{inputenc}
        \usepackage{lmodern}
        \usepackage{enumitem}
        \usepackage{amsmath,amssymb}
        \usepackage{booktabs}
        \usepackage{graphicx}
        \usepackage{eso-pic}
        \usepackage{xcolor}
        \usepackage[hidelinks]{hyperref}
        \setlength{\parindent}{0pt}
        \setlength{\parskip}{0.45em}
        \newcommand{\unitheader}[2]{%
          \vspace{0.35em}
          {\Large\bfseries Unit #1. #2\par}
          \vspace{0.2em}
          \hrule
          \vspace{0.55em}
        }
        \newcommand{\CodexWatermark}{%
          \AddToShipoutPictureBG{%
            \AtPageCenter{%
              \makebox(0,0){%
                \rotatebox{45}{%
                  \textcolor[gray]{0.92}{\fontsize{22}{22}\selectfont\bfseries Winston Huang-Generated with Codex}%
                }%
              }%
            }%
          }%
        }
        \begin{document}
        \CodexWatermark
        {\centering
        {\LARGE\bfseries AP Microeconomics Intensive Unit 1--6 Review\par}
        \vspace{0.4em}
        {\large Answer Key and Explanations\par}
        \vspace{0.9em}}
        """
    )


def solutions_postamble() -> str:
    return normalize(
        r"""
        \end{document}
        """
    )


def render_exam() -> str:
    parts = [exam_preamble()]
    first_block = True
    for unit in UNITS:
        parts.append(f"\\unitheader{{{unit['unit']}}}{{{unit['title']}}}\n")
        for block in unit["blocks"]:
            if block.get("stimulus"):
                parts.append("\\begin{stimulus}\n")
                parts.append(normalize(block["stimulus"]))
                parts.append("\\end{stimulus}\n")
            enum_opt = "series=apq" if first_block else "resume*=apq"
            parts.append(
                f"\\begin{{enumerate}}[{enum_opt}, leftmargin=*, itemsep=0.85em, topsep=0.2em, parsep=0pt]\n"
            )
            for question in block["questions"]:
                parts.append(f"\\item {question['prompt']}\n")
                parts.append(render_choices(question["choices"]) + "\n")
            parts.append("\\end{enumerate}\n")
            first_block = False
    parts.append(exam_postamble())
    return "".join(parts)


def render_solutions() -> str:
    parts = [solutions_preamble()]
    first_block = True
    for unit in UNITS:
        parts.append(f"\\unitheader{{{unit['unit']}}}{{{unit['title']}}}\n")
        for block in unit["blocks"]:
            enum_opt = "series=aps" if first_block else "resume*=aps"
            parts.append(
                f"\\begin{{enumerate}}[{enum_opt}, leftmargin=*, itemsep=0.6em, topsep=0.2em, parsep=0pt]\n"
            )
            for question in block["questions"]:
                parts.append(
                    f"\\item \\textbf{{Answer: {question['answer']}}}. {question['explanation']}\n"
                )
            parts.append("\\end{enumerate}\n")
            first_block = False
    parts.append(solutions_postamble())
    return "".join(parts)


def main() -> None:
    validate()
    EXAM_TEX.write_text(render_exam(), encoding="utf-8")
    SOLUTIONS_TEX.write_text(render_solutions(), encoding="utf-8")


if __name__ == "__main__":
    main()
