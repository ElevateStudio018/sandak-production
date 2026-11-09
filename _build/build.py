#!/usr/bin/env python3
"""
Sandak Production – static site generator.

Run:  python3 _build/build.py
Writes Swedish pages to the site root and English pages to /en/.

ADDING A LANGUAGE
1. Add an entry to LANGS below (code, output folder, label).
2. Add that language code as an extra key in every L(...) call (missing keys fall back to Swedish).
3. Add UI strings for the language in assets/main.js (UI object).

CONTACT DETAILS live in SITE below – change them in one place.
"""
import os, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SITE = {
    'name': 'SanDak Production',
    'email': 'info@sandakproduction.com',          # TODO: confirm the company's real address
    'instagram': 'https://www.instagram.com/sandakproduction/',
    'ig_handle': '@sandakproduction',
    'whatsapp': '',                                 # TODO: company WhatsApp number, digits only incl. country code, e.g. 46701234567
    'phone': '',                                    # TODO: shown on the contact page when set, e.g. '+46 70 123 45 67'
    # Contact form backend (Formspree): every request is e-mailed to the owner AND stored in the Formspree dashboard.
    # Create a form at formspree.io with the owner's e-mail and paste its endpoint here, e.g. 'https://formspree.io/f/abcdwxyz'.
    # While empty, the form falls back to opening the visitor's e-mail app.
    'form_endpoint': '',
    # Social profiles – only the ones filled in are shown.
    'socials': {
        'instagram': 'https://www.instagram.com/sandakproduction/',
        'facebook': '',
        'tiktok': '',
        'youtube': '',
        'linkedin': '',
    },
    'version': '7',
}

LANGS = [
    {'code': 'sv', 'dir': '', 'label': 'Svenska', 'short': 'SV'},
    {'code': 'en', 'dir': 'en/', 'label': 'English', 'short': 'EN'},
]

def L(sv, en=None, **more):
    d = {'sv': sv, 'en': en if en is not None else sv}
    d.update(more)
    return d

class Ctx:
    lang = 'sv'; P = ''; slug = 'index.html'
C = Ctx()

def x(d):
    if isinstance(d, dict):
        return d.get(C.lang) or d['sv']
    return d

def A(path):  # asset path
    return C.P + 'assets/' + path

V = lambda n: A('video/' + n)
I = lambda n: A('img/' + n)

def wa_link():
    text = x(L('Hej SanDak Production! Jag vill gärna prata om ett projekt.', "Hi SanDak Production! I'd like to talk about a project."))
    from urllib.parse import quote
    num = SITE['whatsapp']
    return f"https://wa.me/{num}?text={quote(text)}" if num else f"https://wa.me/?text={quote(text)}"

WA_ICON = '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38a9.9 9.9 0 0 0 4.74 1.21h.01c5.46 0 9.9-4.45 9.9-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0 0 12.04 2Zm0 18.15h-.01a8.23 8.23 0 0 1-4.2-1.15l-.3-.18-3.11.82.83-3.04-.2-.31a8.2 8.2 0 0 1-1.26-4.38c0-4.54 3.7-8.23 8.25-8.23 2.2 0 4.27.86 5.83 2.42a8.18 8.18 0 0 1 2.41 5.83c0 4.54-3.7 8.22-8.24 8.22Zm4.52-6.16c-.25-.12-1.47-.72-1.69-.81-.23-.08-.39-.12-.56.13-.16.25-.64.81-.79.97-.14.17-.29.19-.54.06-.25-.12-1.05-.39-1.99-1.23-.74-.66-1.23-1.47-1.38-1.72-.14-.25-.02-.38.11-.51.11-.11.25-.29.37-.43.13-.15.17-.25.25-.42.08-.16.04-.31-.02-.43-.06-.12-.56-1.34-.76-1.84-.2-.48-.41-.42-.56-.43h-.48c-.17 0-.43.06-.66.31-.22.25-.86.85-.86 2.07 0 1.22.89 2.4 1.01 2.56.12.17 1.75 2.67 4.23 3.74.59.26 1.05.41 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.47-.6 1.67-1.18.21-.58.21-1.07.14-1.18-.06-.1-.22-.16-.47-.28Z"/></svg>'
IG_ICON = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".8" fill="currentColor"/></svg>'
SOCIAL_ICONS = {
    'instagram': IG_ICON,
    'facebook': '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M14 8h3V4h-3c-2.8 0-4.5 1.8-4.5 4.6V11H7v4h2.5v9h4v-9h3l.5-4h-3.5V8.8c0-.5.3-.8.5-.8Z"/></svg>',
    'tiktok': '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.6 2h-3.4v13.4a2.9 2.9 0 1 1-2.9-2.9c.3 0 .6 0 .9.1V9.2a6.3 6.3 0 1 0 5.4 6.2V8.7a8 8 0 0 0 4.4 1.3V6.6a4.5 4.5 0 0 1-4.4-4.6Z"/></svg>',
    'youtube': '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M23 7.2a3 3 0 0 0-2.1-2.1C19 4.6 12 4.6 12 4.6s-7 0-8.9.5A3 3 0 0 0 1 7.2 31 31 0 0 0 .5 12c0 1.6.2 3.2.5 4.8a3 3 0 0 0 2.1 2.1c1.9.5 8.9.5 8.9.5s7 0 8.9-.5a3 3 0 0 0 2.1-2.1c.3-1.6.5-3.2.5-4.8s-.2-3.2-.5-4.8ZM9.8 15.1V8.9l5.8 3.1-5.8 3.1Z"/></svg>',
    'linkedin': '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5ZM3 9.5h4V21H3V9.5Zm7 0h3.8v1.6h.1c.5-1 1.8-2 3.8-2 4 0 4.8 2.6 4.8 6V21h-4v-5.2c0-1.2 0-2.9-1.8-2.9s-2 1.4-2 2.8V21h-4V9.5Z"/></svg>',
}
SOCIAL_NAMES = {'instagram': 'Instagram', 'facebook': 'Facebook', 'tiktok': 'TikTok', 'youtube': 'YouTube', 'linkedin': 'LinkedIn'}

def social_row():
    items = ''.join(f'<a href="{u}" target="_blank" rel="noopener" aria-label="{SOCIAL_NAMES[k]}">{SOCIAL_ICONS[k]}</a>' for k, u in SITE['socials'].items() if u)
    return f'<div class="social-row">{items}</div>' if items else ''

MAIL_ICON = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>'

# ------------------------------------------------------------------ navigation
NAV = [
    ('foto.html', L('Foto', 'Photo'), 'foto'),
    ('video.html', L('Video', 'Video'), 'video'),
    ('foretag.html', L('Företag', 'Business'), 'foretag'),
    ('brollop.html', L('Bröllop', 'Weddings'), 'brollop'),
    ('portfolio.html', L('Portfolio', 'Portfolio'), 'portfolio'),
    ('om-oss.html', L('Om oss', 'About'), 'om'),
]

# The nine service areas (link targets are pages/anchors on the site)
SERVICES = [
    ('foto', 'foto.html', 'r-portrait2.jpg', L('Professionell fotografering', 'Professional photography'),
     L('Genomarbetade bilder för webb, kampanjer, press och sociala medier.', 'Considered imagery for web, campaigns, press and social media.')),
    ('video', 'video.html', 'v-crew.jpg', L('Videoproduktion', 'Video production'),
     L('Från idé och manus till inspelning, klippning och färdig film.', 'From idea and script to filming, editing and the finished film.')),
    ('reklam', 'foretag.html#reklam', 'v-cameraman.jpg', L('Företagsreklam & marknadsföring', 'Commercials & marketing'),
     L('Reklamfilm och bildmaterial som stärker ert varumärke.', 'Commercials and visual content that strengthen your brand.')),
    ('event', 'foretag.html#event', 'v-stage.jpg', L('Event', 'Events'),
     L('Konferenser, lanseringar och fester – dokumenterade på foto och film.', 'Conferences, launches and parties – documented in photo and film.')),
    ('brollop', 'brollop.html', 'p_18398510.jpg', L('Bröllop', 'Weddings'),
     L('Hela dagen på foto och film, med känsla för detaljer.', 'The whole day in photo and film, with an eye for detail.')),
    ('restaurang', 'foretag.html#restaurang', 'v-chef.jpg', L('Restauranger & hotell', 'Restaurants & hotels'),
     L('Mat, miljöer och stämning som får gäster att vilja komma.', 'Food, spaces and atmosphere that make guests want to visit.')),
    ('fastighet', 'foretag.html#fastighet', 'v-living.jpg', L('Fastighetsfotografering', 'Real estate photography'),
     L('Ljusa, rättvisande bilder och filmer av bostäder och lokaler.', 'Bright, accurate photos and films of homes and commercial spaces.')),
    ('portratt', 'foto.html#portratt', 'r-portrait.jpg', L('Porträttfotografering', 'Portrait photography'),
     L('Personliga porträtt för team, ledning och personligt varumärke.', 'Personal portraits for teams, leadership and personal brands.')),
    ('design', 'foretag.html#design', 'v-design.jpg', L('Grafisk design', 'Graphic design'),
     L('Grafiskt material som hänger ihop med era bilder och filmer.', 'Graphic material that ties in with your photos and films.')),
]

def lang_switch():
    out = []
    for lg in LANGS:
        if lg['code'] == C.lang:
            out.append(f'<span class="on" aria-current="true">{lg["short"]}</span>')
        else:
            href = ('../' if C.lang != 'sv' else '') + lg['dir'] + C.slug
            href = href.replace('index.html', '') or './'
            out.append(f'<a href="{href}" hreflang="{lg["code"]}" lang="{lg["code"]}" data-setlang="{lg["code"]}" aria-label="{lg["label"]}">{lg["short"]}</a>')
    return '<div class="lang" role="group" aria-label="Language">' + '<i></i>'.join(out) + '</div>'

