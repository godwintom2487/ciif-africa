"""CIIFA team profile generator.
Drop ciifa-profile-*.json files (from CIIFA-Team-Profile-Form.html) into profiles/, then:
    python build_team.py
Outputs, per person:
  out/<slug>-card.png            branded 1080x1350 profile card (social/press)
  ../site/assets/img/team/<slug>.jpg   square headshot for the website
  out/team-cards.html            ready-to-paste cards for site/team.html
"""
import base64, glob, io as iomod, json, os, re
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = os.path.join(HERE, '..', 'flyers', 'assets', 'Outfit.ttf')
OUT = os.path.join(HERE, 'out')
SITE_IMG = os.path.join(HERE, '..', 'site', 'assets', 'img', 'team')
os.makedirs(OUT, exist_ok=True)
os.makedirs(SITE_IMG, exist_ok=True)

INK, LIME, WHITE, GREY = (17, 20, 24), (144, 224, 64), (255, 255, 255), (185, 196, 176)

def font(size, weight=700):
    f = ImageFont.truetype(FONT, size)
    f.set_variation_by_axes([weight])
    return f

def wrap(d, text, fnt, maxw):
    words, lines, cur = text.split(), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if d.textlength(t, font=fnt) <= maxw:
            cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def slugify(name):
    return re.sub(r'-+', '-', re.sub(r'[^a-z0-9]+', '-', name.lower())).strip('-')

def circle_photo(photo, size):
    r = max(size / photo.size[0], size / photo.size[1])
    photo = photo.resize((round(photo.size[0]*r), round(photo.size[1]*r)), Image.LANCZOS)
    x, y = (photo.size[0]-size)//2, (photo.size[1]-size)//2
    photo = photo.crop((x, y, x+size, y+size))
    mask = Image.new('L', (size, size), 0)
    ImageDraw.Draw(mask).ellipse([0, 0, size, size], fill=255)
    out = Image.new('RGBA', (size, size))
    out.paste(photo, (0, 0), mask)
    return out

def build_card(p, photo, slug):
    W, H = 1080, 1350
    base = Image.new('RGBA', (W, H), INK)
    layer = Image.new('RGBA', base.size, (0, 0, 0, 0))
    dd = ImageDraw.Draw(layer)
    dd.ellipse([W-380, -260, W+260, 380], fill=LIME + (60,))
    dd.ellipse([-260, H-380, 380, H+260], fill=LIME + (35,))
    base.alpha_composite(layer.filter(ImageFilter.GaussianBlur(130)))
    d = ImageDraw.Draw(base)

    # logo top-left
    logo = Image.open(os.path.join(HERE, '..', 'site', 'assets', 'img', 'ciifa-logo-dark.png')).convert('RGBA')
    lw = 170
    logo = logo.resize((lw, round(logo.size[1]*lw/logo.size[0])), Image.LANCZOS)
    base.alpha_composite(logo, (64, 60))
    d.text((W-64, 76), 'THE TEAM', font=font(26, 800), fill=LIME, anchor='ra')

    # photo with lime ring
    ps = 400
    cx = W // 2
    ring = Image.new('RGBA', (ps+24, ps+24))
    ImageDraw.Draw(ring).ellipse([0, 0, ps+23, ps+23], outline=LIME, width=7)
    base.alpha_composite(ring, (cx-(ps+24)//2, 168))
    base.alpha_composite(circle_photo(photo, ps), (cx-ps//2, 180))

    y = 630
    d.text((cx, y), p['name'], font=font(62, 800), fill=WHITE, anchor='ma'); y += 84
    d.text((cx, y), p['role'], font=font(34, 700), fill=LIME, anchor='ma'); y += 52
    if p.get('location'):
        d.text((cx, y), p['location'], font=font(26, 500), fill=GREY, anchor='ma'); y += 48
    # team chips
    chips = p.get('teams', [])[:4]
    if chips:
        cf = font(22, 700)
        widths = [d.textlength(c, font=cf) + 36 for c in chips]
        total = sum(widths) + 12*(len(chips)-1)
        x = cx - total/2
        for c, wdt in zip(chips, widths):
            d.rounded_rectangle([x, y, x+wdt, y+40], 20, outline=LIME, width=2)
            d.text((x+wdt/2, y+9), c, font=cf, fill=LIME, anchor='ma')
            x += wdt + 12
        y += 68
    if p.get('oneliner'):
        for ln in wrap(d, '“' + p['oneliner'] + '”', font(30, 600), 860):
            d.text((cx, y), ln, font=font(30, 600), fill=WHITE, anchor='ma'); y += 42
        y += 14
    if p.get('bio'):
        for ln in wrap(d, p['bio'], font(25, 400), 880)[:6]:
            d.text((cx, y), ln, font=font(25, 400), fill=GREY, anchor='ma'); y += 36
        y += 16
    for h in p.get('highlights', [])[:3]:
        d.text((cx, y), '·  ' + h + '  ·', font=font(23, 600), fill=(174, 227, 111), anchor='ma'); y += 36

    d.line([64, H-96, W-64, H-96], fill=(60, 66, 58), width=2)
    d.text((64, H-72), 'ciif.africa/team.html', font=font(24, 700), fill=LIME)
    d.text((W-64, H-72), 'Creative Industries Initiative for Africa', font=font(22, 500), fill=GREY, anchor='ra')
    base.convert('RGB').save(os.path.join(OUT, f'{slug}-card.png'))

def person_html(p, slug):
    teams = ' · '.join(p.get('teams', []))
    bio = (p.get('bio') or p.get('oneliner') or '').replace('&', '&amp;').replace('<', '&lt;')
    return f'''      <div class="card" style="--pc:var(--fair)"><span class="bar"></span>
        <div class="person">
          <img class="avatar-img" src="assets/img/team/{slug}.jpg" alt="{p['name']}">
          <div>
            <h3>{p['name']}</h3>
            <div class="role">{p['role']}</div>
            <p>{bio}</p>
          </div>
        </div>
      </div>'''

cards_html = []
for f in sorted(glob.glob(os.path.join(HERE, 'profiles', 'ciifa-profile-*.json'))):
    p = json.load(open(f, encoding='utf-8-sig'))
    slug = slugify(p['name'])
    b64 = p['photo'].split(',', 1)[1]
    photo = Image.open(iomod.BytesIO(base64.b64decode(b64))).convert('RGB')
    # site headshot
    sq = circle_photo(photo, 480).convert('RGB')  # circle not needed for site; save square crop instead
    r = max(480/photo.size[0], 480/photo.size[1])
    sqim = photo.resize((round(photo.size[0]*r), round(photo.size[1]*r)), Image.LANCZOS)
    x, y = (sqim.size[0]-480)//2, (sqim.size[1]-480)//2
    sqim.crop((x, y, x+480, y+480)).save(os.path.join(SITE_IMG, slug + '.jpg'), quality=82)
    build_card(p, photo, slug)
    cards_html.append(person_html(p, slug))
    print('built:', p['name'], '->', slug)

if cards_html:
    with open(os.path.join(OUT, 'team-cards.html'), 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(cards_html) + '\n')
    print(f'\n{len(cards_html)} profiles -> out/ + site/assets/img/team/')
    print('paste out/team-cards.html cards into site/team.html, then deploy')
else:
    print('no profiles found in profiles/ — drop ciifa-profile-*.json files there first')
