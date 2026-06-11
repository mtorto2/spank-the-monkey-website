# Spank The Monkey Website

Repo-controlled rebuild for `https://spankthemonkeyrocks.com`.

## Objective

Replace the former Hostinger Website Builder/Zyro site with a maintainable static website that can be expanded into a stronger booking funnel over time.

## Current state

- Production domain: `spankthemonkeyrocks.com`
- Platform: Hostinger PHP/HTML/static hosting
- Deploy source: `src/`
- FTP upload mirror: `hostinger-public_html/`
- Credentials: stored in 1Password only; never commit FTP/API credentials
- Booking CTA: `Booking@SpankTheMonkeyRocks.com` plus `/booking/` booking agent voice-agent landing page
- Old site capture: `archive/current-site/20260610-061810/`
- Research/design references: `research/`
- Upcoming shows: generated from Apple Calendar `Gigs` by `tools/gig_export.py`

## Approval gates

Do not do these without explicit approval:

- Change Hostinger DNS, nameservers, redirects, email records, or Titan mail settings
- Deploy production changes
- Push to GitHub or connect deployment providers
- Send client/customer-facing messages or booking tests to real inboxes unless approved
- Publish times, notes, pay, contacts, source URLs, or private calendar details from Apple Calendar

## Working folders

```text
archive/current-site/       Former live-site capture: DOM, text, links, assets, screenshots
research/                   Inspiration sites, screenshots, design notes
notes/                      Brand/content decisions, future funnel/agent plans
src/                        Static website source
hostinger-public_html/      FTP upload mirror for public_html
screenshots/                Handy screenshots copied for quick review
tests/                      Unit tests for gig export/sanitation
tools/                      Site support scripts
```

## Gig calendar update workflow

Read from Apple Calendar and regenerate the static browser data:

```bash
python3 tools/gig_export.py --days 144 --output src/gigs-data.js --index src/index.html --print
python3 -m unittest discover -s tests -v
```

Rules:

- Source calendar: Apple/iCloud `Gigs`.
- Include Spank-related dates only; exclude Matt Rich dates.
- Publish date + location only.
- Do not publish times, notes, contacts, pay, source URLs, or private calendar details.
- Use explicit venue display overrides in `tools/gig_export.py` for public-friendly venue names.
- After regenerating, sync changed files into `hostinger-public_html/`, upload only intended files, then verify live with a fresh query string.

## Current live versions

- `styles.css?v=aec2db035fdc`
- `gigs-data.js?v=cf66522bc4d6`
- `site.js?v=d475f0f0947a`

## Current booking funnel

- `/booking/` landing page embeds booking agent intro video and ElevenLabs ConvAI widget.
- Agent ID: `agent_9401ktscyd0efq1r6k7ds27xcxq3`.
- Public pricing/base-area bullets are intentionally removed from the landing page; booking agent handles lead intake.
- Root homepage CTAs route to `/booking/`; inline agent is not embedded on the root homepage.

## Future improvements

- Replace the temporary static gig bridge with a two-layer public gig publishing workflow.
- Add optional booking form/voice agent/EPK assets after the base site is checkpointed.
- Add image optimization/responsive `srcset` if performance becomes a priority.

## Measurement v1

The site ships tracking-ready event hooks without embedding vendor credentials. `site.js` exposes `window.spankTrack(eventName, props)` and forwards events to `gtag` and/or `plausible` if either analytics library is later installed. Add `?trackdebug=1` to any page to log events in the browser console.

Tracked actions include:

- booking CTA clicks
- booking email clicks
- booking agent intro video play/complete
- booking agent ElevenLabs widget clicks
- booking agent fallback link clicks
- social/music/video outbound clicks

SEO/discovery files included:

- `sitemap.xml`
- `robots.txt`
- MusicGroup/Event JSON-LD on the root page
- booking WebPage/ContactPoint JSON-LD on `/booking/`
