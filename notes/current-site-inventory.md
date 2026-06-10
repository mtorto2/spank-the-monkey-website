# Current Site Inventory — Spank The Monkey

Captured from `https://spankthemonkeyrocks.com` on 2026-06-10.

Source capture folder: `../archive/current-site/20260610-061810/`

## Capture artifacts

- `full-page-browser-screenshot.png` — visual record of the existing live site.
- `dom.html` — browser DOM capture, truncated at 200k chars by tool limit but includes key metadata/content.
- `visible-text.txt` — visible text extracted from the current page.
- `links.json` — extracted clickable links.
- `asset-manifest.json` — downloaded asset URLs and local files.
- `assets/` — downloaded Zyro/Hostinger image assets where accessible.
- `http-capture.txt` — curl headers/body attempt. First HTTP pass hit browser-check/bot-detection, then browser session loaded real page.

## Metadata found

- Title: `Spank The Monkey | Spank The Monkey`
- Description: `Rock band from Louisiana playing original and cover rock songs - 90's and 2000's including bands like Tool, Stone Temple Pilots, and more!`
- Canonical: `https://spankthemonkeyrocks.com/`
- Favicon hosted on `assets.zyrosite.com`

## Current visible structure

1. Header/nav
   - Logo
   - Home link only
2. Hero / intro
   - Large live-performance image
   - Social icons
   - Main heading: `SPANK THE MONKEY`
   - Booking email link
   - Bio paragraph
3. Energy/proof statement
   - One strong centered quote-style paragraph
4. Upcoming Dates
   - 6/29 — Fat Cat Saloon (Prairieville, LA)
   - 7/4 — Fred's On The River (Prairieville, LA)
   - 7/12 — Rock N' Bowl (Lafayette, LA)
   - 7/13 — L'Auberge Casino (Baton Rouge, LA)
   - 7/19 — Coop's On 621 (Gonzales, LA)
5. Photo gallery
   - Multiple live-performance/gallery images from Hostinger/Zyro CDN
6. Music / albums
   - White Trash Lullabies
   - 3
   - Spank The Monkey
   - Each has YouTube, Spotify, Apple/iTunes, and Amazon links
7. Contact form
   - Name
   - Last name
   - Your email*
   - Message*
   - Submit
8. Footer
   - `SPANK THE MONKEY (C) 2024`
   - Booking email
   - Social links

## Copy to preserve or rewrite

### Existing bio

> SPANK THE MONKEY has been playing its own brand of hard hitting rock & roll since 1995. Rising from the fog covered swamps of southern Louisiana, SPANK THE MONKEY created their own style of music that lead to the creation of their first album, self titled, "SPANK THE MONKEY", followed by their second release, "WHITE TRASH LULLABIES", then onto their third release, "3".

### Existing live-energy statement

> The energy and music SPANK THE MONKEY produces on stage is unreal, and they command any stage they grace. From their originals such as Sweet Daisy & Lies, to the music of greats such as Stone Temple Pilots & Tool, SPANK THE MONKEY always leaves them wanting more!

Rewrite note: keep the swamp-born Louisiana hard-rock identity and long-running credibility, but tighten grammar, punch, and booking value.

## Links captured

### Social / artist

- Facebook: `https://www.facebook.com/profile.php?id=100063495493449`
- Instagram: `https://www.instagram.com/spankthemonkeyban/`
- Spotify artist: `https://open.spotify.com/artist/5QQmPLrpzqJfXLnXwNua5G?si=ZMMGFkNcTFKZBqnOJ0IpNQ`
- Amazon artist: `https://www.amazon.com/music/player/artists/B000S2G5H2/spank-the-monkey`
- Booking email: `booking@SpankTheMonkeyRocks.com`

### Albums

#### White Trash Lullabies

- YouTube: `https://www.youtube.com/watch?v=hCH1TjU-KYA&list=OLAK5uy_mgzMQCv46AlJ-WmEZ3nQ4C4Jef3yMwY94`
- Spotify: `https://open.spotify.com/album/1IwvTInyRSVwXVHkSrHzhT?si=-GMr4JQvRkGVG7tdwn1ncA`
- Apple Music: `https://music.apple.com/us/album/white-trash-lullabies/4011732`
- Amazon: `https://www.amazon.com/music/player/albums/B000S5865S`

#### 3

- YouTube: `https://www.youtube.com/watch?v=JUj4JtGbZVc&list=OLAK5uy_lXpKgSodIKyWDW3Y6TSkMnNIYvA4K4j8w`
- Spotify: `https://open.spotify.com/album/7oNpcvnyXUqIPKFwXEpyqr?si=xvBDiCMTTJevFmPLbjK0Zg`
- Apple Music: `https://music.apple.com/us/album/3/479463039`
- Amazon: `https://www.amazon.com/music/player/albums/B006646DYG`

#### Spank The Monkey

- YouTube: `https://www.youtube.com/watch?v=ST5MF8qrT-4&list=OLAK5uy_lT6H8XCiHU5G0ioP9393pWnAH-Ivp0eb4`
- Spotify: `https://open.spotify.com/album/6oRYSzCLhXWNqmlyfQpt9I?si=N4_PfhGyTaCHqhMTyPIIig`
- Apple Music: `https://music.apple.com/us/album/spank-the-monkey/489771284`
- Amazon: `https://www.amazon.com/music/player/albums/B006NJS6WG`

## Initial assessment

### Keep

- High-energy live photography
- Dark rock-and-roll base palette
- Booking email front and center
- Dates, music, gallery, contact all on one simple path
- Louisiana / hard-rock origin story

### Improve

- Add real navigation anchors: Shows, Music, Videos, Gallery, EPK, Booking
- Make shows action-oriented: date, venue, city, ticket/RSVP/map links if available
- Add an EPK/booking section for venue buyers
- Better mobile hierarchy and stronger CTA buttons
- Replace generic contact form with a clear booking inquiry flow and direct email fallback
- Update copyright year and show data before launch
- Add SEO/social share metadata with strong OG image
- Add accessibility alt text for band/logo/gallery assets

## Open questions for Matt

1. Is this primarily a fan site, venue-booking site, or both? Recommended: both, but homepage should bias toward booking/show attendance.
2. Do we want a dedicated EPK page/download?
3. What is the updated show calendar source of truth?
4. Are current Hostinger photos/logo approved for reuse in the rebuild?
5. Should the site keep only Spank The Monkey identity, or mention related member/Matt projects anywhere? Recommended: keep entities separate unless there is a deliberate cross-link section.
