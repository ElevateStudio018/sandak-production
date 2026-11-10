"""Three refined design proposals for the home intro section (Swedish preview only, not linked, noindex).
Based on the client's favourites from the first round: 10 (bento), 6 (video card), 4 (collage) and 3 (big year)."""
import os


def build_variants(b):
    V, I, page, L = b.V, b.I, b.page, b.L
    H = 'En produktionsbyrå för <em>foto, film och design</em> – från en enskild porträttbild till en hel kampanj.'
    P1 = ('Sedan 2011 har vi arbetat med fotografering, videoproduktion, redigering och grafisk design. Den erfarenheten '
          'använder vi för att skapa det ni behöver – för ert varumärke, er verksamhet eller ert event.')
    P2 = 'Målet är alltid detsamma: material av hög kvalitet som överträffar förväntningarna.'
    eb = '<span class="eyebrow">SanDak Production</span>'
    arrow = '<a href="om-oss.html" class="btn btn-line" data-arrow>Om oss</a>'
    disc = '<ul class="iw-disc"><li>Fotografering</li><li>Videoproduktion</li><li>Redigering</li><li>Grafisk design</li></ul>'

    def vid(n):
        return f'<video src="{V(n)}.mp4" poster="{V(n)}.jpg" muted loop playsinline autoplay aria-hidden="true"></video>'

    def img(n, cap=''):
        c = f'<figcaption>{cap}</figcaption>' if cap else ''
        return f'<figure><img src="{I(n)}" alt="" loading="lazy">{c}</figure>'

    def tag(letter, name, note):
        return f'<div class="iv-label"><span>Förslag {letter}</span><b>{name}</b><em>{note}</em></div>'

    out = []

    # A — Bento (10) + collage images (4)
    out.append(tag('A', 'Bento', 'Bygger på 10 · med bilder från olika områden (4)') + f'''
<section class="sec sec-sand iwA"><div class="wrap"><div class="iwA-grid">
  <div class="t t-intro">{eb}<p class="statement">{H}</p></div>
  <div class="t t-vid">{vid('v-studio')}<span class="t-chip">Foto · Video · Design</span></div>
  <div class="t t-year"><b>2011</b><span>Erfarenhet av foto, film, redigering och design</span></div>
  <div class="t t-img">{img('v-chef.jpg', 'Restaurang')}</div>
  <div class="t t-img">{img('v-living.jpg', 'Fastighet')}</div>
  <div class="t t-text"><p>{P1}</p><p class="t-goal">{P2}</p>{arrow}</div>
  <div class="t t-reach"><b>Hela Sverige</b><span>och internationellt – bl.a. Spanien</span></div>
  <div class="t t-img">{img('r-portrait2.jpg', 'Porträtt')}</div>
</div></div></section>''')

    # B — Video card (6) + thumbnail collage (4)
    out.append(tag('B', 'Videokort', 'Bygger på 6 · med miniatyrer (4) och nyckeltal') + f'''
<section class="sec iwB"><div class="wrap"><div class="iwB-card">
  <div class="iwB-media">{vid('v-crew')}<div class="iwB-badge"><b>2011</b><span>sedan</span></div></div>
  <div class="iwB-text">{eb}<p class="statement">{H}</p><p class="iwB-p">{P1}</p>
    <div class="iwB-thumbs">{img('r-portrait.jpg')}{img('v-chef.jpg')}{img('v-living.jpg')}{img('s-vows.jpg')}</div>
    <div class="iwB-foot"><div class="iwB-stats"><div><b>15+</b><span>år i branschen</span></div><div><b>9</b><span>tjänsteområden</span></div><div><b>SE · ES</b><span>Sverige &amp; Spanien</span></div></div>{arrow}</div>
  </div>
</div></div></section>''')

    # C — Editorial big year (3) + staggered collage (4)
    out.append(tag('C', 'Redaktionell', 'Bygger på 3 · stort ”2011” med förskjutet kollage (4)') + f'''
<section class="sec iwC"><div class="wrap iwC-grid">
  <div class="iwC-text">
    <div class="iwC-year"><span class="serif">sedan</span>2011</div>
    {eb}<p class="statement">{H}</p><p class="lead">{P1}</p>{disc}{arrow}
  </div>
  <div class="iwC-collage">
    <div class="c1">{img('r-portrait2.jpg', 'Porträtt')}</div>
    <div class="c2">{vid('v-chef')}</div>
    <div class="c3">{img('v-living.jpg', 'Fastighet')}</div>
    <div class="c4">{img('v-stage.jpg', 'Event')}</div>
  </div>
</div></section>''')

    nav = ''.join(f'<a href="#v{c}">{c}</a>' for c in 'ABC')
    body = ('<section class="iv-head"><div class="wrap"><span class="eyebrow">Designförslag · runda 2</span>'
            '<h1>Intro-sektionen – <span class="serif">tre förslag</span></h1>'
            '<p class="lead">Baserade på era favoriter 10, 6, 4 och 3. Välj A, B eller C så byggs den in på startsidan.</p>'
            f'<nav class="iv-nav">{nav}</nav></div></section>')
    body += ''.join(f'<div id="v{c}" class="iv-wrap">{v}</div>' for c, v in zip('ABC', out))
    page('intro-varianter.html', 'variants', L('Designförslag – intro'), L('Designförslag'), body)
    path = os.path.join(b.ROOT, 'intro-varianter.html')
    h = open(path).read()
    open(path, 'w').write(h.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<meta name="robots" content="noindex">', 1))
