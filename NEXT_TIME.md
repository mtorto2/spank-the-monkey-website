# NEXT TIME — Spank The Monkey Website

## Resume here

- **Project:** Spank The Monkey Website
- **Production:** https://spankthemonkeyrocks.com/
- **Source:** `src/`
- **Hostinger FTP deploy mirror:** `hostinger-public_html/`
- **Branch:** `main` tracking `origin/main`
- **Last checkpoint:** `07ea0ec` — `feat: add booking inquiry form and refresh fall shows`
- **Credential posture:** Hostinger FTP credentials remain in 1Password item `Spank FTP`. Never place credentials in this repo, chat, logs, or commits.

## Verified current state — 2026-08-31

- Local `main` is clean and matches `origin/main`.
- Source and deploy mirror match for:
  - `index.html`
  - `styles.css`
  - `gigs-data.js`
  - `booking/index.html`
- Public homepage and `/booking/` both return HTTP 200.
- Homepage title: `Spank The Monkey | 90s & 2000s Rock`.
- Booking-page title: `Book Spank The Monkey | 90s & 2000s Rock Booking`.
- Homepage CTAs use **Start Booking Inquiry** and route buyers to `/booking/`.
- `/booking/` contains the booking assistant and the Formspree booking inquiry form. The current public form endpoint is intentionally visible in the HTML; it is not a credential.

## Current public positioning

- **Primary frame:** `90s & 2000s rock`.
- **Event fit:** festivals, casinos, venues, and private events.
- Louisiana / Gulf South is home-base and search context, not the primary genre label.
- Do not use `Louisiana rock`, bar-first language, or internal phrases such as `higher-paying` / `higher-value` in public copy.
- Keep entity boundaries clean: this is Spank The Monkey, not Matt Rich, Matthew Rich, Vidalia, or Wedding DJ Leadgen.

## Booking funnel

- Homepage remains music-first; it does **not** embed the assistant inline.
- `/booking/` is the dedicated inquiry page.
- Preserve parallel buyer paths:
  - booking assistant,
  - Formspree inquiry form,
  - visible booking email fallback.
- Do not add CRM/webhook chains, automated quoting, calendar holds, deposits, or lead routing without a separate approved design and ownership decision.

## Public show feed

- Source: Apple Calendar `Gigs`.
- Public output: date + venue/location only. Never ship times, notes, pay, contacts, source URLs, calendar IDs, or non-Spank events.
- Current feed contains 10 dates, from Aug. 28, 2026 through Jan. 16, 2027.
- Regenerate when the confirmed Spank calendar changes:

```bash
python3 tools/gig_export.py --days 144 --output src/gigs-data.js --index src/index.html --print
make test
```

- Then mirror only intended changed files into `hostinger-public_html/`. Deployment requires Matt's explicit approval.

## Local review

```bash
make preview  # serves src/ at http://127.0.0.1:8768/
make test
```

Before a content or funnel change, verify:

1. Source and deploy mirror parity.
2. `make test` and `git diff --check` pass.
3. Homepage and `/booking/` layout, CTA consistency, and browser-console cleanliness.
4. Public calendar payload contains only allowed fields.
5. Live HTML/CSS/data markers after an approved deployment; use curl with a cache-busting query string if Hostinger/HCDN browser checks are unreliable.

## Highest-leverage next lanes

1. **Fall promotion:** turn confirmed shows into grounded, venue-specific website/social assets.
2. **Booking proof:** add real receipts—confirmed venue/festival/casino names, an approved quote, stage plot/input list, set lengths, or EPK material. Do not invent proof.
3. **Mobile conversion pass:** audit hero, booking form, video/widget behavior, accessibility, and direct-email fallback on real phone-sized layouts.
4. **Public gigs architecture:** replace the temporary direct Calendar export bridge with a reviewed public-gigs feed when the present workflow becomes burdensome.

## Approval boundaries

Get Matt's explicit approval before:

- production uploads/deploys or Hostinger changes;
- DNS, nameserver, redirect, Titan email, or mailbox changes;
- form submissions that create a real booking-mail side effect;
- external messages, posts, booking replies, purchases, commits, or pushes;
- public pricing, availability, guarantees, venue claims, testimonials, technical specs, or calendar data beyond the approved feed.

## Useful project materials

- `README.md` — project structure and operating constraints.
- `notes/` — brand/content decisions and future funnel planning.
- `research/` — reference material and design research.
- `archive/current-site/20260610-061810/` — preserved pre-rebuild Hostinger/Zyro capture.
- `tests/test_gig_export.py` — public-gig sanitation/regression coverage.