def header(key):
    links = ''.join(f'<a href="{h}"{" aria-current=page" if k == key else ""}>{x(t)}</a>' for h, t, k in NAV)
    return f'''<header class="site-header{' light' if key in ('kontakt',) else ''}"><div class="wrap">
  <a href="./" class="logo" aria-label="{x(L('SanDak Production, startsida', 'SanDak Production, home'))}"><b>SANDAK</b><span>PRODUCTION</span></a>
  <nav class="nav" id="nav" aria-label="{x(L('Huvudmeny', 'Main menu'))}">{links}
    <a href="kontakt.html" class="btn btn-solid">{x(L('Kontakt', 'Contact'))}</a>
    <div class="nav-lang">{lang_switch()}</div></nav>
  <div class="head-right">{lang_switch()}
  <button class="menu-btn" aria-label="{x(L('Meny', 'Menu'))}" aria-controls="nav" aria-expanded="false"><span></span><span></span></button></div>
</div></header>'''

def footer():
    svc = ''.join(f'<li><a href="{s[1]}">{x(s[3])}</a></li>' for s in SERVICES)
    pages = ''.join(f'<li><a href="{h}">{x(t)}</a></li>' for h, t, k in NAV)
    return f'''<footer class="footer"><div class="wrap"><div class="footer-top">
  <div><a href="./" class="logo"><b>SANDAK</b><span>PRODUCTION</span></a>
    <p class="big">{x(L('Foto och film som <em>gör skillnad.</em>', 'Photo and film that <em>makes a difference.</em>'))}</p>
    <a href="kontakt.html" class="btn btn-solid" style="margin-top:28px" data-arrow>{x(L('Starta ett projekt', 'Start a project'))}</a></div>
  <div><h5>{x(L('Tjänster', 'Services'))}</h5><ul>{svc}</ul></div>
  <div><h5>{x(L('Utforska', 'Explore'))}</h5><ul>{pages}<li><a href="kontakt.html">{x(L('Kontakt', 'Contact'))}</a></li></ul></div>
  <div><h5>{x(L('Kontakt', 'Contact'))}</h5><ul>
    <li><a href="mailto:{SITE['email']}">{SITE['email']}</a></li>
    <li><a href="{wa_link()}" target="_blank" rel="noopener">WhatsApp ↗</a></li>
    {''.join(f'<li><a href="{u}" target="_blank" rel="noopener">{SOCIAL_NAMES[k]} ↗</a></li>' for k, u in SITE['socials'].items() if u)}
    {f'<li><a href="tel:{SITE["phone"].replace(" ", "")}">{SITE["phone"]}</a></li>' if SITE['phone'] else ''}
    <li>{x(L('Hela Sverige & internationellt', 'All of Sweden & internationally'))}</li></ul>
    <div style="margin-top:26px">{lang_switch()}</div></div>
</div><div class="footer-bottom"><span>© <span data-year>2026</span> SanDak Production</span><span>{x(L('Foto · Video · Design · Sedan 2011', 'Photo · Video · Design · Since 2011'))}</span></div></div></footer>'''

def contact_dock(key):
    if key == 'kontakt':
        return ''
    return f'''<div class="mobile-bar"><a href="kontakt.html" class="btn btn-solid">{x(L('Kontakta oss', 'Contact us'))}</a><a href="{wa_link()}" class="btn ig wa" target="_blank" rel="noopener" aria-label="WhatsApp">{WA_ICON}</a></div>
<a href="{wa_link()}" class="wa-float" target="_blank" rel="noopener" aria-label="{x(L('Skriv till oss på WhatsApp', 'Message us on WhatsApp'))}">{WA_ICON}<span>WhatsApp</span></a>'''

def page(slug, key, title, desc, body):
    alts = ''
    for lg in LANGS:
        href = ('../' if C.lang != 'sv' else '') + lg['dir'] + slug
        alts += f'<link rel="alternate" hreflang="{lg["code"]}" href="{href}">\n'
    html = f'''<!doctype html>
<html lang="{C.lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{x(title)} — SanDak Production</title>
<meta name="description" content="{x(desc)}">
<meta property="og:title" content="{x(title)} — SanDak Production">
<meta property="og:description" content="{x(desc)}">
<meta name="theme-color" content="#1B1916">
{alts}<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500&family=Cormorant+Garamond:ital,wght@1,400;1,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{A('style.css')}?v={SITE['version']}">
</head>
<body data-page="{key}">
<a class="skip" href="#main">{x(L('Hoppa till innehållet', 'Skip to content'))}</a>
{header(key)}
<main id="main">
{body}
</main>
{footer()}
{contact_dock(key)}
<script src="{A('main.js')}?v={SITE['version']}"></script>
</body>
</html>
'''
    out = os.path.join(ROOT, [l for l in LANGS if l['code'] == C.lang][0]['dir'], slug)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w').write(html)

# ------------------------------------------------------------------ components
def hero_page(eyebrow, h1, p, media, extra='', img=False, pos=''):
    m = (f'<img src="{I(media)}" alt="" aria-hidden="true"{pos}>' if img else
         f'<video src="{V(media)}.mp4" poster="{V(media)}.jpg" autoplay muted loop playsinline aria-hidden="true"></video>')
    return f'''<section class="page-hero">{m}
  <div class="wrap"><span class="eyebrow">{x(eyebrow)}</span><h1>{x(h1)}</h1><p>{x(p)}</p>{extra}</div>
</section>'''

def cta(h, btn=L('Starta ett projekt', 'Start a project'), media='v-event-film', eyebrow=L('Nästa steg', 'Next step')):
    return f'''<section class="cta-band">
  <video src="{V(media)}.mp4" poster="{V(media)}.jpg" muted loop playsinline data-inview aria-hidden="true"></video>
  <div class="wrap"><span class="eyebrow" data-r>{x(eyebrow)}</span><h2 data-r>{x(h)}</h2>
  <div class="ctas" data-r><a href="kontakt.html" class="btn btn-solid" data-arrow>{x(btn)}</a><a href="{wa_link()}" target="_blank" rel="noopener" class="btn btn-ghost">{WA_ICON} WhatsApp</a></div></div>
</section>'''

def media_el(src, alt=''):
    if src.endswith('.jpg'):
        return f'<img src="{I(src)}" alt="{x(alt)}" loading="lazy">'
    return f'<video src="{V(src)}.mp4" poster="{V(src)}.jpg" muted loop playsinline data-inview aria-hidden="true"></video>'

def split(eyebrow, h2, body, media, rev=False, sid='', extra='', alt='', ratio=''):
    style = f' style="aspect-ratio:{ratio}"' if ratio else ''
    return f'''<div class="split{' rev' if rev else ''}"{f' id="{sid}"' if sid else ''}>
    <div class="media" data-r{style}>{media_el(media, alt)}</div>
    <div><span class="eyebrow" data-r>{x(eyebrow)}</span><h2 class="h2-sm" style="margin:20px 0 24px" data-r>{x(h2)}</h2>
      <div data-r>{x(body)}</div>{extra}</div>
  </div>'''

def ticks(items):
    return '<ul class="ticks">' + ''.join(f'<li>{x(i)}</li>' for i in items) + '</ul>'

def svc_grid():
    cards = ''
    for n, (k, href, img, t, d) in enumerate(SERVICES, 1):
        cards += f'''<a href="{href}" class="svc-card" data-r="{(n-1)%3*90}"><div class="svc-img"><img src="{I(img)}" alt="" loading="lazy"></div>
      <div class="svc-body"><span class="svc-n">{n:02d}</span><h3>{x(t)}</h3><p>{x(d)}</p><span class="svc-more">{x(L('Läs mer', 'Learn more'))} →</span></div></a>'''
    return f'<div class="svc-grid">{cards}</div>'

def vcard(src, title, cat, vertical=False):
    return f'''<figure class="vcard{' tall' if vertical else ''}" data-lb data-title="{x(title)}" tabindex="0" role="button" aria-label="{x(L('Spela', 'Play'))}: {x(title)}" data-r>
  <video src="{V(src)}.mp4" poster="{V(src)}.jpg" muted loop playsinline preload="none"></video>
  <span class="play" aria-hidden="true"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></span>
  <figcaption><span class="vcat">{x(cat)}</span><b>{x(title)}</b></figcaption></figure>'''

def faq(qs):
    return '<div class="faq">' + ''.join(f'<details data-r><summary>{x(q)}<i></i></summary><p>{x(a)}</p></details>' for q, a in qs) + '</div>'

PROCESS = [
    (L('Ni hör av er', 'Get in touch'), L('Berätta om projektet, tidsramen och vad ni vill uppnå – via formuläret, mejl eller WhatsApp.', 'Tell us about the project, timeline and goals – via the form, e-mail or WhatsApp.')),
    (L('Idé & planering', 'Idea & planning'), L('Vi tar fram ett upplägg: koncept, platser, tidsplan och vad som ska levereras.', 'We put together a plan: concept, locations, schedule and deliverables.')),
    (L('Produktion', 'Production'), L('Fotografering och inspelning med fokus på ljus, känsla och detaljer.', 'Photography and filming with a focus on light, feeling and detail.')),
    (L('Redigering & leverans', 'Editing & delivery'), L('Bildbehandling, klippning, färg och ljud – levererat i de format ni behöver.', 'Retouching, editing, colour and sound – delivered in the formats you need.')),
]

