"""Bundle the whole ciif.africa site into ONE self-contained HTML file for sharing.
Every page, stylesheet and image is embedded; internal links become in-file navigation.
Usage: python build-preview.py  ->  CIIFA-Website-Preview.html
"""
import base64, os, re, posixpath, datetime

SITE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'site')
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'CIIFA-Website-Preview.html')

PAGES = [  # (file, key, label) in nav-story order; career-fair.html is a redirect, mapped to amedi
    ('index.html', 'index'), ('programmes.html', 'programmes'),
    ('programmes/skill-pool.html', 'programmes/skill-pool'), ('programmes/cba.html', 'programmes/cba'),
    ('programmes/enterprise.html', 'programmes/enterprise'), ('programmes/safehouse.html', 'programmes/safehouse'),
    ('programmes/amedi.html', 'programmes/amedi'), ('programmes/investors-session.html', 'programmes/investors-session'),
    ('impact.html', 'impact'), ('about.html', 'about'), ('about-ctf.html', 'about-ctf'), ('team.html', 'team'),
    ('events.html', 'events'), ('news.html', 'news'), ('partner.html', 'partner'),
    ('contact.html', 'contact'), ('team-form.html', 'team-form'),
    ('privacy.html', 'privacy'), ('terms.html', 'terms'),
]
KEY_OF = {f: k for f, k in PAGES}
KEY_OF['programmes/career-fair.html'] = 'programmes/amedi'  # folded

# ---- assets -> data URIs (each embedded once) ----
assets = {}
for root, _, files in os.walk(os.path.join(SITE, 'assets', 'img')):
    for fn in files:
        if not fn.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            continue
        full = os.path.join(root, fn)
        rel = os.path.relpath(full, SITE).replace('\\', '/')
        mime = 'image/png' if fn.lower().endswith('.png') else 'image/jpeg'
        with open(full, 'rb') as fh:
            assets[rel] = f'data:{mime};base64,' + base64.b64encode(fh.read()).decode()

css = open(os.path.join(SITE, 'assets', 'css', 'style.css'), encoding='utf-8').read()

def resolve(page_file, href):
    """Resolve an href relative to its page; return normalized site path."""
    return posixpath.normpath(posixpath.join(posixpath.dirname(page_file), href))

sections, extra_styles = [], []
for page_file, key in PAGES:
    html = open(os.path.join(SITE, page_file), encoding='utf-8').read()
    body = re.search(r'<body[^>]*>(.*)</body>', html, re.S).group(1)
    for st in re.findall(r'<style>(.*?)</style>', html, re.S):  # per-page styles (team-form)
        extra_styles.append(st)
    body = re.sub(r'<script src="[^"]*nav\.js"></script>', '', body)

    def fix_href(m):
        href = m.group(1)
        if re.match(r'^(mailto:|tel:|https?:|#)', href):
            return m.group(0)
        path, _, anchor = href.partition('#')
        target = resolve(page_file, path) if path else page_file
        if target in KEY_OF:
            return 'href="#%s%s"' % (KEY_OF[target], ('@' + anchor) if anchor else '')
        return m.group(0)
    body = re.sub(r'href="([^"]+)"', fix_href, body)

    def fix_img(m):
        rel = resolve(page_file, m.group(1))
        return f'src="{assets[rel]}"' if rel in assets else m.group(0)
    body = re.sub(r'src="([^"]+)"', fix_img, body)

    def fix_bg(m):  # --img:url('../assets/img/photos/x.jpg') inside style attributes
        rel = resolve(page_file, m.group(1))
        return f"url('{assets[rel]}')" if rel in assets else m.group(0)
    body = re.sub(r"url\('([^']+)'\)", fix_bg, body)

    sections.append(f'<div class="vpage" data-page="{key}" hidden>\n{body}\n</div>')

today = datetime.date.today().strftime('%d %b %Y')
doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CIIFA · Website Preview</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300..800&display=swap" rel="stylesheet">
<style>
{css}
{chr(10).join(extra_styles)}
.vpage[hidden]{{display:none}}
#pvbadge{{position:fixed;bottom:12px;left:12px;z-index:99;background:#111418;color:#9aa694;border:1px solid #2a3122;
  border-left:3px solid #90E040;border-radius:8px;padding:6px 12px;font:600 11.5px 'Outfit',sans-serif;opacity:.92}}
#pvbadge b{{color:#90E040}}
</style>
</head>
<body>
{chr(10).join(sections)}
<div id="pvbadge"><b>CIIFA</b> website · preview copy · {today} · live: godwintom2487.github.io/ciif-africa</div>
<script>
(function(){{
  function show(hash){{
    var h = (hash || '#index').slice(1) || 'index';
    var parts = h.split('@'), key = parts[0], anchor = parts[1];
    var found = false;
    document.querySelectorAll('.vpage').forEach(function(s){{
      var on = s.getAttribute('data-page') === key;
      s.hidden = !on; if (on) found = true;
    }});
    if (!found) document.querySelector('.vpage[data-page="index"]').hidden = false;
    window.scrollTo(0, 0);
    if (anchor) {{
      var el = document.querySelector('.vpage:not([hidden]) #' + anchor);
      if (el) el.scrollIntoView();
    }}
  }}
  window.addEventListener('hashchange', function(){{ show(location.hash); }});
  document.addEventListener('click', function(e){{
    var b = e.target.closest('.menubtn');
    if (b) {{ var nl = b.parentElement.querySelector('.navlinks'); if (nl) nl.classList.toggle('open'); }}
  }});
  show(location.hash);
}})();
</script>
</body>
</html>'''

with open(OUT, 'w', encoding='utf-8') as fh:
    fh.write(doc)
print('written', OUT, '%.1f MB' % (os.path.getsize(OUT) / 1048576))
