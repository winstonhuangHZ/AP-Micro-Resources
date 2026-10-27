#!/usr/bin/env python3
"""Build calculated cost schedules used by the AP Micro teaching figures.

The model tables are calculated first and the figures draw the sampled points
with linear interpolation between them.  This keeps MC, AVC, and ATC
consistent instead of drawing visually convenient but unrelated curves.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "APMICRO-Teaching" / "Visual-Plan" / "assets" / "data" / "illustrative"


def u_shaped_mc(quantity: np.ndarray, minimum: float, turning_quantity: float, curvature: float) -> np.ndarray:
    """Return a U-shaped marginal-cost schedule with a Nike-like profile."""
    return minimum + curvature * (quantity - turning_quantity) ** 2


def variable_cost_from_mc(
    quantity: np.ndarray, minimum: float, turning_quantity: float, curvature: float
) -> np.ndarray:
    """Integrate the quadratic MC curve from zero output so VC(0)=0."""
    return minimum * quantity + curvature / 3.0 * (
        (quantity - turning_quantity) ** 3 + turning_quantity**3
    )


def per_unit_columns(
    quantity: np.ndarray,
    fixed_cost: float,
    variable_cost: np.ndarray,
    marginal_cost: np.ndarray,
) -> pd.DataFrame:
    total_cost = fixed_cost + variable_cost
    avc = np.full_like(quantity, np.nan, dtype=float)
    atc = np.full_like(quantity, np.nan, dtype=float)
    positive = quantity > 0
    avc[positive] = variable_cost[positive] / quantity[positive]
    atc[positive] = total_cost[positive] / quantity[positive]
    return pd.DataFrame(
        {
            "quantity": quantity,
            "fixed_cost": np.full_like(quantity, fixed_cost, dtype=float),
            "variable_cost": variable_cost,
            "total_cost": total_cost,
            "atc": atc,
            "avc": avc,
            "marginal_cost": marginal_cost,
        }
    )


def build_short_run_cost_schedule() -> pd.DataFrame:
    quantity = np.arange(0.0, 20.0001, 0.05)
    marginal_cost = u_shaped_mc(quantity, minimum=6.0, turning_quantity=4.0, curvature=0.75)
    variable_cost = variable_cost_from_mc(quantity, minimum=6.0, turning_quantity=4.0, curvature=0.75)
    return per_unit_columns(quantity, fixed_cost=60.0, variable_cost=variable_cost, marginal_cost=marginal_cost)


def build_monopoly_schedule() -> pd.DataFrame:
    quantity = np.arange(0.0, 50.0001, 0.25)
    marginal_cost = u_shaped_mc(quantity, minimum=8.0, turning_quantity=10.0, curvature=0.08)
    variable_cost = variable_cost_from_mc(quantity, minimum=8.0, turning_quantity=10.0, curvature=0.08)
    data = per_unit_columns(quantity, fixed_cost=120.0, variable_cost=variable_cost, marginal_cost=marginal_cost)
    data = data.rename(columns={"marginal_cost": "mc"})
    data.insert(1, "price", 100.0 - quantity)
    data.insert(2, "mr", 100.0 - 2.0 * quantity)
    return data


def build_competitive_firm_schedule() -> pd.DataFrame:
    quantity = np.arange(0.0, 100.0001, 0.25)
    marginal_cost = u_shaped_mc(quantity, minimum=8.0, turning_quantity=25.0, curvature=0.025)
    variable_cost = variable_cost_from_mc(quantity, minimum=8.0, turning_quantity=25.0, curvature=0.025)
    data = per_unit_columns(quantity, fixed_cost=160.0, variable_cost=variable_cost, marginal_cost=marginal_cost)
    data.insert(1, "market_price", 47.0)
    return data


def build_monopolistic_competition_schedule() -> pd.DataFrame:
    quantity = np.arange(0.0, 80.0001, 0.25)
    marginal_cost = u_shaped_mc(quantity, minimum=8.0, turning_quantity=20.0, curvature=0.018)
    variable_cost = variable_cost_from_mc(quantity, minimum=8.0, turning_quantity=20.0, curvature=0.018)
    data = per_unit_columns(quantity, fixed_cost=110.0, variable_cost=variable_cost, marginal_cost=marginal_cost)
    data.insert(1, "demand_short_run", 100.0 - 0.9 * quantity)
    data.insert(2, "mr_short_run", 100.0 - 1.8 * quantity)
    # The long-run demand is calculated as the tangent to ATC at Q=20.
    # Since ATC'=(MC-ATC)/Q, its slope is the slope used below.
    tangent_q = 20.0
    tangent_atc = float(data.loc[np.isclose(data.quantity, tangent_q), "atc"].iloc[0])
    tangent_mc = float(data.loc[np.isclose(data.quantity, tangent_q), "marginal_cost"].iloc[0])
    demand_slope = (tangent_atc - tangent_mc) / tangent_q
    demand_intercept = tangent_atc + demand_slope * tangent_q
    data.insert(3, "demand_long_run", demand_intercept - demand_slope * quantity)
    data.insert(4, "mr_long_run", demand_intercept - 2.0 * demand_slope * quantity)
    return data


def write_all_models(output_dir: Path = DATA) -> dict[str, pd.DataFrame]:
    output_dir.mkdir(parents=True, exist_ok=True)
    models = {
        "cost-curves.csv": build_short_run_cost_schedule(),
        "monopoly.csv": build_monopoly_schedule(),
        "competitive-firm.csv": build_competitive_firm_schedule(),
        "monopolistic-competition.csv": build_monopolistic_competition_schedule(),
    }
    for filename, frame in models.items():
        frame.to_csv(output_dir / filename, index=False, float_format="%.6f")
    return models


if __name__ == "__main__":
    frames = write_all_models()
    for filename, frame in frames.items():
        print(f"wrote {len(frame)} rows to {DATA / filename}")