def process_section():
    items = ''.join(f'<li data-r><span class="pn">{n:02d}</span><div><h4>{x(t)}</h4><p>{x(d)}</p></div></li>' for n, (t, d) in enumerate(PROCESS, 1))
    return f'''<section class="sec sec-sand">
  <div class="wrap process">
    <div class="process-media" data-r><video src="{V('v-crew')}.mp4" poster="{V('v-crew')}.jpg" muted loop playsinline data-inview aria-hidden="true"></video>
      <div class="process-note"><span class="serif">{x(L('”Material av hög kvalitet som överträffar förväntningarna.”', '“High-quality work that exceeds expectations.”'))}</span></div></div>
    <div>
      <span class="eyebrow" data-r>{x(L('Så arbetar vi', 'How we work'))}</span>
      <h2 class="h2-sm" style="margin:22px 0 18px" data-r>{x(L('Från första kontakt <span class="serif">till färdigt material</span>', 'From first contact <span class="serif">to finished work</span>'))}</h2>
      <p class="lead" data-r>{x(L('Ett tydligt arbetssätt, oavsett om det gäller en reklamfilm, en fastighet eller ett bröllop.', 'A clear process, whether it is a commercial, a property or a wedding.'))}</p>
      <ol class="process-list">{items}</ol>
      <a href="kontakt.html" class="btn btn-dark" style="margin-top:40px" data-r data-arrow>{x(L('Berätta om ert projekt', 'Tell us about your project'))}</a>
    </div>
  </div>
</section>'''

# ------------------------------------------------------------------ pages
def p_index():
    hero = f'''<section class="hero">
  <div class="hero-media" aria-hidden="true">
    <video muted playsinline preload="auto" poster="{V('v-event-film')}.jpg" src="{V('v-event-film')}.mp4" data-m="{V('r-portrait2')}"></video>
    <video muted playsinline preload="metadata" src="{V('v-chef')}.mp4" data-m="{V('r-grill')}"></video>
    <video muted playsinline preload="metadata" src="{V('v-living')}.mp4" data-m="{V('r-suite')}"></video>
    <video muted playsinline preload="metadata" src="{V('hero-aisle')}.mp4" data-m="{V('reel-vows')}"></video>
  </div>
  <div class="hero-inner wrap">
    <span class="eyebrow hero-eyebrow fade-in">{x(L('Foto · Video · Design', 'Photo · Video · Design'))}</span>
    <h1><span class="reveal-line"><span>{x(L('Bilder som syns.', 'Images that stand out.'))}</span></span><span class="reveal-line"><span class="serif">{x(L('Film som känns.', 'Films that move.'))}</span></span></h1>
    <p class="fade-in">{x(L('Foto- och videoproduktion sedan 2011 – för företag, restauranger, hotell, fastigheter, event och bröllop. I hela Sverige och internationellt.', 'Photo and video production since 2011 – for businesses, restaurants, hotels, real estate, events and weddings. Across Sweden and internationally.'))}</p>
    <div class="ctas fade-in">
      <a href="kontakt.html" class="btn btn-solid" data-arrow>{x(L('Starta ett projekt', 'Start a project'))}</a>
      <a href="portfolio.html" class="btn btn-ghost">{x(L('Se portfolio', 'View portfolio'))}</a>
    </div>
  </div>
  <div class="hero-meta"><div class="wrap"><span class="loc">{x(L("Hela Sverige · Internationellt", "Sweden · International"))}</span><div class="hero-dots"></div><span>{x(L('Scrolla', 'Scroll'))}</span></div></div>
</section>'''
    intro = f'''<section class="sec">
  <div class="wrap intro-grid">
    <div><span class="eyebrow" data-r>SanDak Production</span>
      <p class="statement" style="margin-top:28px" data-r>{x(L('En produktionsbyrå för <em>foto, film och design</em> – från en enskild porträttbild till en hel kampanj.', 'A production studio for <em>photo, film and design</em> – from a single portrait to a full campaign.'))}</p></div>
    <div class="side" data-r="150">
      <p>{x(L('Sedan 2011 har vi arbetat med fotografering, videoproduktion, redigering och grafisk design. Den erfarenheten använder vi för att skapa det ni behöver – för ert varumärke, er verksamhet eller ert event – och se till att ert budskap och er känsla når fram till rätt publik.', 'Since 2011 we have worked across photography, video production, editing and graphic design. We use that experience to create what you need – for your brand, your business or your event – and make sure your message and feeling reach the right audience.'))}</p>
      <p>{x(L('Målet är alltid detsamma: material av hög kvalitet som överträffar förväntningarna.', 'The goal is always the same: high-quality work that exceeds expectations.'))}</p>
      <a href="om-oss.html" class="btn btn-line" style="margin-top:12px" data-arrow>{x(L('Om oss', 'About us'))}</a>
      <div class="stats"><div><b>2011</b><span>{x(L('erfarenhet sedan', 'experience since'))}</span></div><div><b>{x(L('Sverige', 'Sweden'))}</b><span>{x(L('uppdrag i hela landet', 'assignments nationwide'))}</span></div><div><b>{x(L('Världen', 'Abroad'))}</b><span>{x(L('bl.a. Spanien', 'incl. Spain'))}</span></div></div>
    </div>
  </div>
</section>'''
    services = f'''<section class="sec sec-sand" id="tjanster">
  <div class="wrap">
    <div class="head-row">
      <div><span class="eyebrow" data-r>{x(L('Tjänster', 'Services'))}</span><h2 data-r>{x(L('Allt inom <span class="serif">bild och rörligt</span>', 'Everything in <span class="serif">image and motion</span>'))}</h2></div>
      <p class="lead" data-r="120">{x(L('Nio områden, ett team. Välj det ni behöver – eller kombinera foto, film och design i samma produktion.', 'Nine areas, one team. Choose what you need – or combine photo, film and design in a single production.'))}</p>
    </div>
    {svc_grid()}
  </div>
</section>'''
    pillars = f'''<section class="sec">
  <div class="wrap pillars">
    <a href="foto.html" class="pillar" data-r><div class="pillar-media"><img src="{I('v-studio.jpg')}" alt="{x(L('Porträttfotografering i studio', 'Portrait photography in the studio'))}" loading="lazy"></div>
      <span class="eyebrow">{x(L('Fotografering', 'Photography'))}</span><h3>{x(L('Bilder som bär ert budskap', 'Images that carry your message'))}</h3>
      <p>{x(L('Porträtt, fastigheter, restauranger, hotell, event och bröllop – redigerade för hand med ett sammanhållet uttryck.', 'Portraits, real estate, restaurants, hotels, events and weddings – hand-edited with a consistent look.'))}</p><span class="btn btn-line">{x(L('Fotografering', 'Photography'))} →</span></a>
    <a href="video.html" class="pillar" data-r="150"><div class="pillar-media"><video src="{V('v-event-film')}.mp4" poster="{V('v-event-film')}.jpg" muted loop playsinline data-inview aria-hidden="true"></video></div>
      <span class="eyebrow">{x(L('Videoproduktion', 'Video production'))}</span><h3>{x(L('Film som fångar uppmärksamhet', 'Film that captures attention'))}</h3>
      <p>{x(L('Reklamfilm, eventfilm och innehåll för sociala medier – från planering och inspelning till klippning och leverans.', 'Commercials, event films and social content – from planning and filming to editing and delivery.'))}</p><span class="btn btn-line">{x(L('Videoproduktion', 'Video production'))} →</span></a>
  </div>
</section>'''
    aud = [
        ('foretag.html#reklam', 'v-crew', L('Företag & varumärken', 'Businesses & brands'), L('Reklamfilm, bildbank och porträtt', 'Commercials, image libraries, portraits')),
        ('foretag.html#restaurang', 'r-grill', L('Restauranger & hotell', 'Restaurants & hotels'), L('Mat, miljöer och upplevelser', 'Food, spaces and experiences')),
        ('foretag.html#fastighet', 'v-living', L('Fastigheter', 'Real estate'), L('Bostäder, lokaler och objekt', 'Homes, offices and listings')),
        ('brollop.html', 'reel-embrace', L('Bröllop & privat', 'Weddings & private'), L('Hela dagen på foto och film', 'The whole day in photo and film')),
    ]
    acards = ''.join(f'<a href="{h}" class="svc" data-r="{i*100}"><video src="{V(m)}.mp4" poster="{V(m)}.jpg" muted loop playsinline data-inview aria-hidden="true"></video><span class="num">0{i+1}</span><div class="in"><h3>{x(t)}</h3><p>{x(d)}</p><span class="more">{x(L("Utforska", "Explore"))} →</span></div></a>' for i, (h, m, t, d) in enumerate(aud))
    audience = f'''<section class="sec sec-dark">
  <div class="wrap">
    <div class="head-row"><div><span class="eyebrow" data-r>{x(L('Vi arbetar med', 'Who we work with'))}</span><h2 data-r>{x(L('För verksamheter <span class="serif">och människor</span>', 'For businesses <span class="serif">and people</span>'))}</h2></div>
      <p class="lead" data-r>{x(L('Samma känsla för ljus och detaljer – anpassad efter era mål och er publik.', 'The same eye for light and detail – tailored to your goals and your audience.'))}</p></div>
    <div class="services four">{acards}</div>
    <span class="swipe-hint">{x(L('Svep för fler', 'Swipe for more'))}</span>
  </div>
</section>'''
    work = ''.join([
        vcard('v-event-film', L('Eventfilm', 'Event film'), L('Video · Event', 'Video · Event')),
        vcard('v-chef', L('Restaurang', 'Restaurant'), L('Video · Restaurang', 'Video · Restaurant')),
        vcard('v-living', L('Bostad', 'Residence'), L('Video · Fastighet', 'Video · Real estate')),
        vcard('hero-aisle', L('Vigsel', 'Ceremony'), L('Video · Bröllop', 'Video · Wedding')),
    ])
    selected = f'''<section class="sec">
  <div class="wrap">
    <div class="head-row"><div><span class="eyebrow" data-r>{x(L('Utvalt arbete', 'Selected work'))}</span><h2 data-r>{x(L('Se det <span class="serif">i rörelse</span>', 'See it <span class="serif">in motion</span>'))}</h2></div>
      <a href="portfolio.html" class="btn btn-line" data-r data-arrow>{x(L('Hela portfolion', 'Full portfolio'))}</a></div>
    <div class="vgrid">{work}</div>
  </div>
</section>'''
    body = hero + intro + services + pillars + audience + selected + process_section() + cta(L('Har ni ett projekt? <span class="serif">Låt oss prata.</span>', 'Have a project in mind? <span class="serif">Let’s talk.</span>'))
    page('index.html', 'home', L('Foto- och videoproduktion i hela Sverige', 'Photo & video production across Sweden'),
         L('SanDak Production – professionell fotografering, videoproduktion, företagsreklam, event, bröllop, restauranger, hotell, fastigheter, porträtt och grafisk design – i hela Sverige och internationellt, bland annat i Spanien.',
           'SanDak Production – professional photography, video production, commercials, events, weddings, restaurants, hotels, real estate, portraits and graphic design – across Sweden and internationally, including Spain.'), body)

