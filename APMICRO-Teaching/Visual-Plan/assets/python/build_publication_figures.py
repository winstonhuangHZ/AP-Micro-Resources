#!/usr/bin/env python3
"""Build publication-quality AP Microeconomics figures with matplotlib.pyplot.

Every figure is exported as PNG, SVG, and PDF. Synthetic values are explicitly
labelled as illustrative; official series point back to the local data manifest.
"""
from __future__ import annotations

import re
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import FancyArrowPatch, Rectangle
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[4]
ASSET = ROOT / "APMICRO-Teaching" / "Visual-Plan" / "assets"
DATA = ASSET / "data"
OUT = ASSET / "exports" / "figures"
MANIFEST = OUT / "figure-manifest.csv"

INK = "#17324D"
MUTED = "#5F7184"
GRID = "#D9E3EC"
BLUE = "#1F6FEB"
TEAL = "#2A9D8F"
ORANGE = "#E76F51"
GOLD = "#E9C46A"
RED = "#C94C4C"
PURPLE = "#7353A6"
SKY = "#6BAED6"
PALE_BLUE = "#DCEEFF"
PALE_ORANGE = "#FCE2D7"
PALE_TEAL = "#D8F0EA"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.titlesize": 12,
    "axes.labelsize": 10,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "axes.edgecolor": INK,
    "axes.linewidth": 0.8,
    "axes.labelcolor": INK,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
    "text.color": INK,
    "savefig.facecolor": "white",
    "figure.facecolor": "white",
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "svg.fonttype": "none",
})

FIGURES: list[dict] = []


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def source_text(path: str, note: str = "") -> str:
    return f"Source: {path}. {note}".strip()


def figure(title: str, subtitle: str = "", figsize=(7.2, 4.5)):
    fig, ax = plt.subplots(figsize=figsize, constrained_layout=False)
    fig.suptitle(title, x=0.09, y=0.965, ha="left", va="top", fontsize=14, fontweight="bold", color=INK)
    if subtitle:
        fig.text(0.09, 0.915, subtitle, ha="left", va="top", fontsize=9.5, color=MUTED)
    return fig, ax


def style_axes(ax, xlabel=None, ylabel=None, zero=False):
    ax.grid(axis="y", color=GRID, linewidth=0.7, alpha=0.8)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(INK)
    ax.spines["bottom"].set_color(INK)
    if xlabel:
        ax.set_xlabel(xlabel, labelpad=7)
    if ylabel:
        ax.set_ylabel(ylabel, labelpad=7)
    if zero:
        ax.axhline(0, color=INK, linewidth=0.8)


def econ_axes(ax, xlabel="Quantity (Q)", ylabel="Price (P)", origin=True):
    """Apply AP Micro style axis names and mark the origin."""
    ax.set_xlabel(xlabel, labelpad=7)
    ax.set_ylabel(ylabel, labelpad=7)
    style_axes(ax)
    if origin and ax.get_xlim()[0] <= 0 <= ax.get_xlim()[1] and ax.get_ylim()[0] <= 0 <= ax.get_ylim()[1]:
        ax.annotate("0", xy=(0, 0), xytext=(-7, -9), textcoords="offset points",
                    ha="right", va="top", fontsize=8.5, color=MUTED)


def project_point(ax, x, y, x_label, y_label, color=MUTED, linewidth=0.9, label_offset=2):
    """Draw the standard dashed projections from a key point to both axes."""
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    ax.plot([x, x], [ymin, y], color=color, linewidth=linewidth, linestyle=(0, (3, 3)), zorder=1)
    ax.plot([xmin, x], [y, y], color=color, linewidth=linewidth, linestyle=(0, (3, 3)), zorder=1)
    x_pad = 0.035 * (xmax - xmin)
    y_pad = 0.035 * (ymax - ymin)
    ax.text(x, ymin - y_pad, format_label(x_label), ha="center", va="top", fontsize=8.5, color=INK,
            fontweight="bold", clip_on=False)
    ax.text(xmin - x_pad, y, format_label(y_label), ha="right", va="center", fontsize=8.5, color=INK,
            fontweight="bold", clip_on=False)


def project_x(ax, x, x_label, y=None, color=MUTED, linewidth=0.9, label_offset=0):
    ymin, ymax = ax.get_ylim()
    if y is None:
        y = ymax
    ax.plot([x, x], [ymin, y], color=color, linewidth=linewidth, linestyle=(0, (3, 3)), zorder=1)
    y_pad = 0.035 * (ymax - ymin)
    ax.text(x, ymin - y_pad - label_offset * y_pad, format_label(x_label), ha="center", va="top", fontsize=8.5, color=INK,
            fontweight="bold", clip_on=False)


def project_y(ax, y, y_label, x=None, color=MUTED, linewidth=0.9, label_offset=0, label_y_offset=0):
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    if x is None:
        x = xmax
    ax.plot([xmin, x], [y, y], color=color, linewidth=linewidth, linestyle=(0, (3, 3)), zorder=1)
    x_pad = 0.035 * (xmax - xmin)
    ax.text(xmin - x_pad - label_offset * x_pad,
            y + label_y_offset * 0.035 * (ymax - ymin),
            format_label(y_label), ha="right", va="center", fontsize=8.5, color=INK,
            fontweight="bold", clip_on=False)


def mark_equilibrium(ax, x, y, x_label="Q*", y_label="P*", point_label=None, color=INK):
    ax.scatter([x], [y], color=color, s=42, zorder=5)
    project_point(ax, x, y, x_label, y_label)
    if point_label:
        add_label(ax, x + 2, y + 3, point_label, weight="bold")


def polish(fig, axes, source: str, note: str = ""):
    if isinstance(axes, np.ndarray):
        axes = list(axes.ravel())
    elif not isinstance(axes, (list, tuple)):
        axes = [axes]
    for ax in axes:
        if ax is not None:
            style_axes(ax)
    footer = source if not note else f"{source}  |  {note}"
    fig.text(0.09, 0.035, footer, ha="left", va="bottom", fontsize=7.5, color=MUTED)
    fig.tight_layout(rect=[0.06, 0.09, 0.98, 0.88])


def save(fig, session: int, visual: str, source: str, note: str = ""):
    OUT.mkdir(parents=True, exist_ok=True)
    stem = f"session-{session:02d}-{slug(visual)}"
    for ext in ("png", "svg", "pdf"):
        fig.savefig(OUT / f"{stem}.{ext}", dpi=320 if ext == "png" else None, bbox_inches="tight", pad_inches=0.08)
    plt.close(fig)
    FIGURES.append({
        "session": session,
        "visual": visual,
        "status": "rendered",
        "png": f"APMICRO-Teaching/Visual-Plan/assets/exports/figures/{stem}.png",
        "svg": f"APMICRO-Teaching/Visual-Plan/assets/exports/figures/{stem}.svg",
        "pdf": f"APMICRO-Teaching/Visual-Plan/assets/exports/figures/{stem}.pdf",
        "source": source,
        "note": note,
    })


def add_label(ax, x, y, text, color=INK, ha="left", va="bottom", size=9, weight="normal"):
    ax.text(x, y, format_label(text), color=color, ha=ha, va=va, fontsize=size, fontweight=weight,
            bbox=dict(boxstyle="round,pad=0.22", facecolor="white", edgecolor="none", alpha=0.85))


def format_label(text):
    """Render labels with AP-style subscripts and superscripts through mathtext."""
    if isinstance(text, str) and ("_" in text or "^" in text) and not text.startswith("$"):
        return f"${text}$"
    return text


def change_arrow(ax, start, end, label=None, color=INK, bidirectional=False,
                 text_offset=(0, 0), connectionstyle="arc3,rad=0", linewidth=1.5,
                 mutation_scale=13):
    """Add a compact arrow for a curve, price, or quantity change."""
    style = "<->" if bidirectional else "-|>"
    ax.annotate(
        "", xy=end, xytext=start,
        arrowprops=dict(
            arrowstyle=style, color=color, linewidth=linewidth,
            mutation_scale=mutation_scale, shrinkA=2, shrinkB=2,
            connectionstyle=connectionstyle,
        ),
        zorder=6,
    )
    if label:
        mid = ((start[0] + end[0]) / 2 + text_offset[0],
               (start[1] + end[1]) / 2 + text_offset[1])
        add_label(ax, mid[0], mid[1], label, color=color, ha="center", va="center", size=8.5, weight="bold")


def draw_market(ax, demand, supply, title, xlim=None, ylim=None, equilibrium=True, fill=None):
    q = np.linspace(0, 100, 301)
    pdemand = demand(q)
    psupply = supply(q)
    ax.plot(q, pdemand, color=BLUE, linewidth=2.4, label="Demand")
    ax.plot(q, psupply, color=ORANGE, linewidth=2.4, label="Supply")
    if equilibrium:
        idx = int(np.argmin(np.abs(pdemand - psupply)))
        qe, pe = q[idx], pdemand[idx]
        if xlim:
            ax.set_xlim(*xlim)
        if ylim:
            ax.set_ylim(*ylim)
        mark_equilibrium(ax, qe, pe, "Q_M", "P_M", f"E ({qe:.0f}, {pe:.0f})")
    ax.set_title(title, loc="left", fontsize=10.5, fontweight="bold", pad=8)
    econ_axes(ax)
    if xlim:
        ax.set_xlim(*xlim)
    if ylim:
        ax.set_ylim(*ylim)
    ax.legend(frameon=False, loc="upper right", ncol=2)
    style_axes(ax)


