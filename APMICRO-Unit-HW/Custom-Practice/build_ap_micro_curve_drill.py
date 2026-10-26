from __future__ import annotations

from pathlib import Path
from textwrap import dedent

from ap_micro_curve_hard_data import BLOCKS


ROOT = Path(__file__).resolve().parent
EXAM_TEX = ROOT / "ap_micro_curve_challenge.tex"
SOLUTIONS_TEX = ROOT / "ap_micro_curve_challenge_solutions.tex"


def normalize(text: str) -> str:
    return dedent(text).strip() + "\n"


def validate() -> None:
    total = 0
    for block in BLOCKS:
        for question in block["questions"]:
            if len(question["choices"]) != 5:
                raise ValueError("Every question must have 5 choices.")
            if question["answer"] not in {"A", "B", "C", "D", "E"}:
                raise ValueError("Invalid answer key.")
            total += 1
    if total != 40:
        raise ValueError(f"Expected 40 questions, found {total}.")


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
        \usepackage{amsmath,amssymb}
        \usepackage{tikz}
        \usepackage{graphicx}
        \usepackage{eso-pic}
        \usepackage{fancyhdr}
        \usepackage{lastpage}
        \usepackage{needspace}
        \usepackage{xcolor}
        \usepackage[hidelinks]{hyperref}
        \setlength{\columnsep}{0.28in}
        \setlength{\parindent}{0pt}
        \setlength{\parskip}{0.35em}
        \emergencystretch=1em
        \raggedbottom
        \pagestyle{fancy}
        \fancyhf{}
        \fancyhead[L]{\textsf{AP MICROECONOMICS}}
        \fancyhead[C]{\textsf{Curve Challenge Booklet}}
        \fancyhead[R]{\textsf{Page \thepage\ of \pageref*{LastPage}}}
        \fancyfoot[R]{\textsf{GO TO THE NEXT PAGE.}}
        \renewcommand{\headrulewidth}{0.4pt}
        \renewcommand{\footrulewidth}{0pt}
        \newenvironment{choiceslist}
          {\begin{enumerate}[label=(\Alph*), leftmargin=1.55em, itemsep=0.1em, topsep=0.15em, parsep=0pt]}
          {\end{enumerate}}
        \newenvironment{stimulus}
          {\begin{center}\begin{minipage}{0.97\columnwidth}\footnotesize\itshape\setlength{\tabcolsep}{3pt}\renewcommand{\arraystretch}{0.96}}
          {\end{minipage}\end{center}}
        \newcommand{\sectiontitle}[1]{%
          \vspace{0.35em}
          {\large\bfseries #1\par}
          \vspace{0.15em}
          \hrule
          \vspace{0.4em}
        }
        \newcommand{\CodexWatermark}{%
          \AddToShipoutPictureBG{%
            \AtPageCenter{%
              \makebox(0,0){%
                \rotatebox{45}{%
                  \textcolor[gray]{0.93}{\fontsize{22}{22}\selectfont\bfseries Winston Huang-Generated with Codex}%
                }%
              }%
            }%
          }%
        }
        \begin{document}
        \CodexWatermark
        {\centering
        {\LARGE\bfseries AP Microeconomics Curve Challenge\par}
        \vspace{0.35em}
        {\large 40 Hard AP-Style Graph and Curve Problems\par}
        \vspace{0.85em}}
        \textbf{Directions:} Choose the best answer for each question. Every question in this booklet is built around a graph, curve, or curve-based inference in the style of difficult AP Microeconomics multiple-choice and FRQ graph reasoning.

        \textbf{Source basis:} The topics, graph types, and traps in this booklet were synthesized from the 82 TB/SG/FRQ/progress-check PDFs in this folder, especially the repeated graph work on price controls, taxation, trade, perfect competition, monopoly, monopolistic competition, labor markets, monopsony, externalities, and inequality.

        \vspace{0.7em}
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
        \usepackage{graphicx}
        \usepackage{eso-pic}
        \usepackage{xcolor}
        \usepackage[hidelinks]{hyperref}
        \setlength{\parindent}{0pt}
        \setlength{\parskip}{0.42em}
        \newcommand{\sectiontitle}[1]{%
          \vspace{0.35em}
          {\Large\bfseries #1\par}
          \vspace{0.2em}
          \hrule
          \vspace{0.5em}
        }
        \newcommand{\CodexWatermark}{%
          \AddToShipoutPictureBG{%
            \AtPageCenter{%
              \makebox(0,0){%
                \rotatebox{45}{%
                  \textcolor[gray]{0.93}{\fontsize{22}{22}\selectfont\bfseries Winston Huang-Generated with Codex}%
                }%
              }%
            }%
          }%
        }
        \begin{document}
        \CodexWatermark
        {\centering
        {\LARGE\bfseries AP Microeconomics Curve Challenge\par}
        \vspace{0.3em}
        {\large Answer Key and Explanations\par}
        \vspace{0.8em}}
        """
    )


def solutions_postamble() -> str:
    return "\\end{document}\n"


def render_exam() -> str:
    parts = [exam_preamble(), "\\sectiontitle{Graph Problems}\n"]
    first_block = True
    for block in BLOCKS:
        parts.append("\\Needspace{18\\baselineskip}\n")
        parts.append("\\begin{stimulus}\n")
        parts.append(normalize(block["stimulus"]))
        parts.append("\\end{stimulus}\n")
        enum_opt = "series=curveq" if first_block else "resume*=curveq"
        parts.append(
            f"\\begin{{enumerate}}[{enum_opt}, leftmargin=*, itemsep=0.8em, topsep=0.18em, parsep=0pt]\n"
        )
        for question in block["questions"]:
            parts.append(f"\\item {question['prompt']}\n")
            parts.append(render_choices(question["choices"]) + "\n")
        parts.append("\\end{enumerate}\n")
        first_block = False
    parts.append(exam_postamble())
    return "".join(parts)


def render_solutions() -> str:
    parts = [solutions_preamble(), "\\sectiontitle{Solutions}\n"]
    first_block = True
    for block in BLOCKS:
        enum_opt = "series=curves" if first_block else "resume*=curves"
        parts.append(
            f"\\begin{{enumerate}}[{enum_opt}, leftmargin=*, itemsep=0.58em, topsep=0.18em, parsep=0pt]\n"
        )
        for question in block["questions"]:
            parts.append(f"\\item \\textbf{{Answer: {question['answer']}}}. {question['explanation']}\n")
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
