// Data catalog filters. Rows, facets and the cohort x modality matrix are rendered by
// layouts/catalog.html; this script shows and hides rows in place. Filter state is kept
// in the URL (?q=&cohort=&family=...) so a filtered view can be linked, for example from
// the coverage matrix on the home page.
(function () {
  var root = document.querySelector('[data-catalog]');
  if (!root) return;

  var KEYS = ['kind', 'cohort', 'family', 'tissue', 'status', 'access'];
  var rows = Array.prototype.slice.call(root.querySelectorAll('[data-row]'));
  var opts = Array.prototype.slice.call(root.querySelectorAll('[data-facet]'));
  var qInput = root.querySelector('[data-q]');
  var countEl = root.querySelector('[data-count]');
  var emptyEl = root.querySelector('[data-empty]');
  var filterCountEl = root.querySelector('[data-filter-count]');
  var clearBtns = root.querySelectorAll('[data-clear]');
  var state = { q: '' };
  KEYS.forEach(function (k) { state[k] = null; });

  // Read the initial state from the URL
  var params = new URLSearchParams(location.search);
  KEYS.forEach(function (k) { if (params.get(k)) state[k] = params.get(k); });
  state.q = params.get('q') || '';
  qInput.value = state.q;

  function matches(row, except) {
    for (var i = 0; i < KEYS.length; i++) {
      var k = KEYS[i];
      if (k !== except && state[k] && row.dataset[k] !== state[k]) return false;
    }
    var q = state.q.trim().toLowerCase();
    if (q) {
      var words = q.split(/\s+/);
      for (var j = 0; j < words.length; j++) if (row.dataset.search.indexOf(words[j]) < 0) return false;
    }
    return true;
  }

  function writeURL() {
    var p = new URLSearchParams();
    if (state.q) p.set('q', state.q);
    KEYS.forEach(function (k) { if (state[k]) p.set(k, state[k]); });
    var s = p.toString();
    history.replaceState(null, '', location.pathname + (s ? '?' + s : '') + location.hash);
  }

  function render() {
    var shown = 0;
    rows.forEach(function (r) {
      var ok = matches(r);
      r.hidden = !ok;
      if (ok) shown++;
    });
    // Facet counts: how many rows each option would give, given the other filters
    opts.forEach(function (o) {
      var k = o.dataset.facet, v = o.dataset.value, on = state[k] === v;
      var n = 0;
      rows.forEach(function (r) { if (r.dataset[k] === v && matches(r, k)) n++; });
      o.setAttribute('aria-pressed', on ? 'true' : 'false');
      var c = o.querySelector('[data-count-for]');
      if (c) c.textContent = n;
      if (o.classList.contains('fopt')) o.disabled = !n && !on;
    });
    // Matrix: highlight the selected cell, row or column, dim the rest
    root.querySelectorAll('[data-matrix-cell]').forEach(function (b) {
      var cf = b.dataset.matrixCell.split('|');
      var on = state.cohort === cf[0] && state.family === cf[1];
      var dim = (state.cohort && state.cohort !== cf[0]) || (state.family && state.family !== cf[1]);
      b.setAttribute('aria-pressed', on ? 'true' : 'false');
      b.classList.toggle('is-dim', !!dim);
    });
    root.querySelectorAll('[data-matrix-row]').forEach(function (tr) {
      tr.classList.toggle('is-selected', state.cohort === tr.dataset.matrixRow);
    });
    root.querySelectorAll('[data-matrix-col]').forEach(function (b) {
      b.classList.toggle('is-selected', state.family === b.dataset.matrixCol);
    });
    var nF = KEYS.filter(function (k) { return state[k]; }).length;
    countEl.textContent = shown + ' of ' + rows.length + ' shown';
    emptyEl.hidden = shown > 0;
    if (filterCountEl) filterCountEl.textContent = nF;
    clearBtns.forEach(function (b) { if (b.closest('.catalog__mobilebar')) b.hidden = !(nF || state.q); });
    writeURL();
  }

  opts.forEach(function (o) {
    o.addEventListener('click', function () {
      var k = o.dataset.facet, v = o.dataset.value;
      state[k] = state[k] === v ? null : v;
      render();
    });
  });

  var t;
  qInput.addEventListener('input', function () {
    clearTimeout(t);
    t = setTimeout(function () { state.q = qInput.value; render(); }, 120);
  });

  clearBtns.forEach(function (b) {
    b.addEventListener('click', function () {
      KEYS.forEach(function (k) { state[k] = null; });
      state.q = ''; qInput.value = '';
      render();
    });
  });

  root.querySelectorAll('[data-matrix-cell]').forEach(function (b) {
    b.addEventListener('click', function () {
      var cf = b.dataset.matrixCell.split('|');
      var on = state.cohort === cf[0] && state.family === cf[1];
      state.cohort = on ? null : cf[0];
      state.family = on ? null : cf[1];
      state.kind = on ? null : 'qtl';
      render();
    });
  });
  root.querySelectorAll('[data-matrix-row-btn]').forEach(function (b) {
    b.addEventListener('click', function () {
      var c = b.dataset.matrixRowBtn, on = state.cohort === c && !state.family;
      state.cohort = on ? null : c; state.family = null;
      render();
    });
  });
  root.querySelectorAll('[data-matrix-col]').forEach(function (b) {
    b.addEventListener('click', function () {
      var f = b.dataset.matrixCol, on = state.family === f && !state.cohort;
      state.family = on ? null : f; state.cohort = null;
      render();
    });
  });

  // Phones: facets open as a sheet
  var facets = root.querySelector('#facets');
  var openBtn = root.querySelector('[data-filters-open]');
  var closeBtn = root.querySelector('[data-filters-close]');
  function sheet(open) {
    facets.classList.toggle('is-open', open);
    openBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    if (open) facets.querySelector('button').focus(); else openBtn.focus();
  }
  openBtn.addEventListener('click', function () { sheet(true); });
  closeBtn.addEventListener('click', function () { sheet(false); });
  facets.addEventListener('keydown', function (e) { if (e.key === 'Escape') sheet(false); });

  render();
})();