def load_csv(rel: str) -> pd.DataFrame:
    return pd.read_csv(DATA / rel)


def make_scarcity():
    fig, ax = figure("Scarcity makes trade-offs visible", "A fixed resource bundle must be divided among competing uses.")
    uses = ["Food", "Shelter", "Education"]
    labor = np.array([7, 5, 3])
    materials = np.array([4, 6, 2])
    time = np.array([5, 2, 7])
    x = np.arange(len(uses))
    ax.bar(x, labor, color=BLUE, label="Labor")
    ax.bar(x, materials, bottom=labor, color=TEAL, label="Materials")
    ax.bar(x, time, bottom=labor + materials, color=GOLD, label="Time")
    ax.set_xticks(x, uses)
    ax.set_ylabel("Allocated resource units")
    ax.legend(frameon=False, ncol=3, loc="upper right")
    style_axes(ax)
    polish(fig, ax, "Source: Original illustrative model data.", "Illustrative allocation; units are synthetic.")
    save(fig, 1, "Three-resource scarcity panel", "Original illustrative model data", "Synthetic allocation table for teaching.")


def make_ppc():
    d = load_csv("illustrative/ppc.csv")
    fig, ax = figure("Production possibilities frontier", "Efficiency, unattainability, and growth on one coordinate system.")
    ax.plot(d.x_good_a, d.y_good_b, color=BLUE, linewidth=2.6, label="Current PPC")
    ax.plot(d.x_good_a, d.growth_y_good_b, color=TEAL, linewidth=2.2, linestyle=(0, (5, 3)), label="Growth")
    ax.fill_between(d.x_good_a, 0, d.y_good_b, color=PALE_BLUE, alpha=0.65)
    ax.scatter([30, 80, 55], [40, 30, 83], color=[ORANGE, RED, INK], s=42, zorder=4)
    add_label(ax, 30, 44, "Inefficient", color=ORANGE, weight="bold")
    add_label(ax, 80, 34, "Unattainable", color=RED, weight="bold")
    add_label(ax, 56, 86, "Efficient", color=INK, weight="bold")
    ax.set_xlabel("Good A (Q_A)")
    ax.set_ylabel("Good B (Q_B)")
    ax.set_xlim(0, 105)
    ax.set_ylim(0, 120)
    ax.legend(frameon=False, loc="upper right")
    polish(fig, ax, "Source: APMICRO illustrative data / ppc.csv.", "Model values are illustrative.")
    save(fig, 2, "PPC with efficiency zones", "APMICRO illustrative data / ppc.csv", "Model values are illustrative.")


def make_trade_flow():
    fig, ax = figure("Specialization and mutually beneficial trade", "Opportunity cost determines specialization; terms of trade connect the two producers.", figsize=(7.2, 4.6))
    ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis("off")
    for x, label, color in [(1.5, "Producer A", BLUE), (8.5, "Producer B", ORANGE)]:
        ax.add_patch(Rectangle((x - 1.25, 2.1), 2.5, 1.8, facecolor="white", edgecolor=color, linewidth=2.0))
        ax.text(x, 3.0, label, ha="center", va="center", fontsize=12, fontweight="bold")
    arrows = [(2.8, 3.1, 6.9, 3.1, "Food"), (7.0, 2.8, 2.8, 2.8, "Cloth")]
    for x1, y1, x2, y2, label in arrows:
        ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=16, linewidth=2, color=TEAL))
        ax.text((x1+x2)/2, y1 + (0.27 if y1 > 3 else -0.35), label, ha="center", va="center", color=TEAL, fontweight="bold")
    ax.text(5, 1.0, "Specialization → exchange → a larger attainable consumption set", ha="center", fontsize=11, color=INK)
    polish(fig, [], "Source: APMICRO illustrative data / comparative-advantage.csv.", "Schematic teaching diagram; arrows show direction of trade.")
    save(fig, 3, "Specialization and trade flow map", "APMICRO illustrative data / comparative-advantage.csv", "Schematic teaching diagram.")


def make_comp_adv_heatmap():
    d = load_csv("illustrative/comparative-advantage.csv").pivot(index="producer", columns="product", values="opportunity_cost")
    fig, ax = figure("Comparative advantage is a relative-cost relationship", "Lower opportunity cost identifies the producer with comparative advantage.")
    cmap = LinearSegmentedColormap.from_list("cost", [PALE_TEAL, GOLD, PALE_ORANGE])
    im = ax.imshow(d.values, cmap=cmap, aspect="auto")
    ax.set_xticks(range(len(d.columns)), d.columns); ax.set_yticks(range(len(d.index)), d.index)
    for i in range(d.shape[0]):
        for j in range(d.shape[1]):
            ax.text(j, i, f"{d.iloc[i,j]:.1f}", ha="center", va="center", fontweight="bold")
    ax.set_xlabel("Product"); ax.set_ylabel("Producer"); ax.set_title("Opportunity cost", loc="left", fontsize=10.5, fontweight="bold")
    style_axes(ax); ax.grid(False)
    polish(fig, ax, "Source: APMICRO illustrative data / comparative-advantage.csv.", "Lower values indicate lower opportunity cost.")
    save(fig, 3, "Comparative-advantage heatmap", "APMICRO illustrative data / comparative-advantage.csv", "Lower values indicate lower opportunity cost.")


def make_cba():
    fig, ax = figure("Total benefit, total cost, and net benefit", "A marginal comparison explains why net benefit peaks at the chosen quantity.")
    q = np.arange(1, 8); mb = np.array([18, 15, 12, 9, 6, 3, 1]); mc = np.array([2, 4, 6, 8, 10, 12, 14])
    total_benefit = np.cumsum(mb); total_cost = np.cumsum(mc); net_benefit = total_benefit - total_cost
    width = 0.25
    ax.bar(q-width, total_benefit, width, color=BLUE, label="Total benefit")
    ax.bar(q, total_cost, width, color=ORANGE, label="Total cost")
    ax.bar(q+width, net_benefit, width, color=TEAL, label="Net benefit")
    best = int(q[np.argmax(net_benefit)])
    ax.axvline(best, color=MUTED, linestyle=(0,(3,3)), linewidth=1)
    add_label(ax, best + .1, max(net_benefit) + 3, f"Best choice: Q = {best}", color=INK, weight="bold")
    ax.set_xlabel("Quantity of activity (Q)"); ax.set_ylabel("Cumulative value")
    ax.legend(frameon=False, ncol=3, loc="upper left")
    style_axes(ax); polish(fig, ax, "Source: Original illustrative model data.", "Synthetic cumulative values; the marginal rule identifies the same choice.")
    save(fig, 4, "Total benefit, total cost, and net benefit bars", "Original illustrative model data", "Synthetic cumulative values.")


def make_demand_supply():
    d = load_csv("illustrative/demand-supply.csv")
    fig, ax = figure("Market equilibrium", "The intersection identifies the market-clearing price and quantity.")
    ax.plot(d.quantity, d.demand_price, color=BLUE, linewidth=2.6, label="Demand")
    ax.plot(d.quantity, d.supply_price, color=ORANGE, linewidth=2.6, label="Supply")
    q = 53.333; p = 46.667
    mark_equilibrium(ax, q, p, "Q*", "P*", "Equilibrium")
    change_arrow(ax, (18, 82), (38, 62), "movement along D", color=BLUE, text_offset=(0, 6), connectionstyle="arc3,rad=-0.12")
    change_arrow(ax, (56, 48), (76, 58), "movement along S", color=ORANGE, text_offset=(0, -6), connectionstyle="arc3,rad=0.12")
    econ_axes(ax)
    ax.legend(frameon=False, loc="upper right"); polish(fig, ax, "Source: APMICRO illustrative data / demand-supply.csv.", "Synthetic linear market schedule.")
    save(fig, 5, "Market equilibrium chart", "APMICRO illustrative data / demand-supply.csv", "Synthetic linear market schedule.")


def make_elasticity():
    fig, ax = figure("Elasticity is visible in the slope of the response", "The same price movement produces different quantity responses on elastic and inelastic demand curves.")
    q = np.linspace(5, 95, 200)
    ax.plot(q, 100 - 0.45*q, color=BLUE, linewidth=2.4, label="More elastic")
    ax.plot(q, 100 - 1.25*q, color=ORANGE, linewidth=2.4, label="More inelastic")
    p1, p2 = 52, 68
    ax.vlines([q[0], q[-1]], 0, 0, alpha=0)
    ax.annotate("Same price change", xy=(35, p2), xytext=(51, p2+14), arrowprops=dict(arrowstyle="<->", color=MUTED), color=INK, ha="center")
    econ_axes(ax, "Quantity demanded (Q)", "Price (P)")
    ax.set_xlim(0, 100); ax.set_ylim(0, 100)
    ax.legend(frameon=False, loc="upper right"); polish(fig, ax, "Source: Original illustrative model data.", "Curves are stylized for comparison.")
    save(fig, 6, "Steep versus flat demand curves", "Original illustrative model data", "Stylized elasticity comparison.")


