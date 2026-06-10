# NEXT TIME — Spank The Monkey Website

## Current state

- Project path: `/Users/matt/Dropbox/CLIENTS/SAVANT SOFTWARE SYSTEMS/DEV/Spank-The-Monkey-Website`
- Production domain: `https://spankthemonkeyrocks.com/`
- Local static source lives under `src/`.
- FTP deploy payload mirror lives under `hostinger-public_html/`.
- Old Hostinger/Zyro Website Builder site capture lives under `archive/current-site/20260610-061810/`.
- Research/design references live under `research/`.
- Booking CTA: `Booking@SpankTheMonkeyRocks.com`.
- Credentials remain in 1Password; do not write FTP/API credentials into this repo.

## Production state

- Static rebuild is live on Hostinger.
- Titan email/DNS records were preserved during launch.
- Current live asset versions:
  - `styles.css?v=965fc1197fe7`
  - `gigs-data.js?v=f1e0519f2655`
  - `site.js?v=ad31c84fc365`
- `hostinger-public_html/.htaccess` forces `no-cache, no-store, must-revalidate` for `index.html`, `styles.css`, `site.js`, and `gigs-data.js` to avoid Hostinger/Safari stale-cache issues.

## Gig calendar source

- Upcoming shows are generated from Apple Calendar `Gigs` via `tools/gig_export.py`.
- Website publishes date + location only — no times, notes, pay, contacts, source URLs, or private calendar IDs.
- Current temporary production choice: website is limited to confirmed/current Spank gigs through October 2026.
- Current live public gigs count: 8.
- Current final two public entries:
  - `2026-09-10 Gulf Place — Gulf Shores, AL`
  - `2026-10-11 Houma Fest — Houma, LA`

Regenerate before show-list deployments:

```bash
python3 tools/gig_export.py --days 144 --output src/gigs-data.js --index src/index.html --print
python3 -m unittest discover -s tests -v
```

Then sync changed files into `hostinger-public_html/`, rebuild the zip if needed, upload changed files to `/public_html`, and verify the live URL with a fresh query string.

## Wrap-up / pending

- Initial local git checkpoint should capture the launched site, research, archive, docs, and gig-export tests.
- Do not push to GitHub, change DNS/email, or deploy additional changes unless Matt explicitly approves.
- Future enhancement: replace the temporary static gig bridge with a cleaner two-layer public gig publishing workflow (`Gigs` calendar = private operational source, reviewed public feed = website source).
- Future enhancement: add optional booking form/voice agent/EPK assets only after the base website is checkpointed.
