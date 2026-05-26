import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

results = {}

# ══════════════════════════════════════════════════════════════
# 1. Scroll-Fortschrittsleiste: <div id="scroll-bar"> nach <body>
# ══════════════════════════════════════════════════════════════
old_body = '<body>\n\n<!-- ═══════════════════════════════════════════\n     HEADER'
new_body = '''<body>

<div id="scroll-bar"></div>

<!-- ═══════════════════════════════════════════
     HEADER'''

if old_body in html:
    html = html.replace(old_body, new_body)
    results['Scroll-Bar HTML'] = 'OK'
else:
    results['Scroll-Bar HTML'] = 'FEHLER: Anker nicht gefunden'

# ══════════════════════════════════════════════════════════════
# 2. CSS ans Ende des <style>-Blocks
# ══════════════════════════════════════════════════════════════
old_style_end = '''    /* Scrollbar */
    ::-webkit-scrollbar-thumb { background: #1895BB !important; }
</style>'''

new_style_end = '''    /* Scrollbar */
    ::-webkit-scrollbar-thumb { background: #1895BB !important; }

    /* ── L6: Scroll-Fortschrittsleiste ── */
    #scroll-bar {
      position: fixed;
      top: 0; left: 0;
      height: 3px;
      background: linear-gradient(90deg, #1895BB, #5DD4F0);
      width: 0%;
      z-index: 9999;
      transition: width .08s linear;
      pointer-events: none;
    }

    /* ── L6: Page-Load Fade-in ── */
    body { opacity: 0 !important; transition: opacity .45s ease !important; }
    body.loaded { opacity: 1 !important; }

    /* ── L6: Hero-Headline Shimmer ── */
    .hero-shimmer {
      background: linear-gradient(100deg, #1895BB 0%, #5DD4F0 38%, #1E3E4F 55%, #1895BB 100%);
      background-size: 300% 100%;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      animation: shimmer 5s ease infinite;
    }
    @keyframes shimmer {
      0%   { background-position: 100% 50%; }
      100% { background-position:   0% 50%; }
    }

    /* ── L6: Marquee / Scroll-Ticker ── */
    .marquee-strip {
      background: #1E3E4F;
      overflow: hidden;
      padding: 14px 0;
      position: relative;
      white-space: nowrap;
    }
    .marquee-inner {
      display: inline-block;
      animation: marquee 35s linear infinite;
    }
    .marquee-inner:hover { animation-play-state: paused; }
    @keyframes marquee {
      0%   { transform: translateX(0); }
      100% { transform: translateX(-50%); }
    }
    .marquee-item {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      padding: 0 32px;
      font-family: 'Bebas Neue', sans-serif;
      font-size: 1rem;
      letter-spacing: .15em;
      color: rgba(255,255,255,.75);
    }
    .marquee-dot {
      display: inline-block;
      width: 5px; height: 5px;
      border-radius: 50%;
      background: #1895BB;
      flex-shrink: 0;
    }
</style>'''

if old_style_end in html:
    html = html.replace(old_style_end, new_style_end)
    results['CSS L6'] = 'OK'
else:
    results['CSS L6'] = 'FEHLER: </style>-Anker nicht gefunden'

# ══════════════════════════════════════════════════════════════
# 3. Hero-Span: gradient-text → gradient-text hero-shimmer
# ══════════════════════════════════════════════════════════════
old_hero_span = '<span class="gradient-text">ELEKTRIKER</span>'
new_hero_span = '<span class="gradient-text hero-shimmer">ELEKTRIKER</span>'

if old_hero_span in html:
    html = html.replace(old_hero_span, new_hero_span)
    results['Hero Shimmer Klasse'] = 'OK'
else:
    results['Hero Shimmer Klasse'] = 'FEHLER: Span nicht gefunden'

# ══════════════════════════════════════════════════════════════
# 4. Marquee-Strip zwischen Hero und Leistungen einfügen
# ══════════════════════════════════════════════════════════════
old_leistungen_anchor = '''<!-- ═══════════════════════════════════════════
     LEISTUNGEN
═══════════════════════════════════════════ -->
<section id="leistungen"'''

# Marquee-Inhalt: doppelt für nahtlosen Loop
marquee_content = ('⚡ NOTDIENST 24/7'
    + ' · WALLBOX-INSTALLATION'
    + ' · ZÄHLERSCHRANK & UNTERVERTEILER'
    + ' · REGENSBURG & UMGEBUNG'
    + ' · LIZENZIERTER FACHBETRIEB'
    + ' · 100+ REALISIERTE PROJEKTE'
    + ' · SCHNELL · ZUVERLÄSSIG · LIZENZIERT')

