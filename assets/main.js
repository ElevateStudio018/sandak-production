/* Sandak Production — behaviour (markup is generated per language by _build/build.py) */
(() => {
  const html = document.documentElement;
  const lang = html.lang || 'sv';
  const UI = {
    sv: { close: 'Stäng', prev: 'Föregående', next: 'Nästa' },
    en: { close: 'Close', prev: 'Previous', next: 'Next' }
  };
  const t = k => (UI[lang] || UI.sv)[k];
  const arrow = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>';

  /* Remember language choice */
  const store = { get(k){ try { return localStorage.getItem(k); } catch(e){ return null; } }, set(k,v){ try { localStorage.setItem(k,v); } catch(e){} } };
  document.querySelectorAll('[data-setlang]').forEach(a => a.addEventListener('click', () => store.set('sd-lang', a.dataset.setlang)));
  const saved = store.get('sd-lang');
  const fromOutside = !document.referrer || new URL(document.referrer, location.href).origin !== location.origin;
  const alt = document.querySelector(`link[rel="alternate"][hreflang="${saved}"]`);
  if (saved && saved !== lang && fromOutside && alt) { location.replace(alt.href); return; }

  /* Header */
  const header = document.querySelector('.site-header');
  const mb = header && header.querySelector('.menu-btn');
  if (mb) mb.addEventListener('click', () => { const o = document.body.classList.toggle('menu-open'); mb.setAttribute('aria-expanded', o); });
  document.querySelectorAll('.nav a').forEach(a => a.addEventListener('click', () => document.body.classList.remove('menu-open')));
  const onScroll = () => header && header.classList.toggle('solid', scrollY > 60);
  addEventListener('scroll', onScroll, {passive:true}); onScroll();

  /* Mobile contact bar */
  const bar = document.querySelector('.mobile-bar');
  if (bar) {
    const ft = () => { const nearEnd = innerHeight + scrollY > document.body.scrollHeight - 500; bar.classList.toggle('show', scrollY > innerHeight * .6 && !nearEnd); };
    addEventListener('scroll', ft, {passive:true}); ft();
  }

  document.querySelectorAll('[data-arrow]').forEach(b => b.insertAdjacentHTML('beforeend', ' ' + arrow));

  /* Hero video rotation (vertical sources on phones) */
  const hv = [...document.querySelectorAll('.hero-media video')];
  const dots = document.querySelector('.hero-dots');
  if (hv.length) {
    let i = 0;
    if (matchMedia('(max-width:640px)').matches) hv.forEach(v => { if (v.dataset.m) { v.src = v.dataset.m + '.mp4'; v.poster = v.dataset.m + '.jpg'; } });
    if (dots) dots.innerHTML = hv.map(() => '<i></i>').join('');
    const show = n => {
      hv.forEach((v,k) => { v.classList.toggle('on', k===n); if (k===n){ v.currentTime=0; v.play().catch(()=>{}); } });
      if (dots) [...dots.children].forEach((d,k) => { d.classList.remove('on'); if(k===n){ void d.offsetWidth; d.classList.add('on'); } });
    };
    show(0);
    if (hv.length > 1) setInterval(() => { i = (i+1) % hv.length; show(i); }, 7000);
  }

  /* Play inline videos only in view */
  const vio = new IntersectionObserver(es => es.forEach(e => { const v = e.target; if (e.isIntersecting) v.play().catch(()=>{}); else v.pause(); }), {threshold:.15});
  document.querySelectorAll('video[data-inview]').forEach(v => vio.observe(v));

  /* Reveal */
  const rio = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting){ e.target.classList.add('in'); rio.unobserve(e.target); } }), {threshold:.12, rootMargin:'0px 0px -40px'});
  document.querySelectorAll('[data-r]').forEach(el => { el.style.transitionDelay = (el.dataset.r||0) + 'ms'; rio.observe(el); });

  /* Portfolio tabs (Foto / Video) */
  const tabs = document.querySelectorAll('[data-tab]');
  const showTab = id => {
    tabs.forEach(b => { const on = b.dataset.tab === id; b.classList.toggle('on', on); b.setAttribute('aria-selected', on); });
    document.querySelectorAll('[data-panel]').forEach(p => { p.hidden = p.dataset.panel !== id; });
  };
  tabs.forEach(b => b.addEventListener('click', () => { showTab(b.dataset.tab); history.replaceState(null, '', '#' + b.dataset.tab); }));

  /* Filters */
  const fb = document.querySelectorAll('.filters button');
  const applyFilter = f => {
    fb.forEach(x => x.classList.toggle('on', x.dataset.f === f));
    document.querySelectorAll('.masonry figure').forEach(fig => fig.classList.toggle('hide', f !== 'alla' && !fig.dataset.cat.split(' ').includes(f)));
  };
  fb.forEach(b => b.addEventListener('click', () => applyFilter(b.dataset.f)));
  if (location.hash) {
    const h = location.hash.slice(1);
    if ([...tabs].some(b => b.dataset.tab === h)) showTab(h);
    else if ([...fb].some(b => b.dataset.f === h)) { if (tabs.length) showTab('foto'); applyFilter(h); }
  }

  /* Video project cards: preview on hover (desktop) */
  document.querySelectorAll('.vcard').forEach(c => {
    const v = c.querySelector('video');
    if (!v || matchMedia('(hover:none)').matches) return;
    c.addEventListener('mouseenter', () => v.play().catch(()=>{}));
    c.addEventListener('mouseleave', () => v.pause());
  });

  /* Lightbox (images + videos with player controls) */
  const items = () => [...document.querySelectorAll('[data-lb]')].filter(f => !f.classList.contains('hide') && !f.closest('[hidden]'));
  if (document.querySelector('[data-lb]')) {
    const lb = document.createElement('div');
    lb.className = 'lb'; lb.setAttribute('role','dialog'); lb.setAttribute('aria-modal','true');
    lb.innerHTML = `<div class="stage"></div><button class="x" aria-label="${t('close')}">✕</button><button class="prev" aria-label="${t('prev')}">←</button><button class="next" aria-label="${t('next')}">→</button><div class="count"></div>`;
    document.body.append(lb);
    const stage = lb.querySelector('.stage'); let cur = 0, list = [], last = null;
    stage.style.cssText = 'width:100%;height:100%;display:flex;align-items:center;justify-content:center';
    const render = () => {
      const f = list[cur]; const v = f.querySelector('video'); const im = f.querySelector('img');
      const title = f.dataset.title ? `<p class="lb-title">${f.dataset.title}</p>` : '';
      stage.innerHTML = v
        ? `<div class="lb-media"><video src="${v.getAttribute('src')}" poster="${v.getAttribute('poster')||''}" autoplay loop muted playsinline controls></video>${title}</div>`
        : `<div class="lb-media"><img src="${im.currentSrc || im.src}" alt="${im.alt}">${title}</div>`;
      lb.querySelector('.count').textContent = `${cur+1} / ${list.length}`;
    };
    const open = f => { last = f; list = items(); cur = Math.max(0, list.indexOf(f)); render(); lb.classList.add('on'); document.body.style.overflow='hidden'; lb.querySelector('.x').focus(); };
    const close = () => { lb.classList.remove('on'); stage.innerHTML=''; document.body.style.overflow=''; if (last && last.focus) last.focus(); };
    const go = d => { cur = (cur + d + list.length) % list.length; render(); };
    document.addEventListener('click', e => { const f = e.target.closest('[data-lb]'); if (f) { e.preventDefault(); open(f); } });
    document.addEventListener('keydown', e => { const f = e.target.closest && e.target.closest('[data-lb]'); if (f && (e.key === 'Enter' || e.key === ' ')) { e.preventDefault(); open(f); } });
    lb.querySelector('.x').onclick = close; lb.querySelector('.prev').onclick = () => go(-1); lb.querySelector('.next').onclick = () => go(1);
    lb.addEventListener('click', e => { if (e.target === lb || e.target === stage) close(); });
    let sx = 0;
    lb.addEventListener('touchstart', e => { sx = e.touches[0].clientX; }, {passive:true});
    lb.addEventListener('touchend', e => { const dx = e.changedTouches[0].clientX - sx; if (Math.abs(dx) > 50) go(dx < 0 ? 1 : -1); });
    addEventListener('keydown', e => { if (!lb.classList.contains('on')) return; if (e.key==='Escape') close(); if (e.key==='ArrowLeft') go(-1); if (e.key==='ArrowRight') go(1); });
  }

  /* Contact form → opens the visitor's e-mail app with the request filled in */
  const form = document.querySelector('#bokning');
  if (form) form.addEventListener('submit', e => {
    e.preventDefault();
    if (!form.reportValidity()) return;
    const d = new FormData(form);
    const services = d.getAll('service').join(', ');
    const lines = [...form.querySelectorAll('[data-label]')].map(el => {
      const v = el.type === 'checkbox' ? null : el.value;
      return v ? `${el.dataset.label}: ${v}` : null;
    }).filter(Boolean);
    if (services) lines.unshift(`${form.dataset.servicesLabel}: ${services}`);
    location.href = `mailto:${form.dataset.mail}?subject=${encodeURIComponent(form.dataset.subject + (services ? ' – ' + services : ''))}&body=${encodeURIComponent(lines.join('\n'))}`;
    form.hidden = true; document.querySelector('.form-ok').style.display = 'block';
  });
})();
