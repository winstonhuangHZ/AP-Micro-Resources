#!/usr/bin/env python3
"""Build the missing core concept visuals for the AP Microeconomics course.

These are original, graph-first teaching assets. They use matplotlib.pyplot and
are exported in PNG, SVG, and PDF formats for handouts and slides.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle, FancyBboxPatch
import numpy as np


ROOT = Path(__file__).resolve().parents[4]
ASSET = ROOT / "APMICRO-Teaching" / "Visual-Plan" / "assets"
OUT = ASSET / "diagrams"
MANIFEST = OUT / "diagram-manifest.csv"

INK = "#17324D"
MUTED = "#5F7184"
GRID = "#D9E3EC"
BLUE = "#1F6FEB"
TEAL = "#2A9D8F"
ORANGE = "#E76F51"
GOLD = "#E9C46A"
RED = "#C94C4C"
PURPLE = "#7353A6"
PALE_BLUE = "#DCEEFF"
PALE_ORANGE = "#FCE2D7"
PALE_TEAL = "#D8F0EA"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.labelsize": 10,
    "xtick.labelsize": 8.5,
    "ytick.labelsize": 8.5,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.facecolor": "white",
})


def base(figsize=(7.2, 4.8)):
    fig, ax = plt.subplots(figsize=figsize, constrained_layout=False)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return fig, ax


def box(ax, xy, w, h, text="", edge=INK, fill="white", radius=0.02, size=10, weight="normal"):
    patch = FancyBboxPatch(
        xy, w, h, boxstyle=f"round,pad=0.012,rounding_size={radius}",
        facecolor=fill, edgecolor=edge, linewidth=1.8,
    )
    ax.add_patch(patch)
    if text:
        ax.text(xy[0] + w / 2, xy[1] + h / 2, text, ha="center", va="center", color=INK, fontsize=size, fontweight=weight)
    return patch


def arrow(ax, start, end, color=INK, style="-|>", lw=1.8, mutation=14, linestyle="-"):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle=style, mutation_scale=mutation,
                                 linewidth=lw, linestyle=linestyle, color=color))


def save(fig, session, slug, intended_use, note="Original diagram"):
    OUT.mkdir(parents=True, exist_ok=True)
    stem = f"session-{session:02d}-{slug}"
    for ext in ("png", "svg", "pdf"):
        fig.savefig(OUT / f"{stem}.{ext}", dpi=300 if ext == "png" else None,
                    bbox_inches="tight", pad_inches=0.06)
    plt.close(fig)
    return {
        "asset_id": stem,
        "session": f"Session {session:02d}",
        "filename": f"{stem}.png",
        "svg": f"{stem}.svg",
        "pdf": f"{stem}.pdf",
        "type": "original concept diagram",
        "intended_use": intended_use,
        "license": "Original work; repository license applies",
        "note": note,
    }


def graph_axes(ax, xlabel="Quantity (Q)", ylabel="Price (P)"):
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(INK)
    ax.spines["bottom"].set_color(INK)
    ax.grid(axis="y", color=GRID, linewidth=0.65)
    ax.set_axisbelow(True)
    ax.set_xlabel(xlabel, labelpad=12, color=INK)
    ax.set_ylabel(ylabel, labelpad=12, color=INK)
    ax.tick_params(colors=MUTED)


def draw_s01():
    fig, ax = base()
    ax.text(.08, .86, "Choice", fontsize=15, fontweight="bold", color=INK)
    box(ax, (.08, .34), .30, .34, "Option A\nbenefit = 8", edge=BLUE, fill=PALE_BLUE, size=12, weight="bold")
    box(ax, (.62, .34), .30, .34, "Option B\nbenefit = 5", edge=ORANGE, fill=PALE_ORANGE, size=12, weight="bold")
    arrow(ax, (.39, .51), (.60, .51), color=INK)
    ax.text(.50, .59, "choose", ha="center", color=MUTED)
    ax.text(.50, .18, "Opportunity cost of A = foregone benefit of B = 5", ha="center", fontsize=11, color=INK, fontweight="bold")
    return save(fig, 1, "choice-opportunity-cost-card", "Choice, scarcity, and opportunity cost.")


def draw_s02():
    fig, axs = plt.subplots(2, 2, figsize=(7.2, 4.8), constrained_layout=False)
    q = np.linspace(0, 100, 200)
    panels = [("Movement along PPC", 0, 1), ("Inefficient point", 1, 2), ("Unattainable point", 2, 3), ("Economic growth", 3, 4)]
    for ax, (label, mode, _) in zip(axs.flat, panels):
        ax.plot(q, 92 - .007*q*q, color=BLUE, linewidth=2.2, label="PPC")
        if mode == 3:
            ax.plot(q, 108 - .007*q*q, color=TEAL, linewidth=2.0, linestyle=(0, (5, 3)), label="New PPC")
            ax.scatter([52], [89], color=TEAL, s=28)
        elif mode == 0:
            ax.scatter([35, 62], [83, 65], color=[BLUE, ORANGE], s=28)
            arrow(ax, (35, 83), (62, 65), color=ORANGE, style="-|>", lw=1.4)
        elif mode == 1:
            ax.scatter([50], [55], color=ORANGE, s=30)
        else:
            ax.scatter([70], [88], color=RED, s=30)
        ax.set_title(label, loc="left", fontsize=9, color=INK, fontweight="bold")
        ax.set_xlim(0, 100); ax.set_ylim(0, 105); ax.set_xticks([]); ax.set_yticks([])
        ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    fig.tight_layout(pad=1.2)
    return save(fig, 2, "ppc-movement-animation-frames", "Movement along a PPC, efficiency, unattainability, and growth.")


def draw_s04():
    fig, ax = plt.subplots(figsize=(7.2, 4.8))
    q = np.linspace(0, 100, 250)
    mb = 92 - .75*q
    mc = 12 + .65*q
    ax.plot(q, mb, color=BLUE, linewidth=2.5, label="MB")
    ax.plot(q, mc, color=ORANGE, linewidth=2.5, label="MC")
    qstar = (92 - 12) / (0.75 + 0.65); y = 92 - .75*qstar
    ax.scatter([qstar], [y], color=INK, s=42, zorder=4)
    ax.plot([qstar, qstar], [0, y], color=INK, linestyle=(0, (3, 3)), linewidth=1)
    ax.plot([0, qstar], [y, y], color=INK, linestyle=(0, (3, 3)), linewidth=1)
    ax.text(qstar, -8, "Q*", ha="center", va="top", color=INK, fontweight="bold")
    ax.text(-5, y, "MB = MC", ha="right", va="center", color=INK, fontweight="bold")
    ax.legend(frameon=False, loc="upper right")
    graph_axes(ax, "Quantity of activity (Q)", "Marginal benefit / cost")
    return save(fig, 4, "mb-mc-crossing-diagram", "Marginal analysis and optimal choice.")


def draw_s05():
    fig, ax = base(figsize=(8.0, 3.8))
    labels = [("Income", "Y", BLUE), ("Tastes", "♥", RED), ("Substitutes", "P_s", TEAL), ("Complements", "P_c", ORANGE), ("Expectations", "E", PURPLE), ("Input prices", "P_i", GOLD)]
    xs = np.linspace(.10, .90, len(labels))
    for x, (name, symbol, color) in zip(xs, labels):
        ax.add_patch(Circle((x, .58), .075, facecolor="white", edgecolor=color, linewidth=2.2))
        ax.text(x, .58, symbol, ha="center", va="center", color=color, fontsize=13, fontweight="bold")
        ax.text(x, .38, name, ha="center", va="top", color=INK, fontsize=8.5)
        arrow(ax, (x, .49), (.50, .20), color=color, lw=1.1, mutation=10)
    box(ax, (.38, .05), .24, .16, "Demand", edge=BLUE, fill=PALE_BLUE, size=12, weight="bold")
    return save(fig, 5, "demand-shifters-icon-strip", "Demand determinants and shift prompts.")


def draw_s06():
    fig, axs = plt.subplots(1, 4, figsize=(8.0, 3.0), constrained_layout=False)
    slopes = [(-.35, "More elastic"), (-.75, "Moderately elastic"), (-1.35, "Moderately inelastic"), (-2.4, "More inelastic")]
    for ax, (slope, label) in zip(axs, slopes):
        q = np.linspace(8, 92, 100); p = 86 + slope*(q-8)
        ax.plot(q, p, color=BLUE, linewidth=2.2)
        ax.axhline(52, color=ORANGE, linestyle=(0, (3, 3)), linewidth=1)
        ax.scatter([40], [52], color=INK, s=18)
        ax.set_title(label, fontsize=8.2, color=INK, loc="left")
        ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.set_xticks([]); ax.set_yticks([])
        ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    fig.text(.50, .02, "Same price movement → different percentage quantity response", ha="center", color=MUTED, fontsize=9)
    fig.tight_layout(rect=[0, .08, 1, 1])
    return save(fig, 6, "elasticity-slider-sequence", "Visual sequence for price elasticity.")


def draw_s07():
    fig, ax = base()
    nodes = {"Tea": (.20, .68), "Coffee": (.50, .68), "Sugar": (.80, .68), "Tea\n& biscuits": (.50, .25)}
    for name, (x, y) in nodes.items():
        box(ax, (x-.10, y-.07), .20, .14, name, edge=BLUE if "&" not in name else ORANGE,
            fill=PALE_BLUE if "&" not in name else PALE_ORANGE, size=9.5, weight="bold")
    arrow(ax, (.30, .68), (.40, .68), color=TEAL); ax.text(.35, .73, "+", ha="center", color=TEAL, fontsize=13, fontweight="bold")
    arrow(ax, (.70, .68), (.60, .68), color=RED); ax.text(.65, .73, "−", ha="center", color=RED, fontsize=13, fontweight="bold")
    arrow(ax, (.20, .59), (.43, .32), color=TEAL); ax.text(.27, .43, "+", color=TEAL, fontsize=13, fontweight="bold")
    arrow(ax, (.80, .59), (.57, .32), color=RED); ax.text(.72, .43, "−", color=RED, fontsize=13, fontweight="bold")
    ax.text(.50, .88, "Cross-price relationships", ha="center", color=INK, fontsize=13, fontweight="bold")
    return save(fig, 7, "substitute-complement-network", "Substitutes, complements, and cross-price elasticity.")


def draw_s08():
    fig, ax = base(figsize=(7.2, 4.8))
    buyers = [92, 84, 76, 68, 60]; sellers = [34, 43, 51, 59, 72]
    for i, v in enumerate(buyers):
        ax.plot([.18, .46], [.80 - i*.10, .80 - i*.10], color=BLUE, linewidth=5, solid_capstyle="round")
        ax.text(.12, .80 - i*.10, f"bid {v}", ha="right", va="center", color=BLUE, fontsize=8)
    for i, v in enumerate(sellers):
        ax.plot([.54, .82], [.80 - i*.10, .80 - i*.10], color=ORANGE, linewidth=5, solid_capstyle="round")
        ax.text(.88, .80 - i*.10, f"ask {v}", ha="left", va="center", color=ORANGE, fontsize=8)
    ax.plot([.50, .50], [.10, .90], color=INK, linestyle=(0, (3, 3)), linewidth=1)
    ax.text(.50, .94, "market price", ha="center", color=INK, fontsize=9, fontweight="bold")
    ax.text(.32, .08, "buyers with willingness to pay above price", ha="center", color=BLUE, fontsize=8)
    ax.text(.68, .08, "sellers with cost below price", ha="center", color=ORANGE, fontsize=8)
    return save(fig, 8, "auction-price-ladder", "Willingness to pay, willingness to sell, and surplus.")


def draw_s09():
    fig, axs = plt.subplots(1, 3, figsize=(8.0, 3.2), constrained_layout=False)
    q = np.linspace(0, 100, 200)
    panels = [("Initial", 0), ("Demand shock", 1), ("New equilibrium", 2)]
    for ax, (label, mode) in zip(axs, panels):
        ax.plot(q, 92 - .72*q, color=BLUE, linewidth=2)
        ax.plot(q, 15 + .55*q, color=ORANGE, linewidth=2)
        if mode >= 1: ax.plot(q, 28 + .55*q, color=TEAL, linewidth=2, linestyle=(0, (4, 3)))
        if mode == 0: ax.scatter([60], [49], color=INK, s=24)
        if mode == 2: ax.scatter([51], [55], color=TEAL, s=24)
        ax.set_title(label, loc="left", fontsize=8.8, color=INK, fontweight="bold")
        ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.set_xticks([]); ax.set_yticks([])
        ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    fig.tight_layout(pad=1.1)
    return save(fig, 9, "shock-to-equilibrium-storyboard", "Initial equilibrium, market shock, and adjustment.")


def draw_s10():
    fig, ax = plt.subplots(figsize=(7.2, 4.8))
    q = np.linspace(0, 100, 200); d = 92 - .7*q; s = 12 + .55*q
    ax.plot(q, d, color=BLUE, linewidth=2.4, label="Demand")
    ax.plot(q, s, color=ORANGE, linewidth=2.4, label="Supply")
    qb, qs, pb, ps = 48, 63, 58, 42
    ax.axhline(pb, color=BLUE, linestyle=(0, (3, 3)), linewidth=1); ax.axhline(ps, color=ORANGE, linestyle=(0, (3, 3)), linewidth=1)
    ax.plot([qb, qb], [0, pb], color=BLUE, linestyle=(0, (3, 3)), linewidth=1)
    ax.plot([qs, qs], [0, ps], color=ORANGE, linestyle=(0, (3, 3)), linewidth=1)
    ax.fill_between([qb, qs], ps, pb, color=PALE_ORANGE, alpha=.8)
    ax.text((qb+qs)/2, (pb+ps)/2, "tax wedge", ha="center", va="center", color=RED, fontsize=10, fontweight="bold")
    ax.text(qb, -8, "Q_D", ha="center", va="top", color=BLUE, fontweight="bold")
    ax.text(qs, -8, "Q_S", ha="center", va="top", color=ORANGE, fontweight="bold")
    ax.text(-4, pb, "P_b", ha="right", va="center", color=BLUE, fontweight="bold")
    ax.text(-4, ps, "P_s", ha="right", va="center", color=ORANGE, fontweight="bold")
    ax.legend(frameon=False, loc="upper right")
    graph_axes(ax, "Quantity (Q)", "Price (P)")
    return save(fig, 10, "tax-wedge-incidence-diagram", "Tax wedge, buyer price, seller price, and incidence.")


def draw_s13():
    fig, ax = base(figsize=(7.2, 4.6))
    cols = ["Output", "FC", "VC", "TC", "ATC", "AVC", "MC"]
    vals = [["Q", "fixed", "variable", "FC+VC", "TC/Q", "VC/Q", "ΔTC/ΔQ"], ["1", "20", "12", "32", "32", "12", "—"], ["2", "20", "20", "40", "20", "10", "8"]]
    x0, y0, cw, rh = .06, .72, .125, .15
    for r, row in enumerate(vals):
        for c, val in enumerate(row):
            fc = PALE_BLUE if r == 0 else (PALE_TEAL if c in (4, 5, 6) else "white")
            ax.add_patch(Rectangle((x0+c*cw, y0-r*rh), cw, rh, facecolor=fc, edgecolor=GRID, linewidth=1))
            ax.text(x0+c*cw+cw/2, y0-r*rh+rh/2, val, ha="center", va="center", color=INK, fontsize=8.6, fontweight="bold" if r == 0 else "normal")
    ax.text(.50, .18, "TC = FC + VC    |    ATC = TC/Q    |    AVC = VC/Q    |    MC = ΔTC/ΔQ", ha="center", color=INK, fontsize=10, fontweight="bold")
    ax.text(.50, .90, "Cost-table annotation", ha="center", color=INK, fontsize=14, fontweight="bold")
    return save(fig, 13, "cost-table-annotation-visual", "Connecting a cost schedule to the cost curves.")


def draw_s14():
    fig, ax = base(figsize=(7.2, 4.8))
    rows = [("Total revenue", "+", BLUE), ("Explicit costs", "−", ORANGE), ("Accounting profit", "=", TEAL), ("Implicit costs", "−", PURPLE), ("Economic profit", "=", RED)]
    y = .76
    for label, sign, color in rows:
        box(ax, (.20, y-.06), .40, .12, label, edge=color, fill="white", size=10, weight="bold")
        ax.text(.67, y, sign, ha="center", va="center", color=color, fontsize=17, fontweight="bold")
        y -= .14
    ax.text(.82, .76, "P × Q", ha="center", color=BLUE, fontweight="bold")
    ax.text(.82, .62, "wages + rent", ha="center", color=ORANGE, fontsize=8)
    ax.text(.82, .48, "financial result", ha="center", color=TEAL, fontsize=8)
    ax.text(.82, .34, "opportunity cost", ha="center", color=PURPLE, fontsize=8)
    ax.text(.82, .20, "economic result", ha="center", color=RED, fontsize=8)
    return save(fig, 14, "accounting-economic-profit-ledger", "Accounting profit versus economic profit.")


def draw_s16():
    fig, ax = base(figsize=(7.2, 4.6))
    box(ax, (.08, .70), .23, .13, "P ≥ AVC?", edge=BLUE, fill=PALE_BLUE, weight="bold")
    box(ax, (.39, .70), .22, .13, "Produce", edge=TEAL, fill=PALE_TEAL, weight="bold")
    box(ax, (.70, .70), .22, .13, "Shutdown", edge=RED, fill=PALE_ORANGE, weight="bold")
    arrow(ax, (.31, .765), (.38, .765), color=TEAL); arrow(ax, (.31, .735), (.69, .735), color=RED)
    ax.text(.345, .80, "yes", color=TEAL, fontsize=8); ax.text(.48, .70, "no", color=RED, fontsize=8)
    box(ax, (.08, .32), .23, .13, "Long run", edge=INK, fill="white", weight="bold")
    box(ax, (.39, .32), .22, .13, "Enter", edge=TEAL, fill=PALE_TEAL, weight="bold")
    box(ax, (.70, .32), .22, .13, "Exit", edge=RED, fill=PALE_ORANGE, weight="bold")
    arrow(ax, (.31, .385), (.38, .385), color=TEAL); arrow(ax, (.31, .355), (.69, .355), color=RED)
    ax.text(.345, .42, "profit", color=TEAL, fontsize=8); ax.text(.48, .34, "loss", color=RED, fontsize=8)
    arrow(ax, (.50, .70), (.50, .46), color=INK, style="-|>")
    return save(fig, 16, "entry-exit-flowchart", "Short-run shutdown and long-run entry/exit decisions.")


def draw_s17():
    fig, ax = base(figsize=(7.2, 4.8))
    items = [("Many firms", "N", BLUE), ("Identical product", "=", TEAL), ("Price taker", "P", ORANGE), ("Free entry/exit", "↔", PURPLE)]
    xs = [.17, .39, .61, .83]
    for x, (label, symbol, color) in zip(xs, items):
        ax.add_patch(Circle((x, .58), .09, facecolor="white", edgecolor=color, linewidth=2.2))
        ax.text(x, .58, symbol, ha="center", va="center", fontsize=17, color=color, fontweight="bold")
        ax.text(x, .39, label, ha="center", va="top", fontsize=9, color=INK, fontweight="bold")
    ax.text(.50, .84, "Perfect competition assumptions", ha="center", fontsize=13, color=INK, fontweight="bold")
    return save(fig, 17, "perfect-competition-assumptions-card", "Perfect-competition assumptions and market structure review.")


def draw_s18():
    fig, ax = base(figsize=(8.0, 4.8))
    cols = ["Structure", "Firms", "Product", "Entry"]
    rows = [["Perfect comp.", "many", "identical", "easy"], ["Monopolistic comp.", "many", "differentiated", "easy"], ["Oligopoly", "few", "same/diff.", "difficult"], ["Monopoly", "one", "unique", "blocked"]]
    x0, y0, cw, rh = .06, .82, .22, .14
    widths = [.30, .17, .26, .20]
    x = x0
    for c, (head, w) in enumerate(zip(cols, widths)):
        ax.add_patch(Rectangle((x, y0), w, rh, facecolor=PALE_BLUE, edgecolor=GRID, linewidth=1)); ax.text(x+w/2, y0+rh/2, head, ha="center", va="center", fontweight="bold", color=INK); x += w
    for r, row in enumerate(rows, 1):
        x=x0
        for c, (val, w) in enumerate(zip(row, widths)):
            fc = PALE_TEAL if r == 1 else (PALE_ORANGE if r == 4 else "white")
            ax.add_patch(Rectangle((x, y0-r*rh), w, rh, facecolor=fc, edgecolor=GRID, linewidth=1)); ax.text(x+w/2, y0-r*rh+rh/2, val, ha="center", va="center", fontsize=8.6, color=INK); x += w
    ax.text(.50, .10, "Market power rises as competitive pressure falls", ha="center", color=INK, fontsize=10.5, fontweight="bold")
    return save(fig, 18, "market-structure-comparison-matrix", "Market-structure comparison and barriers to entry.")


def draw_s19():
    fig, ax = base(figsize=(7.2, 4.6))
    items = [("Legal barrier", "license / patent", BLUE), ("Ownership", "control of input", PURPLE), ("Natural monopoly", "large fixed cost", ORANGE)]
    for i, (head, sub, color) in enumerate(items):
        x=.08+i*.31
        box(ax, (x, .42), .23, .22, head, edge=color, fill="white", size=10, weight="bold")
        ax.text(x+.115, .32, sub, ha="center", color=MUTED, fontsize=8.5)
        if i < 2: arrow(ax, (x+.24, .53), (x+.30, .53), color=INK, mutation=10)
    ax.text(.50, .83, "Entry barriers limit competitive pressure", ha="center", color=INK, fontsize=13, fontweight="bold")
    arrow(ax, (.50, .22), (.50, .38), color=RED)
    ax.text(.50, .13, "market power", ha="center", color=RED, fontweight="bold")
    return save(fig, 19, "entry-barrier-storyboard", "Sources of monopoly power and barriers to entry.")


def draw_s20():
    fig, ax = base(figsize=(7.2, 4.6))
    box(ax, (.10, .38), .30, .28, "Segment A\nhigh willingness to pay\nP_A", edge=BLUE, fill=PALE_BLUE, size=11, weight="bold")
    box(ax, (.60, .38), .30, .28, "Segment B\nlower willingness to pay\nP_B", edge=ORANGE, fill=PALE_ORANGE, size=11, weight="bold")
    arrow(ax, (.41, .52), (.59, .52), color=INK)
    ax.text(.50, .60, "different prices", ha="center", color=INK, fontsize=9)
    ax.text(.50, .18, "same seller · separate markets · limited resale", ha="center", color=MUTED, fontsize=10)
    return save(fig, 20, "price-menu-cards", "Price discrimination and segmented markets.")


def draw_s21():
    fig, ax = base(figsize=(7.2, 4.8))
    products = [("taste", BLUE), ("location", TEAL), ("design", ORANGE), ("service", PURPLE)]
    for i, (label, color) in enumerate(products):
        x=.10+i*.22
        ax.add_patch(Circle((x+.07, .62), .07, facecolor="white", edgecolor=color, linewidth=2.3))
        ax.add_patch(Circle((x+.05, .64), .015, facecolor=color, edgecolor="none"))
        ax.add_patch(Circle((x+.09, .60), .015, facecolor=color, edgecolor="none"))
        ax.text(x+.07, .43, label, ha="center", color=INK, fontsize=9, fontweight="bold")
    ax.text(.50, .82, "Product differentiation", ha="center", color=INK, fontsize=14, fontweight="bold")
    ax.text(.50, .19, "similar products · different perceived attributes", ha="center", color=MUTED, fontsize=10)
    return save(fig, 21, "product-differentiation-collage", "Product differentiation in monopolistic competition.")


def draw_s22():
    fig, ax = base(figsize=(7.2, 4.8))
    box(ax, (.08, .46), .18, .12, "Start", edge=INK, fill="white", weight="bold")
    box(ax, (.40, .68), .20, .12, "Cooperate", edge=TEAL, fill=PALE_TEAL, weight="bold")
    box(ax, (.40, .24), .20, .12, "Defect", edge=RED, fill=PALE_ORANGE, weight="bold")
    box(ax, (.76, .68), .16, .12, "repeat", edge=PURPLE, fill="white", weight="bold")
    box(ax, (.76, .24), .16, .12, "payoff", edge=PURPLE, fill="white", weight="bold")
    arrow(ax, (.27, .52), (.39, .73), color=TEAL); arrow(ax, (.27, .52), (.39, .29), color=RED)
    arrow(ax, (.61, .74), (.75, .74), color=TEAL); arrow(ax, (.61, .30), (.75, .30), color=RED)
    ax.text(.33, .65, "A chooses", color=MUTED, fontsize=8, rotation=28)
    ax.text(.33, .38, "B responds", color=MUTED, fontsize=8, rotation=-28)
    return save(fig, 22, "repeated-game-decision-tree", "Strategic interaction and repeated-game reasoning.")


def draw_s24():
    fig, ax = base(figsize=(8.0, 3.8))
    labels = [("Product\ndemand", BLUE), ("Marginal\nrevenue", TEAL), ("Marginal\nproduct", ORANGE), ("MRP / labor\ndemand", PURPLE)]
    for i, (label, color) in enumerate(labels):
        x=.05+i*.245
        box(ax, (x, .40), .18, .20, label, edge=color, fill="white", size=10, weight="bold")
        if i < 3: arrow(ax, (x+.19, .50), (x+.235, .50), color=color)
    ax.text(.50, .78, "Derived demand chain", ha="center", color=INK, fontsize=14, fontweight="bold")
    ax.text(.50, .16, "demand for the final product creates demand for productive inputs", ha="center", color=MUTED, fontsize=9.5)
    return save(fig, 24, "derived-demand-chain", "Derived demand for labor and other factors.")


def draw_s25():
    fig, ax = base(figsize=(7.2, 4.8))
    center = (.50, .50)
    box(ax, (.37, .43), .26, .14, "Labor supply", edge=BLUE, fill=PALE_BLUE, size=11, weight="bold")
    nodes = [("wages", .18, .78, TEAL), ("benefits", .82, .78, ORANGE), ("alternatives", .18, .22, PURPLE), ("population", .82, .22, GOLD)]
    for label, x, y, color in nodes:
        box(ax, (x-.10, y-.055), .20, .11, label, edge=color, fill="white", size=9, weight="bold")
        arrow(ax, (x, y-.07 if y>.5 else y+.07), (center[0] + (.10 if x<.5 else -.10), center[1] + (.05 if y>.5 else -.05)), color=color, lw=1.3, mutation=10)
    return save(fig, 25, "labor-supply-determinants-map", "Determinants that shift factor supply.")


def draw_s26():
    fig, ax = plt.subplots(figsize=(7.2, 4.8))
    q = np.arange(1, 9); mrp = np.array([90, 80, 70, 60, 50, 40, 30, 20]); w = np.full(8, 40)
    ax.plot(q, mrp, color=BLUE, linewidth=2.5, marker="o", label="MRP")
    ax.plot(q, w, color=ORANGE, linewidth=2.2, label="Factor price")
    ax.axvline(5, color=INK, linestyle=(0, (3, 3)), linewidth=1)
    ax.scatter([5], [40], color=INK, s=38)
    ax.text(5, -7, "L*", ha="center", va="top", color=INK, fontweight="bold")
    ax.text(-.2, 40, "W*", ha="right", va="center", color=INK, fontweight="bold")
    ax.legend(frameon=False, loc="upper right")
    graph_axes(ax, "Quantity of labor (L)", "Wage / MRP")
    return save(fig, 26, "mrp-factor-price-decision-chart", "Competitive factor-market hiring decision.")


def draw_s27():
    fig, ax = base(figsize=(7.2, 4.4))
    box(ax, (.08, .43), .22, .16, "Workers", edge=TEAL, fill=PALE_TEAL, size=11, weight="bold")
    box(ax, (.39, .43), .22, .16, "One large\nemployer", edge=ORANGE, fill=PALE_ORANGE, size=10.5, weight="bold")
    box(ax, (.70, .43), .22, .16, "Local labor\nmarket", edge=BLUE, fill=PALE_BLUE, size=10.5, weight="bold")
    arrow(ax, (.31, .51), (.38, .51), color=TEAL); arrow(ax, (.62, .51), (.69, .51), color=BLUE)
    ax.text(.50, .79, "Monopsony map", ha="center", color=INK, fontsize=14, fontweight="bold")
    ax.text(.50, .17, "the employer faces the market supply curve and internalizes the hiring effect", ha="center", color=MUTED, fontsize=8.8)
    return save(fig, 27, "single-employer-labor-market-map", "Monopsony and the single-buyer labor market.")


def draw_s28():
    fig, axs = plt.subplots(1, 3, figsize=(8.0, 3.2), constrained_layout=False)
    q = np.linspace(0, 100, 160)
    for ax, label, shift in zip(axs, ["Underproduction", "Efficient output", "Overproduction"], [-18, 0, 18]):
        mb = 84 - .6*q; mc = 16 + .55*q
        ax.plot(q, mb, color=BLUE, linewidth=2); ax.plot(q, mc, color=ORANGE, linewidth=2)
        q1 = 45 + shift; q2 = 55 + shift
        if shift < 0: ax.fill_between(q[q1<q], mb[q1<q], mc[q1<q], where=(q[q1<q] >= q1) & (q[q1<q] <= q2), color=PALE_ORANGE, alpha=.8)
        elif shift > 0: ax.fill_between(q, mb, mc, where=(q >= q1) & (q <= q2), color=PALE_ORANGE, alpha=.8)
        ax.axvline(50, color=INK, linestyle=(0, (3, 3)), linewidth=.8)
        ax.set_title(label, fontsize=8.7, loc="left", color=INK, fontweight="bold")
        ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.set_xticks([]); ax.set_yticks([])
        ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    fig.tight_layout(pad=1.1)
    return save(fig, 28, "efficiency-triangle-animation-frames", "Marginal benefit, marginal cost, and efficiency loss.")


def draw_s29():
    fig, ax = base(figsize=(7.2, 4.8))
    box(ax, (.35, .76), .30, .12, "Externality", edge=INK, fill="white", size=11, weight="bold")
    box(ax, (.08, .45), .28, .13, "Negative\nexternality", edge=RED, fill=PALE_ORANGE, size=10, weight="bold")
    box(ax, (.64, .45), .28, .13, "Positive\nexternality", edge=TEAL, fill=PALE_TEAL, size=10, weight="bold")
    box(ax, (.08, .16), .28, .13, "Pigouvian\ntax", edge=ORANGE, fill="white", size=10, weight="bold")
    box(ax, (.64, .16), .28, .13, "Pigouvian\nsubsidy", edge=BLUE, fill="white", size=10, weight="bold")
    arrow(ax, (.43, .76), (.25, .59), color=RED); arrow(ax, (.57, .76), (.75, .59), color=TEAL)
    arrow(ax, (.22, .45), (.22, .30), color=ORANGE); arrow(ax, (.78, .45), (.78, .30), color=BLUE)
    return save(fig, 29, "pigouvian-tax-subsidy-decision-tree", "Policy responses to negative and positive externalities.")


def draw_s30():
    fig, ax = base(figsize=(6.8, 5.0))
    x0, y0, cw, rh = .20, .20, .30, .26
    ax.text(.50, .92, "Rivalry × excludability", ha="center", fontsize=14, color=INK, fontweight="bold")
    ax.text(.35, .13, "nonrival", ha="center", color=INK, fontsize=9, fontweight="bold")
    ax.text(.65, .13, "rival", ha="center", color=INK, fontsize=9, fontweight="bold")
    ax.text(.12, .47, "nonexcludable", ha="center", rotation=90, color=INK, fontsize=9, fontweight="bold")
    ax.text(.12, .73, "excludable", ha="center", rotation=90, color=INK, fontsize=9, fontweight="bold")
    cells = [[("Public good", PALE_TEAL), ("Common resource", PALE_ORANGE)], [("Club good", PALE_BLUE), ("Private good", "white")]]
    for r in range(2):
        for c in range(2):
            x=x0+c*cw; y=y0+(1-r)*rh
            ax.add_patch(Rectangle((x,y),cw,rh,facecolor=cells[r][c][1],edgecolor=GRID,linewidth=1.2))
            ax.text(x+cw/2,y+rh/2,cells[r][c][0],ha="center",va="center",color=INK,fontsize=9.5,fontweight="bold")
    return save(fig, 30, "rivalry-excludability-matrix", "Public, private, club, and common-resource goods.")


def draw_s33():
    fig, ax = base(figsize=(8.0, 4.2))
    box(ax, (.05, .41), .20, .18, "Private\nmarket outcome", edge=BLUE, fill=PALE_BLUE, size=10, weight="bold")
    box(ax, (.34, .68), .20, .15, "Externality", edge=RED, fill=PALE_ORANGE, size=10, weight="bold")
    box(ax, (.34, .42), .20, .15, "Public good", edge=TEAL, fill=PALE_TEAL, size=10, weight="bold")
    box(ax, (.34, .16), .20, .15, "Information", edge=PURPLE, fill="white", size=10, weight="bold")
    box(ax, (.72, .41), .22, .18, "Policy /\ninstitution", edge=ORANGE, fill="white", size=10, weight="bold")
    for y, color in [(.75, RED), (.50, TEAL), (.24, PURPLE)]:
        arrow(ax, (.26, .50), (.33, y), color=color, lw=1.5)
        arrow(ax, (.55, y), (.71, .50), color=color, lw=1.5)
    ax.text(.50, .92, "Market-failure synthesis", ha="center", color=INK, fontsize=14, fontweight="bold")
    return save(fig, 33, "market-failure-synthesis-map", "Synthesis of market failure and policy responses.")


def draw_s34():
    fig, axs = plt.subplots(2, 3, figsize=(8.0, 5.0), constrained_layout=False)
    labels = ["Demand / supply", "PPC", "Cost curves", "Monopoly", "Factor market", "Externality"]
    for ax, label in zip(axs.flat, labels):
        ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_xticks([]); ax.set_yticks([])
        ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
        ax.text(.05, .93, label, transform=ax.transAxes, color=MUTED, fontsize=8, fontweight="bold")
        ax.set_xlabel("Quantity", fontsize=7, labelpad=1); ax.set_ylabel("Price / value", fontsize=7, labelpad=1)
    fig.tight_layout(pad=1.2)
    return save(fig, 34, "blank-graph-practice-sheet", "Blank AP graph practice for review sessions.")


def draw_s36():
    fig, ax = base(figsize=(8.0, 3.8))
    parts = [("Graph", BLUE), ("Calculation", ORANGE), ("Explanation", TEAL), ("Conclusion", PURPLE)]
    for i, (label, color) in enumerate(parts):
        x=.07+i*.235
        box(ax, (x, .42), .17, .20, label, edge=color, fill="white", size=10, weight="bold")
        if i < 3: arrow(ax, (x+.18, .52), (x+.225, .52), color=INK, mutation=10)
    ax.text(.50, .80, "FRQ response anatomy", ha="center", color=INK, fontsize=14, fontweight="bold")
    ax.text(.50, .18, "show the model · show the work · explain the mechanism · answer the question", ha="center", color=MUTED, fontsize=9.5)
    return save(fig, 36, "frq-response-anatomy", "FRQ response structure and scoring opportunities.")


BUILDERS = [draw_s01, draw_s02, draw_s04, draw_s05, draw_s06, draw_s07, draw_s08, draw_s09,
            draw_s10, draw_s13, draw_s14, draw_s16, draw_s17, draw_s18, draw_s19, draw_s20,
            draw_s21, draw_s22, draw_s24, draw_s25, draw_s26, draw_s27, draw_s28, draw_s29,
            draw_s30, draw_s33, draw_s34, draw_s36]


def main():
    rows = [builder() for builder in BUILDERS]
    with MANIFEST.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"built {len(rows)} concept diagrams in {OUT}")


if __name__ == "__main__":
    main()