def make_total_revenue():
    d = load_csv("illustrative/elasticity-and-revenue.csv")
    fig, ax = figure("Total revenue across the demand curve", "Revenue rises, peaks at unit elasticity, then falls as the demand response becomes inelastic.")
    ax.plot(d.quantity, d.revenue, color=BLUE, linewidth=2.6)
    peak = d.loc[d.revenue.idxmax()]
    ax.scatter([peak.quantity], [peak.revenue], color=ORANGE, s=48, zorder=3)
    add_label(ax, peak.quantity + 2, peak.revenue + 80, "Unit-elastic midpoint", color=ORANGE, weight="bold")
    ax.set_xlabel("Quantity sold"); ax.set_ylabel("Total revenue")
    style_axes(ax); polish(fig, ax, "Source: APMICRO illustrative data / elasticity-and-revenue.csv.", "Synthetic demand schedule.")
    save(fig, 7, "Total-revenue curve", "APMICRO illustrative data / elasticity-and-revenue.csv", "Synthetic demand schedule.")


def make_income_ladder():
    fig, ax = figure("Income elasticity places goods on a response ladder", "Positive, near-zero, and negative income elasticities describe different demand responses.")
    names = ["Inferior", "Necessity", "Normal", "Luxury"]
    vals = [-0.5, 0.1, 0.8, 1.7]
    colors = [RED, GOLD, TEAL, BLUE]
    y = np.arange(len(names))
    ax.barh(y, vals, color=colors, height=.55)
    ax.axvline(0, color=INK, linewidth=.9)
    ax.set_yticks(y, names); ax.set_xlabel("Illustrative income elasticity")
    for i,v in enumerate(vals): ax.text(v + (0.06 if v >= 0 else -0.06), i, f"{v:+.1f}", va="center", ha="left" if v >= 0 else "right", fontweight="bold")
    style_axes(ax); polish(fig, ax, "Source: Original illustrative model data.", "Synthetic taxonomy; values are not estimates for a specific product.")
    save(fig, 7, "Income elasticity product ladder", "Original illustrative model data", "Synthetic taxonomy.")


def make_surplus():
    fig, ax = figure("Consumer surplus and producer surplus", "The equilibrium divides gains from exchange between buyers and sellers.")
    q = np.linspace(0, 100, 301); demand = 100-q; supply=20+.5*q; qe=53.333; pe=46.667
    ax.fill_between(q[q<=qe], pe, demand[q<=qe], color=PALE_BLUE, label="Consumer surplus")
    ax.fill_between(q[q<=qe], supply[q<=qe], pe, color=PALE_ORANGE, label="Producer surplus")
    ax.plot(q, demand, color=BLUE, linewidth=2.3, label="Demand"); ax.plot(q, supply, color=ORANGE, linewidth=2.3, label="Supply")
    mark_equilibrium(ax, qe, pe, "Q*", "P*", "Equilibrium")
    add_label(ax, 17, 78, "CS", color=BLUE, weight="bold"); add_label(ax, 16, 31, "PS", color=ORANGE, weight="bold")
    econ_axes(ax); ax.legend(frameon=False, ncol=2, loc="upper right")
    polish(fig, ax, "Source: APMICRO illustrative data / surplus-and-intervention.csv.", "Synthetic linear market schedule.")
    save(fig, 8, "Consumer and producer surplus graph", "APMICRO illustrative data / surplus-and-intervention.csv", "Synthetic linear market schedule.")


def make_shortage_surplus():
    fig, axs = plt.subplots(1,2,figsize=(8.6,4.3), constrained_layout=False)
    fig.suptitle("Disequilibrium creates a shortage or a surplus", x=.08, y=.965, ha="left", fontsize=14, fontweight="bold", color=INK)
    q=np.linspace(0,100,301); demand=100-q; supply=20+.5*q; qe=53.333; pe=46.667
    for ax, price, label, color, qd, qs in [(axs[0],35,"Shortage",RED,65,30),(axs[1],65,"Surplus",TEAL,35,90)]:
        ax.plot(q,demand,color=BLUE,linewidth=2.2,label="Demand"); ax.plot(q,supply,color=ORANGE,linewidth=2.2,label="Supply"); ax.axhline(price,color=color,linewidth=1.8)
        ax.set_xlim(0,100); ax.set_ylim(0,105)
        ax.scatter([qd,qs],[price,price],color=[BLUE,ORANGE],s=30,zorder=4)
        project_x(ax, qd, "Q_D", price, color=BLUE); project_x(ax, qs, "Q_S", price, color=ORANGE); project_y(ax, price, "P_c" if label == "Shortage" else "P_f", max(qd, qs), color=color)
        if label == "Shortage":
            change_arrow(ax, (qs, price - 7), (qd, price - 7), "shortage: Q_D − Q_S", color=RED, bidirectional=True, text_offset=(0, -1))
        else:
            change_arrow(ax, (qd, price + 7), (qs, price + 7), "surplus: Q_S − Q_D", color=TEAL, bidirectional=True, text_offset=(0, 1))
        ax.set_title(label,loc="left",fontsize=10.5,fontweight="bold"); econ_axes(ax)
        ax.text((qd+qs)/2, price+5, f"Gap = {abs(qs-qd)}", ha="center", color=color, fontweight="bold")
    axs[0].legend(frameon=False, fontsize=8, loc="upper right")
    polish(fig, axs, "Source: APMICRO illustrative data / surplus-and-intervention.csv.", "Synthetic price-control examples.")
    save(fig, 9, "Shortage and surplus side-by-side", "APMICRO illustrative data / surplus-and-intervention.csv", "Synthetic price-control examples.")


def make_policy_grid():
    fig, axs = plt.subplots(2,2,figsize=(8,6), constrained_layout=False)
    fig.suptitle("Four common government interventions", x=.08, y=.97, ha="left", fontsize=14, fontweight="bold", color=INK)
    # Use near-unit-elastic illustrative schedules so the policy effects occupy
    # readable vertical and horizontal space without making the curves flat.
    q=np.linspace(0,80,301); demand=100-1.20*q; supply=10+1.00*q
    items=[("Price ceiling",38,RED), ("Price floor",62,TEAL), ("Per-unit tax",12,ORANGE), ("Subsidy",12,PURPLE)]
    for ax,(label,policy,color) in zip(axs.flat,items):
        ax.set_xlim(0,80); ax.set_ylim(0,105)
        if label == "Per-unit tax":
            ax.plot(q,demand,color=BLUE,linewidth=1.9,label="D"); ax.plot(q,supply,color=ORANGE,linewidth=1.9,label="S"); ax.plot(q,supply+policy,color=RED,linewidth=1.9,label="S + tax");
            q_tax = (100 - 10 - policy) / (1.20 + 1.00)
            p_buyer = 100 - 1.20*q_tax; p_seller = 10 + 1.00*q_tax
            ax.vlines(q_tax, p_seller, p_buyer, color=color, linewidth=3.0, alpha=.6); project_x(ax, q_tax, "Q_tax", p_buyer, color=color, label_offset=2.0); project_y(ax, p_buyer, "P_b", q_tax, color=BLUE, label_y_offset=0.7); project_y(ax, p_seller, "P_s", q_tax, color=ORANGE, label_offset=1.5, label_y_offset=-0.7)
            change_arrow(ax, (q_tax + 5, p_seller), (q_tax + 5, p_buyer), "tax wedge", color=color, bidirectional=True, text_offset=(18, 6))
            change_arrow(ax, (q_tax, 22), (q_tax - 10, 22), "Q ↓", color=RED, text_offset=(0, -5))
        elif label == "Subsidy":
            ax.plot(q,demand,color=BLUE,linewidth=1.9,label="D"); ax.plot(q,supply,color=ORANGE,linewidth=1.9,label="S"); ax.plot(q,supply-policy,color=PURPLE,linewidth=1.9,label="S − subsidy");
            q_sub = (100 - 10 + policy) / (1.20 + 1.00)
            p_buyer = 100 - 1.20*q_sub; p_seller = 10 + 1.00*q_sub
            ax.vlines(q_sub, p_buyer, p_seller, color=color, linewidth=3.0, alpha=.6); project_x(ax, q_sub, "Q_sub", p_seller, color=color, label_offset=2.0); project_y(ax, p_buyer, "P_b", q_sub, color=BLUE, label_y_offset=-0.7); project_y(ax, p_seller, "P_s", q_sub, color=ORANGE, label_offset=1.5, label_y_offset=0.7)
            change_arrow(ax, (q_sub + 5, p_buyer), (q_sub + 5, p_seller), "subsidy wedge", color=color, bidirectional=True, text_offset=(20, 8))
            change_arrow(ax, (q_sub, 22), (q_sub + 10, 22), "Q ↑", color=PURPLE, text_offset=(0, -5))
        else:
            ax.plot(q,demand,color=BLUE,linewidth=1.9,label="D"); ax.plot(q,supply,color=ORANGE,linewidth=1.9,label="S"); ax.axhline(policy,color=color,linewidth=1.8,label="Policy price")
            qd = (100-policy)/1.20; qs = (policy-10)/1.00
            project_x(ax, qd, "Q_D", policy, color=BLUE); project_x(ax, qs, "Q_S", policy, color=ORANGE); project_y(ax, policy, "P_c" if label == "Price ceiling" else "P_f", max(qd, qs), color=color)
            p_eq = (1.00 * 100.0 + 1.20 * 10.0) / (1.20 + 1.00)
            if label == "Price ceiling":
                change_arrow(ax, (66, p_eq), (66, policy), "P ↓", color=RED, text_offset=(8, 0))
                change_arrow(ax, (qs, policy - 7), (qd, policy - 7), color=RED, bidirectional=True)
                add_label(ax, (qs + qd) / 2, policy - 16, "Q_D > Q_S", color=RED, ha="center", va="center", size=8.5, weight="bold")
            else:
                change_arrow(ax, (66, p_eq), (66, policy), "P ↑", color=TEAL, text_offset=(8, 0))
                change_arrow(ax, (qd, policy + 7), (qs, policy + 7), color=TEAL, bidirectional=True)
                add_label(ax, (qd + qs) / 2, policy + 16, "Q_S > Q_D", color=TEAL, ha="center", va="center", size=8.5, weight="bold")
        ax.set_title(label,loc="left",fontsize=10,fontweight="bold"); econ_axes(ax)
    axs[0,0].legend(frameon=False, fontsize=8, ncol=2, loc="upper right")
    polish(fig, axs, "Source: APMICRO illustrative data / surplus-and-intervention.csv.", "Schematic comparison; policy lines are illustrative.")
    save(fig, 10, "Price ceiling, price floor, tax, and subsidy grid", "APMICRO illustrative data / surplus-and-intervention.csv", "Schematic comparison.")


