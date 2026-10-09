// Site behaviour shared by every page: theme toggle, copy buttons, "On this page"
// highlighting and collapsible sections on phones. Everything degrades to plain links.
(function () {
  var doc = document.documentElement;

  // Theme: automatic (follows the system), light or dark. The choice is kept per browser.
  var btn = document.getElementById('theme-toggle');
  var order = ['auto', 'light', 'dark'];
  function current() {
    try { return localStorage.getItem('xqtl-theme') || 'auto'; } catch (e) { return 'auto'; }
  }
  function apply(mode) {
    if (mode === 'auto') doc.removeAttribute('data-theme'); else doc.setAttribute('data-theme', mode);
    doc.setAttribute('data-theme-pref', mode);
    if (btn) btn.setAttribute('aria-label', 'Colour theme: ' + (mode === 'auto' ? 'automatic' : mode));
  }
  apply(current());
  if (btn) btn.addEventListener('click', function () {
    var next = order[(order.indexOf(current()) + 1) % order.length];
    try { localStorage.setItem('xqtl-theme', next); } catch (e) {}
    apply(next);
  });

  // Copy buttons: [data-copy] copies its value, code blocks copy their text
  function copy(text, el) {
    var done = function () {
      var old = el.textContent;
      el.textContent = 'Copied';
      setTimeout(function () { el.textContent = old; }, 1400);
    };
    if (navigator.clipboard) navigator.clipboard.writeText(text).then(done, function () {});
  }
  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-copy]');
    if (b) { copy(b.getAttribute('data-copy'), b); return; }
    var c = e.target.closest('[data-copy-code]');
    if (c) {
      var code = c.closest('.codeblock').querySelector('pre code, pre');
      copy(code.innerText.replace(/\n$/, ''), c);
    }
  });

  // Close the phone menu with Escape
  var navToggle = document.getElementById('nav-toggle');
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && navToggle && navToggle.checked) navToggle.checked = false;
  });
  document.querySelectorAll('.topbar__menu').forEach(function (l) {
    l.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); navToggle.checked = !navToggle.checked; }
    });
  });

  // "On this page": mark the section in view
  var toc = document.querySelector('.pagetoc');
  if (toc && 'IntersectionObserver' in window) {
    var links = Array.prototype.slice.call(toc.querySelectorAll('a[href^="#"]'));
    var targets = links.map(function (a) { return document.getElementById(decodeURIComponent(a.hash.slice(1))); });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var i = targets.indexOf(en.target);
        if (i < 0) return;
        links.forEach(function (a) { a.classList.remove('is-current'); });
        links[i].classList.add('is-current');
      });
    }, { rootMargin: '0px 0px -70% 0px' });
    targets.forEach(function (t) { if (t) io.observe(t); });
  }

  // Phones: the Markdown sections of a dataset page fold under their headings (design 3b)
  var prose = document.querySelector('.page--dataset .prose');
  if (prose && window.matchMedia('(max-width: 720px)').matches) {
    var hs = Array.prototype.slice.call(prose.children).filter(function (n) { return n.tagName === 'H2'; });
    hs.forEach(function (h) {
      var det = document.createElement('details');
      det.className = 'fold';
      var sum = document.createElement('summary');
      sum.innerHTML = h.innerHTML;
      sum.id = h.id;
      det.appendChild(sum);
      var n = h.nextSibling;
      while (n && n.tagName !== 'H2') { var nx = n.nextSibling; det.appendChild(n); n = nx; }
      h.replaceWith(det);
    });
    if (location.hash) {
      var t = document.getElementById(decodeURIComponent(location.hash.slice(1)));
      var d = t && t.closest('details'); if (d) d.open = true;
    }
  }

  // The previous theme registered a service worker; remove it so pages are never stale
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.getRegistrations().then(function (rs) { rs.forEach(function (r) { r.unregister(); }); }).catch(function () {});
  }
})();