def p_foto():
    areas = [
        ('portratt', 'r-portrait.jpg', L('Porträtt', 'Portraits'), L('Porträtt <span class="serif">med personlighet</span>', 'Portraits <span class="serif">with personality</span>'),
         L('<p>Porträtt för ledning och medarbetare, talare, kreatörer och personligt varumärke. I studio, på kontoret eller på en plats som säger något om er.</p>', '<p>Portraits for leadership and staff, speakers, creatives and personal brands. In the studio, at the office or in a location that says something about you.</p>'),
         [L('Företagsporträtt och teambilder', 'Corporate and team portraits'), L('Personligt varumärke', 'Personal branding'), L('Enhetlig stil för hela organisationen', 'Consistent style across the organisation')]),
        ('fastighet', 'v-kitchen.jpg', L('Fastighet', 'Real estate'), L('Rum som <span class="serif">säljer sig själva</span>', 'Spaces that <span class="serif">sell themselves</span>'),
         L('<p>Ljusa och rättvisande bilder av bostäder, lokaler och kommersiella fastigheter – för mäklare, fastighetsägare och arkitekter.</p>', '<p>Bright, accurate images of homes, offices and commercial property – for agents, property owners and architects.</p>'),
         [L('Bostäder och lokaler', 'Homes and commercial spaces'), L('Interiör och exteriör', 'Interior and exterior'), L('Kan kombineras med film', 'Can be combined with film')]),
        ('restaurang', 'v-flame.jpg', L('Restaurang & hotell', 'Restaurants & hotels'), L('Smak, miljö <span class="serif">och stämning</span>', 'Taste, space <span class="serif">and atmosphere</span>'),
         L('<p>Mat, dryck, interiörer och människorna bakom – bilder för menyer, webb, bokningssajter och sociala medier.</p>', '<p>Food, drinks, interiors and the people behind them – images for menus, websites, booking platforms and social media.</p>'),
         [L('Mat- och dryckesfoto', 'Food and drink photography'), L('Interiör och rum', 'Interiors and rooms'), L('Personal och gästupplevelse', 'Staff and guest experience')]),
        ('event', 'v-audience.jpg', L('Event', 'Events'), L('Dokumentation <span class="serif">som lever vidare</span>', 'Coverage <span class="serif">that lives on</span>'),
         L('<p>Konferenser, lanseringar, mässor och fester. Vi rör oss diskret och fångar både helheten och de små ögonblicken.</p>', '<p>Conferences, launches, trade shows and parties. We move discreetly and capture both the big picture and the small moments.</p>'),
         [L('Konferenser och föreläsningar', 'Conferences and talks'), L('Lanseringar och fester', 'Launches and parties'), L('Snabbt urval för sociala medier', 'Quick selection for social media')]),
    ]
    blocks = ''.join(split(e, h, x(b) + ticks(t), img, rev=i % 2 == 1, sid=k) for i, (k, img, e, h, b, t) in enumerate(areas))
    strip = ''.join(f'<figure class="tall" data-lb data-r="{i*80}"><img src="{I(s)}" alt="" loading="lazy"></figure>' for i, s in enumerate(['r-portrait2.jpg', 'r-hotel.jpg', 's-vows.jpg']))
    body = hero_page(L('Fotografering', 'Photography'), L('Fotografering <span class="serif">med känsla.</span>', 'Photography <span class="serif">with feeling.</span>'),
                     L('Professionella bilder för företag, verksamheter och privatpersoner – planerade, fotograferade och redigerade med omsorg.', 'Professional images for businesses and individuals – planned, photographed and edited with care.'),
                     'v-studio') + f'''
<section class="sec"><div class="wrap intro-grid">
  <p class="statement" data-r>{x(L('Bra bilder gör mer än att visa. De <em>berättar</em> vem ni är.', 'Good images do more than show. They <em>tell</em> people who you are.'))}</p>
  <div class="side" data-r="150"><p>{x(L('Vi arbetar med naturligt ljus när det finns och kompletterar med ljussättning när det behövs. Varje bild redigeras för att passa ert uttryck och era kanaler.', 'We work with natural light where possible and add lighting when needed. Every image is edited to fit your look and your channels.'))}</p>
  <a href="portfolio.html#foto" class="btn btn-line" style="margin-top:12px" data-arrow>{x(L('Se fotoportfolio', 'View photo portfolio'))}</a></div>
</div></section>
<section class="sec sec-sand"><div class="wrap stack">{blocks}</div></section>
<section class="sec"><div class="wrap">
  <div class="head-row"><div><span class="eyebrow" data-r>{x(L('Även', 'Also'))}</span><h2 data-r>{x(L('Bröllop <span class="serif">och privat</span>', 'Weddings <span class="serif">and private</span>'))}</h2></div><a href="brollop.html" class="btn btn-line" data-r data-arrow>{x(L('Bröllop', 'Weddings'))}</a></div>
  <div class="gallery-rows"><div class="row r3">{strip}</div></div>
</div></section>
''' + cta(L('Behöver ni <span class="serif">nya bilder?</span>', 'Need <span class="serif">new images?</span>'), media='v-studio')
    page('foto.html', 'foto', L('Fotografering', 'Photography'), L('Porträtt-, fastighets-, restaurang-, hotell- och eventfotografering i hela Sverige och internationellt.', 'Portrait, real estate, restaurant, hotel and event photography across Sweden and internationally.'), body)

