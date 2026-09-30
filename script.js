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

// Express Interest form — posts to Formspree in the background and shows an inline
// success state. Until a real Formspree ID is set on the form's action, the button
// falls back to a prefilled email so it still works.
(function () {
  var form = document.getElementById('interest-form');
  if (!form) return;
  var status = form.querySelector('.form__status');
  var success = document.getElementById('interest-success');
  var btn = form.querySelector('button[type="submit"]');
  var fallback = form.getAttribute('data-fallback-email') || '';
  var configured = /formspree\.io\/f\/[a-z0-9]+$/i.test(form.action) && form.action.indexOf('YOUR_FORM_ID') === -1;

  function showError(msg) {
    status.textContent = msg;
    status.hidden = false;
    btn.disabled = false;
  }

  form.addEventListener('submit', function (e) {
    if (!form.checkValidity()) return; // let the browser show its validation messages

    if (!configured) {
      e.preventDefault();
      var lines = [];
      new FormData(form).forEach(function (v, k) {
        if (k.charAt(0) !== '_' && String(v).trim()) lines.push(k + ': ' + v);
      });
      window.location.href = 'mailto:' + fallback +
        '?subject=' + encodeURIComponent('Express interest — Hawaiʻi Co-op Hui') +
        '&body=' + encodeURIComponent(lines.join('\n'));
      return;
    }

    if (!window.fetch) return; // very old browser: plain POST to Formspree's own thank-you page
    e.preventDefault();
    btn.disabled = true;
    status.hidden = true;
    fetch(form.action, { method: 'POST', body: new FormData(form), headers: { 'Accept': 'application/json' } })
      .then(function (r) {
        if (!r.ok) throw new Error('HTTP ' + r.status);
        form.hidden = true;
        success.hidden = false;
        success.setAttribute('tabindex', '-1');
        success.focus();
      })
      .catch(function () {
        showError('Something went wrong sending that. Please try again' + (fallback ? ', or email ' + fallback : '') + '.');
      });
  });
})();