def make_tariff():
    d=load_csv("illustrative/tariff.csv"); fig,ax=figure("Tariff wedge and the gains from trade", "A tariff raises the domestic price, reduces imports, and creates deadweight loss.")
    ax.plot(d.quantity,d.domestic_demand_price,color=BLUE,linewidth=2.3,label="Domestic demand"); ax.plot(d.quantity,d.domestic_supply_price,color=ORANGE,linewidth=2.3,label="Domestic supply")
    ax.axhline(40,color=TEAL,linewidth=2,label=r"World price, $P_W$"); ax.axhline(55,color=RED,linewidth=2,label=r"Tariff price, $P_T$")
    ax.fill_between([30,50],40,55,color=PALE_ORANGE,alpha=.7,label="Tariff wedge")
    qd_w, qs_w, qd_t, qs_t = 60, 40, 45, 30
    project_x(ax, qd_w, "Q_D^W", 40, color=TEAL, label_offset=1.2); project_x(ax, qs_w, "Q_S^W", 40, color=TEAL, label_offset=0.2); project_x(ax, qd_t, "Q_D^T", 55, color=RED, label_offset=1.2); project_x(ax, qs_t, "Q_S^T", 55, color=RED, label_offset=0.2); project_y(ax, 40, "P_W", qd_w, color=TEAL); project_y(ax, 55, "P_T", qd_t, color=RED)
    change_arrow(ax, (72, 40), (72, 55), "P ↑", color=RED, text_offset=(8, 0))
    change_arrow(ax, (qd_w, 32), (qd_t, 32), "Q_D ↓", color=RED, text_offset=(0, -4))
    change_arrow(ax, (qs_w, 24), (qs_t, 24), "Q_S ↓", color=RED, text_offset=(0, -4))
    econ_axes(ax); ax.legend(frameon=False,fontsize=8,ncol=2,loc="upper right"); polish(fig,ax,"Source: APMICRO illustrative data / tariff.csv.","Synthetic international-trade schedule.")
    save(fig,11,"Tariff graph with world price","APMICRO illustrative data / tariff.csv","Synthetic international-trade schedule.")


def make_trade_map():
    fig,ax=figure("Trade connects specialized producers", "A schematic route map keeps the price and quantity arrows visible before students add the graph.",figsize=(7.5,4.5))
    ax.set_xlim(0,10); ax.set_ylim(0,6); ax.axis("off")
    for x, label, sub, color in [(1.5,"Exporter","Lower opportunity cost",TEAL),(8.5,"Importer","Higher opportunity cost",BLUE)]:
        ax.add_patch(Rectangle((x-1.35,2.1),2.7,1.8,facecolor="white",edgecolor=color,linewidth=2))
        ax.text(x,3.15,label,ha="center",fontsize=12,fontweight="bold"); ax.text(x,2.65,sub,ha="center",fontsize=8.5,color=MUTED)
    ax.add_patch(FancyArrowPatch((2.9,3.3),(7.1,3.3),arrowstyle="-|>",mutation_scale=17,linewidth=2.4,color=TEAL)); ax.text(5,3.55,"Goods flow",ha="center",color=TEAL,fontweight="bold")
    ax.add_patch(FancyArrowPatch((7.1,2.7),(2.9,2.7),arrowstyle="-|>",mutation_scale=17,linewidth=2.4,color=GOLD)); ax.text(5,2.45,"Payment flow",ha="center",color=INK,fontweight="bold")
    polish(fig,[],"Source: Original illustrative model diagram.","Schematic trade-route visual; no geographic claims.")
    save(fig,11,"Trade route map","Original illustrative model diagram","Schematic trade-route visual.")


def make_production():
    d=load_csv("illustrative/production-function.csv"); fig,ax=figure("Total, average, and marginal product", "Diminishing marginal product appears after the turning point in the production process.")
    ax.plot(d.labor,d.total_product,color=BLUE,linewidth=2.5,marker="o",markersize=3.5,label="Total product")
    ax.plot(d.labor,d.average_product,color=TEAL,linewidth=2.2,marker="s",markersize=3.5,label="Average product")
    ax.plot(d.labor,d.marginal_product,color=ORANGE,linewidth=2.2,marker="^",markersize=3.5,label="Marginal product")
    ax.set_xlabel("Labor input (L)"); ax.set_ylabel("Product units (Q)"); ax.legend(frameon=False,ncol=3,fontsize=8,loc="upper left"); polish(fig,ax,"Source: APMICRO illustrative data / production-function.csv.","Synthetic production table.")
    save(fig,12,"TP, AP, and MP curves","APMICRO illustrative data / production-function.csv","Synthetic production table.")


def make_production_heatmap():
    d=load_csv("illustrative/production-function.csv"); matrix=np.vstack([d.total_product, d.average_product.fillna(0), d.marginal_product.fillna(0)])
    fig,ax=figure("Reading a production table as a heatmap", "The color bands make the stages of production easier to scan before calculating.")
    im=ax.imshow(matrix,aspect="auto",cmap="YlGnBu"); ax.set_yticks(range(3),["Total product","Average product","Marginal product"]); ax.set_xticks(range(len(d)),d.labor); ax.set_xlabel("Labor input")
    threshold = matrix.max() * 0.58
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            text_color = "white" if matrix[i, j] >= threshold else INK
            ax.text(j, i, f"{matrix[i,j]:.0f}", ha="center", va="center", fontsize=8, color=text_color)
    ax.grid(False); polish(fig,ax,"Source: APMICRO illustrative data / production-function.csv.","Synthetic production table.")
    save(fig,12,"Production-table heatmap","APMICRO illustrative data / production-function.csv","Synthetic production table.")


def make_costs():
    d=load_csv("illustrative/cost-curves.csv"); fig,ax=figure("Short-run cost curves", "Average and marginal costs describe how the firm's cost structure changes with output.")
    for col,color,label in [("fixed_cost",MUTED,"FC"),("variable_cost",SKY,"VC"),("total_cost",INK,"TC"),("atc",BLUE,"ATC"),("avc",TEAL,"AVC"),("marginal_cost",ORANGE,"MC")]: ax.plot(d.quantity,d[col],linewidth=2 if col in ["atc","avc","marginal_cost"] else 1.5,color=color,label=label)
    ax.set_xlabel("Output (Q)"); ax.set_ylabel("Cost ($)"); ax.legend(frameon=False,ncol=3,fontsize=8,loc="upper left"); polish(fig,ax,"Source: APMICRO illustrative data / cost-curves.csv.","Synthetic short-run cost schedule.")
    save(fig,13,"FC, VC, TC, ATC, AVC, and MC curves","APMICRO illustrative data / cost-curves.csv","Synthetic short-run cost schedule.")


def make_lratc():
    d=load_csv("illustrative/lratc.csv"); fig,ax=figure("Long-run average total cost", "Scale economies lower average cost until the efficient scale, after which diseconomies appear.")
    ax.plot(d.output,d.lratc,color=BLUE,linewidth=2.7); i=d.lratc.idxmin(); ax.scatter([d.output[i]],[d.lratc[i]],color=ORANGE,s=50); add_label(ax,d.output[i]+2,d.lratc[i]+2,"Minimum efficient scale",color=ORANGE,weight="bold")
    ax.axvspan(1,d.output[i],color=PALE_TEAL,alpha=.35); ax.axvspan(d.output[i],50,color=PALE_ORANGE,alpha=.25); ax.set_xlabel("Output (Q)"); ax.set_ylabel("Long-run average total cost ($)")
    polish(fig,ax,"Source: APMICRO illustrative data / lratc.csv.","Synthetic long-run cost curve.")
    save(fig,14,"LRATC economies-of-scale curve","APMICRO illustrative data / lratc.csv","Synthetic long-run cost curve.")


