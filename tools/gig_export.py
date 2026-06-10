#!/usr/bin/env python3
"""Generate Spank The Monkey website gig data from Apple Calendar exports.

The website is static, so Calendar remains the source of truth through a
repeatable generation step: read the local Apple/iCloud `Gigs` calendar,
filter Spank-related entries, and write `src/gigs-data.js` for the browser.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

LOCAL_TZ = ZoneInfo("America/Chicago")
APPLE_CALENDAR_SWIFT = Path("/Users/matt/.hermes/profiles/business/skills/apple/apple-calendar/scripts/apple_calendar.swift")
SPANK_BARE_VENUE_TITLES = {
    "fat cat",
    "coops",
    "coop's",
    "coop’s",
    "rock n bowl laffy",
    "rock n' bowl laffy",
    "rock n’ bowl laffy",
}

VENUE_DISPLAY_OVERRIDES = {
    "cajun wharf lake charles": "Cajun Wharf — Lake Charles, LA",
    "coop's": "Coop’s on 621 — Gonzales, LA",
    "coop’s": "Coop’s on 621 — Gonzales, LA",
    "coops": "Coop’s on 621 — Gonzales, LA",
    "fred's river": "Fred’s on the River — Prairieville, LA",
    "fred’s river": "Fred’s on the River — Prairieville, LA",
    "fat cat": "Fat Cat Saloon — Prairieville, LA",
    "rock n bowl laffy": "Rock ’n’ Bowl de Lafayette — Lafayette, LA",
    "rock n' bowl laffy": "Rock ’n’ Bowl de Lafayette — Lafayette, LA",
    "rock n’ bowl laffy": "Rock ’n’ Bowl de Lafayette — Lafayette, LA",
    "houma fest": "Houma Fest — Houma, LA",
    "gulf place, gulf shores, al": "Gulf Place — Gulf Shores, AL",
}


def normalize_venue_key(value: str) -> str:
    key = value.casefold().strip()
    key = re.sub(r"^spank\s*[-–—:]?\s*", "", key, flags=re.I).strip()
    key = re.sub(r"\s+", " ", key)
    return key


def parse_event_date(event: dict) -> date:
    raw = event["start"]
    parsed = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    # EventKit exports starts as UTC timestamps. The public site should show the
    # Calendar day Matt sees locally, not the UTC day. Evening gigs often cross
    # midnight in UTC, so using parsed.date() shifts them one day late.
    return parsed.astimezone(LOCAL_TZ).date()


def is_spank_event(event: dict) -> bool:
    title = str(event.get("title") or "").strip()
    title_l = title.lower()
    notes_l = str(event.get("notes") or "").lower()

    # Explicitly keep Matt Rich / other artist dates off the Spank website.
    if "matt rich" in title_l or "artist project: matt rich" in notes_l:
        return False

    if "spank" in title_l or "spank the monkey" in notes_l:
        return True

    # Some confirmed band-thread placeholders were entered as venue-only titles.
    return normalize_venue_key(title) in SPANK_BARE_VENUE_TITLES


def clean_location(event: dict) -> str:
    location = str(event.get("location") or "").strip()
    if location:
        key = normalize_venue_key(location)
        return VENUE_DISPLAY_OVERRIDES.get(key, location)

    title = str(event.get("title") or "").strip()
    key = normalize_venue_key(title)
    if key in VENUE_DISPLAY_OVERRIDES:
        return VENUE_DISPLAY_OVERRIDES[key]

    title = re.sub(r"^spank\s*[-–—:]?\s*", "", title, flags=re.I).strip()
    return title or "Location TBA"


def format_display_date(d: date) -> str:
    return d.strftime("%b %-d")


def extract_spank_gigs(events: list[dict], today: date | None = None) -> list[dict]:
    today = today or datetime.now(LOCAL_TZ).date()
    gigs: list[dict] = []
    seen: set[tuple[str, str]] = set()

    for event in events:
        if not is_spank_event(event):
            continue
        gig_date = parse_event_date(event)
        if gig_date < today:
            continue
        location = clean_location(event)
        key = (gig_date.isoformat(), location.casefold())
        if key in seen:
            continue
        seen.add(key)
        gigs.append(
            {
                "date": format_display_date(gig_date),
                "isoDate": gig_date.isoformat(),
                "location": location,
            }
        )

    return sorted(gigs, key=lambda g: (g["isoDate"], g["location"].casefold()))


def write_js(gigs: list[dict], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(gigs, ensure_ascii=False, indent=2)
    output_path.write_text(
        f"window.SPANK_SHOWS = {payload};\n",
        encoding="utf-8",
    )


def update_index_cache_buster(index_path: Path, gigs_path: Path) -> str:
    """Point the HTML at gigs-data.js with a content-hash query string.

    Hostinger serves JS with a one-week cache lifetime. Keeping the file name
    stable but changing `?v=<hash>` lets Safari and HCDN fetch the new calendar
    export as soon as index.html updates.
    """

    version = hashlib.sha256(gigs_path.read_bytes()).hexdigest()[:12]
    html = index_path.read_text(encoding="utf-8")
    updated = re.sub(
        r'gigs-data\.js(?:\?v=[0-9a-f]+)?',
        f"gigs-data.js?v={version}",
        html,
    )
    if updated == html and "gigs-data.js" not in html:
        raise ValueError(f"No gigs-data.js script reference found in {index_path}")
    index_path.write_text(updated, encoding="utf-8")
    return version


def read_calendar_events(days: int) -> list[dict]:
    cmd = ["swift", str(APPLE_CALENDAR_SWIFT), "events", "--days", str(days), "--calendar", "Gigs"]
    raw = subprocess.check_output(cmd, text=True)
    return json.loads(raw)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-json", type=Path, help="Use an existing EventKit JSON export instead of reading Calendar")
    parser.add_argument("--days", type=int, default=365, help="Days ahead to read from Apple Calendar")
    parser.add_argument("--output", type=Path, default=Path("src/gigs-data.js"), help="Output JS file")
    parser.add_argument("--index", type=Path, default=Path("src/index.html"), help="HTML file whose gigs-data.js script query should be cache-busted")
    parser.add_argument("--no-cache-bust", action="store_true", help="Do not update the index.html gigs-data.js version query")
    parser.add_argument("--print", action="store_true", help="Print extracted gigs as JSON")
    args = parser.parse_args(argv)

    events = json.loads(args.input_json.read_text()) if args.input_json else read_calendar_events(args.days)
    gigs = extract_spank_gigs(events)
    write_js(gigs, args.output)
    version = None if args.no_cache_bust else update_index_cache_buster(args.index, args.output)
    if args.print:
        print(json.dumps(gigs, ensure_ascii=False, indent=2))
        if version:
            print(f"gigs-data version: {version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
