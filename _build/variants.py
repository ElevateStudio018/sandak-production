"""Design proposals for the home intro section (Swedish preview only, not linked, noindex)."""
import os


def build_variants(b):
    V, I, page, L = b.V, b.I, b.page, b.L
    H = 'En produktionsbyrå för <em>foto, film och design</em> – från en enskild porträttbild till en hel kampanj.'
    P1 = ('Sedan 2011 har vi arbetat med fotografering, videoproduktion, redigering och grafisk design. Den erfarenheten '
          'använder vi för att skapa det ni behöver – för ert varumärke, er verksamhet eller ert event – och se till att '
          'ert budskap och er känsla når fram till rätt publik.')
    P2 = 'Målet är alltid detsamma: material av hög kvalitet som överträffar förväntningarna.'
    BTN = '<a href="om-oss.html" class="btn btn-line" data-arrow>Om oss</a>'
    BTNL = '<a href="om-oss.html" class="btn btn-solid" data-arrow>Om oss</a>'
    STATS = [('2011', 'erfarenhet sedan'), ('Sverige', 'uppdrag i hela landet'), ('Världen', 'bl.a. Spanien')]

    def facts(cls='iv-facts'):
        return f'<div class="{cls}">' + ''.join(f'<div><b>{a}</b><span>{s}</span></div>' for a, s in STATS) + '</div>'

    def vid(n):
        return f'<video src="{V(n)}.mp4" poster="{V(n)}.jpg" muted loop playsinline autoplay aria-hidden="true"></video>'

    def img(n):
        return f'<img src="{I(n)}" alt="" loading="lazy">'

    def tag(n, name, note):
        return f'<div class="iv-label"><span>Variant {n:02d}</span><b>{name}</b><em>{note}</em></div>'

    eb = '<span class="eyebrow">SanDak Production</span>'
    out = []
    out.append(tag(1, 'Bild + text', 'Stort foto till vänster med ”Sedan 2011”-märke, text till höger.') +
               f'<section class="sec iv1"><div class="wrap"><div class="iv1-media">{img("v-cameraman.jpg")}'
               f'<div class="iv-badge"><b>2011</b><span>sedan</span></div></div>'
               f'<div>{eb}<p class="statement" style="margin:24px 0">{H}</p><p class="lead">{P1}</p><p>{P2}</p>{facts()}{BTN}</div></div></section>')
    out.append(tag(2, 'Helbild', 'Video i full bredd bakom texten, siffrorna i glaskort längst ner.') +
               f'<section class="iv2">{vid("v-crew")}<div class="wrap">{eb}<p class="statement">{H}</p><p class="iv2-p">{P1}</p>'
               f'<div class="iv2-bottom">{facts("iv-facts glass")}{BTNL}</div></div></section>')
    out.append(tag(3, 'Redaktionell siffra', 'Ett stort ”2011” som blickfång, bildremsa under.') +
               f'<section class="sec iv3"><div class="wrap"><div class="iv3-top"><div class="iv3-year">2011<span>Foto · Video · Redigering · Design</span></div>'
               f'<div>{eb}<p class="statement" style="margin:22px 0">{H}</p><p>{P1}</p>{BTN}</div></div>'
               f'<div class="iv3-strip">{img("r-portrait2.jpg")}{img("v-chef.jpg")}{img("v-living.jpg")}{img("s-vows.jpg")}</div></div></section>')
    out.append(tag(4, 'Kollage', 'Tre förskjutna bilder från olika områden bredvid texten.') +
               f'<section class="sec iv4"><div class="wrap"><div class="iv4-col">{img("r-portrait.jpg")}{img("v-chef.jpg")}{img("v-living.jpg")}</div>'
               f'<div>{eb}<p class="statement" style="margin:24px 0">{H}</p><p class="lead">{P1}</p>{facts()}{BTN}</div></div></section>')
    stats5 = ''.join(f'<div><b>{a}</b><span>{s}</span></div>' for a, s in STATS) + '<div><b>9</b><span>tjänsteområden</span></div>'
    out.append(tag(5, 'Mörk med siffror', 'Mörk sektion, video i ruta och stora siffror med avdelare.') +
               f'<section class="sec sec-dark iv5"><div class="wrap"><div class="iv5-top"><div>{eb}<p class="statement" style="margin-top:24px">{H}</p></div>'
               f'<div class="iv5-media">{vid("v-event-film")}</div></div><div class="iv5-stats">{stats5}</div><p class="iv5-p">{P1}</p></div></section>')
    out.append(tag(6, 'Kort med video', 'Rundat kort: video till vänster, text till höger.') +
               f'<section class="sec iv6"><div class="wrap"><div class="iv6-card"><div class="iv6-media">{vid("v-studio")}</div>'
               f'<div class="iv6-text">{eb}<p class="statement" style="margin:22px 0">{H}</p><p>{P1}</p>{facts()}{BTN}</div></div></div></section>')
    pill = lambda n: f'<span class="iv7-pill">{img(n)}</span>'
    out.append(tag(7, 'Bild i rubriken', 'Centrerad rubrik med små runda bilder infällda i texten.') +
               f'<section class="sec iv7"><div class="wrap">{eb}<p class="iv7-h">En produktionsbyrå för {pill("r-portrait2.jpg")} foto, '
               f'{pill("v-crew.jpg")} film och {pill("v-design.jpg")} <em>design</em> – sedan 2011.</p>'
               f'<p class="lead iv7-p">{P1}</p>{facts("iv-facts center")}<div style="text-align:center">{BTN}</div></div></section>')
    line = ''.join(f'<li><b>{a}</b><span>{s}</span></li>' for a, s in [
        ('2011', 'Fotografering & videoproduktion'), ('→', 'Redigering & grafisk design'),
        ('→', 'Företag, event, restauranger, hotell, fastigheter & bröllop'), ('Idag', 'Hela Sverige och internationellt – bl.a. Spanien')])
    out.append(tag(8, 'Tidslinje', 'Linje från 2011 till idag med disciplinerna, bild till höger.') +
               f'<section class="sec sec-sand iv8"><div class="wrap"><div>{eb}<p class="statement" style="margin:24px 0 36px">{H}</p>'
               f'<ol class="iv8-line">{line}</ol>{BTN}</div><div class="iv8-media">{img("v-studio.jpg")}</div></div></section>')
    out.append(tag(9, 'Överlappande kort', 'Stor bild med ett ljust textkort som lägger sig över hörnet.') +
               f'<section class="sec iv9"><div class="wrap"><div class="iv9-media">{img("v-crew.jpg")}</div>'
               f'<div class="iv9-card">{eb}<p class="statement" style="margin:22px 0">{H}</p><p>{P1}</p>{facts()}{BTN}</div></div></section>')
    out.append(tag(10, 'Bento-rutnät', 'Rutor med text, bild, video och siffror i olika storlekar.') +
               f'<section class="sec sec-sand iv10"><div class="wrap"><div class="iv10-grid">'
               f'<div class="b b-text">{eb}<p class="statement" style="margin-top:22px">{H}</p></div>'
               f'<div class="b b-img">{img("r-portrait2.jpg")}</div>'
               f'<div class="b b-num"><b>2011</b><span>erfarenhet sedan</span></div>'
               f'<div class="b b-vid">{vid("v-chef")}</div>'
               f'<div class="b b-p"><p>{P1}</p>{BTN}</div>'
               f'<div class="b b-num dark"><b>Sverige</b><span>och internationellt, bl.a. Spanien</span></div></div></div></section>')

    nav = ''.join(f'<a href="#v{i + 1}">{i + 1:02d}</a>' for i in range(10))
    body = ('<section class="iv-head"><div class="wrap"><span class="eyebrow">Designförslag</span>'
            '<h1>Intro-sektionen – <span class="serif">10 varianter</span></h1>'
            '<p class="lead">Samma text i tio olika layouter. Välj ett nummer, så byggs den in på startsidan.</p>'
            f'<nav class="iv-nav">{nav}</nav></div></section>')
    body += ''.join(f'<div id="v{i + 1}" class="iv-wrap">{v}</div>' for i, v in enumerate(out))
    page('intro-varianter.html', 'variants', L('Designförslag – intro'), L('Designförslag'), body)
    path = os.path.join(b.ROOT, 'intro-varianter.html')
    h = open(path).read()
    open(path, 'w').write(h.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<meta name="robots" content="noindex">', 1))