def make_profit_max():
    d=load_csv("illustrative/monopoly.csv"); fig,ax=figure("Profit maximization occurs where marginal revenue meets marginal cost", "The firm chooses output first, then reads price from the demand curve.")
    ax.plot(d.quantity,d.price,color=BLUE,linewidth=2.3,label="Demand / price"); ax.plot(d.quantity,d.mr,color=PURPLE,linewidth=2.3,label="MR"); ax.plot(d.quantity,d.mc,color=ORANGE,linewidth=2.3,label="MC")
    idx=np.argmin(np.abs(d.mr-d.mc)); q=d.quantity.iloc[idx]; p=d.price.iloc[idx]; atc=d.atc.iloc[idx]
    ax.set_xlim(0, 50); ax.set_ylim(0, 105); mark_equilibrium(ax, q, p, "Q*", "P*", f"Q* = {q:.0f}; P* = {p:.0f}"); project_y(ax, atc, "ATC*", q, color=TEAL); ax.plot([q,q],[atc,p],color=TEAL,linewidth=6,alpha=.3)
    econ_axes(ax, "Output (Q)", "Price / cost ($)"); ax.legend(frameon=False,ncol=3,fontsize=8,loc="upper right"); polish(fig,ax,"Source: APMICRO illustrative data / monopoly.csv.","Synthetic MR-MC schedule.")
    save(fig,15,"MR, MC, and profit-maximizing output","APMICRO illustrative data / monopoly.csv","Synthetic MR-MC schedule.")


def make_firm_dashboard():
    fig,axs=plt.subplots(2,2,figsize=(7.5,5.6),constrained_layout=False); fig.suptitle("Firm decision dashboard",x=.08,y=.97,ha="left",fontsize=14,fontweight="bold",color=INK)
    labels=["Output","Price","Average cost","Profit per unit"]; vals=[24,76,51,25]; colors=[BLUE,TEAL,ORANGE,GOLD]
    for ax,label,val,color in zip(axs.flat,labels,vals,colors):
        ax.bar([0],[val],color=color,width=.55); ax.set_title(label,loc="left",fontsize=10.5,fontweight="bold"); ax.set_xticks([]); ax.set_ylim(0,100); ax.text(0,val+5,str(val),ha="center",fontweight="bold",fontsize=14); style_axes(ax)
    polish(fig,axs,"Source: APMICRO illustrative data / monopoly.csv.","Illustrative firm snapshot; values are synthetic.")
    save(fig,15,"Firm decision dashboard","APMICRO illustrative data / monopoly.csv","Illustrative firm snapshot.")


def make_shutdown():
    d=load_csv("illustrative/cost-curves.csv"); fig,ax=figure("Produce in the short run only when price covers AVC", "The shutdown rule compares price with average variable cost; the exit rule belongs to the long run.")
    ax.plot(d.quantity,d.marginal_cost,color=ORANGE,linewidth=2.4,label="MC"); ax.plot(d.quantity,d.avc,color=TEAL,linewidth=2.4,label="AVC"); ax.plot(d.quantity,d.atc,color=BLUE,linewidth=2.4,label="ATC"); ax.axhline(38,color=INK,linewidth=1.8,label="Market price")
    ax.fill_between(d.quantity,38,d.avc,where=d.avc<38,color=PALE_TEAL,alpha=.6); ax.fill_between(d.quantity,0,d.avc,where=d.avc>38,color=PALE_ORANGE,alpha=.5)
    q_star = 10; project_x(ax, q_star, "Q*", 38, color=INK); project_y(ax, 38, "P", q_star, color=INK)
    add_label(ax,5,41,"Produce if P ≥ AVC",color=TEAL,weight="bold"); add_label(ax,14,20,"Shutdown region",color=RED,weight="bold")
    econ_axes(ax, "Output (Q)", "Cost / price ($)"); ax.legend(frameon=False,ncol=4,fontsize=8,loc="upper left"); polish(fig,ax,"Source: APMICRO illustrative data / cost-curves.csv.","Synthetic short-run shutdown illustration.")
    save(fig,16,"Shutdown decision graph","APMICRO illustrative data / cost-curves.csv","Synthetic short-run shutdown illustration.")


def make_market_firm():
    fig,axs=plt.subplots(1,2,figsize=(8.6,4.2),constrained_layout=False); fig.suptitle("Industry equilibrium and the representative firm",x=.08,y=.965,ha="left",fontsize=14,fontweight="bold",color=INK)
    draw_market(axs[0],lambda q:100-q,lambda q:20+.5*q,"Industry",xlim=(0,100),ylim=(0,105),equilibrium=True)
    q=np.linspace(0,100,200); axs[1].axhline(47,color=BLUE,linewidth=2.4,label="D = MR = P"); axs[1].plot(q,20+.5*q,color=ORANGE,linewidth=2.4,label="MC"); axs[1].set_title("Representative firm",loc="left",fontsize=10.5,fontweight="bold"); axs[1].set_xlim(0,100); axs[1].set_ylim(0,105); project_x(axs[1], 54, "Q*", 47, color=INK); project_y(axs[1], 47, "P*", 54, color=INK); change_arrow(axs[1], (30, 47), (54, 47), "Q ↑ to Q*", color=BLUE, text_offset=(0, 7)); econ_axes(axs[1], "Firm output (q)", "Price / cost ($)"); axs[1].legend(frameon=False,fontsize=8)
    polish(fig,axs,"Source: APMICRO illustrative model data.","Schematic perfect-competition comparison.")
    save(fig,17,"Market-versus-firm two-panel graph","Original illustrative model data","Schematic perfect-competition comparison.")


def make_concentration():
    fig,ax=figure("Market concentration is a structural clue", "A four-firm concentration ratio summarizes how much market share is held by the largest firms.")
    sectors=["Local farms","Restaurants","Airlines","Telecom","Utilities"]; cr4=[12,24,62,78,95]
    ax.barh(sectors,cr4,color=[TEAL,TEAL,BLUE,PURPLE,ORANGE]); ax.set_xlim(0,100); ax.set_xlabel("CR4: share held by four largest firms (%)")
    for y,v in enumerate(cr4): ax.text(v+2,y,f"{v}%",va="center",fontweight="bold")
    style_axes(ax); polish(fig,ax,"Source: Original illustrative model data.","Synthetic industry examples; not measured market shares.")
    save(fig,18,"Concentration ratio bar chart","Original illustrative model data","Synthetic industry examples.")


def make_monopoly():
    d=load_csv("illustrative/monopoly.csv"); fig,ax=figure("Monopoly output, price, and deadweight loss", "A monopoly restricts output relative to the competitive benchmark in this stylized model.")
    ax.plot(d.quantity,d.price,color=BLUE,linewidth=2.4,label="Demand"); ax.plot(d.quantity,d.mr,color=PURPLE,linewidth=2.4,label="MR"); ax.plot(d.quantity,d.mc,color=ORANGE,linewidth=2.4,label="MC"); ax.plot(d.quantity,d.atc,color=TEAL,linewidth=2.1,label="ATC")
    idx=np.argmin(np.abs(d.mr-d.mc)); q=float(d.quantity.iloc[idx]); p=float(d.price.iloc[idx]);
    q_comp=float(d.quantity.iloc[np.argmin(np.abs(d.price-d.mc))]); p_comp=float(d.price.iloc[np.argmin(np.abs(d.price-d.mc))])
    ax.set_xlim(0, 50); ax.set_ylim(0, 105); mark_equilibrium(ax, q, p, "Q_M", "P_M", "Monopoly choice"); project_x(ax, q_comp, "Q_C", p_comp, color=TEAL); project_y(ax, p_comp, "P_C", q_comp, color=TEAL); change_arrow(ax, (q_comp, 17), (q, 17), "Q_M < Q_C", color=RED, bidirectional=True, text_offset=(0, -4)); econ_axes(ax, "Output (Q)", "Price / cost ($)"); ax.legend(frameon=False,ncol=4,fontsize=8,loc="upper right"); polish(fig,ax,"Source: APMICRO illustrative data / monopoly.csv.","Synthetic monopoly model.")
    save(fig,19,"Monopoly D-MR-MC-ATC graph","APMICRO illustrative data / monopoly.csv","Synthetic monopoly model.")


