const shows = window.SPANK_SHOWS || [];

const escapeHtml = value => String(value).replace(/[&<>"]/g, char => ({
  '&': '&amp;',
  '<': '&lt;',
  '>': '&gt;',
  '"': '&quot;',
}[char]));

const list = document.querySelector('[data-show-list]');
if (list) {
  if (shows.length === 0) {
    list.innerHTML = `
      <article class="show-card empty-show-card">
        <div class="show-date">Shows</div>
        <div><h3>Dates are being updated</h3></div>
      </article>
    `;
  } else {
    list.innerHTML = shows.map(show => {
      const location = escapeHtml(show.location);
      const date = escapeHtml(show.date);
      return `
        <article class="show-card show-card-simple">
          <div class="show-date">${date}</div>
          <div><h3>${location}</h3></div>
        </article>
      `;
    }).join('');
  }
}

const toggle = document.querySelector('[data-nav-toggle]');
const nav = document.querySelector('[data-nav]');
if (toggle && nav) {
  toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('is-open');
    toggle.setAttribute('aria-expanded', String(open));
  });
  nav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
    nav.classList.remove('is-open');
    toggle.setAttribute('aria-expanded', 'false');
  }));
}


const trackingDebug = new URLSearchParams(window.location.search).has('trackdebug');
const normalizeTrackName = value => String(value || '').trim().replace(/[^a-zA-Z0-9_:-]+/g, '_').replace(/^_+|_+$/g, '').toLowerCase();
const collectTrackProps = element => Object.fromEntries(Object.entries(element.dataset || {})
  .filter(([key]) => key !== 'track' && key !== 'trackVideo')
  .map(([key, value]) => [key, value]));

window.spankTrack = (name, props = {}) => {
  const eventName = normalizeTrackName(name || 'interaction');
  const payload = { page_path: window.location.pathname, ...props };
  if (typeof window.gtag === 'function') {
    window.gtag('event', eventName, payload);
  }
  if (typeof window.plausible === 'function') {
    window.plausible(eventName, { props: payload });
  }
  window.dispatchEvent(new CustomEvent('spank:track', { detail: { eventName, props: payload } }));
  if (trackingDebug) {
    console.info('[spank-track]', eventName, payload);
  }
};

document.querySelectorAll('[data-track]').forEach(element => {
  element.addEventListener('click', () => {
    window.spankTrack(element.dataset.track, collectTrackProps(element));
  }, { passive: true });
});

document.querySelectorAll('video[data-track-video]').forEach(video => {
  let played = false;
  video.addEventListener('play', () => {
    if (played) return;
    played = true;
    window.spankTrack('video_play', { label: video.dataset.trackVideo });
  }, { passive: true });
  video.addEventListener('ended', () => {
    window.spankTrack('video_complete', { label: video.dataset.trackVideo });
  }, { passive: true });
});
