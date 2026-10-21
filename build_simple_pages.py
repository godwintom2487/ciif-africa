# One-off: writes the simplified about.html and contact.html
import io, os

SITE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'site')

NAV = '''<nav class="nav">
  <div class="wrap">
    <a class="logo" href="index.html"><img class="lm-light" src="assets/img/ciifa-logo.png" alt="CIIFA"><img class="lm-dark" src="assets/img/ciifa-logo-dark.png" alt="CIIFA"></a>
    <button class="menubtn" aria-label="Menu">Menu</button>
    <div class="navlinks">
      <a href="safehouse.html">The SafeHouse</a>
      <a href="programmes.html">Programmes</a>
      <a href="about.html">About</a>
      <a href="contact.html">Contact</a>
      <a class="cta" href="safehouse.html#book">Book a visit</a>
    </div>
  </div>
</nav>'''

FOOTER = '''<footer>
  <div class="wrap">
    <div class="cols">
      <div>
        <div class="flogo"><img src="assets/img/ciifa-logo-dark.png" alt="CIIFA" style="height:36px;width:auto"></div>
        <p>The Creative Industries Initiative for Africa. Lagos, Nigeria.</p>
        <p style="margin-top:10px">4B Onikoyi Lane, Parkview Estate, Ikoyi, Lagos</p>
      </div>
      <div>
        <h4>Visit</h4>
        <a href="safehouse.html">The SafeHouse</a>
        <a href="programmes/food-days.html">Food Days</a>
        <a href="programmes.html">Programmes</a>
      </div>
      <div>
        <h4>CIIFA</h4>
        <a href="about.html">About &amp; team</a>
        <a href="contact.html">Contact</a>
        <a href="mailto:info@ciif.africa">info@ciif.africa</a>
        <a href="tel:+2347017341434">0701 734 1434</a>
      </div>
    </div>
    <div class="legal">
      <span>&#169; 2026 Creative Industries Initiative for Africa (CIIFA). &#183; <a href="privacy.html">Privacy</a> &#183; <a href="terms.html">Terms</a></span>
      <span>CBA for Africa is executed by CIIFA for the Creative Talent Foundation (CTF).</span>
    </div>
  </div>
</footer>'''

def head(title, desc, path):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/png" sizes="32x32" href="assets/img/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="assets/img/favicon-192.png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="CIIFA">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://ciif.africa/assets/img/og-card.jpg">
<meta property="og:url" content="https://ciif.africa/{path}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300..800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
'''

def person(initials, name, role):
    return f'''      <div class="card" style="--pc:var(--fair)"><span class="bar"></span>
        <div class="person">
          <div class="avatar">{initials}</div>
          <div><h3>{name}</h3><div class="role">{role}</div></div>
        </div>
      </div>'''

PLOGOS = '''    <div class="plogos" style="margin-top:20px">
      <div class="plogo"><img src="assets/img/partners/google-org.png" alt="Google.org" loading="lazy"></div>
      <div class="plogo"><img src="assets/img/partners/british-council.png" alt="British Council" loading="lazy"></div>
      <div class="plogo"><img src="assets/img/partners/french-embassy.png" alt="French Embassy" loading="lazy"></div>
      <div class="plogo"><img src="assets/img/partners/sacem.png" alt="SACEM" loading="lazy"></div>
      <div class="plogo"><img src="assets/img/partners/afreximbank.png" alt="Afreximbank" loading="lazy"></div>
      <div class="plogo"><img src="assets/img/partners/mavin.png" alt="Mavin" loading="lazy"></div>
      <div class="plogo">Chocolate City</div>
      <div class="plogo"><img src="assets/img/partners/us-consulate.png" alt="US Consulate" loading="lazy"></div>
      <div class="plogo"><img src="assets/img/partners/spotify.png" alt="Spotify" loading="lazy"></div>
      <div class="plogo"><img src="assets/img/partners/youtube.png" alt="YouTube" loading="lazy"></div>
    </div>'''

TEAM = '\n'.join([
    person('GT', 'Godwin Tom', 'Founder &amp; CEO'),
    person('FT', 'Femi Taylor', 'Co-Founder'),
    person('AO', 'Abigail Ogunmiloro', 'Chief of Staff'),
    person('KE', 'Kini-Abasi Edet', 'Head of Business Development'),
    person('AW', 'Ayorinde Williams', 'Head of Projects'),
    person('HA', 'Hyeladzira Adamu', 'Administration &amp; Community Manager'),
])

about = head('About · CIIFA',
             "Who CIIFA is: the people and story behind Africa's creative industries initiative, the numbers so far, and the foundation we build with.",
             'about.html') + NAV + '''