def make_price_discrimination():
    fig,ax=figure("Price discrimination separates consumer segments", "Different demand segments can face different prices when resale is limited and market power is present.")
    q=np.linspace(0,40,200); ax.plot(q,90-1.5*q,color=BLUE,linewidth=2.5,label="Segment A"); ax.plot(q,65-.8*q,color=ORANGE,linewidth=2.5,label="Segment B"); ax.axhline(45,color=TEAL,linewidth=1.8,label="Uniform price")
    ax.scatter([20,25],[60,45],color=[BLUE,ORANGE],s=42); add_label(ax,20,64,"Higher willingness to pay",color=BLUE,weight="bold"); add_label(ax,25,39,"Lower segment price",color=ORANGE,weight="bold")
    econ_axes(ax, "Quantity in segment (Q)", "Price (P)"); ax.legend(frameon=False,ncol=3,fontsize=8,loc="upper right"); polish(fig,ax,"Source: Original illustrative model data.","Stylized segment-demand example.")
    save(fig,20,"Segmented-price graph","Original illustrative model data","Stylized segment-demand example.")


def make_mono_comp():
    fig,axs=plt.subplots(1,2,figsize=(8.6,4.2),constrained_layout=False); fig.suptitle("Monopolistic competition adjusts through entry and exit",x=.08,y=.965,ha="left",fontsize=14,fontweight="bold",color=INK)
    q=np.linspace(0,80,200)
    for ax,shift,label in [(axs[0],0,"Short run: economic profit"),(axs[1],18,"Long run: zero economic profit")]:
        demand=100-shift-0.9*q; mr=100-shift-1.8*q; mc=18+0.55*q; atc=62-0.25*q+0.006*q*q
        ax.plot(q,demand,color=BLUE,linewidth=2.2,label="D"); ax.plot(q,mr,color=PURPLE,linewidth=2.2,label="MR"); ax.plot(q,mc,color=ORANGE,linewidth=2.2,label="MC"); ax.plot(q,atc,color=TEAL,linewidth=2.2,label="ATC"); ax.set_title(label,loc="left",fontsize=10.5,fontweight="bold"); ax.set_xlim(0,80); ax.set_ylim(0,105); econ_axes(ax, "Output (Q)", "Price / cost ($)")
    change_arrow(axs[0], (56, 50), (36, 50), "entry shifts D left", color=PURPLE, text_offset=(0, 7), connectionstyle="arc3,rad=0.12")
    change_arrow(axs[1], (36, 32), (36, 50), "P ↓", color=PURPLE, text_offset=(7, 0))
    axs[0].legend(frameon=False,fontsize=8,ncol=4,loc="upper right")
    polish(fig,axs,"Source: Original illustrative model data.","Stylized monopolistic-competition comparison.")
    save(fig,21,"Short-run versus long-run monopolistic competition","Original illustrative model data","Stylized comparison.")


def make_payoff():
    d=load_csv("illustrative/oligopoly-payoffs.csv"); matrix=d.pivot(index="strategy_a",columns="strategy_b",values="payoff_a").loc[["Cooperate","Defect"],["Cooperate","Defect"]].values
    fig,ax=figure("Payoff matrix: strategic interdependence", "Each player's payoff depends on both firms' choices.")
    im=ax.imshow(matrix,cmap=LinearSegmentedColormap.from_list("pay",[PALE_ORANGE, GOLD, PALE_TEAL]),vmin=0,vmax=10); ax.set_xticks([0,1],["Cooperate","Defect"]); ax.set_yticks([0,1],["Cooperate","Defect"]); ax.set_xlabel("Firm B"); ax.set_ylabel("Firm A")
    for i in range(2):
        for j in range(2):
            pair=d[(d.strategy_a==["Cooperate","Defect"][i])&(d.strategy_b==["Cooperate","Defect"][j])].iloc[0]; ax.text(j,i,f"{pair.payoff_a:.0f}, {pair.payoff_b:.0f}",ha="center",va="center",fontweight="bold")
    ax.grid(False); polish(fig,ax,"Source: APMICRO illustrative data / oligopoly-payoffs.csv.","Cells show Firm A payoff, Firm B payoff.")
    save(fig,22,"Payoff matrix heatmap","APMICRO illustrative data / oligopoly-payoffs.csv","Cells show Firm A payoff, Firm B payoff.")


def make_efficiency_comparison():
    fig,axs=plt.subplots(1,2,figsize=(8.6,4.2),constrained_layout=False); fig.suptitle("Market structures differ in price, output, and efficiency",x=.08,y=.965,ha="left",fontsize=14,fontweight="bold",color=INK)
    names=["Perfect competition","Monopolistic competition","Oligopoly","Monopoly"]; price=[38,48,58,72]; output=[92,76,65,48]; dwl=[0,8,14,26]
    axs[0].bar(names,price,color=[TEAL,BLUE,PURPLE,ORANGE]); axs[0].set_ylabel("Relative price"); axs[0].tick_params(axis="x",rotation=25); style_axes(axs[0])
    axs[1].bar(names,output,color=[TEAL,BLUE,PURPLE,ORANGE],label="Output"); axs[1].plot(names,dwl,color=RED,marker="o",linewidth=2.2,label="Relative DWL"); axs[1].set_ylabel("Relative output / loss"); axs[1].tick_params(axis="x",rotation=25); axs[1].legend(frameon=False); style_axes(axs[1])
    polish(fig,axs,"Source: Original illustrative model data.","Relative comparison; values are synthetic.")
    save(fig,23,"Efficiency comparison bars","Original illustrative model data","Relative comparison.")


def make_market_dashboard():
    fig,axs=plt.subplots(2,2,figsize=(7.6,5.6),constrained_layout=False); fig.suptitle("Four market structures at a glance",x=.08,y=.97,ha="left",fontsize=14,fontweight="bold",color=INK)
    names=["Perfect competition","Monopolistic competition","Oligopoly","Monopoly"]; data={"Firms":[5,4,2,1],"Product differentiation":[1,4,5,3],"Price power":[1,3,4,5],"Entry barriers":[1,2,4,5]}
    for ax,(label,vals) in zip(axs.flat,data.items()): ax.bar(names,vals,color=[TEAL,BLUE,PURPLE,ORANGE]); ax.set_title(label,loc="left",fontsize=10.5,fontweight="bold"); ax.set_ylim(0,5.5); ax.tick_params(axis="x",rotation=25); style_axes(ax)
    polish(fig,axs,"Source: Original illustrative model data.","Ordinal teaching comparison; values are synthetic.")
    save(fig,23,"Four-market-structure dashboard","Original illustrative model data","Ordinal teaching comparison.")


def make_mrp():
    d=load_csv("illustrative/factor-market.csv"); fig,ax=figure("Derived demand for labor: hire until MRP equals factor price", "The marginal revenue product curve links product-market conditions to input demand.")
    ax.plot(d.labor,d.mrp,color=BLUE,linewidth=2.5,label="MRP"); ax.axhline(40,color=ORANGE,linewidth=2.1,label="Factor price"); q=20; ax.set_xlim(0,30); ax.set_ylim(0,105); project_x(ax,q,"L*",40,color=INK); project_y(ax,40,"W",q,color=ORANGE); ax.scatter([q],[40],color=INK,s=42); add_label(ax,q+1,44,"Employment choice",weight="bold")
    econ_axes(ax, "Quantity of labor (L)", "Wage / MRP ($)"); ax.legend(frameon=False,loc="upper right"); polish(fig,ax,"Source: APMICRO illustrative data / factor-market.csv.","Synthetic factor-demand schedule.")
    save(fig,24,"MRP schedule chart","APMICRO illustrative data / factor-market.csv","Synthetic factor-demand schedule.")


def make_factor_shift():
    fig,ax=figure("Factor demand shifts with productivity and product price", "A rightward shift can come from stronger product demand, higher product price, or higher worker productivity.")
    q=np.linspace(0,80,200); ax.plot(q,90-q,color=BLUE,linewidth=2.4,label="Initial MRP"); ax.plot(q,110-q,color=TEAL,linewidth=2.4,label="Higher productivity / product price"); ax.axhline(40,color=ORANGE,linewidth=1.8,label="Factor price")
    q1=(90-40); q2=(110-40); ax.set_xlim(0,80); ax.set_ylim(0,110); project_x(ax,q1,"L₁",40,color=BLUE); project_x(ax,q2,"L₂",40,color=TEAL); project_y(ax,40,"W",q2,color=ORANGE); econ_axes(ax,"Quantity of labor (L)","Wage / MRP ($)"); ax.legend(frameon=False,fontsize=8,ncol=3,loc="upper right"); polish(fig,ax,"Source: Original illustrative model data.","Stylized factor-demand shift.")
    change_arrow(ax, (24, 66), (44, 66), "MRP shifts right", color=TEAL, text_offset=(0, 7), connectionstyle="arc3,rad=-0.12")
    change_arrow(ax, (q1, 34), (q2, 34), "L ↑", color=TEAL, bidirectional=True, text_offset=(0, -4))
    save(fig,25,"Factor-market shift chart","Original illustrative model data","Stylized factor-demand shift.")


