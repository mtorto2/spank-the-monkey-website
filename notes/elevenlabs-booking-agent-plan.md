# ElevenLabs Booking Agent Plan — Spank The Monkey

## Purpose

Use an ElevenLabs voice agent as the primary website booking assistant and as a conversion surface for social ads / Google traffic.

The agent should not be a gimmick. It should qualify real booking leads, capture structured details, verify seriousness, and route warm/active opportunities to Matt for follow-up.

## Funnel roles

1. **Website booking assistant**
   - Embedded on the site near the hero / booking / EPK sections.
   - Gives visitors a low-friction way to ask about booking the band.
   - Captures details without exposing private calendars or making commitments.

2. **Landing-page ad funnel**
   - Dedicated campaign path for Facebook/Instagram/Google ads.
   - Message match: “Book a Louisiana hard-rock band” / “Live rock for clubs, casinos, festivals, private events.”
   - Voice agent is the qualification step, with clear fallback to email.

3. **Lead verification layer**
   - Identify serious buyers vs casual fans.
   - Collect enough context for Matt to decide if follow-up is worth it.
   - Summarize inquiry in a structured lead format.

## Qualification flow

The agent should collect:

- Caller / buyer name
- Callback phone and/or email
- Event type: club, casino, festival, private party, corporate/event, other
- Venue / city / state
- Requested date and rough time window
- Expected audience size
- Desired set length / number of sets
- Production situation: house PA/lights, outdoor stage, backline, load-in constraints
- Budget range if offered; do not force too early
- Decision timeline and whether caller is the decision-maker
- Any preferred songs/style notes

## Accuracy and boundaries

The agent must:

- Never quote rates unless Matt provides approved rate ranges.
- Never confirm availability as final.
- Never create a calendar hold or booking unless a future approved tool exists.
- Never expose private calendar details.
- Say availability and pricing require Matt/band confirmation.
- Keep entities separate: this agent is for Spank The Monkey, not Matt Rich solo or Matthew Rich DJ unless Matt intentionally creates cross-sell routing.

## Availability integration path

Phase 1:

- No live availability check.
- Agent captures requested date/time and says Matt will confirm.

Phase 2:

- Add a read-only availability tool.
- Tool requires exact date, start/end or duration, and location/timezone.
- Tool returns only sanitized state: `open`, `busy`, or `needs confirmation`.
- No event titles, personal details, or calendar source names.

Phase 3:

- Optional lead routing/notification automation.
- Still no booking write/hold without explicit approval.

## Website integration

Use the ElevenLabs ConvAI widget pattern:

```html
<elevenlabs-convai agent-id="AGENT_ID"></elevenlabs-convai>
<script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
```

Recommended site placements:

- Hero CTA: “Talk to the booking assistant” / “Check date fit”
- EPK/Booking section: embedded widget card
- Dedicated `/booking` or `/book` landing page for ads

## Lead data / automation options

MVP:

- ElevenLabs conversation history + manual review.
- Website mailto fallback.

Better:

- Poll/subscribe to completed ElevenLabs conversations by agent ID.
- Classify lead state:
  - casual fan
  - incomplete inquiry
  - warm lead
  - active booking request
- Alert Matt only for warm/active leads with a compact summary.

Future:

- CRM/Airtable/Google Sheet lead log.
- Meta/Google conversion events for widget open, booking-agent start, completed lead, and warm lead.

## Prompt stance

Tone:

- Friendly, direct, energetic, professional.
- Southern Louisiana rock-and-roll edge without parody.
- Fast qualification, not long rambling.

Opening idea:

> Hey — this is the Spank The Monkey booking assistant. I can help get your event details together so Matt can confirm availability and pricing. What date and city are you looking at?

Close idea:

> Got it. I’ll package this up for Matt so he can confirm availability and pricing. If you want the fastest response, make sure I have your name, callback number, email, event date, venue/city, and rough event details.

## Build tasks

1. Update website prototype to reserve an ElevenLabs booking-agent card/section.
2. Create or identify the ElevenLabs agent.
3. Write prompt + first message + hard accuracy rules.
4. Add widget embed once `agent_id` exists.
5. Test with skeptical buyer scenarios:
   - asks for rate
   - asks if date is available
   - asks to book immediately
   - vague private party inquiry
   - venue buyer with complete info
   - casual fan asking show questions
6. Add lead-watcher automation after live widget exists.


## 2026-06-10 booking agent live widget integration

- ElevenLabs agent: `agent_9401ktscyd0efq1r6k7ds27xcxq3` (`booking agent - Spank The Monkey Booking Agent`).
- Voice: `booking agent V1 (from ads)` / `CuGMltppBgjcO4au0sa4`.
- Corrected base area: Baton Rouge / Lafayette only.
- Outside Baton Rouge / Lafayette: travel fee may apply and hotel rooms may be needed.
- Site integration: `#booking-agent` section embeds the booking agent intro MP4 and inline ElevenLabs ConvAI widget.
- Public fallback link: `https://elevenlabs.io/app/talk-to?agent_id=agent_9401ktscyd0efq1r6k7ds27xcxq3`.

## 2026-06-10 ads landing page deployment

- Live landing page: `https://spankthemonkeyrocks.com/booking/`.
- Root homepage CTAs link to `/booking/`; the root homepage intentionally does not embed the voice agent inline.
- Deployed Hostinger files: `index.html`, `styles.css`, `booking/index.html`, `assets/booking-agent.mp4`, `assets/logo-patriot.png`.
- Live verification confirmed `/booking/` contains the booking agent agent ID, widget script, and MP4 reference; public pricing/base-area bullets are intentionally removed from the page.