def p_video():
    types = [
        ('v-cameraman', L('Reklamfilm & varumärkesfilm', 'Commercials & brand films'), L('Film som presenterar er verksamhet, er produkt eller ert erbjudande.', 'Films that present your business, product or offer.')),
        ('r-portrait2', L('Sociala medier', 'Social media'), L('Korta, vertikala klipp anpassade för Instagram, TikTok och Reels.', 'Short vertical clips made for Instagram, TikTok and Reels.')),
        ('v-stage', L('Eventfilm', 'Event films'), L('Från konferens till fest – en sammanfattning eller hela föreläsningar.', 'From conference to party – a highlight film or full-length talks.')),
        ('v-chef', L('Restaurang & hotell', 'Restaurants & hotels'), L('Stämningsfulla filmer som får gäster att vilja boka.', 'Atmospheric films that make guests want to book.')),
        ('v-home', L('Fastighetsfilm', 'Property films'), L('Visningsfilmer som ger en känsla för rum och flöde.', 'Walkthrough films that convey space and flow.')),
        ('reel-embrace', L('Bröllopsfilm', 'Wedding films'), L('Dagens berättelse med löften, tal och musik.', 'The story of the day with vows, speeches and music.')),
    ]
    tcards = ''.join(f'<div class="type" data-r="{i%3*90}"><div class="type-media">{media_el(m)}</div><h3>{x(t)}</h3><p>{x(d)}</p></div>' for i, (m, t, d) in enumerate(types))
    steps = [
        (L('Förproduktion', 'Pre-production'), L('Mål, idé, manus, platser och tidsplan.', 'Goals, idea, script, locations and schedule.')),
        (L('Inspelning', 'Filming'), L('Bild, ljus och ljud på plats.', 'Picture, light and sound on location.')),
        (L('Postproduktion', 'Post-production'), L('Klippning, färgsättning, ljud och grafik.', 'Editing, colour grading, sound and graphics.')),
        (L('Leverans', 'Delivery'), L('Versioner och format för varje kanal.', 'Versions and formats for every channel.')),
    ]
    st = ''.join(f'<div class="step" data-r="{i*100}"><i>0{i+1}</i><h4>{x(t)}</h4><p>{x(d)}</p></div>' for i, (t, d) in enumerate(steps))
    reels = ''.join(f'<div class="reel" data-r="{i*100}"><video src="{V(m)}.mp4" poster="{V(m)}.jpg" muted loop playsinline data-inview></video><span class="lbl">{x(t)}</span></div>' for i, (m, t) in enumerate([
        ('r-grill', L('Restaurang', 'Restaurant')), ('r-hotel', L('Hotell', 'Hotel')), ('r-portrait', L('Porträtt', 'Portrait')), ('reel-vows', L('Bröllop', 'Wedding'))]))
    body = hero_page(L('Videoproduktion', 'Video production'), L('Film som <span class="serif">fångar.</span>', 'Film that <span class="serif">captures.</span>'),
                     L('Reklamfilm, eventfilm och innehåll för sociala medier – producerat från idé till färdig leverans.', 'Commercials, event films and social content – produced from idea to final delivery.'),
                     'v-crew', extra=f'<div class="hero-btns"><a href="kontakt.html" class="btn btn-solid" data-arrow>{x(L("Starta ett projekt", "Start a project"))}</a><a href="portfolio.html#video" class="btn btn-ghost">{x(L("Se filmer", "Watch films"))}</a></div>') + f'''
<section class="sec"><div class="wrap">
  <div class="head-row"><div><span class="eyebrow" data-r>{x(L('Det vi producerar', 'What we produce'))}</span><h2 data-r>{x(L('Film för <span class="serif">varje behov</span>', 'Film for <span class="serif">every need</span>'))}</h2></div>
    <p class="lead" data-r>{x(L('Vi anpassar format, längd och uttryck efter var filmen ska visas och vem den ska nå.', 'We adapt format, length and style to where the film will be shown and who it needs to reach.'))}</p></div>
  <div class="types">{tcards}</div>
</div></section>
<section class="sec sec-dark"><div class="wrap">
  <div class="head-row"><div><span class="eyebrow" data-r>{x(L('Vertikalt', 'Vertical'))}</span><h2 data-r>{x(L('Gjort för <span class="serif">mobilen</span>', 'Made for <span class="serif">mobile</span>'))}</h2></div>
    <p class="lead" data-r>{x(L('Korta klipp i 9:16 för sociala medier – levererade separat eller som komplement till en längre film.', 'Short 9:16 clips for social media – delivered on their own or alongside a longer film.'))}</p></div>
  <div class="reels">{reels}</div><span class="swipe-hint">{x(L('Svep för fler', 'Swipe for more'))}</span>
</div></section>
<section class="sec sec-sand"><div class="wrap">
  <div class="head-row"><div><span class="eyebrow" data-r>{x(L('Produktion', 'Production'))}</span><h2 data-r>{x(L('Från idé <span class="serif">till leverans</span>', 'From idea <span class="serif">to delivery</span>'))}</h2></div></div>
  <div class="steps light">{st}</div>
</div></section>
''' + cta(L('Vad vill ni <span class="serif">berätta?</span>', 'What do you want <span class="serif">to say?</span>'), media='v-cameraman')
    page('video.html', 'video', L('Videoproduktion', 'Video production'), L('Reklamfilm, eventfilm, fastighetsfilm och video för sociala medier – i hela Sverige och internationellt.', 'Commercials, event films, property films and social media video – across Sweden and internationally.'), body)

def p_foretag():
    secs = [
        ('reklam', 'v-cameraman', L('Företagsreklam & marknadsföring', 'Commercials & marketing'), L('Synas, <span class="serif">och bli ihågkommen</span>', 'Be seen, <span class="serif">and remembered</span>'),
         L('<p>Reklamfilm, kampanjbilder och löpande innehåll för webb och sociala medier. Vi tar fram material som speglar ert varumärke och når fram till rätt målgrupp.</p>', '<p>Commercials, campaign imagery and ongoing content for web and social media. We create material that reflects your brand and reaches the right audience.</p>'),
         [L('Reklam- och varumärkesfilm', 'Commercials and brand films'), L('Bildbank för webb och press', 'Image library for web and press'), L('Innehåll för sociala medier', 'Social media content')]),
        ('restaurang', 'v-chef', L('Restauranger & hotell', 'Restaurants & hotels'), L('Gör gästen <span class="serif">sugen</span>', 'Make guests <span class="serif">want to come</span>'),
         L('<p>Foto och film av mat, dryck, rum och miljöer – för menyer, webbplats, bokningssajter och sociala kanaler.</p>', '<p>Photo and film of food, drinks, rooms and spaces – for menus, websites, booking platforms and social channels.</p>'),
         [L('Mat- och dryckesfoto', 'Food and drink photography'), L('Hotellrum, lobby och miljöer', 'Hotel rooms, lobbies and spaces'), L('Stämningsfilmer och reels', 'Mood films and reels')]),
        ('fastighet', 'v-living', L('Fastigheter', 'Real estate'), L('Visa rummen <span class="serif">från sin bästa sida</span>', 'Show every space <span class="serif">at its best</span>'),
         L('<p>Fastighetsfotografering och visningsfilm för mäklare, fastighetsägare och förvaltare – bostäder, kontor och kommersiella lokaler.</p>', '<p>Real estate photography and walkthrough films for agents, owners and property managers – homes, offices and commercial spaces.</p>'),
         [L('Interiör och exteriör', 'Interior and exterior'), L('Visningsfilm', 'Walkthrough film'), L('Bostäder och lokaler', 'Homes and commercial spaces')]),
        ('event', 'v-stage', L('Event', 'Events'), L('Ert event, <span class="serif">långt efteråt</span>', 'Your event, <span class="serif">long after</span>'),
         L('<p>Foto och film från konferenser, lanseringar, kundevent och personalfester – för internkommunikation, marknadsföring och minnen.</p>', '<p>Photo and film from conferences, launches, client events and staff parties – for internal communication, marketing and memories.</p>'),
         [L('Konferens och föreläsning', 'Conferences and talks'), L('Sammanfattningsfilm', 'Highlight film'), L('Bilder för sociala medier', 'Images for social media')]),
        ('design', 'v-design', L('Grafisk design', 'Graphic design'), L('Grafik som <span class="serif">hänger ihop</span>', 'Graphics that <span class="serif">fit together</span>'),
         L('<p>Grafiskt material som kompletterar era bilder och filmer, så att uttrycket blir enhetligt i alla kanaler.</p>', '<p>Graphic material that complements your photos and films, so your look stays consistent across every channel.</p>'),
         [L('Grafik för sociala medier', 'Social media graphics'), L('Trycksaker och presentationer', 'Print and presentations'), L('Grafik och text i film', 'Graphics and titles in film')]),
    ]
    blocks = ''.join(split(e, h, x(b) + ticks(t), m, rev=i % 2 == 1, sid=k) for i, (k, m, e, h, b, t) in enumerate(secs))
    nav = ''.join(f'<a href="#{k}">{x(e)}</a>' for k, m, e, h, b, t in secs)
    body = hero_page(L('För företag', 'For business'), L('Foto och film <span class="serif">för er verksamhet.</span>', 'Photo and film <span class="serif">for your business.</span>'),
                     L('För företag, restauranger, hotell och fastighetsägare som vill synas med bilder och filmer som håller hög kvalitet.', 'For businesses, restaurants, hotels and property owners who want to stand out with high-quality images and films.'),
                     'v-stage', extra=f'<div class="hero-btns"><a href="kontakt.html" class="btn btn-solid" data-arrow>{x(L("Begär offert", "Request a quote"))}</a></div>') + f'''
<nav class="subnav" aria-label="{x(L('Områden', 'Areas'))}"><div class="wrap">{nav}</div></nav>
<section class="sec"><div class="wrap stack">{blocks}</div></section>
''' + process_section() + cta(L('Låt oss ta fram <span class="serif">ett upplägg.</span>', 'Let’s put together <span class="serif">a plan.</span>'), btn=L('Begär offert', 'Request a quote'), media='v-audience')
    page('foretag.html', 'foretag', L('För företag', 'For business'), L('Företagsreklam, marknadsföring, restaurang- och hotellfoto, fastighetsfotografering, event och grafisk design.', 'Commercials, marketing, restaurant and hotel photography, real estate, events and graphic design.'), body)

