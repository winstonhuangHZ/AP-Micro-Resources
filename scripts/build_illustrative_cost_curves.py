#!/usr/bin/env python3
"""Generate a mathematically consistent short-run cost schedule.

The functions are deliberately simple enough for AP Microeconomics teaching,
while preserving the relationships students are expected to recognize:

    TC = FC + VC
    ATC = TC / Q
    AVC = VC / Q
    MC = dTC/dQ = dVC/dQ

The resulting MC curve crosses AVC at AVC's minimum and ATC at ATC's
minimum. Values are illustrative and are not estimates for a real firm.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "APMICRO-Teaching" / "Visual-Plan" / "assets" / "data" / "illustrative" / "cost-curves.csv"


def build_schedule() -> pd.DataFrame:
    quantity = np.arange(0.0, 20.0001, 0.05)
    fixed_cost = np.full_like(quantity, 60.0)
    variable_cost = 0.25 * quantity**3 - 3.0 * quantity**2 + 18.0 * quantity
    total_cost = fixed_cost + variable_cost
    avc = np.full_like(quantity, np.nan)
    atc = np.full_like(quantity, np.nan)
    positive = quantity > 0
    avc[positive] = variable_cost[positive] / quantity[positive]
    atc[positive] = total_cost[positive] / quantity[positive]
    marginal_cost = 0.75 * quantity**2 - 6.0 * quantity + 18.0
    return pd.DataFrame({
        "quantity": quantity,
        "fixed_cost": fixed_cost,
        "variable_cost": variable_cost,
        "total_cost": total_cost,
        "atc": atc,
        "avc": avc,
        "marginal_cost": marginal_cost,
    })


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    data = build_schedule()
    data.to_csv(OUT, index=False, float_format="%.6f")
    avc_i = data["avc"].idxmin()
    atc_i = data["atc"].idxmin()
    print(f"wrote {len(data)} rows to {OUT}")
    print(f"AVC minimum: Q={data.loc[avc_i, 'quantity']:.2f}, AVC={data.loc[avc_i, 'avc']:.2f}, MC={data.loc[avc_i, 'marginal_cost']:.2f}")
    print(f"ATC minimum: Q={data.loc[atc_i, 'quantity']:.2f}, ATC={data.loc[atc_i, 'atc']:.2f}, MC={data.loc[atc_i, 'marginal_cost']:.2f}")


if __name__ == "__main__":
    main()
