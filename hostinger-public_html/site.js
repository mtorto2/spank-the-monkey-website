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