def make_competitive_labor():
    d=load_csv("illustrative/factor-market.csv"); fig,ax=figure("Competitive labor-market equilibrium", "The market wage and employment level occur where labor demand meets labor supply.")
    q=np.linspace(0,30,200); demand=100-3*q; supply=20+q; ax.plot(q,demand,color=BLUE,linewidth=2.4,label="Labor demand"); ax.plot(q,supply,color=ORANGE,linewidth=2.4,label="Labor supply"); qe=20; we=40; ax.set_xlim(0,30); ax.set_ylim(0,105); mark_equilibrium(ax,qe,we,"L*","W*","Market equilibrium"); econ_axes(ax,"Quantity of labor (L)","Wage (W)"); ax.legend(frameon=False,loc="upper right"); polish(fig,ax,"Source: APMICRO illustrative data / factor-market.csv.","Synthetic labor-market schedule.")
    save(fig,26,"Competitive labor-market equilibrium","APMICRO illustrative data / factor-market.csv","Synthetic labor-market schedule.")


def make_monopsony():
    d=load_csv("illustrative/monopsony.csv"); fig,ax=figure("Monopsony chooses employment where MFC equals MRP", "The single dominant buyer faces an upward-sloping labor supply and a marginal factor cost above the wage.")
    ax.plot(d.labor,d.labor_supply_wage,color=TEAL,linewidth=2.3,label="Labor supply / wage"); ax.plot(d.labor,d.mfc,color=ORANGE,linewidth=2.3,label="MFC"); ax.plot(d.labor,d.mrp,color=BLUE,linewidth=2.3,label="MRP"); idx=np.argmin(np.abs(d.mfc-d.mrp)); q=d.labor.iloc[idx]; w=d.labor_supply_wage.iloc[idx]; ax.set_xlim(0,30); ax.set_ylim(0,105); mark_equilibrium(ax,q,w,"L_M","W_M","Monopsony choice"); econ_axes(ax,"Quantity of labor (L)","Wage / marginal value ($)"); ax.legend(frameon=False,fontsize=8,ncol=3,loc="upper right"); polish(fig,ax,"Source: APMICRO illustrative data / monopsony.csv.","Synthetic monopsony schedule.")
    save(fig,27,"Monopsony MFC-MRP graph","APMICRO illustrative data / monopsony.csv","Synthetic monopsony schedule.")


def make_externality():
    d=load_csv("illustrative/externalities.csv"); fig,ax=figure("Private and social costs can imply different quantities", "With a negative externality, social marginal cost lies above private marginal cost.")
    ax.plot(d.quantity,d.marginal_benefit,color=BLUE,linewidth=2.4,label="Marginal benefit"); ax.plot(d.quantity,d.private_marginal_cost,color=ORANGE,linewidth=2.4,label="Private MC"); ax.plot(d.quantity,d.social_marginal_cost,color=RED,linewidth=2.4,label="Social MC"); ax.fill_between(d.quantity,d.private_marginal_cost,d.social_marginal_cost,color=PALE_ORANGE,alpha=.65,label="External cost")
    q_market = 40; q_efficient = 35; p_market = 50; p_efficient = 55; ax.set_xlim(0,80); ax.set_ylim(0,105); project_x(ax,q_market,"Q_M",p_market,color=ORANGE); project_x(ax,q_efficient,"Q*",p_efficient,color=RED); project_y(ax,p_market,"P_M",q_market,color=ORANGE); project_y(ax,p_efficient,"P*",q_efficient,color=RED); econ_axes(ax,"Quantity (Q)","Benefit / cost ($)"); ax.legend(frameon=False,fontsize=8,ncol=3,loc="upper right"); polish(fig,ax,"Source: APMICRO illustrative data / externalities.csv.","Synthetic negative-externality schedule.")
    change_arrow(ax, (q_market, 18), (q_efficient, 18), "Q ↓ to efficient level", color=RED, text_offset=(0, -4))
    add_label(ax, 49, 73, "external cost", color=RED, weight="bold")
    save(fig,28,"Private versus social benefit/cost graph","APMICRO illustrative data / externalities.csv","Synthetic negative-externality schedule.")


def make_externality_pair():
    fig,axs=plt.subplots(1,2,figsize=(8.6,4.2),constrained_layout=False); fig.suptitle("Externalities can create overproduction or underproduction",x=.08,y=.965,ha="left",fontsize=14,fontweight="bold",color=INK)
    q=np.linspace(0,80,200); mb=90-q; pmc=10+q; smc_neg=22+q; smc_pos=-4+q
    for ax,title,smc,color in [(axs[0],"Negative externality",smc_neg,RED),(axs[1],"Positive externality",smc_pos,TEAL)]:
        ax.plot(q,mb,color=BLUE,linewidth=2.2,label="MB"); ax.plot(q,pmc,color=ORANGE,linewidth=2.2,label="Private MC"); ax.plot(q,smc,color=color,linewidth=2.2,label="Social MC / MB"); ax.set_title(title,loc="left",fontsize=10.5,fontweight="bold"); ax.set_ylim(0,100); econ_axes(ax,"Quantity (Q)","Benefit / cost ($)")
    change_arrow(axs[0], (42, 24), (34, 24), "Q ↓", color=RED, text_offset=(0, -4))
    change_arrow(axs[1], (36, 24), (44, 24), "Q ↑", color=TEAL, text_offset=(0, -4))
    axs[0].legend(frameon=False,fontsize=8,ncol=3,loc="upper right"); polish(fig,axs,"Source: Original illustrative model data.","Stylized comparison of market failure channels.")
    save(fig,29,"Negative and positive externality pair","Original illustrative model data","Stylized comparison.")


def make_free_rider():
    d=load_csv("illustrative/public-goods.csv"); fig,ax=figure("Free-rider incentives weaken voluntary contribution", "A public good can benefit people even when some individuals choose not to contribute.")
    ax.bar(d.person,d.marginal_benefit,color=[TEAL,BLUE,ORANGE]); ax.axhline(30,color=INK,linewidth=1.8,label="Marginal cost");
    for i,row in d.iterrows():
        if row.free_rider_flag: ax.text(i,row.marginal_benefit+2,"free rider",ha="center",fontsize=8,color=RED,fontweight="bold")
    ax.set_xlabel("Person"); ax.set_ylabel("Marginal benefit / cost"); ax.legend(frameon=False); style_axes(ax); polish(fig,ax,"Source: APMICRO illustrative data / public-goods.csv.","Synthetic classroom contribution model.")
    save(fig,30,"Free-rider participation chart","APMICRO illustrative data / public-goods.csv","Synthetic classroom contribution model.")


def make_policy_dashboard():
    fig,axs=plt.subplots(1,3,figsize=(8.8,3.7),constrained_layout=False); fig.suptitle("Policy tools change different margins",x=.08,y=.965,ha="left",fontsize=14,fontweight="bold",color=INK)
    names=["Ceiling","Floor","Tax","Subsidy"]; q=[35,70,44,64]; p=[35,65,55,38]
    axs[0].bar(names,q,color=[RED,TEAL,ORANGE,PURPLE]); axs[0].set_title("Quantity traded",loc="left",fontsize=10.5,fontweight="bold"); axs[0].set_ylabel("Relative quantity"); axs[0].tick_params(axis="x",rotation=30); style_axes(axs[0])
    axs[1].bar(names,p,color=[RED,TEAL,ORANGE,PURPLE]); axs[1].set_title("Policy price",loc="left",fontsize=10.5,fontweight="bold"); axs[1].set_ylabel("Relative price"); axs[1].tick_params(axis="x",rotation=30); style_axes(axs[1])
    axs[2].bar(["Consumer","Producer","Government"],[20,25,15],color=[BLUE,ORANGE,TEAL]); axs[2].set_title("Who is directly affected?",loc="left",fontsize=10.5,fontweight="bold"); axs[2].set_ylabel("Illustrative impact"); style_axes(axs[2])
    polish(fig,axs,"Source: Original illustrative model data.","Comparison is conceptual; magnitudes are synthetic.")
    save(fig,31,"Policy-tool comparison dashboard","Original illustrative model data","Conceptual comparison.")


def make_unemployment():
    d=load_csv("derived/unemployment-with-recessions.csv"); d.date=pd.to_datetime(d.date); fig,ax=figure("U.S. unemployment rate with recession shading", "Historical policy context and indicator extension; unemployment is not an AP Micro core unit.",figsize=(8.2,4.5))
    ax.plot(d.date,d.unemployment_rate,color=BLUE,linewidth=1.8); rec=d.recession.to_numpy(); dates=d.date.to_numpy(); in_rec=False; start=None
    for date,flag in zip(dates,rec):
        if flag and not in_rec: start=date; in_rec=True
        if in_rec and (not flag or date==dates[-1]):
            end=date; ax.axvspan(start,end,color=GRID,alpha=.55); in_rec=False
    ax.set_xlabel("Date"); ax.set_ylabel("Unemployment rate (%)"); style_axes(ax); polish(fig,ax,"Source: FRED UNRATE and USREC snapshots in local data manifest.","Gray bands mark NBER recession periods.")
    save(fig,31,"Great Depression unemployment-rate timeline","FRED UNRATE and USREC local snapshots","Gray bands mark NBER recession periods.")


