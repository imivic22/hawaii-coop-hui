// Hawaiʻi Co-op Hui — behavior: (1) mobile menu, (2) active-section nav highlight.

// Mobile menu
(function () {
  var toggle = document.getElementById('navtoggle');
  var links = document.getElementById('navlinks');
  if (!toggle || !links) return;

  function isMobile() { return window.matchMedia('(max-width:1000px)').matches; }

  function setHidden(h) {
    if (isMobile()) { links.hidden = h; } else { links.hidden = false; }
    toggle.setAttribute('aria-expanded', String(!h && isMobile()));
  }

  setHidden(true);
  toggle.addEventListener('click', function () { setHidden(!links.hidden); });
  links.addEventListener('click', function (e) {
    if (e.target.closest('a') && isMobile()) { setHidden(true); }
  });
  window.addEventListener('resize', function () {
    if (!isMobile()) { links.hidden = false; }
    else if (toggle.getAttribute('aria-expanded') !== 'true') { links.hidden = true; }
  });
})();

// Active-section highlight
(function () {
  var map = {};
  document.querySelectorAll('.nav__links a').forEach(function (a) {
    var id = a.getAttribute('href').slice(1);
    if (id) map[id] = a;
  });
  var ids = Object.keys(map);
  if (!ids.length || !('IntersectionObserver' in window)) return;

  var obs = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting) {
        ids.forEach(function (id) { map[id].classList.remove('active'); });
        var m = map[en.target.id];
        if (m) m.classList.add('active');
      }
    });
  }, { rootMargin: '-45% 0px -50% 0px', threshold: 0 });

  ids.forEach(function (id) {
    var el = document.getElementById(id);
    if (el) obs.observe(el);
  });
})();