def p_brollop():
    opts = [
        (L('Foto', 'Photo'), L('Från förberedelser och vigsel till porträtt och fest – ett redigerat galleri att spara och dela.', 'From getting ready and the ceremony to portraits and the party – an edited gallery to keep and share.')),
        (L('Film', 'Film'), L('En bröllopsfilm med löften, tal och musik, samt korta klipp för sociala medier.', 'A wedding film with vows, speeches and music, plus short clips for social media.')),
        (L('Foto + film', 'Photo + film'), L('Ett samspelt team som planerar och arbetar tillsammans under hela dagen.', 'A coordinated team that plans and works together throughout the day.')),
    ]
    oc = ''.join(f'<div class="pkg{" feat" if i == 2 else ""}" data-r="{i*100}"><h3>{x(t)}</h3><p class="price">{x(L("Anpassas efter er dag", "Tailored to your day"))}</p><p>{x(d)}</p><a href="kontakt.html" class="btn {"btn-solid" if i == 2 else "btn-line"}">{x(L("Begär offert", "Request a quote"))}</a></div>' for i, (t, d) in enumerate(opts))
    projects = f'''<div class="stories">
      <a href="projekt-skogsbrollop.html" class="story" data-r><div class="img"><video src="{V('reel-embrace')}.mp4" poster="{V('reel-embrace')}.jpg" muted loop playsinline data-inview></video></div><div class="meta"><h3>{x(L('Skogsbröllop', 'Forest wedding'))}</h3><span>{x(L('Foto + film', 'Photo + film'))}</span></div></a>
      <a href="projekt-sommarvigsel.html" class="story" data-r="150"><div class="img"><img src="{I('s-vows.jpg')}" alt="" loading="lazy"></div><div class="meta"><h3>{x(L('Sommarvigsel', 'Summer ceremony'))}</h3><span>{x(L('Foto + film', 'Photo + film'))}</span></div></a>
    </div><span class="swipe-hint">{x(L('Svep för fler', 'Swipe for more'))}</span>'''
    body = hero_page(L('Bröllop', 'Weddings'), L('Hela dagen. <span class="serif">Alla känslor.</span>', 'The whole day. <span class="serif">Every feeling.</span>'),
                     L('Foto, film eller båda – från förberedelser till sista dansen.', 'Photo, film or both – from getting ready to the last dance.'), 'hero-aisle',
                     extra=f'<div class="hero-btns"><a href="kontakt.html" class="btn btn-solid" data-arrow>{x(L("Fråga om ert datum", "Ask about your date"))}</a><a href="#upplagg" class="btn btn-ghost">{x(L("Upplägg", "Options"))}</a></div>') + f'''
<section class="sec"><div class="wrap">{split(L('Vårt sätt', 'Our approach'), L('Diskret när det behövs, <span class="serif">närvarande</span> hela tiden', 'Discreet when needed, <span class="serif">present</span> throughout'),
    L('<p class="lead">De bästa bilderna kommer när ni glömmer att vi är där. Vi arbetar lugnt i bakgrunden och tar oss tid för porträtten när ljuset är som vackrast.</p><p>Vi går igenom tidsplanen tillsammans med er innan dagen, så att ni kan vara närvarande när det väl gäller.</p>',
      '<p class="lead">The best images happen when you forget we’re there. We work calmly in the background and take time for portraits when the light is at its best.</p><p>We go through the timeline with you beforehand, so you can be fully present on the day.</p>'),
    'p_18398510.jpg')}</div></section>
<section class="sec sec-dark"><div class="wrap">
  <div class="head-row"><div><span class="eyebrow" data-r>{x(L('Dagen', 'The day'))}</span><h2 data-r>{x(L('Från förberedelser <span class="serif">till fest</span>', 'From getting ready <span class="serif">to the party</span>'))}</h2></div></div>
  <div class="steps">
    <div class="step" data-r><i>I</i><h4>{x(L('Förberedelser', 'Getting ready'))}</h4><p>{x(L('Detaljer, klädsel och stunderna innan.', 'Details, outfits and the moments before.'))}</p></div>
    <div class="step" data-r="100"><i>II</i><h4>{x(L('Vigseln', 'Ceremony'))}</h4><p>{x(L('Löften, ringar och gästernas reaktioner.', 'Vows, rings and your guests’ reactions.'))}</p></div>
    <div class="step" data-r="200"><i>III</i><h4>{x(L('Porträtt', 'Portraits'))}</h4><p>{x(L('En avslappnad stund för er två.', 'A relaxed moment for the two of you.'))}</p></div>
    <div class="step" data-r="300"><i>IV</i><h4>{x(L('Middag & fest', 'Dinner & party'))}</h4><p>{x(L('Tal, skratt och första dansen.', 'Speeches, laughter and the first dance.'))}</p></div>
  </div>
</div></section>
<section class="sec sec-sand" id="upplagg"><div class="wrap">
  <div class="head-row"><div><span class="eyebrow" data-r>{x(L('Upplägg', 'Options'))}</span><h2 data-r>{x(L('Välj det som <span class="serif">passar er</span>', 'Choose what <span class="serif">suits you</span>'))}</h2></div>
    <p class="lead" data-r>{x(L('Varje bröllop är olika. Berätta om er dag så tar vi fram ett förslag och en offert.', 'Every wedding is different. Tell us about your day and we’ll send a proposal and quote.'))}</p></div>
  <div class="packages">{oc}</div>
</div></section>
<section class="sec"><div class="wrap">
  <div class="head-row"><div><span class="eyebrow" data-r>{x(L('Projekt', 'Projects'))}</span><h2 data-r>{x(L('Bröllop <span class="serif">i bild och film</span>', 'Weddings <span class="serif">in photo and film</span>'))}</h2></div><a href="portfolio.html#brollop" class="btn btn-line" data-r data-arrow>{x(L('Fler bilder', 'More images'))}</a></div>
  {projects}
</div></section>
<section class="sec sec-sand"><div class="wrap narrow">
  <span class="eyebrow" data-r>{x(L('Vanliga frågor', 'FAQ'))}</span><h2 class="h2-sm" style="margin:22px 0 40px" data-r>{x(L('Bra att <span class="serif">veta</span>', 'Good <span class="serif">to know</span>'))}</h2>
  {faq([
    (L('Hur långt i förväg bör vi höra av oss?', 'How far in advance should we get in touch?'), L('Så snart ni har ett datum. Populära helger under sommaren bokas ofta tidigt.', 'As soon as you have a date. Popular summer weekends tend to book up early.')),
    (L('Var tar ni uppdrag?', 'Where do you work?'), L('I hela Sverige, och vi tar även internationella uppdrag – bland annat i Spanien. Hör av er med plats och datum så återkommer vi med ett förslag.', 'All over Sweden, and we also take international assignments – including in Spain. Send us the location and date and we’ll come back with a proposal.')),
    (L('Kan vi boka både foto och film?', 'Can we book both photo and film?'), L('Absolut. Då planerar och arbetar foto och film tillsammans under dagen.', 'Absolutely. Photo and film then plan and work together throughout the day.')),
    (L('Hur bokar vi?', 'How do we book?'), L('Skicka en förfrågan via formuläret, mejl eller WhatsApp. Vi går igenom upplägget och skickar en offert.', 'Send a request via the form, e-mail or WhatsApp. We’ll go through the details and send a quote.')),
  ])}
</div></section>
''' + cta(L('Låt oss planera <span class="serif">er dag.</span>', 'Let’s plan <span class="serif">your day.</span>'), btn=L('Fråga om ert datum', 'Ask about your date'), media='hero-sunset')
    page('brollop.html', 'brollop', L('Bröllopsfoto & bröllopsfilm', 'Wedding photography & film'), L('Bröllopsfotografering och bröllopsfilm i hela Sverige och utomlands, bland annat i Spanien.', 'Wedding photography and films across Sweden and abroad, including Spain.'), body)

def p_portfolio():
    cats = [('alla', L('Alla', 'All')), ('portratt', L('Porträtt', 'Portraits')), ('fastighet', L('Fastighet', 'Real estate')), ('restaurang', L('Restaurang & hotell', 'Restaurants & hotels')),
            ('event', L('Event', 'Events')), ('foretag', L('Företag', 'Business')), ('brollop', L('Bröllop', 'Weddings'))]
    photos = [
        ('portratt', 'r-portrait2.jpg', L('Porträtt i studio', 'Studio portrait')), ('fastighet', 'v-living.jpg', L('Vardagsrum', 'Living room')),
        ('restaurang', 'v-chef.jpg', L('Öppet kök', 'Open kitchen')), ('brollop', 'p_18398510.jpg', L('Brudpar', 'Wedding couple')),
        ('event', 'v-stage.jpg', L('Föreläsning', 'Keynote')), ('restaurang', 'r-hotel.jpg', L('Hotellmiljö', 'Hotel interior')),
        ('foretag', 'v-crew.jpg', L('Filmproduktion', 'Film production')), ('fastighet', 'v-kitchen.jpg', L('Kök & matplats', 'Kitchen & dining')),
        ('portratt', 'r-portrait.jpg', L('Porträtt', 'Portrait')), ('brollop', 's-vows.jpg', L('Vigsel', 'Ceremony')),
        ('restaurang', 'r-grill.jpg', L('Grill', 'Grill')), ('event', 'v-audience.jpg', L('Konferens', 'Conference')),
        ('foretag', 'v-design.jpg', L('Grafisk design', 'Graphic design')), ('restaurang', 'r-suite.jpg', L('Svit', 'Suite')),
        ('brollop', 's-embrace1.jpg', L('Skogsbröllop', 'Forest wedding')), ('fastighet', 'v-home.jpg', L('Villa', 'Villa')),
        ('portratt', 'v-studio.jpg', L('Studiofotografering', 'Studio session')), ('restaurang', 'v-flame.jpg', L('Kök i arbete', 'Kitchen at work')),
        ('event', 'v-event-film.jpg', L('Eventdokumentation', 'Event coverage')), ('brollop', 'p_1801263.jpg', L('Porträtt', 'Portrait')),
        ('foretag', 'v-cameraman.jpg', L('Bakom kameran', 'Behind the camera')), ('restaurang', 'v-lobby.jpg', L('Lobby', 'Lobby')),
        ('brollop', 's-cer1.jpg', L('Vigsel', 'Ceremony')), ('foretag', 'v-tablet.jpg', L('Design', 'Design')),
        ('brollop', 's-sunset.jpg', L('Solnedgång', 'Sunset')), ('brollop', 's-exit.jpg', L('Utgången', 'Exit')),
    ]
    figs = ''.join(f'<figure data-cat="{c}" data-lb data-title="{x(t)}" tabindex="0" data-r><img src="{I(s)}" alt="{x(t)}" loading="lazy"><figcaption><span>{x(t)}</span><span>↗</span></figcaption></figure>' for c, s, t in photos)
    fbtn = ''.join(f'<button data-f="{k}"{" class=on" if k == "alla" else ""}>{x(t)}</button>' for k, t in cats)
    land = ''.join([
        vcard('v-event-film', L('Eventfilm', 'Event film'), L('Event', 'Event')),
        vcard('v-crew', L('Bakom kulisserna', 'Behind the scenes'), L('Produktion', 'Production')),
        vcard('v-chef', L('Restaurangfilm', 'Restaurant film'), L('Restaurang', 'Restaurant')),
        vcard('v-living', L('Visningsfilm', 'Walkthrough film'), L('Fastighet', 'Real estate')),
        vcard('v-stage', L('Konferens', 'Conference'), L('Event', 'Event')),
        vcard('v-lobby', L('Hotellmiljö', 'Hotel atmosphere'), L('Hotell', 'Hotel')),
        vcard('v-design', L('Grafik i rörelse', 'Motion graphics'), L('Design', 'Design')),
        vcard('hero-aisle', L('Vigsel', 'Ceremony'), L('Bröllop', 'Wedding')),
    ])
    vert = ''.join([
        vcard('r-grill', L('Grillen', 'The grill'), L('Restaurang', 'Restaurant'), True),
        vcard('r-hotel', L('Hotell', 'Hotel'), L('Hotell', 'Hotel'), True),
        vcard('r-portrait', L('Porträtt', 'Portrait'), L('Porträtt', 'Portrait'), True),
        vcard('reel-embrace', L('Skogsbröllop', 'Forest wedding'), L('Bröllop', 'Wedding'), True),
    ])
    body = hero_page(L('Portfolio', 'Portfolio'), L('Foto <span class="serif">&amp;</span> video', 'Photo <span class="serif">&amp;</span> video'),
                     L('Ett urval av bilder och filmer. Välj foto eller video och klicka för att öppna i fullstorlek.', 'A selection of photos and films. Choose photo or video and click to open full size.'), 'v-event-film') + f'''
<section class="sec" style="padding-top:clamp(50px,6vw,90px)"><div class="wrap">
  <div class="tabs" role="tablist" aria-label="{x(L('Typ av arbete', 'Type of work'))}">
    <button role="tab" data-tab="foto" class="on" aria-selected="true">{x(L('Foto', 'Photo'))} <small>{len(photos)}</small></button>
    <button role="tab" data-tab="video" aria-selected="false">Video <small>{12}</small></button>
  </div>
  <div data-panel="foto">
    <div class="filters" role="group" aria-label="{x(L('Filtrera', 'Filter'))}">{fbtn}</div>
    <div class="masonry">{figs}</div>
  </div>
  <div data-panel="video" hidden>
    <h3 class="panel-h">{x(L('Liggande film', 'Landscape films'))}</h3>
    <div class="vgrid">{land}</div>
    <h3 class="panel-h">{x(L('Vertikalt för sociala medier', 'Vertical for social media'))}</h3>
    <div class="vgrid tall-row">{vert}</div>
  </div>
</div></section>
''' + cta(L('Vill ni ha något <span class="serif">liknande?</span>', 'Want something <span class="serif">similar?</span>'))
    page('portfolio.html', 'portfolio', L('Portfolio – foto & video', 'Portfolio – photo & video'), L('Foto- och videoprojekt från SanDak Production.', 'Photo and video projects by SanDak Production.'), body)

