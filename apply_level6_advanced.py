import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

results = {}

# ══════════════════════════════════════════════════════════════
# 1. CSS: .svc-card.active (Mobile Touch-Äquivalent zu :hover)
#         + Typewriter-Cursor #hero-typed
#         + Hero-Parallax ID
# ══════════════════════════════════════════════════════════════
old_arrow_css = '''    /* Pfeil */
    .svc-arrow { transition: transform .3s; color: #5DD4F0; }
    .svc-card:hover .svc-arrow { transform: translateX(5px); }'''

new_arrow_css = '''    /* Pfeil */
    .svc-arrow { transition: transform .3s; color: #5DD4F0; }
    .svc-card:hover .svc-arrow { transform: translateX(5px); }
    .svc-card.active  .svc-arrow { transform: translateX(5px); }

    /* ── Mobile Touch: .active spiegelt :hover komplett ── */
    .svc-card.active { transform: translateY(-6px); box-shadow: 0 24px 60px rgba(0,0,0,.25); }
    .svc-card.active .svc-bg      { transform: scale(1.06); }
    .svc-card.active .svc-default { opacity: 0; pointer-events: none; }
    .svc-card.active .svc-content { opacity: 1; }

    /* ── Typewriter Cursor im Hero ── */
    #hero-typed { color: #5DD4F0; }
    #hero-typed::after {
      content: '|';
      display: inline-block;
      margin-left: 2px;
      animation: blink .75s step-end infinite;
    }
    @keyframes blink { 50% { opacity: 0; } }'''

if old_arrow_css in html:
    html = html.replace(old_arrow_css, new_arrow_css)
    results['CSS mobile active + typewriter cursor'] = 'OK'
else:
    results['CSS mobile active + typewriter cursor'] = 'FEHLER: Anker nicht gefunden'

# ══════════════════════════════════════════════════════════════
# 2. Hero-Tagline: letztes Wort in <span id="hero-typed"> wrappen
# ══════════════════════════════════════════════════════════════
old_tagline = '        SCHNELL &middot; ZUVERLÄSSIG &middot; LIZENZIERT'
new_tagline = '        SCHNELL &middot; ZUVERLÄSSIG &middot; <span id="hero-typed">LIZENZIERT</span>'

if old_tagline in html:
    html = html.replace(old_tagline, new_tagline)
    results['Hero Tagline Span'] = 'OK'
else:
    results['Hero Tagline Span'] = 'FEHLER: Tagline nicht gefunden'

# ══════════════════════════════════════════════════════════════
# 3. Hero-Section: id="hero-section" für JS-Parallax
# ══════════════════════════════════════════════════════════════
old_hero_section = '<section class="hero-img min-h-screen flex flex-col justify-center pt-20 pb-16 relative overflow-hidden">'
new_hero_section = '<section id="hero-section" class="hero-img min-h-screen flex flex-col justify-center pt-20 pb-16 relative overflow-hidden">'

if old_hero_section in html:
    html = html.replace(old_hero_section, new_hero_section)
    results['Hero Section ID'] = 'OK'
else:
    results['Hero Section ID'] = 'FEHLER: Hero-Anker nicht gefunden'

# ══════════════════════════════════════════════════════════════
# 4. JS: Typewriter + Parallax + Mobile Touch
# ══════════════════════════════════════════════════════════════
old_js_end = '''// ── L6: Page-Load Fade-in ──
window.addEventListener('load', function() {
  setTimeout(function() { document.body.classList.add('loaded'); }, 60);
});
</script>'''

new_js_end = '''// ── L6: Page-Load Fade-in ──
window.addEventListener('load', function() {
  setTimeout(function() { document.body.classList.add('loaded'); }, 60);
});

// ── L6 Advanced: Typewriter auf Hero-Tagline ──
(function() {
  var el = document.getElementById('hero-typed');
  if (!el) return;
  var words = ['LIZENZIERT', 'ERFAHREN', '24/7 VOR ORT', 'IHR PARTNER', 'FAIR & KOMPETENT'];
  var wi = 0, ci = 0, del = false;
  function tick() {
    var w = words[wi];
    if (!del) {
      ci++;
      el.textContent = w.slice(0, ci);
      if (ci === w.length) { del = true; setTimeout(tick, 2200); return; }
      setTimeout(tick, 110);
    } else {
      ci--;
      el.textContent = w.slice(0, ci);
      if (ci === 0) { del = false; wi = (wi + 1) % words.length; }
      setTimeout(tick, 55);
    }
  }
  setTimeout(tick, 1800);
})();

// ── L6 Advanced: Hero-Parallax (Desktop only) ──
(function() {
  var hero = document.getElementById('hero-section');
  if (!hero) return;
  function onScroll() {
    if (window.innerWidth < 768) return;
    var offset = window.scrollY;
    hero.style.backgroundPositionY = 'calc(40% + ' + (offset * 0.22) + 'px)';
  }
  window.addEventListener('scroll', onScroll, { passive: true });
})();

// ── L6 Advanced: Mobile Touch für Service-Cards ──
(function() {
  var cards = document.querySelectorAll('.svc-card');
  cards.forEach(function(card) {
    card.addEventListener('click', function(e) {
      // Wenn Modal-Button geklickt: nicht togglen
      if (e.target.closest('button[onclick]') || e.target.closest('a')) return;
      var isActive = card.classList.contains('active');
      // Alle anderen schließen
      cards.forEach(function(c) { c.classList.remove('active'); });
      if (!isActive) card.classList.add('active');
    });
  });
  // Klick außerhalb → alle schließen
  document.addEventListener('click', function(e) {
    if (!e.target.closest('.svc-card')) {
      cards.forEach(function(c) { c.classList.remove('active'); });
    }
  });
})();
</script>'''

if old_js_end in html:
    html = html.replace(old_js_end, new_js_end)
    results['JS Typewriter + Parallax + Touch'] = 'OK'
else:
    results['JS Typewriter + Parallax + Touch'] = 'FEHLER: JS-Anker nicht gefunden'

# ══════════════════════════════════════════════════════════════
# SPEICHERN
# ══════════════════════════════════════════════════════════════
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('\n=== Level 6 Advanced ===\n')
for k, v in results.items():
    print(f'  {"OK  ✓" if v == "OK" else "FEHLER →"} [{k}]')
    if v != 'OK':
        print(f'         → {v}')

print('\n--- Verifikation ---')
checks = {
    'svc-card.active CSS':       '.svc-card.active {' in html,
    '#hero-typed span':          'id="hero-typed"' in html,
    'blink animation':           'animation: blink' in html,
    'hero-section id':           'id="hero-section"' in html,
    'Typewriter JS':             'words[wi]' in html,
    'Parallax JS':               'backgroundPositionY' in html,
    'Mobile Touch JS':           'svc-card' in html and 'classList.remove' in html,
}
for k, v in checks.items():
    print(f'  {"OK" if v else "FEHLER"} - {k}')
