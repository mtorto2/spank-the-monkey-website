# Rebuild Plan — Spank The Monkey Website

## Goal

Replace the current Hostinger Website Builder site with a repo-controlled, polished, mobile-first site that preserves the current brand/content record and improves booking/fan conversion.

## Non-goals until approved

- No production Hostinger edits
- No DNS/email changes
- No deployment/cutover
- No public posts or external sends
- No claims about rates, availability, venues, or guarantees that Matt has not confirmed

## Phase 1 — Capture and research

Status: started.

Completed:

- Created project folder under DEV.
- Captured current live site screenshot, DOM/text/links, and accessible CDN assets.
- Wrote current-site inventory.
- Captured/reference-reviewed several rock/regional band sites.
- Wrote initial design recommendation.

Still useful:

- Manual Safari review of current site if Matt wants a human-visible archive PDF.
- Pull any original photo/logo assets from local folders if higher resolution exists than Hostinger CDN copies.

## Phase 2 — Content and assets

Needed inputs:

- Confirm approved logo file.
- Confirm best hero photo.
- Confirm current show dates and source of truth.
- Confirm desired booking CTA: email only, contact form, or both.
- Confirm whether to include EPK page/download.
- Confirm video links to feature.
- Confirm album links and preferred order.

## Phase 3 — Prototype

Recommended prototype shape:

```text
src/
  index.html
  styles.css
  site.js
  data/
    shows.json
    music.json
  assets/
    logo.png
    hero.jpg
    gallery/
```

Core sections:

1. Hero
2. Shows
3. Watch / Listen
4. About
5. Gallery
6. EPK / Booking
7. ElevenLabs voice booking assistant / lead verification card
8. Footer

Voice-agent funnel note:

- The site should include an ElevenLabs voice agent for booking requests and ad-driven landing-page traffic.
- See `notes/elevenlabs-booking-agent-plan.md` for the prompt, qualification flow, integration plan, and lead-automation path.

## Phase 4 — Verification

Before presenting as a real candidate:

- Run local static server.
- Open in browser and inspect desktop/mobile.
- Check console errors.
- Verify all internal anchors/buttons.
- Verify external links open correctly.
- Check Lighthouse-style basics if time: title, description, headings, alt text, contrast.

## Phase 5 — Deployment/cutover

Only after Matt approval:

- Choose hosting target.
- Back up current Hostinger site/DNS/email state.
- Deploy preview or staging URL first.
- Verify production candidate.
- Cut over web hosting only; preserve email records.
