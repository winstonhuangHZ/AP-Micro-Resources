#!/usr/bin/env python3
"""Download selected Wikimedia Commons visuals and append auditable metadata."""
from __future__ import annotations

import csv
import hashlib
import html
import json
import re
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "APMICRO-Teaching/Visual-Plan/assets/source"
CSV_PATH = OUT / "sources.csv"
API = "https://commons.wikimedia.org/w/api.php"
USER_AGENT = "APMicroResources/1.0 (educational asset collection; Wikimedia Commons attribution audit)"

ASSETS = [
    {
        "filename": "empty-supermarket-shelves-australia.jpg",
        "title": "File:2020-03-15 Empty supermarket shelves in Australian supermarket 01.jpg",
        "session": "Session 9",
        "intended_use": "Shortage, rationing, stockouts, and non-price adjustment.",
    },
    {
        "filename": "supermarket-queue-jerusalem.jpg",
        "title": "File:A queue of people applying physical social distancing outside of a supermarket in Jerusalem.jpg",
        "session": "Session 9",
        "intended_use": "Queues and non-price rationing as a market-disequilibrium prompt.",
    },
    {
        "filename": "traffic-congestion-makati.jpg",
        "title": "File:11 Traffic congestion in Makati city, Manila, Philippines.jpg",
        "session": "Session 29",
        "intended_use": "Congestion as a negative externality and social-cost example.",
    },
    {
        "filename": "severe-air-pollution-new-delhi-nasa.jpg",
        "title": "File:PIA21100 Severe Air Pollution in New Delhi View by NASA's MISR.jpg",
        "session": "Session 28",
        "intended_use": "Air pollution as a negative externality context image; NASA public-domain source.",
    },
    {
        "filename": "vocational-training-programs.jpg",
        "title": "File:Summer vocational training programs (14888328719).jpg",
        "session": "Session 25",
        "intended_use": "Human capital, training, and shifts in labor supply or factor productivity.",
    },
    {
        "filename": "higashi-osaka-public-housing.jpg",
        "title": "File:Higashi-Osaka Harumiya Public Housing 2025-09.jpg",
        "session": "Session 32",
        "intended_use": "Housing access, opportunity, and inequality discussion prompt.",
    },
    {
        "filename": "utility-works-copenhagen.jpg",
        "title": "File:006 Utility works in Copenhagen, Denmark - utility infrastructure trench maintenance dig site.jpg",
        "session": "Session 19",
        "intended_use": "Utility infrastructure and natural-monopoly barriers to entry.",
    },
    {
        "filename": "broadway-avenue-bridge-public-works.jpg",
        "title": "File:Broadway Avenue Bridge, Minneapolis Public Works, ca. 1910s.jpg",
        "session": "Sessions 19 and 33",
        "intended_use": "Bridge infrastructure, public investment, and policy-response context.",
    },
    {
        "filename": "dale-creek-bridge-railroad.jpg",
        "title": "File:Dale Creek Bridge Union Pacific Railroad Company by Andrew J Russell.jpg",
        "session": "Session 19",
        "intended_use": "Rail infrastructure and a natural-monopoly or network-barrier example.",
    },
    {
        "filename": "ccc-workers-lunch.jpg",
        "title": "File:CCC (Civilian Conservation Corps) workers at lunch, Cow Creek, Rocky Mountain National Park. (a7af327c5e064da6955af178424118ed).jpg",
        "session": "Session 33",
        "intended_use": "Government response and public-service employment context; historical extension.",
    },
    {
        "filename": "vacant-retail-storefront-plano.jpg",
        "title": "File:A vacant retail storefront at The Shops at Willow Bend in Plano, Texas.jpg",
        "session": "Session 16",
        "intended_use": "Vacant storefront as an exit and long-run market-adjustment prompt.",
    },
    {
        "filename": "indiana-wheat-harvest.jpg",
        "title": "File:Indiana Wheat Harvest (20210628-NRCS-BJOC-001).jpg",
        "session": "Session 17",
        "intended_use": "Agricultural commodity production and standardized-product markets.",
    },
]


def clean(value: str | None) -> str:
    if not value:
        return ""
    value = re.sub(r"<[^>]+>", "", value)
    value = html.unescape(value)
    return " ".join(value.split())


def api_query(title: str) -> dict:
    params = {
        "action": "query",
        "format": "json",
        "titles": title,
        "prop": "imageinfo",
        "iiprop": "url|extmetadata|size",
        "iiurlwidth": "1600",
    }
    request = urllib.request.Request(
        API + "?" + urllib.parse.urlencode(params),
        headers={"User-Agent": USER_AGENT},
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        payload = json.load(response)
    pages = payload.get("query", {}).get("pages", {})
    page = next(iter(pages.values()))
    if "imageinfo" not in page:
        raise RuntimeError(f"No image info returned for {title}: {page}")
    return page


def download(url: str, destination: Path) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=120) as response:
        data = response.read()
    destination.write_bytes(data)
    return data


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "filename", "local_path", "commons_file", "page_url", "download_url",
        "download_variant", "session", "intended_use", "historical_date", "author",
        "source_credit", "license_or_terms", "mime", "bytes", "sha256", "retrieved_on",
    ]
    with CSV_PATH.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    existing = {row["filename"] for row in rows}

    for asset in ASSETS:
        if asset["filename"] in existing:
            print(f"skip existing {asset['filename']}")
            continue
        page = api_query(asset["title"])
        info = page["imageinfo"][0]
        metadata = info.get("extmetadata", {})
        title_without_prefix = asset["title"][5:]
        page_url = "https://commons.wikimedia.org/wiki/File:" + urllib.parse.quote(
            title_without_prefix.replace(" ", "_"), safe="()_,.-"
        )
        download_url = (info.get("thumburl") or info["url"]).split("?", 1)[0]
        destination = OUT / asset["filename"]
        data = download(download_url, destination)
        row = {
            "filename": asset["filename"],
            "local_path": str(destination.relative_to(ROOT)),
            "commons_file": asset["title"],
            "page_url": page_url,
            "download_url": download_url,
            "download_variant": "1600px Commons thumbnail; canonical file URL and page recorded",
            "session": asset["session"],
            "intended_use": asset["intended_use"],
            "historical_date": clean(metadata.get("DateTimeOriginal", {}).get("value")) or clean(metadata.get("DateTime", {}).get("value")),
            "author": clean(metadata.get("Artist", {}).get("value")),
            "source_credit": clean(metadata.get("Credit", {}).get("value")) or clean(metadata.get("Artist", {}).get("value")),
            "license_or_terms": clean(metadata.get("LicenseShortName", {}).get("value")) or clean(metadata.get("UsageTerms", {}).get("value")),
            "mime": info.get("mime", ""),
            "bytes": str(len(data)),
            "sha256": hashlib.sha256(data).hexdigest(),
            "retrieved_on": str(date.today()),
        }
        rows.append(row)
        existing.add(asset["filename"])
        print(f"downloaded {asset['filename']} | {row['license_or_terms']} | {row['author']}")

    with CSV_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