new_leistungen_anchor = '''<!-- ═══════════════════════════════════════════
     MARQUEE TICKER
═══════════════════════════════════════════ -->
<div class="marquee-strip">
  <div class="marquee-inner" aria-hidden="true">
    <span class="marquee-item"><span class="marquee-dot"></span>NOTDIENST 24/7</span>
    <span class="marquee-item"><span class="marquee-dot"></span>WALLBOX-INSTALLATION</span>
    <span class="marquee-item"><span class="marquee-dot"></span>ZÄHLERSCHRANK &amp; UNTERVERTEILER</span>
    <span class="marquee-item"><span class="marquee-dot"></span>REGENSBURG &amp; UMGEBUNG</span>
    <span class="marquee-item"><span class="marquee-dot"></span>LIZENZIERTER FACHBETRIEB</span>
    <span class="marquee-item"><span class="marquee-dot"></span>100+ PROJEKTE</span>
    <span class="marquee-item"><span class="marquee-dot"></span>SCHNELL · ZUVERLÄSSIG · LIZENZIERT</span>
    <span class="marquee-item"><span class="marquee-dot"></span>NOTDIENST 24/7</span>
    <span class="marquee-item"><span class="marquee-dot"></span>WALLBOX-INSTALLATION</span>
    <span class="marquee-item"><span class="marquee-dot"></span>ZÄHLERSCHRANK &amp; UNTERVERTEILER</span>
    <span class="marquee-item"><span class="marquee-dot"></span>REGENSBURG &amp; UMGEBUNG</span>
    <span class="marquee-item"><span class="marquee-dot"></span>LIZENZIERTER FACHBETRIEB</span>
    <span class="marquee-item"><span class="marquee-dot"></span>100+ PROJEKTE</span>
    <span class="marquee-item"><span class="marquee-dot"></span>SCHNELL · ZUVERLÄSSIG · LIZENZIERT</span>
  </div>
</div>

<!-- ═══════════════════════════════════════════
     LEISTUNGEN
═══════════════════════════════════════════ -->
<section id="leistungen"'''

if old_leistungen_anchor in html:
    html = html.replace(old_leistungen_anchor, new_leistungen_anchor)
    results['Marquee HTML'] = 'OK'
else:
    results['Marquee HTML'] = 'FEHLER: Leistungen-Anker nicht gefunden'

# ══════════════════════════════════════════════════════════════
# 5. JS: Scroll-Bar + Page-Load ans Ende des letzten <script>
# ══════════════════════════════════════════════════════════════
old_script_end = '''// Escape-Taste schließt Modal
document.addEventListener('keydown', e => {
  if (e.key === 'Escape' && sozialesModal.classList.contains('open')) {
    closeSozialesModal();
  }
});
</script>'''

new_script_end = '''// Escape-Taste schließt Modal
document.addEventListener('keydown', e => {
  if (e.key === 'Escape' && sozialesModal.classList.contains('open')) {
    closeSozialesModal();
  }
});

// ── L6: Scroll-Fortschrittsleiste ──
(function() {
  const bar = document.getElementById('scroll-bar');
  if (!bar) return;
  window.addEventListener('scroll', function() {
    const scrolled = window.scrollY;
    const total = document.body.scrollHeight - window.innerHeight;
    bar.style.width = (total > 0 ? (scrolled / total) * 100 : 0) + '%';
  }, { passive: true });
})();

// ── L6: Page-Load Fade-in ──
window.addEventListener('load', function() {
  setTimeout(function() { document.body.classList.add('loaded'); }, 60);
});
</script>'''

if old_script_end in html:
    html = html.replace(old_script_end, new_script_end)
    results['JS L6'] = 'OK'
else:
    results['JS L6'] = 'FEHLER: Script-Anker nicht gefunden'

# ══════════════════════════════════════════════════════════════
# SPEICHERN
# ══════════════════════════════════════════════════════════════
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('\n=== Level 6 Design-Feinschliff ===\n')
for k, v in results.items():
    status = 'OK  ✓' if v == 'OK' else f'FEHLER → {v}'
    print(f'  {status}  [{k}]')

# Verifikation
print('\n--- Verifikation ---')
checks = {
    'scroll-bar div':     '<div id="scroll-bar"></div>' in html,
    'body fade-in CSS':   'body.loaded { opacity: 1' in html,
    '#scroll-bar CSS':    '#scroll-bar {' in html,
    'shimmer animation':  'animation: shimmer' in html,
    'hero-shimmer Klasse':'hero-shimmer">ELEKTRIKER' in html,
    'marquee-strip':      'marquee-strip' in html,
    'marquee-inner':      'marquee-inner' in html,
    'JS scroll-bar':      'scroll-bar\');' in html or "getElementById('scroll-bar')" in html,
    'JS body.loaded':     "body.classList.add('loaded')" in html,
}
for k, v in checks.items():
    print(f'  {"OK" if v else "FEHLER"} - {k}')
