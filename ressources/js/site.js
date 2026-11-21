/* Interactions du site : navigation, entrées animées, copie du courriel, barre de lecture, mode jour / nuit. */
(() => {
  'use strict';
  const root = document.documentElement;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const page = document.querySelector('main.page');

  /* Trait coloré sous l'onglet actif, qui suit la souris */
  const nav = document.querySelector('nav.tabs .links'), mark = document.querySelector('.nav-mark');
  if (nav && mark) {
    const active = () => nav.querySelector('a[aria-current="page"]');
    const place = a => {
      if (!a) { mark.style.opacity = '0'; return; }
      mark.style.left = a.offsetLeft + 'px'; mark.style.width = a.offsetWidth + 'px'; mark.style.opacity = '1';
    };
    mark.style.transition = 'none'; place(active()); void mark.offsetWidth; mark.style.transition = '';
    nav.querySelectorAll('a').forEach(a => a.addEventListener('mouseenter', () => place(a)));
    nav.addEventListener('mouseleave', () => place(active()));
    addEventListener('resize', () => place(active()));
    if (document.fonts) document.fonts.ready.then(() => place(active()));
    const cur = active();
    if (cur && cur.scrollIntoView && innerWidth < 640) cur.scrollIntoView({ block: 'nearest', inline: 'center' });
  }

  /* Navigation collante : le nom réduit apparaît à gauche */
  const tabs = document.querySelector('nav.tabs'), sentinel = document.querySelector('.sentinel');
  if (tabs && sentinel && 'IntersectionObserver' in window) {
    const links = tabs.querySelector('.links'), inner = tabs.querySelector('.tabs-in'), mini = tabs.querySelector('.mini');
    const shift = () => {
      const free = inner.clientWidth - 40 - links.offsetWidth - (mini ? mini.offsetWidth : 0);
      links.style.setProperty('--shift', Math.max(0, free / 2) + 'px');
    };
    shift(); addEventListener('resize', shift);
    if (document.fonts) document.fonts.ready.then(shift);
    new IntersectionObserver(([e]) => tabs.classList.toggle('stuck', !e.isIntersecting)).observe(sentinel);
  }

  /* Entrée en cascade du contenu, sortie douce vers une autre page */
  if (page && !reduce) {
    [...page.children].forEach((el, i) => { el.classList.add('st'); el.style.setProperty('--i', Math.min(i, 16)); });
    page.classList.add('enter');
    document.querySelectorAll('a[href$=".html"], a[href$="/"]').forEach(a => {
      if (a.target || a.origin !== location.origin) return;
      a.addEventListener('click', e => {
        if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button !== 0) return;
        if (a.pathname === location.pathname) return;
        e.preventDefault();
        page.classList.add('leave');
        setTimeout(() => { location.href = a.href; }, 210);
      });
    });
    addEventListener('pageshow', e => { if (e.persisted) page.classList.remove('leave'); });
  }

  /* Copie du courriel */
  const copyBtn = document.getElementById('copy-email');
  if (copyBtn) {
    const note = copyBtn.querySelector('.copied'), addr = copyBtn.firstChild.textContent.trim();
    const shown = msg => { note.textContent = msg; copyBtn.classList.add('done'); setTimeout(() => copyBtn.classList.remove('done'), 1800); };
    const select = () => {
      const r = document.createRange(); r.selectNodeContents(copyBtn.firstChild);
      const s = getSelection(); s.removeAllRanges(); s.addRange(r); shown(copyBtn.dataset.sel);
    };
    copyBtn.addEventListener('click', () => {
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(addr).then(() => shown(copyBtn.dataset.ok), select);
      else select();
    });
  }

  /* Barre de progression de lecture */
  const bar = document.querySelector('.readbar');
  if (bar) {
    const progress = () => {
      const h = document.documentElement.scrollHeight - innerHeight;
      bar.style.transform = 'scaleX(' + (h > 40 ? Math.min(1, scrollY / h) : 0) + ')';
    };
    addEventListener('scroll', progress, { passive: true }); addEventListener('resize', progress); progress();
  }
})();
