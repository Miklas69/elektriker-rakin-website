import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

with open('index_website.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ─── 1. REPLACE SVC-CARD CSS WITH HOVER-REVEAL SYSTEM ────────────────────────

old_svc_css = """.svc-card {
      position: relative;
      overflow: hidden;
      border: 1px solid rgba(24,149,187,.15);
      border-radius: 20px;
      background: #fff;
      transition: transform .35s ease, box-shadow .35s ease, border-color .35s ease;
    }
    .svc-card::before {
      content: '';
      position: absolute;
      inset: 0;
      background: rgba(0,0,0,.00);
      transition: background .35s ease;
      z-index: 1;
    }
    .svc-card:hover {
      transform: translateY(-6px);
      border-color: rgba(24,149,187,.5);
      box-shadow: 0 20px 50px rgba(24,149,187,.18), 0 0 0 1px rgba(24,149,187,.15);
    }
    .svc-card:hover::before { background: rgba(0,0,0,.10); }
    .svc-card .svc-bg {
      position: absolute;
      inset: 0;
      background-size: cover;
      background-position: center;
      transition: transform .5s ease;
      z-index: 0;
    }
    .svc-card:hover .svc-bg { transform: scale(1.08); }
    .svc-content { position: relative; z-index: 2; }
    .svc-arrow { transition: transform .3s, color .3s; }
    .svc-card:hover .svc-arrow { transform: translateX(5px); color: var(--primary); }
    .svc-icon { transition: background .3s, color .3s; }
    .svc-card:hover .svc-icon { background: rgba(24,149,187,.20); color: #1895BB; }"""

new_svc_css = """/* Service cards – Hover Reveal */
    .svc-card {
      position: relative;
      overflow: hidden;
      border-radius: 20px;
      min-height: 280px;
      cursor: pointer;
      transition: transform .4s ease, box-shadow .4s ease;
    }
    .svc-card:hover {
      transform: translateY(-6px);
      box-shadow: 0 24px 60px rgba(0,0,0,.25);
    }
    .svc-card .svc-bg {
      position: absolute;
      inset: 0;
      background-size: cover;
      background-position: center;
      transition: transform .5s ease;
      z-index: 0;
    }
    .svc-card:hover .svc-bg { transform: scale(1.06); }

    /* Standard: nur Titel am unteren Rand */
    .svc-default {
      position: absolute;
      bottom: 0; left: 0; right: 0;
      padding: 3rem 1.75rem 1.75rem;
      background: linear-gradient(to top, rgba(0,0,0,.75) 0%, transparent 100%);
      z-index: 2;
      transition: opacity .35s ease;
    }
    .svc-card:hover .svc-default { opacity: 0; pointer-events: none; }

    /* Hover: dunkler Overlay + voller Inhalt */
    .svc-content {
      position: absolute;
      inset: 0;
      background: rgba(15,25,35,.82);
      padding: 1.75rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      z-index: 3;
      opacity: 0;
      transition: opacity .35s ease;
    }
    .svc-card:hover .svc-content { opacity: 1; }

    /* Icon */
    .svc-icon {
      width: 3rem; height: 3rem;
      border-radius: 0.75rem;
      background: rgba(24,149,187,.3);
      color: #5DD4F0;
      display: flex; align-items: center; justify-content: center;
      margin-bottom: 1rem;
    }

    /* Pfeil */
    .svc-arrow { transition: transform .3s; color: #5DD4F0; }
    .svc-card:hover .svc-arrow { transform: translateX(5px); }"""

if old_svc_css in html:
    html = html.replace(old_svc_css, new_svc_css)
    print("CSS Hover-Reveal ersetzt OK")
else:
    print("FEHLER: Alter CSS-Block nicht gefunden!")

# ─── 2. SIMPLIFY CLASS ATTRIBUTES ────────────────────────────────────────────

html = html.replace(
    'class="svc-content p-7 h-full flex flex-col justify-between min-h-[280px]"',
    'class="svc-content"'
)
html = html.replace(
    'class="svc-icon w-12 h-12 rounded-xl bg-primary/15 text-primary flex items-center justify-center mb-4"',
    'class="svc-icon"'
)
html = html.replace(
    'class="svc-arrow mt-6 text-sm font-semibold text-muted-light flex items-center gap-2"',
    'class="svc-arrow mt-4 text-sm font-semibold flex items-center gap-2"'
)
# h3 in cards -> white (visible on dark hover overlay)
html = html.replace(
    'class="text-xl font-bold text-text mb-2"',
    'class="text-xl font-bold text-white mb-2"'
)
# description text -> light gray on dark overlay
html = html.replace(
    'class="text-sm text-muted-light leading-relaxed"',
    'class="text-sm text-gray-300 leading-relaxed"'
)
print("Klassen vereinfacht OK")

# ─── 3. INJECT svc-default TITLE BARS ────────────────────────────────────────

# Each service card has a unique title - we inject svc-default BEFORE svc-content
# by finding the svc-bg closing div + svc-content opening for each card

cards = [
    ("Elektriker-Notdienst",      "Elektriker-Notdienst"),
    ("Elektroinstallation",        "Elektroinstallation"),
    ("Sanierung &amp; Renovierung","Sanierung &amp; Renovierung"),
    ("Wallbox &amp; E-Mobilit",    "Wallbox &amp; E-Mobilität"),
    ("Balkonkraftwerk",            "Balkonkraftwerk"),
    ("Netzwerktechnik",            "Netzwerktechnik"),
]

for search_title, display_title in cards:
    h3_marker = f'>{search_title}'
    idx = html.find(h3_marker)
    if idx == -1:
        print(f"NICHT GEFUNDEN: {search_title}")
        continue

    # Find the opening of svc-content before this h3
    svc_pos = html.rfind('<div class="svc-content">', 0, idx)
    if svc_pos == -1:
        print(f"svc-content nicht gefunden fuer: {search_title}")
        continue

    # Inject svc-default right before svc-content
    inject = (
        f'\n        <!-- Standard: Titel sichtbar -->\n'
        f'        <div class="svc-default">\n'
        f'          <h3 class="text-xl font-bold text-white">{display_title}</h3>\n'
        f'        </div>\n        '
    )
    html = html[:svc_pos] + inject + html[svc_pos:]
    print(f"svc-default eingefuegt: {search_title}")

# ─── 4. SAVE ─────────────────────────────────────────────────────────────────
with open('index_website.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("\nGespeichert!")