def p_om():
    vals = [(L('Lyhördhet', 'Listening'), L('Vi börjar med att förstå vad som är viktigt för er.', 'We start by understanding what matters to you.')),
            (L('Hantverk', 'Craft'), L('Ljus, komposition och redigering med omsorg.', 'Light, composition and editing done with care.')),
            (L('Helhet', 'The whole picture'), L('Foto, film och design som hänger ihop.', 'Photo, film and design that work together.')),
            (L('Kvalitet', 'Quality'), L('Material som överträffar förväntningarna.', 'Work that exceeds expectations.'))]
    st = ''.join(f'<div class="step" data-r="{i*100}"><i>0{i+1}</i><h4>{x(t)}</h4><p>{x(d)}</p></div>' for i, (t, d) in enumerate(vals))
    svc = ''.join(f'<li><a href="{s[1]}">{x(s[3])}</a></li>' for s in SERVICES)
    body = hero_page(L('Om oss', 'About'), L('Bakom <span class="serif">kameran</span>', 'Behind <span class="serif">the camera</span>'),
                     L('Foto, video, redigering och grafisk design sedan 2011 – i hela Sverige och internationellt.', 'Photography, video, editing and graphic design since 2011 – across Sweden and internationally.'), 'v-cameraman') + f'''
<section class="sec"><div class="wrap intro-grid">
  <p class="statement" data-r>{x(L('Bakom kameran och vid redigeringsbordet <em>sedan 2011.</em>', 'Behind the camera and in the edit <em>since 2011.</em>'))}</p>
  <div class="side" data-r="150"><p>{x(L('Vi arbetar med företag, verksamheter och privatpersoner – från reklamfilm och eventdokumentation till fastighetsbilder, porträtt och bröllop. Vi ser till att ert budskap och er känsla når fram till er publik.', 'We work with businesses and individuals – from commercials and event coverage to property images, portraits and weddings. We make sure your message and feeling reach your audience.'))}</p>
  <p>{x(L('Målet är alltid att producera material av hög kvalitet som överträffar förväntningarna.', 'The goal is always to produce high-quality work that exceeds expectations.'))}</p></div>
</div></section>
<section class="sec sec-sand"><div class="wrap">
  <div class="head-row"><div><span class="eyebrow" data-r>{x(L('Erfarenhet', 'Experience'))}</span><h2 class="h2-sm" style="margin-top:20px" data-r>{x(L('Fyra discipliner, <span class="serif">en helhet</span>', 'Four disciplines, <span class="serif">one whole</span>'))}</h2></div>
    <p class="lead" data-r>{x(L('Sedan 2011 har arbetet omfattat hela kedjan – från planering och inspelning till redigering och grafisk form. Det gör att idé, bild och slutresultat hänger ihop.', 'Since 2011 the work has covered the whole chain – from planning and shooting to editing and graphic design. That keeps idea, image and final result consistent.'))}</p></div>
  <div class="exp-grid">
    <div class="exp" data-r><span class="exp-y">2011–</span><h4>{x(L('Fotografering', 'Photography'))}</h4><p>{x(L('Porträtt, företag, fastigheter, restauranger, hotell, event och bröllop.', 'Portraits, business, real estate, restaurants, hotels, events and weddings.'))}</p></div>
    <div class="exp" data-r="100"><span class="exp-y">2011–</span><h4>{x(L('Videoproduktion', 'Video production'))}</h4><p>{x(L('Reklam- och varumärkesfilm, eventfilm, sociala medier och bröllopsfilm.', 'Commercials and brand films, event films, social media and wedding films.'))}</p></div>
    <div class="exp" data-r="200"><span class="exp-y">2011–</span><h4>{x(L('Redigering', 'Editing'))}</h4><p>{x(L('Bildbehandling, klippning, färgsättning och ljud.', 'Retouching, editing, colour grading and sound.'))}</p></div>
    <div class="exp" data-r="300"><span class="exp-y">2011–</span><h4>{x(L('Grafisk design', 'Graphic design'))}</h4><p>{x(L('Grafiskt material för digitala kanaler, tryck och film.', 'Graphic material for digital channels, print and film.'))}</p></div>
  </div>
</div></section>
<section class="sec"><div class="wrap reach">
  <div><span class="eyebrow" data-r>{x(L('Var vi arbetar', 'Where we work'))}</span><h2 class="h2-sm" style="margin-top:20px" data-r>{x(L('Hela Sverige. <span class="serif">Och längre bort.</span>', 'All of Sweden. <span class="serif">And beyond.</span>'))}</h2></div>
  <div data-r="120"><p class="lead">{x(L('Vi tar uppdrag i hela Sverige och reser gärna för internationella produktioner – bland annat i Spanien.', 'We work all over Sweden and are happy to travel for international productions – including in Spain.'))}</p>
  <ul class="reach-list"><li>{x(L('Hela Sverige', 'All of Sweden'))}</li><li>{x(L('Spanien', 'Spain'))}</li><li>{x(L('Övriga internationella uppdrag', 'Other international assignments'))}</li></ul></div>
</div></section>
<section class="sec sec-dark"><div class="wrap">
  <div class="head-row"><div><span class="eyebrow" data-r>{x(L('Det vi står för', 'What we stand for'))}</span><h2 data-r>{x(L('Så tänker <span class="serif">vi</span>', 'How we <span class="serif">think</span>'))}</h2></div></div>
  <div class="steps">{st}</div>
</div></section>
<section class="sec"><div class="wrap split">
  <div class="media" data-r><img src="{I('v-crew.jpg')}" alt="" loading="lazy"></div>
  <div><span class="eyebrow" data-r>{x(L('Tjänster', 'Services'))}</span><h2 class="h2-sm" style="margin:20px 0 24px" data-r>{x(L('Ett team, <span class="serif">nio områden</span>', 'One team, <span class="serif">nine areas</span>'))}</h2>
  <ul class="ticks cols" data-r>{svc}</ul>
  <a href="kontakt.html" class="btn btn-dark" style="margin-top:30px" data-r data-arrow>{x(L('Kontakta oss', 'Contact us'))}</a></div>
</div></section>
''' + cta(L('Låt oss <span class="serif">skapa något.</span>', 'Let’s <span class="serif">create something.</span>'), media='v-studio')
    page('om-oss.html', 'om', L('Om oss', 'About'), L('SanDak Production – foto, video, redigering och grafisk design sedan 2011.', 'SanDak Production – photography, video, editing and graphic design since 2011.'), body)

