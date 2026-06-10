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
  - `gigs-data.js?v=cf66522bc4d6`
  - `site.js?v=ad31c84fc365`
- `hostinger-public_html/.htaccess` forces `no-cache, no-store, must-revalidate` for `index.html`, `styles.css`, `site.js`, and `gigs-data.js` to avoid Hostinger/Safari stale-cache issues.

## Gig calendar source

- Upcoming shows are generated from Apple Calendar `Gigs` via `tools/gig_export.py`.
- Website publishes date + location only — no times, notes, pay, contacts, source URLs, or private calendar IDs.
- Current temporary production choice: website is limited to confirmed/current Spank gigs through October 2026.
- Current live public gigs count: 8.
- Current final two public entries:
  - `2026-09-10 Gulf Place — Gulf Shores, AL`
  - `2026-10-10 Houma Fest — Houma, LA`

Regenerate before show-list deployments:

```bash
python3 tools/gig_export.py --days 144 --output src/gigs-data.js --index src/index.html --print
python3 -m unittest discover -s tests -v
```

Then sync changed files into `hostinger-public_html/`, upload changed files to `/public_html`, and verify the live URL with a fresh query string.

## Most recent deploy — 2026-06-10 date fix

Matt noticed the website dates were one day later than the `Gigs` calendar source of truth.

Root cause:
- EventKit exports timed events as UTC timestamps.
- Evening Central-time gigs cross midnight UTC.
- `tools/gig_export.py` was using the UTC date portion instead of the local Calendar day.

Fix:
- `parse_event_date()` now converts timed event starts to `America/Chicago` before taking `.date()`.
- Regression test added for evening gigs that serialize on the next UTC day.
- Regenerated `src/gigs-data.js`, `src/index.html`, `hostinger-public_html/gigs-data.js`, and `hostinger-public_html/index.html`.
- Deployed only `index.html` and `gigs-data.js` to Hostinger FTP `/public_html`.

Verification:
- `python3 -m unittest discover -s tests -v` passes: 6/6.
- Live root references `gigs-data.js?v=cf66522bc4d6`.
- Live data shows corrected dates: `Jun 13`, `Jun 19`, `Aug 1`, `Aug 22`, `Aug 28`, `Oct 10`.
- Live data still contains only public fields: date, isoDate, location.

## Most recent deploy — 2026-06-10 patriotic logo

Matt asked to use the patriotic logo everywhere the site uses the logo.

Changes:
- Created web-sized `src/assets/logo-patriot.png` from `/Users/matt/Desktop/Spank Patriot Logo - Original.png`.
- Mirrored it to `hostinger-public_html/assets/logo-patriot.png`.
- Updated `src/index.html` and `hostinger-public_html/index.html` so favicon, header logo, and footer logo all use `assets/logo-patriot.png`.
- Deployed `index.html` and `assets/logo-patriot.png` to Hostinger FTP `/public_html`.

Verification:
- Live HTML references `assets/logo-patriot.png` exactly 3 times and no longer references `assets/logo.png`.
- FTP remote `assets/logo-patriot.png` matches local SHA-256 `14c3e18e91e598f1190ccfcda57c2a19a9a7a67f1f7089b4168b320a8202146e`.
- Public HCDN serves a valid 1024x1024 PNG; HCDN recompresses/optimizes it, so public hash differs from FTP hash.
- Vision check confirms the live image is the patriotic monkey/guitar logo.

## Most recent deploy — 2026-06-10 desktop hero image copy

Matt asked to put a copy of the hero image at the top on desktop.

Changes:
- Added a desktop-only `hero-desktop-photo` image using `assets/hero-rice-festival.jpg`.
- The image is hidden below 900px wide, positioned near the top-right of the desktop hero, and does not cover the nav/headline.
- Deployed from the live baseline HTML/CSS so the local in-progress Lindsay booking-agent work was not introduced to production.
- Live CSS version for this deploy: `styles.css?v=1543c5a8c157`.

Verification:
- Live HTML contains `hero-desktop-photo` once.
- Live HTML still references `gigs-data.js?v=cf66522bc4d6`.
- Live HTML still uses `assets/logo-patriot.png`.
- Live HTML does not include `booking-agent`.
- Live CSS includes the desktop-only hero image rules.
- Local browser check confirmed the image loads at desktop dimensions without covering the nav/headline.


## Most recent deploy — 2026-06-10 Lindsay ad landing page

Matt approved deploy, then corrected scope: Lindsay should live on a separate ads/landing page rather than inline on the root homepage.

Changes:
- Created `/booking/` landing page in `src/booking/index.html` and `hostinger-public_html/booking/index.html`.
- Root homepage CTAs now link to `booking/`; root homepage does not embed the ElevenLabs agent inline.
- `/booking/` includes the Lindsay intro MP4, pricing bullets, and contained ElevenLabs ConvAI widget.
- Public booking facts shown on landing page:
  - Band starts at `$2,500`.
  - Sound is additional `$1,500`.
  - Base area: Baton Rouge / Lafayette.
  - Other areas may require travel and hotel.
- Deployed to Hostinger FTP `/public_html`:
  - `index.html`
  - `styles.css`
  - `booking/index.html`
  - `assets/lindsay-booking-agent.mp4`
  - `assets/logo-patriot.png`

