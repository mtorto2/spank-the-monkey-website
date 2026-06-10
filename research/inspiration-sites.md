# Website Inspiration Research — Spank The Monkey

Research started 2026-06-10 for the rebuild of `https://spankthemonkeyrocks.com`.

Screenshots are saved in `research/screenshots/`.

## Recommended design lane

Build Spank The Monkey as a **dark, high-energy Louisiana hard-rock booking site**:

- Big live-performance hero image, logo, and direct booking CTA above the fold.
- Tour/show dates as one of the first sections, not buried.
- Music and video proof close behind, with embeds/links that help both fans and venue buyers.
- Separate EPK/booking path for clubs, casinos, festivals, and private buyers.
- Gritty but clean: black/charcoal base, red/amber/acid accent, high-contrast type, large photos, restrained texture.

Avoid copying any reference site directly. Use them as pattern input.

## Current site baseline

- URL: `https://spankthemonkeyrocks.com`
- Screenshot: `../screenshots/current-site-full-page.png`
- Full archive: `../archive/current-site/20260610-061810/`

### What the current site already does well

- Has a real identity: Louisiana hard rock since 1995.
- Shows live performance energy through photos.
- Booking email is visible.
- Albums and social/music platform links are present.
- Simple one-page flow.

### What the rebuild should fix

- Stronger navigation and CTAs.
- Better buyer path: Shows / Music / Videos / EPK / Booking.
- Cleaner event cards with optional ticket/RSVP/map links.
- More polished typography and spacing.
- More useful contact/booking form.
- Accessibility: alt text, contrast, semantic headings.
- Fresh metadata/social preview.

## Reference sites reviewed

### 1. Stone Temple Pilots

- URL: `https://stonetemplepilots.com/`
- Screenshot: `screenshots/stone-temple-pilots.png`

#### Useful patterns

- Strong classic-rock legitimacy through logo + structured nav.
- Clear content buckets: News, Tour Dates, Music, Gallery, Video, Shop.
- Album/music catalog is discoverable instead of buried.
- News/grid treatment gives site a living/current feel.

#### Apply to Spank The Monkey

- Use simple, explicit nav: Home, Shows, Music, Videos, Gallery, EPK, Booking.
- Add album cards with cover art and platform buttons.
- Add a small news/update area only if Matt wants ongoing updates; otherwise don't create a maintenance burden.

#### Watch-outs

- STP's site feels legacy/content-heavy. Spank's first rebuild should stay faster and more booking-focused.

---

### 2. TOOL / Tool Army

- URL: `https://www.toolband.com/home`
- Screenshot: `screenshots/toolband.png`

#### Useful patterns

- Dark, atmospheric hard-rock direction.
- Minimal top nav focused on fan actions: News, Community, Tour, Membership, Store.
- The site makes the band feel like a world, not just a brochure.
- Strong use of negative space and mysterious art direction.

#### Apply to Spank The Monkey

- Use black/dark-charcoal as the primary frame.
- Build atmosphere through live-stage imagery, smoke/light texture, and bold logo use.
- Keep nav short and action-based.
- Consider a fan/community/email-list CTA later, but not before booking and shows are solid.

#### Watch-outs

- TOOL can be cryptic because the brand is massive. Spank's site still needs clarity for venues and local fans.
- Dark-on-dark can hurt readability; keep contrast high.

---

### 3. The Molly Ringwalds

- URL: `https://www.themollyringwalds.com/`
- Screenshot: `screenshots/molly-ringwalds.png`

#### Useful patterns

- Regional/cover-band site with clear buyer/fan sections.
- Homepage surfaces live dates, videos, press, merch/products, and social links.
- Dedicated EPK link in nav — important for booking credibility.
- Retro/party identity is memorable and consistent.

#### Apply to Spank The Monkey

- Add an EPK link/page early.
- Put live dates and video proof high on the homepage.
- Use press/social proof if available: notable venues, festivals, casino dates, quotes, local media.
- Lean into Spank's own era/style: 90s/2000s hard rock, Louisiana, swamp, grit, stage power.

#### Watch-outs

- Homepage can feel busy. Keep Spank's page more muscular and less cluttered.

---

### 4. The Chee-Weez

- URL: `https://thecheeweez.com/`
- Screenshot: `screenshots/chee-weez.png`

#### Useful patterns

- Strong regional Louisiana entertainment positioning.
- Top nav maps well to band-buyer tasks: Music, About, Shows, Videos, EPK, Contact.
- Upcoming shows have action buttons: RSVP, Notify Me, Tickets.
- Email subscribe is prominent.
- Watch/listen embeds support quick proof.

#### Apply to Spank The Monkey

- Make Shows a functional conversion section with external links where possible.
- Include a mailing-list/follow CTA after the core booking path is established.
- Add Watch and Listen sections with embedded or linked proof.
- Use EPK/Contact as primary buyer paths.

#### Watch-outs

- Heavy texture can age quickly. Use texture subtly; let live photos carry most of the energy.

---

### 5. Foo Fighters

- URL attempted: `https://www.foofighters.com/`
- Screenshot: `screenshots/foo-fighters-black-screen.png`

The browser session rendered a black/empty page after cookie handling, so this was not useful as a visual reference in this capture. Keep it in the audit trail, but do not use it as primary design input unless manually reviewed later.

## Competitive/UX recommendations

### Homepage section order

Recommended first pass:

1. Hero: logo, live-stage image, one-line positioning, Book Now / See Shows CTAs
2. Upcoming Shows: next 3-6 dates, venue, city, ticket/RSVP/map links when available
3. Watch / Listen: featured video + album/streaming cards
4. About: tightened origin story and setlist promise
5. Gallery: high-energy live photo grid
6. EPK / Booking: buyer proof, formats, contact form, direct email
7. Footer: socials, booking email, copyright, platform links

### Visual direction

- Base: black / near-black / charcoal
- Accent options: monkey-logo red, amber stage-light yellow, swamp green used sparingly
- Type: bold condensed rock headings + readable sans body
- Texture: subtle stage smoke/noise/grain, not full novelty graphics
- Motion: restrained hover effects, maybe image parallax only if performance stays good

### Buyer-focused content to gather

- Current/upcoming show feed source
- Best 8-12 live photos approved for reuse
- Best video(s): YouTube links or hosted clips
- EPK assets: stage plot, tech needs, logos, press photos, short/long bio
- Venue/festival/casino/private event booking info
- Contact form routing and anti-spam approach

### MVP rebuild stack recommendation

Start static unless Matt wants dynamic calendar/form integrations immediately:

- Static HTML/CSS/JS or Astro
- Version-controlled assets
- Simple event data file (`shows.json`) for easy updates
- Form endpoint decided later: mailto fallback first, then hosted form/API if needed
- Deployment behind explicit approval: Hostinger static, Render static/app, or another approved host

## Open design lanes for Matt to choose

1. **Recommended: Swamp-stage hard rock** — dark, gritty, photo-led, modern booking machine.
2. **Classic rock legacy** — cleaner STP-style site emphasizing discography/history/news.
3. **Regional party-rock booking** — more Chee-Weez/Molly Ringwalds: dates, EPK, subscribe, videos, bright energy.

Recommendation: combine lane 1 with lane 3's booking/event mechanics.