def p_kontakt():
    chips = ''.join(f'<input type="checkbox" name="service" id="s{i}" value="{x(s[3])}"><label for="s{i}">{x(s[3])}</label>' for i, s in enumerate(SERVICES))
    def fld(id, label, typ='text', req=False, full=False, ac='', ph=''):
        return f'<div class="field{" full" if full else ""}"><label for="{id}">{x(label)}{" *" if req else ""}</label><input id="{id}" name="{id}" type="{typ}" data-label="{x(label)}"{" required" if req else ""}{f" autocomplete={ac}" if ac else ""}{f" placeholder=\"{x(ph)}\"" if ph else ""}></div>'
    body = f'''<section class="sec contact-sec">
  <div class="wrap contact-grid">
    <div>
      <span class="eyebrow">{x(L('Kontakt', 'Contact'))}</span>
      <h1 class="contact-h1">{x(L('Berätta om <span class="serif">ert projekt.</span>', 'Tell us about <span class="serif">your project.</span>'))}</h1>
      <p class="lead">{x(L('Fyll i formuläret eller kontakta oss direkt via WhatsApp, mejl eller Instagram.', 'Fill in the form or reach us directly via WhatsApp, e-mail or Instagram.'))}</p>
      <div class="contact-cards">
        <a href="{wa_link()}" target="_blank" rel="noopener" class="ccard wa-card">{WA_ICON}<span><small>WhatsApp</small>{x(L('Starta en konversation', 'Start a conversation'))}</span></a>
        <a href="mailto:{SITE['email']}" class="ccard">{MAIL_ICON}<span><small>{x(L('E-post', 'E-mail'))}</small>{SITE['email']}</span></a>
        {f'<a href="tel:{SITE["phone"].replace(" ", "")}" class="ccard"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg><span><small>{x(L("Telefon", "Phone"))}</small>{SITE["phone"]}</span></a>' if SITE['phone'] else ''}
        <a href="{SITE['instagram']}" target="_blank" rel="noopener" class="ccard">{IG_ICON}<span><small>Instagram</small>{SITE['ig_handle']}</span></a>
      </div>
      {social_row()}
      <p class="form-note" style="margin-top:22px">{x(L('Uppdrag i hela Sverige och internationellt, bland annat i Spanien.', 'Assignments across Sweden and internationally, including Spain.'))}</p>
    </div>
    <div>
      <form id="bokning" class="form" novalidate action="{SITE['form_endpoint']}" method="POST" data-endpoint="{SITE['form_endpoint']}" data-mail="{SITE['email']}" data-subject="{x(L('Förfrågan via webbplatsen', 'Enquiry via website'))}" data-services-label="{x(L('Tjänster', 'Services'))}">
        <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" class="hp" aria-hidden="true">
        <input type="hidden" name="_subject" value="{x(L('Ny förfrågan – SanDak Production', 'New enquiry – SanDak Production'))}">
        <input type="hidden" name="språk" value="{C.lang}">
        <fieldset class="field full"><legend>{x(L('Vad gäller det?', 'What do you need?'))}</legend><div class="chips">{chips}</div></fieldset>
        {fld('namn', L('Namn', 'Name'), req=True, ac='name')}
        {fld('email', L('E-post', 'E-mail'), 'email', True, ac='email')}
        {fld('telefon', L('Telefon', 'Phone'), 'tel', ac='tel')}
        {fld('foretag', L('Företag', 'Company'), ac='organization', ph=L('Valfritt', 'Optional'))}
        {fld('datum', L('Önskat datum', 'Preferred date'), 'date')}
        {fld('plats', L('Plats', 'Location'), ph=L('Ort eller land', 'City or country'))}
        <div class="field full"><label for="meddelande">{x(L('Meddelande', 'Message'))} *</label><textarea id="meddelande" name="meddelande" required data-label="{x(L('Meddelande', 'Message'))}" placeholder="{x(L('Vad vill ni skapa, och var ska materialet användas?', 'What would you like to create, and where will it be used?'))}"></textarea></div>
        <div class="full form-foot"><span class="form-note">{x(L('Vi återkommer till er via e-post.', 'We will get back to you by e-mail.')) if SITE['form_endpoint'] else x(L('Formuläret öppnar ert e-postprogram med förfrågan ifylld.', 'The form opens your e-mail app with your request filled in.'))}</span><button class="btn btn-dark" type="submit" data-arrow>{x(L('Skicka förfrågan', 'Send request'))}</button></div>
      </form>
      <div class="form-ok" role="status" tabindex="-1"><h3 style="margin-bottom:10px">{x(L('Tack för er förfrågan!', 'Thank you for your enquiry!'))}</h3><p style="margin:0">{x(L('Vi har tagit emot ert meddelande och återkommer så snart vi kan. Ni kan också nå oss på WhatsApp.', 'We have received your message and will get back to you as soon as we can. You can also reach us on WhatsApp.')) if SITE['form_endpoint'] else x(L('Ert e-postprogram öppnas med förfrågan ifylld – skicka den så återkommer vi. Ni kan också nå oss på WhatsApp.', 'Your e-mail app is opening with your request filled in – send it and we’ll get back to you. You can also reach us on WhatsApp.'))}</p></div>
      <div class="form-err" role="alert">{x(L('Något gick fel när förfrågan skulle skickas. Försök igen, eller mejla oss direkt på', 'Something went wrong sending your request. Please try again, or e-mail us directly at'))} <a href="mailto:{SITE['email']}">{SITE['email']}</a>.</div>
    </div>
  </div>
</section>'''
    page('kontakt.html', 'kontakt', L('Kontakt', 'Contact'), L('Kontakta SanDak Production för foto, video, event, bröllop och grafisk design.', 'Contact SanDak Production for photo, video, events, weddings and graphic design.'), body)

def p_project(slug, title, place, hero, intro, rows, nxt):
    body = f'''<section class="page-hero" style="min-height:88svh">
  <video src="{V(hero)}.mp4" poster="{V(hero)}.jpg" autoplay muted loop playsinline aria-hidden="true"></video>
  <div class="wrap"><span class="eyebrow">{x(L('Projekt · Bröllop', 'Project · Wedding'))}</span><h1>{x(title)}</h1><p>{x(place)}</p></div>
</section>
<section class="sec"><div class="wrap story-intro">
  <ul class="facts" data-r><li><small>{x(L('Område', 'Area'))}</small>{x(L('Bröllop', 'Wedding'))}</li><li><small>{x(L('Leverans', 'Delivery'))}</small>{x(L('Foto + film', 'Photo + film'))}</li></ul>
  <p class="statement" data-r="120">{x(intro)}</p>
</div></section>
<section style="padding-bottom:clamp(70px,9vw,130px)"><div class="wrap gallery-rows">{rows}</div></section>
<section class="sec" style="padding-bottom:60px;padding-top:0"><div class="wrap"><a href="{nxt[0]}" class="next-story" data-r><span><span class="eyebrow">{x(L('Nästa projekt', 'Next project'))}</span><br><b>{x(nxt[1])}</b></span><span class="btn btn-dark" data-arrow>{x(L('Visa', 'View'))}</span></a></div></section>
''' + cta(L('Ert bröllop <span class="serif">kan vara nästa.</span>', 'Your wedding <span class="serif">could be next.</span>'), btn=L('Fråga om ert datum', 'Ask about your date'), media='hero-sunset')
    page(slug, 'brollop', title, L('Bröllopsprojekt av SanDak Production.', 'Wedding project by SanDak Production.'), body)

def fi(cls, src, d=0):
    return f'<figure class="{cls}" data-lb data-r="{d}" tabindex="0"><img src="{I(src)}" alt="" loading="lazy"></figure>'
def fv(cls, src, d=0):
    return f'<figure class="{cls}" data-lb data-r="{d}" tabindex="0"><video src="{V(src)}.mp4" poster="{V(src)}.jpg" muted loop playsinline data-inview></video></figure>'

def build():
    for lg in LANGS:
        C.lang = lg['code']; C.P = '../' * lg['dir'].count('/')
        for slug, fn in [('index.html', p_index), ('foto.html', p_foto), ('video.html', p_video), ('foretag.html', p_foretag),
                         ('brollop.html', p_brollop), ('portfolio.html', p_portfolio), ('om-oss.html', p_om), ('kontakt.html', p_kontakt)]:
            C.slug = slug; fn()
        C.slug = 'projekt-skogsbrollop.html'
        p_project(C.slug, L('Skogsbröllop', 'Forest wedding'), L('En intim dag bland höga träd', 'An intimate day among tall trees'), 'reel-embrace',
                  L('Mjukt ljus, <em>vinden i slöjan</em> och stunder som inte behövde regisseras.', 'Soft light, <em>wind in the veil</em> and moments that needed no direction.'),
                  f'<div class="row r2">{fi("tall","s-embrace1.jpg")}{fv("tall","reel-embrace",100)}</div><div class="row">{fi("wide","s-sunset.jpg")}</div><div class="row r3">{fi("tall","s-speech.jpg")}{fi("tall","s-tree.jpg",100)}{fi("tall","s-bw.jpg",200)}</div>',
                  ('projekt-sommarvigsel.html', L('Sommarvigsel', 'Summer ceremony')))
        C.slug = 'projekt-sommarvigsel.html'
        p_project(C.slug, L('Sommarvigsel', 'Summer ceremony'), L('Vigsel under öppen himmel', 'A ceremony under open skies'), 'reel-vows',
                  L('Sol, palmblad och ett sällskap som <em>jublade</em> genom hela ceremonin.', 'Sunshine, palm leaves and guests who <em>cheered</em> through the whole ceremony.'),
                  f'<div class="row">{fi("wide","s-cer1.jpg")}</div><div class="row r3">{fi("tall","s-vows.jpg")}{fv("tall","reel-toast",100)}{fi("tall","s-exit.jpg",200)}</div><div class="row r2">{fi("tall","s-cer2.jpg")}{fi("tall","s-cer3.jpg",100)}</div>',
                  ('projekt-skogsbrollop.html', L('Skogsbröllop', 'Forest wedding')))
    print('built', [l['code'] for l in LANGS])

if __name__ == '__main__':
    build()