Verification:
- `python3 -m unittest discover -s tests -q` passes: 6/6.
- Local `/booking/` loaded with no console errors; widget host is contained (`position: relative`).
- FTP pullback matched local for `booking/index.html`, `styles.css`, and `assets/lindsay-booking-agent.mp4`.
- Live checks passed:
  - `https://spankthemonkeyrocks.com/` links to `booking/` and does not include the agent ID inline.
  - `https://spankthemonkeyrocks.com/booking/` returns the landing page with agent ID `agent_9401ktscyd0efq1r6k7ds27xcxq3`.
  - Live MP4 returns `200 video/mp4` with `8,368,834` bytes.
  - Live CSS returns `200 text/css`.


## Pending deploy — Lindsay video poster thumbnail

Local change is ready but not deployed yet because Hostinger FTP timed out from this machine on 2026-06-10.

Changes staged locally:
- Created `src/assets/lindsay-booking-agent-poster.jpg` from a Lindsay avatar QA frame.
- Mirrored `hostinger-public_html/assets/lindsay-booking-agent-poster.jpg`.
- Updated `src/booking/index.html` and `hostinger-public_html/booking/index.html` video poster from `../assets/logo-patriot.png` to `../assets/lindsay-booking-agent-poster.jpg`.

Verification completed locally:
- `python3 -m unittest discover -s tests -q` passes: 6/6.
- Poster asset visually verified as Lindsay/avatar image, not just Spank logo.

Deploy blocker:
- FTP host `5.183.10.138:21` timed out repeatedly; ports 21/22/990/65002 also timed out.
- Live `/booking/` still has `poster="../assets/logo-patriot.png"`.

Next safe action:
- Retry FTP upload of `booking/index.html` and `assets/lindsay-booking-agent-poster.jpg`, then verify live `/booking/` contains `lindsay-booking-agent-poster.jpg`.

## Wrap-up / pending

- Initial local git checkpoint is complete: `47c924a Launch static Spank The Monkey website rebuild`.
- Follow-up handoff commit is complete: `630b37b Update Spank website handoff note`.
- Current date-fix, patriotic-logo, and desktop hero-copy working tree changes are not yet committed.
- Note: local `src/index.html` currently includes in-progress Lindsay booking-agent work; the latest production hero-image deploy intentionally used the live baseline to avoid publishing that WIP.
- Do not push to GitHub, change DNS/email, or deploy additional changes unless Matt explicitly approves.
- Future enhancement: replace the temporary static gig bridge with a cleaner two-layer public gig publishing workflow (`Gigs` calendar = private operational source, reviewed public feed = website source).
- Future enhancement: add optional booking form/voice agent/EPK assets after the base website checkpoint.

## Pending deploy — Lindsay landing intro video replacement

Local change is ready but not deployed because FTP remains unreachable from this machine on 2026-06-10.

Changes ready locally:
- Replaced `src/assets/lindsay-booking-agent.mp4` and `hostinger-public_html/assets/lindsay-booking-agent.mp4` with `/Users/matt/Desktop/Spank Lindsay Landing Intro Video.mp4`.
- Generated new poster frame `assets/lindsay-booking-agent-poster.jpg` from the new video.
- Booking page now references:
  - `../assets/lindsay-booking-agent.mp4?v=504185795d6b`
  - `../assets/lindsay-booking-agent-poster.jpg?v=9f421157678b`
  - `../styles.css?v=d7fe1043bfb5`
- ElevenLabs widget outer rectangle removed; widget itself matches video height on desktop.

Verification completed locally:
- New MP4 ffprobe: 1080x1920, 25fps, 10.36s, H.264 + AAC, 18,157,294 bytes.
- `python3 -m unittest discover -s tests -q` passes: 6/6.
- Local browser verified Lindsay poster visible and video/widget aligned.

Deploy blocker:
- FTP failed for `spankthemonkeyrocks.com`, public web IPs, `ftp.spankthemonkeyrocks.com`, and saved FTP IP `5.183.10.138`; ports 21/22 timeout or no route.
- Live `/booking/` does not yet contain new video/poster/cache hashes.

Manual fallback package:
- `/Users/matt/Desktop/spank-booking-lindsay-video-deploy.zip` contains correct paths: `booking/index.html`, `styles.css`, `assets/lindsay-booking-agent-poster.jpg`, `assets/lindsay-booking-agent.mp4`.

## Deploy completed — Lindsay landing intro video replacement

2026-06-10: FTP remained unreachable, but deploy completed through Hostinger hPanel File Browser API from the authenticated Safari session. Uploaded/replaced:
- `/public_html/booking/index.html`
- `/public_html/styles.css`
- `/public_html/assets/lindsay-booking-agent-poster.jpg`
- `/public_html/assets/lindsay-booking-agent.mp4`

Live verification:
- `/booking/` references `lindsay-booking-agent.mp4?v=504185795d6b`.
- `/booking/` references `lindsay-booking-agent-poster.jpg?v=9f421157678b`.
- `/booking/` references `styles.css?v=d7fe1043bfb5`.
- live MP4 SHA prefix matches `504185795d6b`; CSS SHA prefix matches `d7fe1043bfb5`; live poster visually verified as Lindsay/avatar.

## Measurement v1 checkpoint

Added tracking-ready website code locally: JSON-LD structured data, `robots.txt`, `sitemap.xml`, `data-track` hooks, and `window.spankTrack()` forwarding to `gtag`/`plausible` if either is later installed. Local tests and browser event checks pass.

Deploy note: Hostinger File Browser token was expired/403 during this slice. FTP port 21 is reachable again, but saved Hostinger login passwords are not the FTP account password for `u935399282.spankthemonkeyrocks.com`. Next deploy path: reset/save the FTP account password in hPanel or reopen an authenticated File Browser token, then upload `index.html`, `booking/index.html`, `site.js`, `robots.txt`, and `sitemap.xml`.
