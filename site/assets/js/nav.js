// mobile nav toggle + active-link highlight
document.addEventListener('DOMContentLoaded', function () {
  var btn = document.querySelector('.menubtn');
  var links = document.querySelector('.navlinks');
  if (btn && links) {
    btn.setAttribute('aria-expanded', 'false');
    btn.setAttribute('aria-controls', 'navlinks');
    links.id = links.id || 'navlinks';
    btn.addEventListener('click', function () {
      var open = links.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }
  var here = location.pathname.replace(/index\.html$/, '');
  document.querySelectorAll('.navlinks a').forEach(function (a) {
    var href = a.getAttribute('href');
    if (!href || a.classList.contains('cta')) return;
    var target = new URL(href, location.href).pathname.replace(/index\.html$/, '');
    if (target === here || (target !== '/' && here.indexOf(target.replace(/\.html$/, '')) === 0)) {
      a.classList.add('active');
    }
  });
});
