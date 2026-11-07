(() => {
  const page = document.body.dataset.page || '';
  const arrow = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M4 12h15M13 6l6 6-6 6"/></svg>';
  const IG = 'https://www.instagram.com/sandakproduction/';
  const MAIL = 'info@sandakproduction.com';

  /* Header */
  const links = [['portfolio.html','Portfolio','portfolio'],['brollop.html','Bröllop','brollop'],['film.html','Film','film'],['branding.html','Branding & familj','branding'],['om-oss.html','Om oss','om']];
  const header = document.createElement('header');
  header.className = 'site-header' + (document.body.classList.contains('light-header') ? ' light' : '');
  header.innerHTML = `<div class="wrap">
    <a href="index.html" class="logo" aria-label="Sandak Production, startsida"><b>SANDAK</b><span>PRODUCTION</span></a>
    <nav class="nav" id="nav">${links.map(([h,t,k]) => `<a href="${h}"${k===page?' aria-current="page"':''}>${t}</a>`).join('')}
      <a href="kontakt.html" class="btn btn-solid">Boka ett möte</a></nav>
    <button class="menu-btn" aria-label="Meny" aria-controls="nav" aria-expanded="false"><span></span><span></span></button></div>`;
  document.body.prepend(header);
  const mb = header.querySelector('.menu-btn');
  mb.addEventListener('click', () => { const o = document.body.classList.toggle('menu-open'); mb.setAttribute('aria-expanded', o); });
  const onScroll = () => header.classList.toggle('solid', scrollY > 60);
  addEventListener('scroll', onScroll, {passive:true}); onScroll();

  /* Footer */
  const footer = document.createElement('footer');
  footer.className = 'footer';
  footer.innerHTML = `<div class="wrap"><div class="footer-top">
    <div><a href="index.html" class="logo"><b>SANDAK</b><span>PRODUCTION</span></a>
      <p class="big">Låt oss berätta <em>er</em> historia.</p>
      <a href="kontakt.html" class="btn btn-solid" style="margin-top:28px">Kontrollera ert datum ${arrow}</a></div>
    <div><h5>Utforska</h5><ul>${links.map(([h,t]) => `<li><a href="${h}">${t}</a></li>`).join('')}<li><a href="kontakt.html">Kontakt</a></li></ul></div>
    <div><h5>Berättelser</h5><ul><li><a href="berattelse-sara-adam.html">Sara & Adam</a></li><li><a href="berattelse-elin-marcus.html">Elin & Marcus</a></li><li><a href="portfolio.html#film">Filmer</a></li></ul></div>
    <div><h5>Kontakt</h5><ul><li><a href="mailto:${MAIL}">${MAIL}</a></li><li><a href="${IG}" target="_blank" rel="noopener">Instagram ↗</a></li><li>Stockholm, Sverige</li><li>Tillgängliga i hela Norden</li></ul></div>
  </div><div class="footer-bottom"><span>© ${new Date().getFullYear()} Sandak Production</span><span>Fotografi & film · Stockholm</span></div></div>`;
  document.body.append(footer);

  document.querySelectorAll('[data-arrow]').forEach(b => b.insertAdjacentHTML('beforeend', ' ' + arrow));

  /* Hero video rotation */
  const hv = [...document.querySelectorAll('.hero-media video')];
  const dots = document.querySelector('.hero-dots');
  if (hv.length) {
    let i = 0;
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
  document.querySelectorAll('[data-r]').forEach((el,k) => { el.style.transitionDelay = (el.dataset.r||0) + 'ms'; rio.observe(el); });

  /* Filters */
  const fb = document.querySelectorAll('.filters button');
  const applyFilter = f => {
    fb.forEach(x => x.classList.toggle('on', x.dataset.f === f));
    document.querySelectorAll('.masonry figure').forEach(fig => fig.classList.toggle('hide', f !== 'alla' && !fig.dataset.cat.split(' ').includes(f)));
  };
  fb.forEach(b => b.addEventListener('click', () => { applyFilter(b.dataset.f); history.replaceState(null,'', b.dataset.f==='alla' ? location.pathname : '#'+b.dataset.f); }));
  if (fb.length && location.hash) { const h = location.hash.slice(1); if ([...fb].some(b => b.dataset.f === h)) applyFilter(h); }

  /* Lightbox */
  const items = () => [...document.querySelectorAll('[data-lb]')].filter(f => !f.classList.contains('hide'));
  if (document.querySelector('[data-lb]')) {
    const lb = document.createElement('div');
    lb.className = 'lb'; lb.setAttribute('role','dialog'); lb.setAttribute('aria-modal','true');
    lb.innerHTML = '<div class="stage"></div><button class="x" aria-label="Stäng">✕</button><button class="prev" aria-label="Föregående">←</button><button class="next" aria-label="Nästa">→</button><div class="count"></div>';
    document.body.append(lb);
    const stage = lb.querySelector('.stage'); let cur = 0, list = [];
    stage.style.cssText = 'width:100%;height:100%;display:flex;align-items:center;justify-content:center';
    const render = () => {
      const f = list[cur]; const v = f.querySelector('video'); const im = f.querySelector('img');
      stage.innerHTML = v ? `<video src="${v.getAttribute('src') || v.querySelector('source').src}" autoplay loop muted playsinline controls></video>` : `<img src="${im.src}" alt="${im.alt}">`;
      lb.querySelector('.count').textContent = `${cur+1} / ${list.length}`;
    };
    const open = f => { list = items(); cur = list.indexOf(f); render(); lb.classList.add('on'); document.body.style.overflow='hidden'; lb.querySelector('.x').focus(); };
    const close = () => { lb.classList.remove('on'); stage.innerHTML=''; document.body.style.overflow=''; };
    const go = d => { cur = (cur + d + list.length) % list.length; render(); };
    document.addEventListener('click', e => { const f = e.target.closest('[data-lb]'); if (f) open(f); });
    lb.querySelector('.x').onclick = close; lb.querySelector('.prev').onclick = () => go(-1); lb.querySelector('.next').onclick = () => go(1);
    lb.addEventListener('click', e => { if (e.target === lb || e.target === stage) close(); });
    addEventListener('keydown', e => { if (!lb.classList.contains('on')) return; if (e.key==='Escape') close(); if (e.key==='ArrowLeft') go(-1); if (e.key==='ArrowRight') go(1); });
  }

  /* Contact form → opens e-mail with filled-in request */
  const form = document.querySelector('#bokning');
  if (form) form.addEventListener('submit', e => {
    e.preventDefault();
    const d = new FormData(form);
    const body = [...d.entries()].map(([k,v]) => `${k}: ${v}`).join('\n');
    location.href = `mailto:${MAIL}?subject=${encodeURIComponent('Förfrågan – ' + (d.get('Tjänst')||''))}&body=${encodeURIComponent(body)}`;
    form.hidden = true; document.querySelector('.form-ok').style.display = 'block';
  });
})();