def make_lorenz():
    fig,ax=figure("Lorenz curve and income inequality", "The farther the Lorenz curve lies below equality, the more unequal the distribution.")
    x=np.linspace(0,1,101); y=x**1.8; ax.plot(x,x,color=MUTED,linewidth=1.6,linestyle=(0,(4,3)),label="Line of equality"); ax.plot(x,y,color=BLUE,linewidth=2.6,label="Lorenz curve"); ax.fill_between(x,y,x,color=PALE_BLUE,alpha=.7); ax.set_xlabel("Cumulative share of households"); ax.set_ylabel("Cumulative share of income"); ax.set_xlim(0,1); ax.set_ylim(0,1); ax.set_xticks([0,.25,.5,.75,1],["0%","25%","50%","75%","100%"]); ax.set_yticks([0,.25,.5,.75,1],["0%","25%","50%","75%","100%"]); ax.legend(frameon=False,loc="upper left"); polish(fig,ax,"Source: Lorenz curve constructed from an illustrative distribution; FRED GINIALLRH is available for context.","Curve is synthetic and is not a fitted estimate.")
    save(fig,32,"Lorenz curve and Gini visual","Illustrative Lorenz curve; FRED GINIALLRH context","Curve is synthetic.")


def make_histogram():
    rng=np.random.default_rng(2026); incomes=np.exp(rng.normal(10.6,.55,1800))/1000
    fig,ax=figure("Income distributions are often right-skewed", "A histogram makes concentration and the long upper tail visible before introducing the Lorenz curve.")
    ax.hist(incomes,bins=34,color=BLUE,alpha=.82,edgecolor="white",linewidth=.4); ax.set_xlabel("Illustrative annual income ($ thousands)"); ax.set_ylabel("Household count"); style_axes(ax); polish(fig,ax,"Source: Original synthetic distribution.","Synthetic sample for classroom visualization; not survey data.")
    save(fig,32,"Income-distribution histogram","Original synthetic distribution","Synthetic sample; not survey data.")


def make_policy_evidence():
    d=load_csv("derived/policy-and-indicators-dashboard.csv"); d.month=pd.to_datetime(d.month.astype(str), format="mixed"); fig,axs=plt.subplots(3,1,figsize=(8.2,6.4),sharex=True,constrained_layout=False); fig.suptitle("Macro context dashboard for policy discussion",x=.08,y=.97,ha="left",fontsize=14,fontweight="bold",color=INK)
    panels=[("inflation_yoy_pct", "Inflation (%)", RED), ("unemployment_rate","Unemployment (%)", BLUE),("fedfunds_pct","Fed funds (%)",PURPLE)]
    for ax,(col,label,color) in zip(axs,panels): ax.plot(d.month,d[col],color=color,linewidth=1.6); ax.set_ylabel(label,fontsize=8.5); style_axes(ax)
    axs[-1].set_xlabel("Date"); polish(fig,axs,"Source: FRED CPIAUCSL, UNRATE, and FEDFUNDS snapshots joined in local dashboard.","Macro extension; not an AP Micro core market graph.")
    save(fig,33,"Policy evidence dashboard","FRED CPIAUCSL, UNRATE, FEDFUNDS local dashboard","Macro extension.")


def make_six_core():
    fig,axs=plt.subplots(2,3,figsize=(9,6.1),constrained_layout=False); fig.suptitle("Six core AP Micro graph templates",x=.08,y=.97,ha="left",fontsize=14,fontweight="bold",color=INK)
    q=np.linspace(0,100,100)
    panels=[("Demand / supply",lambda ax:(ax.plot(q,100-q,color=BLUE),ax.plot(q,20+.5*q,color=ORANGE))), ("PPC",lambda ax:ax.plot(q,100*np.sqrt(np.maximum(0,1-(q/100)**2)),color=BLUE)), ("Cost curves",lambda ax:(ax.plot(q,20+.6*q,color=ORANGE),ax.plot(q,60-0.4*q+0.006*q*q,color=BLUE))), ("Monopoly",lambda ax:(ax.plot(q,100-q,color=BLUE),ax.plot(q,100-2*q,color=PURPLE),ax.plot(q,20+.6*q,color=ORANGE))), ("Factor market",lambda ax:(ax.plot(q,100-0.7*q,color=BLUE),ax.plot(q,20+0.6*q,color=ORANGE))), ("Externality",lambda ax:(ax.plot(q,90-q,color=BLUE),ax.plot(q,10+q,color=ORANGE),ax.plot(q,24+q,color=RED)))]
    for ax,(title,fn) in zip(axs.flat,panels): fn(ax); ax.set_title(title,loc="left",fontsize=9.5,fontweight="bold"); ax.set_xticks([]); ax.set_yticks([]); ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False); ax.grid(False)
    polish(fig,axs,"Source: Original illustrative model graphs.","Template poster; labels should be added in the lesson-specific version.")
    save(fig,34,"Six-core-graphs poster","Original illustrative model graphs","Template poster.")


def make_timed_dashboard():
    fig,axs=plt.subplots(1,2,figsize=(8.4,4.1),constrained_layout=False); fig.suptitle("Timed-practice dashboard",x=.08,y=.965,ha="left",fontsize=14,fontweight="bold",color=INK)
    units=["U1","U2","U3","U4","U5","U6"]; accuracy=[.78,.71,.83,.65,.69,.76]; seconds=[52,61,48,72,66,58]
    axs[0].bar(units,accuracy,color=BLUE); axs[0].set_ylim(0,1); axs[0].set_title("Accuracy",loc="left",fontsize=10.5,fontweight="bold"); axs[0].set_ylabel("Share correct"); axs[0].yaxis.set_major_formatter(lambda x,pos:f"{x:.0%}"); style_axes(axs[0])
    axs[1].plot(units,seconds,color=ORANGE,marker="o",linewidth=2.4); axs[1].set_title("Median response time",loc="left",fontsize=10.5,fontweight="bold"); axs[1].set_ylabel("Seconds per question"); style_axes(axs[1])
    polish(fig,axs,"Source: Original synthetic practice log.","Template only; replace with anonymized student data.")
    save(fig,35,"Timed-practice dashboard","Original synthetic practice log","Template only.")


def make_error_heatmap():
    units=["U1","U2","U3","U4","U5","U6"]; errors=["Concept","Graph","Calculation","Reading","Expression"]; vals=np.array([[3,2,1,1,0],[4,5,2,2,1],[2,4,5,1,1],[5,3,2,4,2],[3,2,3,2,4],[2,3,2,1,3]])
    fig,ax=figure("Error-type heatmap", "A compact error profile helps decide which review activity should come next.")
    im=ax.imshow(vals,cmap=LinearSegmentedColormap.from_list("errors",["#EFF6FF",PALE_BLUE,ORANGE,RED]),aspect="auto"); ax.set_xticks(range(len(errors)),errors,rotation=20); ax.set_yticks(range(len(units)),units); ax.set_xlabel("Error type"); ax.set_ylabel("Unit")
    for i in range(vals.shape[0]):
        for j in range(vals.shape[1]): ax.text(j,i,str(vals[i,j]),ha="center",va="center",fontweight="bold")
    ax.grid(False); polish(fig,ax,"Source: Original synthetic practice log.","Template only; replace with anonymized student data.")
    save(fig,35,"Error-type heatmap","Original synthetic practice log","Template only.")


def make_scoring_alignment():
    fig,ax=figure("FRQ response anatomy and point opportunities", "A generic response checklist keeps the graph, calculation, explanation, and conclusion connected.")
    labels=["Economic setup","Graph","Calculation","Explanation","Units / labels","Conclusion"]; vals=[1,2,2,2,1,1]
    y=np.arange(len(labels)); ax.barh(y,vals,color=[BLUE,TEAL,ORANGE,PURPLE,GOLD,SKY]); ax.set_yticks(y,labels); ax.set_xlabel("Illustrative point opportunities"); ax.set_xlim(0,2.5)
    for i,v in enumerate(vals): ax.text(v+.06,i,str(v),va="center",fontweight="bold")
    style_axes(ax); polish(fig,ax,"Source: Original generic rubric structure.","Not a reproduction of restricted College Board scoring text.")
    save(fig,36,"Scoring-guideline alignment chart","Original generic rubric structure","Not restricted scoring text.")


def main():
    for maker in [make_scarcity, make_ppc, make_trade_flow, make_comp_adv_heatmap, make_cba, make_demand_supply, make_elasticity, make_total_revenue, make_income_ladder, make_surplus, make_shortage_surplus, make_policy_grid, make_tariff, make_trade_map, make_production, make_production_heatmap, make_costs, make_lratc, make_profit_max, make_firm_dashboard, make_shutdown, make_market_firm, make_concentration, make_monopoly, make_price_discrimination, make_mono_comp, make_payoff, make_market_dashboard, make_efficiency_comparison, make_mrp, make_factor_shift, make_competitive_labor, make_monopsony, make_externality, make_externality_pair, make_free_rider, make_policy_dashboard, make_unemployment, make_lorenz, make_histogram, make_policy_evidence, make_six_core, make_timed_dashboard, make_error_heatmap, make_scoring_alignment]:
        maker()
    pd.DataFrame(FIGURES).to_csv(MANIFEST, index=False)
    print(f"Rendered {len(FIGURES)} figures to {OUT}")


if __name__ == "__main__":
    main()
