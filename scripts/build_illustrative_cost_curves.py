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

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_consistent_cost_models import (  # noqa: E402
    DATA,
    build_short_run_cost_schedule,
    write_all_models,
)


ROOT = Path(__file__).resolve().parents[1]
OUT = DATA / "cost-curves.csv"


def build_schedule() -> pd.DataFrame:
    return build_short_run_cost_schedule()


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    data = build_schedule()
    write_all_models()
    data.to_csv(OUT, index=False, float_format="%.6f")
    avc_i = data["avc"].idxmin()
    atc_i = data["atc"].idxmin()
    print(f"wrote {len(data)} rows to {OUT}")
    print(f"AVC minimum: Q={data.loc[avc_i, 'quantity']:.2f}, AVC={data.loc[avc_i, 'avc']:.2f}, MC={data.loc[avc_i, 'marginal_cost']:.2f}")
    print(f"ATC minimum: Q={data.loc[atc_i, 'quantity']:.2f}, ATC={data.loc[atc_i, 'atc']:.2f}, MC={data.loc[atc_i, 'marginal_cost']:.2f}")


if __name__ == "__main__":
    main()