<header class="hero slim photo" style="--img:url('assets/img/photos/about.jpg')">
  <div class="wrap">
    <div class="kicker">About us</div>
    <h1>Talent was never the problem.</h1>
    <p class="lead">African creativity travels the world. We exist so the people behind it get the structure, skills and spaces to earn from it properly.</p>
  </div>
</header>

<section class="block">
  <div class="wrap prose">
    <h2>Who we are</h2>
    <p>The Creative Industries Initiative for Africa (CIIFA) is a Lagos company that builds practical things for creative people: a home (the SafeHouse), programmes that teach the business of creativity, and events where talent meets opportunity. We are a business, not a charity, and we measure ourselves by what we deliver.</p>

    <h2 id="impact">The numbers so far</h2>
    <p><strong>12,000+ creatives trained</strong> across Nigeria with Google.org. <strong>1,800+ professionals developed</strong> through the Music Business Academy. <strong>30+ creative startups</strong> supported with the British Council. <strong>50+ talents</strong> taken from discovery to career-ready. Programmes delivered with the French Embassy, SACEM and more.</p>
''' + PLOGOS + '''

    <h2 id="ctf">The foundation we build with</h2>
    <p>The Creative Talent Foundation (CTF) develops Africa's creative talent through patient, mission-first programmes; CIIFA designs and runs the engine behind them. CBA for Africa, our creative business school, is a CTF programme executed by CIIFA.</p>
  </div>
</section>

<section class="block tint" id="team">
  <div class="wrap">
    <h2 class="title">The people</h2>
    <p class="sub">A small senior team that keeps the machine honest.</p>
    <div class="grid p2">
''' + TEAM + '''
    </div>
  </div>
</section>

''' + FOOTER + '''

<script src="assets/js/nav.js"></script>
</body>
</html>
'''

contact = head('Contact · CIIFA',
               'Talk to CIIFA: bookings, programmes, partnerships, press. One address, one number, one building in Ikoyi.',
               'contact.html') + NAV + '''

<header class="hero slim">
  <div class="wrap">
    <div class="kicker">Contact</div>
    <h1>Say hello.</h1>
    <p class="lead">One address, one number, one building in Ikoyi. Tell us what you need and the right person answers.</p>
  </div>
</header>

<section class="block">
  <div class="wrap">
    <div class="grid p3">
      <div class="card" style="--pc:var(--lime)"><span class="bar"></span>
        <div class="tag">Email</div>
        <h3><a href="mailto:info@ciif.africa">info@ciif.africa</a></h3>
        <p>Anything at all. We route it to the right person.</p>
      </div>
      <div class="card" style="--pc:var(--fair)"><span class="bar"></span>
        <div class="tag">Phone</div>
        <h3><a href="tel:+2347017341434">0701 734 1434</a></h3>
        <p>Monday to Friday, Lagos hours.</p>
      </div>
      <div class="card" style="--pc:var(--safe)"><span class="bar"></span>
        <div class="tag">Visit</div>
        <h3>The SafeHouse</h3>
        <p>4B Onikoyi Lane, Parkview Estate, Ikoyi, Lagos.</p>
      </div>
    </div>

    <h2 class="title" style="margin-top:44px">Or write to us right here</h2>
    <form class="f-form" action="https://formsubmit.co/info@ciif.africa" method="POST" style="margin-top:14px">
      <input type="hidden" name="_subject" value="Website enquiry (ciif.africa)">
      <input type="hidden" name="_cc" value="gt@godwintom.com,ea@godwintom.com">
      <input type="hidden" name="_template" value="table">
      <input type="hidden" name="_captcha" value="false">
      <input type="hidden" name="_next" value="https://ciif.africa/thanks.html">
      <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
      <div><label for="c-name">Your name</label><input id="c-name" type="text" name="name" required></div>
      <div><label for="c-email">Email</label><input id="c-email" type="email" name="email" required></div>
      <div><label for="c-topic">What's it about?</label>
        <select id="c-topic" name="topic" required>
          <option value="">Choose a topic</option>
          <option>Booking the SafeHouse</option>
          <option>Food Days</option>
          <option>A programme</option>
          <option>Partnership or sponsorship</option>
          <option>The Investors Session</option>
          <option>Press / media</option>
          <option>Something else</option>
        </select></div>
      <div><label for="c-msg">Your message</label><textarea id="c-msg" name="message" required></textarea></div>
      <button type="submit">Send message</button>
    </form>
  </div>
</section>

''' + FOOTER + '''

<script src="assets/js/nav.js"></script>
</body>
</html>
'''

with io.open(os.path.join(SITE, 'about.html'), 'w', encoding='utf-8') as fh:
    fh.write(about)
with io.open(os.path.join(SITE, 'contact.html'), 'w', encoding='utf-8') as fh:
    fh.write(contact)
print('about.html + contact.html written')
