import json
import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import gig_export


class GigExportTests(unittest.TestCase):
    def test_filters_spank_events_and_excludes_matt_rich(self):
        events = [
            {
                "title": "Spank Coop’s",
                "start": "2026-06-20T00:00:00Z",
                "location": "",
                "notes": "",
                "isAllDay": False,
            },
            {
                "title": "Matt Rich at Tallulah",
                "start": "2026-07-17T23:00:00Z",
                "location": "Tallulah Restaurant, Baton Rouge, LA",
                "notes": "Artist project: Matt Rich",
                "isAllDay": False,
            },
            {
                "title": "Rock N Bowl Laffy",
                "start": "2026-08-23T02:00:00Z",
                "location": "",
                "notes": "Corrected from Spank The Monkey thread / Matt confirmation: 9 PM.",
                "isAllDay": False,
            },
        ]

        gigs = gig_export.extract_spank_gigs(events, today=date(2026, 6, 10))

        self.assertEqual(
            [g["location"] for g in gigs],
            ["Coop’s on 621 — Gonzales, LA", "Rock ’n’ Bowl de Lafayette — Lafayette, LA"],
        )
        self.assertEqual([g["date"] for g in gigs], ["Jun 20", "Aug 23"])
        self.assertNotIn("Matt Rich", json.dumps(gigs))

    def test_uses_calendar_location_when_present_and_date_only_for_all_day(self):
        events = [
            {
                "title": "Spank gulf shores",
                "start": "2026-09-10T23:00:00Z",
                "location": "Gulf Place, Gulf Shores, AL",
                "notes": "Corrected from Spank The Monkey thread",
                "isAllDay": False,
            },
            {
                "title": "Fat cat",
                "start": "2026-11-27T06:00:00Z",
                "location": "",
                "notes": "Spank The Monkey",
                "isAllDay": True,
            },
        ]

        gigs = gig_export.extract_spank_gigs(events, today=date(2026, 6, 10))

        self.assertEqual(gigs[0]["location"], "Gulf Place — Gulf Shores, AL")
        self.assertEqual(gigs[0]["date"], "Sep 10")
        self.assertEqual(gigs[1]["date"], "Nov 27")
        self.assertEqual(gigs[1]["location"], "Fat Cat Saloon — Prairieville, LA")
        self.assertNotRegex(json.dumps(gigs), r"\\d{1,2}:\\d{2}|PM|AM")

    def test_sanitizes_common_spank_venue_titles_for_public_display(self):
        cases = {
            "Spank - Cajun wharf lake Charles": "Cajun Wharf — Lake Charles, LA",
            "Spank Coop’s": "Coop’s on 621 — Gonzales, LA",
            "Coops": "Coop’s on 621 — Gonzales, LA",
            "Spank Fred’s River": "Fred’s on the River — Prairieville, LA",
            "Spank Fat Cat": "Fat Cat Saloon — Prairieville, LA",
            "Fat cat": "Fat Cat Saloon — Prairieville, LA",
            "Rock N Bowl Laffy": "Rock ’n’ Bowl de Lafayette — Lafayette, LA",
            "Spank Houma Fest": "Houma Fest — Houma, LA",
        }
        events = [
            {
                "title": title,
                "start": "2026-08-02T00:00:00Z",
                "location": "",
                "notes": "Spank The Monkey",
                "isAllDay": False,
            }
            for title in cases
        ]

        gigs = gig_export.extract_spank_gigs(events, today=date(2026, 6, 10))

        self.assertEqual({g["location"] for g in gigs}, set(cases.values()))

    def test_writes_browser_consumable_js(self):
        gigs = [{"date": "Jun 19", "isoDate": "2026-06-19", "location": "Coop’s on 621 — Gonzales, LA"}]
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "gigs-data.js"
            gig_export.write_js(gigs, out)
            text = out.read_text()

        self.assertIn("window.SPANK_SHOWS", text)
        self.assertIn("Coop", text)
        self.assertTrue(text.strip().endswith(";"))

    def test_updates_index_script_cache_buster_from_gigs_file(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            gigs_file = root / "gigs-data.js"
            index_file = root / "index.html"
            gigs_file.write_text("window.SPANK_SHOWS = [{\"location\": \"Coop’s\"}];")
            index_file.write_text('<script src="gigs-data.js"></script>')

            version = gig_export.update_index_cache_buster(index_file, gigs_file)

            html = index_file.read_text()
        self.assertRegex(version, r"^[0-9a-f]{12}$")
        self.assertIn(f'gigs-data.js?v={version}', html)


if __name__ == "__main__":
    unittest.main()
