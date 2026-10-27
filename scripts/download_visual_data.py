#!/usr/bin/env python3
"""Download reproducible visual data for the AP Micro teaching plan.

The script deliberately uses official FRED CSV endpoints and locally generated
illustrative tables. It does not require a Kaggle account or an API key.
"""
from __future__ import annotations

import csv
import hashlib
import math
import sys
import urllib.request
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_consistent_cost_models import (  # noqa: E402
    build_competitive_firm_schedule,
    build_monopolistic_competition_schedule,
    build_monopoly_schedule,
    build_short_run_cost_schedule,
)


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "APMICRO-Teaching" / "Visual-Plan" / "assets" / "data"
RAW = DATA / "raw"
DERIVED = DATA / "derived"
ILLUSTRATIVE = DATA / "illustrative"

FRED = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"

SERIES = {
    "UNRATE": ("unrate.csv", "Civilian unemployment rate", "Percent", "BLS"),
    "CPIAUCSL": ("cpiaucsl.csv", "Consumer Price Index for All Urban Consumers", "Index 1982-84=100", "BLS"),
    "GDP": ("gdp.csv", "Gross domestic product", "Billions of dollars", "BEA"),
    "GDPC1": ("gdpc1.csv", "Real gross domestic product", "Billions of chained 2017 dollars", "BEA"),
    "FEDFUNDS": ("fedfunds.csv", "Effective federal funds rate", "Percent", "Federal Reserve"),
    "M2SL": ("m2sl.csv", "M2 money stock", "Billions of dollars", "Federal Reserve"),
    "SP500": ("sp500.csv", "S&P 500 index", "Index", "S&P Dow Jones Indices LLC"),
    "GINIALLRH": ("giniallrh.csv", "Income inequality measure", "Index", "U.S. Census Bureau"),
    "USREC": ("usrec.csv", "NBER recession indicator", "0/1", "NBER via FRED"),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def read_fred(path: Path, value_name: str) -> list[tuple[str, float]]:
    rows: list[tuple[str, float]] = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            date = row.get("observation_date") or row.get("DATE") or row.get("date")
            value = row.get(value_name) or row.get(value_name.upper())
            if not date or value in (None, "", "."):
                continue
            try:
                rows.append((date, float(value)))
            except ValueError:
                continue
    return rows


def month_key(date: str) -> str:
    return date[:7]


def average_by_month(rows: list[tuple[str, float]]) -> dict[str, float]:
    grouped: dict[str, list[float]] = {}
    for date, value in rows:
        grouped.setdefault(month_key(date), []).append(value)
    return {key: sum(values) / len(values) for key, values in grouped.items()}


def download_raw(retrieved_at: str) -> list[dict]:
    manifest: list[dict] = []
    for series_id, (filename, title, units, publisher) in SERIES.items():
        target = RAW / filename
        request = urllib.request.Request(
            FRED.format(series_id=series_id),
            headers={"User-Agent": "AP-Micro-Resources data snapshot/1.0"},
        )
        with urllib.request.urlopen(request, timeout=90) as response:
            payload = response.read()
        target.write_bytes(payload)
        manifest.append({
            "path": target.relative_to(DATA).as_posix(),
            "kind": "raw",
            "series_id": series_id,
            "title": title,
            "publisher": publisher,
            "units": units,
            "source_url": FRED.format(series_id=series_id),
            "retrieved_at": retrieved_at,
            "bytes": target.stat().st_size,
            "sha256": sha256(target),
            "license_or_terms": "FRED-hosted public data; retain source attribution and inspect the series page before publication.",
            "notes": "Raw CSV snapshot downloaded from the official FRED graph endpoint.",
        })
    return manifest


def build_derived() -> list[dict]:
    manifest: list[dict] = []
    def add(path: Path, title: str, notes: str) -> None:
        manifest.append({
            "path": path.relative_to(DATA).as_posix(),
            "kind": "derived",
            "series_id": "",
            "title": title,
            "publisher": "Derived locally",
            "units": "",
            "source_url": "https://fred.stlouisfed.org/",
            "retrieved_at": RETRIEVED_AT,
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
            "license_or_terms": "Derived locally from the cited FRED snapshots.",
            "notes": notes,
        })

    cpi = dict(read_fred(RAW / SERIES["CPIAUCSL"][0], "CPIAUCSL"))
    cpi_rows = []
    for date, value in sorted(cpi.items()):
        prior_date = f"{int(date[:4]) - 1}{date[4:]}"
        if prior_date in cpi:
            cpi_rows.append({"date": date, "cpi_index": f"{value:.6f}", "inflation_yoy_pct": f"{(value / cpi[prior_date] - 1) * 100:.6f}"})
    cpi_path = DERIVED / "cpi-inflation-yoy.csv"
    write_csv(cpi_path, ["date", "cpi_index", "inflation_yoy_pct"], cpi_rows)
    add(cpi_path, "CPI year-over-year inflation", "Computed as 100 x (CPI_t / CPI_(t-12) - 1).")

    real_gdp = dict(read_fred(RAW / SERIES["GDPC1"][0], "GDPC1"))
    gdp_rows = []
    dates = sorted(real_gdp)
    for index, date in enumerate(dates):
        if index >= 1:
            previous = real_gdp[dates[index - 1]]
            gdp_rows.append({"date": date, "real_gdp": f"{real_gdp[date]:.6f}", "quarterly_growth_pct": f"{(real_gdp[date] / previous - 1) * 100:.6f}", "annualized_growth_pct": f"{((real_gdp[date] / previous) ** 4 - 1) * 100:.6f}"})
    gdp_path = DERIVED / "real-gdp-growth.csv"
    write_csv(gdp_path, ["date", "real_gdp", "quarterly_growth_pct", "annualized_growth_pct"], gdp_rows)
    add(gdp_path, "Real GDP growth", "Computed from quarterly GDPC1; annualized growth uses ((GDP_t/GDP_(t-1))^4 - 1) x 100.")

    unemployment = dict(read_fred(RAW / SERIES["UNRATE"][0], "UNRATE"))
    recession = dict(read_fred(RAW / SERIES["USREC"][0], "USREC"))
    rec_rows = [{"date": date, "unemployment_rate": f"{value:.6f}", "recession": int(recession.get(date, 0))} for date, value in sorted(unemployment.items())]
    rec_path = DERIVED / "unemployment-with-recessions.csv"
    write_csv(rec_path, ["date", "unemployment_rate", "recession"], rec_rows)
    add(rec_path, "Unemployment with recession markers", "Joins monthly UNRATE to the monthly USREC recession indicator.")

    fed = average_by_month(read_fred(RAW / SERIES["FEDFUNDS"][0], "FEDFUNDS"))
    m2 = average_by_month(read_fred(RAW / SERIES["M2SL"][0], "M2SL"))
    cpi_yoy = {month_key(row["date"]): float(row["inflation_yoy_pct"]) for row in cpi_rows}
    unrate = average_by_month(read_fred(RAW / SERIES["UNRATE"][0], "UNRATE"))
    sp500 = average_by_month(read_fred(RAW / SERIES["SP500"][0], "SP500"))
    months = sorted(set(fed) | set(m2) | set(cpi_yoy) | set(unrate) | set(sp500))
    dashboard_rows = []
    for month in months:
        dashboard_rows.append({
            "month": month,
            "fedfunds_pct": f"{fed[month]:.6f}" if month in fed else "",
            "m2_billions": f"{m2[month]:.6f}" if month in m2 else "",
            "inflation_yoy_pct": f"{cpi_yoy[month]:.6f}" if month in cpi_yoy else "",
            "unemployment_rate": f"{unrate[month]:.6f}" if month in unrate else "",
            "sp500_monthly_average": f"{sp500[month]:.6f}" if month in sp500 else "",
        })
    dashboard_path = DERIVED / "policy-and-indicators-dashboard.csv"
    write_csv(dashboard_path, ["month", "fedfunds_pct", "m2_billions", "inflation_yoy_pct", "unemployment_rate", "sp500_monthly_average"], dashboard_rows)
    add(dashboard_path, "Policy and indicators dashboard", "Monthly alignment of FRED policy, money, inflation, unemployment, and S&P 500 context series.")

    gini_rows = [{"date": date, "gini_index": f"{value:.6f}"} for date, value in read_fred(RAW / SERIES["GINIALLRH"][0], "GINIALLRH")]
    gini_path = DERIVED / "income-inequality-context.csv"
    write_csv(gini_path, ["date", "gini_index"], gini_rows)
    add(gini_path, "Income inequality context", "FRED/Census series for a context panel; use a locally drawn Lorenz curve for the AP Micro model.")
    return manifest


def build_illustrative() -> list[dict]:
    specs: list[tuple[str, list[str], list[dict], str]] = []
    specs.append(("ppc.csv", ["x_good_a", "y_good_b", "growth_y_good_b"], [{"x_good_a": i, "y_good_b": round(100 * math.sqrt(max(0, 1 - (i / 100) ** 2)), 4), "growth_y_good_b": round(110 * math.sqrt(max(0, 1 - (i / 100) ** 2)), 4)} for i in range(0, 101, 5)], "Illustrative PPC coordinates for graphing efficiency and growth."))
    specs.append(("comparative-advantage.csv", ["producer", "product", "opportunity_cost"], [{"producer": "A", "product": "Food", "opportunity_cost": 1.0}, {"producer": "A", "product": "Cloth", "opportunity_cost": 0.5}, {"producer": "B", "product": "Food", "opportunity_cost": 2.0}, {"producer": "B", "product": "Cloth", "opportunity_cost": 0.5}], "Illustrative opportunity-cost table; no real-world claims."))
    specs.append(("demand-supply.csv", ["quantity", "demand_price", "supply_price"], [{"quantity": q, "demand_price": 100 - q, "supply_price": 20 + 0.5 * q} for q in range(0, 101, 5)], "Illustrative linear market schedule."))
    specs.append(("elasticity-and-revenue.csv", ["quantity", "price", "revenue", "elastic_demand_quantity", "inelastic_demand_quantity"], [{"quantity": q, "price": 100 - q, "revenue": q * (100 - q), "elastic_demand_quantity": round(100 - 1.5 * (100 - q), 4), "inelastic_demand_quantity": round(100 - 0.5 * (100 - q), 4)} for q in range(10, 101, 5)], "Illustrative elasticity and total-revenue table."))
    specs.append(("surplus-and-intervention.csv", ["quantity", "demand_price", "supply_price", "ceiling_price", "floor_price", "taxed_buyer_price", "taxed_seller_price"], [{"quantity": q, "demand_price": 100 - q, "supply_price": 20 + 0.5 * q, "ceiling_price": 45, "floor_price": 70, "taxed_buyer_price": 65, "taxed_seller_price": 55} for q in range(0, 101, 5)], "Illustrative surplus, price-control, and tax-wedge schedule."))
    specs.append(("tariff.csv", ["quantity", "domestic_demand_price", "domestic_supply_price", "world_price", "tariff_price"], [{"quantity": q, "domestic_demand_price": 100 - q, "domestic_supply_price": 20 + 0.5 * q, "world_price": 40, "tariff_price": 55} for q in range(0, 101, 5)], "Illustrative international-trade schedule."))
    production = []
    total = [0, 10, 24, 39, 51, 60, 66, 70, 72]
    for labor, output in enumerate(total):
        production.append({"labor": labor, "total_product": output, "average_product": round(output / labor, 4) if labor else "", "marginal_product": output - total[labor - 1] if labor else ""})
    specs.append(("production-function.csv", ["labor", "total_product", "average_product", "marginal_product"], production, "Illustrative production table for TP, AP, and MP."))
    for filename, frame, notes in [
        ("cost-curves.csv", build_short_run_cost_schedule(), "Calculated short-run cost schedule; MC is U-shaped and crosses AVC and ATC at their minima."),
        ("monopoly.csv", build_monopoly_schedule(), "Calculated monopoly schedule with a U-shaped short-run MC and integrated VC/ATC."),
        ("competitive-firm.csv", build_competitive_firm_schedule(), "Calculated representative-firm schedule with a U-shaped short-run MC."),
        ("monopolistic-competition.csv", build_monopolistic_competition_schedule(), "Calculated monopolistic-competition schedule with a U-shaped short-run MC and ATC-consistent costs."),
    ]:
        frame = frame.where(frame.notna(), "")
        specs.append((filename, list(frame.columns), frame.to_dict(orient="records"), notes))
    specs.append(("lratc.csv", ["output", "lratc"], [{"output": q, "lratc": round(80 - 1.5 * q + 0.03 * q * q, 4)} for q in range(1, 51)], "Illustrative long-run average total cost curve."))
    specs.append(("oligopoly-payoffs.csv", ["strategy_a", "strategy_b", "payoff_a", "payoff_b"], [{"strategy_a": "Cooperate", "strategy_b": "Cooperate", "payoff_a": 8, "payoff_b": 8}, {"strategy_a": "Cooperate", "strategy_b": "Defect", "payoff_a": 2, "payoff_b": 10}, {"strategy_a": "Defect", "strategy_b": "Cooperate", "payoff_a": 10, "payoff_b": 2}, {"strategy_a": "Defect", "strategy_b": "Defect", "payoff_a": 4, "payoff_b": 4}], "Illustrative payoff matrix."))
    specs.append(("factor-market.csv", ["labor", "mrp", "factor_price", "competitive_employment"], [{"labor": q, "mrp": 100 - 3 * q, "factor_price": 40, "competitive_employment": 20} for q in range(0, 31, 2)], "Illustrative MRP and competitive factor-market schedule."))
    specs.append(("monopsony.csv", ["labor", "labor_supply_wage", "mfc", "mrp"], [{"labor": q, "labor_supply_wage": 20 + q, "mfc": 20 + 2 * q, "mrp": 100 - 2 * q} for q in range(0, 31, 2)], "Illustrative monopsony schedule."))
    specs.append(("externalities.csv", ["quantity", "private_marginal_cost", "social_marginal_cost", "marginal_benefit"], [{"quantity": q, "private_marginal_cost": 10 + q, "social_marginal_cost": 20 + q, "marginal_benefit": 90 - q} for q in range(0, 81, 5)], "Illustrative negative-externality schedule."))
    specs.append(("public-goods.csv", ["person", "marginal_benefit", "marginal_cost", "free_rider_flag"], [{"person": "A", "marginal_benefit": 40, "marginal_cost": 30, "free_rider_flag": 0}, {"person": "B", "marginal_benefit": 35, "marginal_cost": 30, "free_rider_flag": 1}, {"person": "C", "marginal_benefit": 25, "marginal_cost": 30, "free_rider_flag": 1}], "Illustrative public-good and free-rider table."))
    specs.append(("review-error-heatmap-template.csv", ["unit", "topic", "error_type", "count"], [{"unit": f"Unit {unit}", "topic": topic, "error_type": error, "count": 0} for unit in range(1, 7) for topic in ["concept", "graph", "calculation", "reading", "expression"] for error in ["concept", "graph", "calculation", "reading", "expression"]], "Blank template; populate only with anonymized student practice logs."))

    manifest: list[dict] = []
    for filename, fields, rows, notes in specs:
        path = ILLUSTRATIVE / filename
        normalized = [{key: str(value) for key, value in row.items()} for row in rows]
        write_csv(path, fields, normalized)
        manifest.append({
            "path": path.relative_to(DATA).as_posix(),
            "kind": "illustrative",
            "series_id": "",
            "title": filename.removesuffix(".csv").replace("-", " ").title(),
            "publisher": "Generated locally",
            "units": "Model values",
            "source_url": "",
            "retrieved_at": RETRIEVED_AT,
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
            "license_or_terms": "Original synthetic teaching data; reusable under the repository license.",
            "notes": notes,
        })
    return manifest


def write_readme() -> None:
    (DATA / "README.md").write_text(
        """# Visual data assets

This directory contains the data inputs for the AP Microeconomics visual plan.

## Source policy

The current batch uses official FRED CSV snapshots for public indicators and locally generated illustrative tables for textbook models. Kaggle is not required for these lessons. Kaggle may be considered later for a specific, well documented industry or household dataset, but it should not replace BLS, BEA, NBER, Census, or Federal Reserve sources when an official series exists.

## Folders

- `raw/` — unchanged FRED CSV snapshots.
- `derived/` — locally calculated inflation, growth, recession joins, and aligned dashboards.
- `illustrative/` — synthetic tables for PPC, supply and demand, elasticity, costs, market structures, factor markets, externalities, and review templates. These are models, not measured real-world observations.
- `manifest.csv` — source URL, retrieval date, byte count, SHA-256, and licensing notes for every CSV.

## Rebuild

From the repository root:

```bash
python3 scripts/download_visual_data.py
python3 scripts/build_visual_plan.py
python3 scripts/update_indexes.py
```

The generated charts should cite the relevant manifest row on the figure itself.
""",
        encoding="utf-8",
    )


def main() -> None:
    global RETRIEVED_AT
    RETRIEVED_AT = datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(timespec="seconds")
    for folder in (RAW, DERIVED, ILLUSTRATIVE):
        folder.mkdir(parents=True, exist_ok=True)
    manifest = download_raw(RETRIEVED_AT)
    manifest.extend(build_derived())
    manifest.extend(build_illustrative())
    fieldnames = ["path", "kind", "series_id", "title", "publisher", "units", "source_url", "retrieved_at", "bytes", "sha256", "license_or_terms", "notes"]
    write_csv(DATA / "manifest.csv", fieldnames, manifest)
    write_readme()
    print(f"Downloaded {len(SERIES)} raw FRED series and wrote {len(manifest)} manifest rows.")


if __name__ == "__main__":
    main()
