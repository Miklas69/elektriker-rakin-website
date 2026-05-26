import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Telefonnummern (vereinheitlicht)
TEL_HERBERT   = ('Herbert',   '0160 9162 8756', '+491609162876')
TEL_HELMUT    = ('Helmut',    '0160 9809 8000', '+4916098098000')
TEL_CHRISTIAN = ('Christian', '0151 5124 9333', '+4915151249333')

changes = []
def rep(old, new, label):
    global html
    if old in html:
        html = html.replace(old, new)
        changes.append(f'OK   {label}')
    else:
        changes.append(f'FAIL {label}')

# ═══════════════════════════════════════════════════════════════
# 1. REZENSIONEN: 28 → 30
# ═══════════════════════════════════════════════════════════════
rep('28 Rezensionen', '30 Rezensionen', '1. Rezensionen 28→30')

# ═══════════════════════════════════════════════════════════════
# 2. PROJEKTE: 500 → 100
# ═══════════════════════════════════════════════════════════════
rep(
    '<div class="counter-num text-5xl sm:text-6xl md:text-7xl gradient-text" data-target="500" data-suffix="+">0+</div>',
    '<div class="counter-num text-5xl sm:text-6xl md:text-7xl gradient-text" data-target="100" data-suffix="+">0+</div>',
    '2a. Stats Counter 500→100'
)
rep(
    '<div class="font-bebas text-2xl tracking-widest text-white">500+</div>',
    '<div class="font-bebas text-2xl tracking-widest text-white">100+</div>',
    '2b. Über-uns Badge 500→100'
)

# ═══════════════════════════════════════════════════════════════
# 3. 24H BUTTON: Immer rot + Glow on Hover
# ═══════════════════════════════════════════════════════════════
old_btn_css = """    .btn-outline-danger {
      border: 2px solid #EF4444;
      color: #EF4444;
      font-weight: 700;
      border-radius: 14px;
      transition: background .2s, color .2s, transform .2s;
    }
    .btn-outline-danger:hover { background: #EF4444; color: #fff; transform: translateY(-1px); }"""

new_btn_css = """    .btn-outline-danger {
      background: #EF4444;
      color: #fff;
      border: 2px solid #EF4444;
      font-weight: 700;
      border-radius: 14px;
      transition: box-shadow .25s ease, transform .25s ease, background .25s ease;
    }
    .btn-outline-danger:hover {
      background: #DC2626;
      box-shadow: 0 0 24px rgba(239,68,68,.6), 0 0 48px rgba(239,68,68,.3);
      transform: translateY(-1px) scale(1.02);
    }"""

rep(old_btn_css, new_btn_css, '3. 24h-Button immer rot + Glow')

# ═══════════════════════════════════════════════════════════════
# 4. TELEFONNUMMERN: Hero & Kontakt – alle 3 gleichrangig
# ═══════════════════════════════════════════════════════════════
# 4a. Im Hero unter den CTA-Buttons eine 3-spaltige Telefon-Karte einfügen
hero_old = """        <a href="tel:+491609162876" class="btn-outline-danger flex items-center gap-2 px-8 py-4 text-base">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
          Notfall? Jetzt anrufen
        </a>
      </div>"""

hero_new = """        <a href="tel:+491609162876" class="btn-outline-danger flex items-center gap-2 px-8 py-4 text-base">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
          Notfall? Jetzt anrufen
        </a>
      </div>

      <!-- Telefon: 3 Brüder, 3 gleichrangige Nummern -->
      <div class="grid sm:grid-cols-3 gap-3 max-w-2xl mb-12 fade-up delay-3">
        <a href="tel:+491609162876" class="group flex items-center gap-3 bg-white/[.06] hover:bg-white/[.12] border border-white/[.10] hover:border-[#5DD4F0]/40 rounded-xl px-4 py-3 transition-all">
          <div class="w-9 h-9 rounded-lg bg-[#5DD4F0]/15 flex items-center justify-center flex-shrink-0">
            <svg class="w-4 h-4 text-[#5DD4F0]" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
          </div>
          <div>
            <div class="text-[10px] uppercase tracking-widest text-white/60 font-semibold">Herbert</div>
            <div class="text-sm font-bold text-white">0160 9162 8756</div>
          </div>
        </a>
        <a href="tel:+4916098098000" class="group flex items-center gap-3 bg-white/[.06] hover:bg-white/[.12] border border-white/[.10] hover:border-[#5DD4F0]/40 rounded-xl px-4 py-3 transition-all">
          <div class="w-9 h-9 rounded-lg bg-[#5DD4F0]/15 flex items-center justify-center flex-shrink-0">
            <svg class="w-4 h-4 text-[#5DD4F0]" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
          </div>
          <div>
            <div class="text-[10px] uppercase tracking-widest text-white/60 font-semibold">Helmut</div>
            <div class="text-sm font-bold text-white">0160 9809 8000</div>
          </div>
        </a>
        <a href="tel:+4915151249333" class="group flex items-center gap-3 bg-white/[.06] hover:bg-white/[.12] border border-white/[.10] hover:border-[#5DD4F0]/40 rounded-xl px-4 py-3 transition-all">
          <div class="w-9 h-9 rounded-lg bg-[#5DD4F0]/15 flex items-center justify-center flex-shrink-0">
            <svg class="w-4 h-4 text-[#5DD4F0]" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
          </div>
          <div>
            <div class="text-[10px] uppercase tracking-widest text-white/60 font-semibold">Christian</div>
            <div class="text-sm font-bold text-white">0151 5124 9333</div>
          </div>
        </a>
      </div>"""

rep(hero_old, hero_new, '4a. Hero 3 Telefonnummern')

# ═══════════════════════════════════════════════════════════════
# 5. ÜBER UNS: Alle 3 als "Co-Gründer & Inhaber"
# ═══════════════════════════════════════════════════════════════
rep(
    'Gründer & Inhaber</p>\n          <p class="text-sm text-muted-light">Elektroinstallation',
    'Co-Gründer & Inhaber</p>\n          <p class="text-sm text-muted-light">Elektroinstallation',
    '5a. Herbert → Co-Gründer'
)
rep(
    'Inhaber</p>\n          <p class="text-sm text-muted-light">Sanierung',
    'Co-Gründer & Inhaber</p>\n          <p class="text-sm text-muted-light">Sanierung',
    '5b. Helmut → Co-Gründer'
)
rep(
    'Inhaber</p>\n          <p class="text-sm text-muted-light">Wallbox',
    'Co-Gründer & Inhaber</p>\n          <p class="text-sm text-muted-light">Wallbox',
    '5c. Christian → Co-Gründer'
)
rep(
    '<div class="text-xs text-muted-light">3 Inhaber</div>',
    '<div class="text-xs text-muted-light">3 Co-Gründer</div>',
    '5d. "3 Inhaber" → "3 Co-Gründer"'
)

# ═══════════════════════════════════════════════════════════════
# 6. SOZIALES ENGAGEMENT – komplett umbauen
# ═══════════════════════════════════════════════════════════════

# 6a. "bereitgestellt" → "gesponsert"
rep(
    'Rettungsleitsystem für den FC Oberhinkofen e.V.</strong> bereitgestellt',
    'Rettungsleitsystem für den FC Oberhinkofen e.V.</strong> gesponsert',
    '6a. "bereitgestellt" → "gesponsert"'
)

# 6b. Herz-Icon → Urkunden-Icon
old_heart_svg = """          <svg class="w-12 h-12 text-[#1895BB]" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z"/>
          </svg>"""

new_certificate_svg = """          <svg class="w-12 h-12 text-[#1895BB]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
            <!-- Dokument-Korpus mit gezackter Unterkante -->
            <path d="M6 3h12a1.5 1.5 0 0 1 1.5 1.5v12.5l-2.2-1.4-2.3 1.4-2.5-1.4-2.5 1.4-2.3-1.4L5 17.5V4.5A1.5 1.5 0 0 1 6 3z"/>
            <!-- Text-Linien -->
            <line x1="8.5" y1="7" x2="15.5" y2="7"/>
            <line x1="8.5" y1="9.5" x2="15.5" y2="9.5"/>
            <!-- Goldenes Siegel mit Häkchen -->
            <circle cx="12" cy="13" r="2.2" fill="#FBBF24" stroke="#FBBF24"/>
            <path d="M10.9 13l.8.8 1.6-1.8" stroke="#fff" stroke-width="1.2" fill="none"/>
          </svg>"""

rep(old_heart_svg, new_certificate_svg, '6b. Herz-Icon → Urkunden-Icon')

# 6c. Card klickbar machen (öffnet Modal beim Klick)
old_card_open = '''<section class="py-16 bg-bg">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="bg-white border border-[#1895BB]/15 rounded-3xl p-8 md:p-12 flex flex-col md:flex-row items-center gap-10 shadow-sm fade-up">'''

new_card_open = '''<section class="py-16 bg-bg">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="bg-white border border-[#1895BB]/15 rounded-3xl p-8 md:p-12 flex flex-col md:flex-row items-center gap-10 shadow-sm fade-up cursor-pointer transition-all hover:shadow-xl hover:-translate-y-1 hover:border-[#1895BB]/40"
         onclick="openSozialesModal()"
         role="button" tabindex="0"
         aria-label="Mehr Infos zum Sozialen Engagement"
         onkeydown="if(event.key==='Enter')openSozialesModal()">'''

rep(old_card_open, new_card_open, '6c. Card klickbar')

# 6d. "Mehr erfahren →" Hinweis in der Text-Sektion ergänzen (am Ende der Badges)
old_badges_end = """            Rettungsleitsystem
          </span>
        </div>
      </div>
    </div>"""

new_badges_end = """            Rettungsleitsystem
          </span>
        </div>
        <div class="mt-5 inline-flex items-center gap-2 text-sm font-bold text-[#1895BB] group">
          <span>Urkunde &amp; Details ansehen</span>
          <svg class="w-4 h-4 transition-transform group-hover:translate-x-1" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
        </div>
      </div>
    </div>"""

rep(old_badges_end, new_badges_end, '6d. "Mehr erfahren" Hinweis')

# 6e. Urkunden-Kachel komplett entfernen (das große Foto)
old_kachel = """
    <!-- Urkunden-Kachel -->
    <div class="mt-6 urkunde-kachel fade-up" onclick="openSozialesModal()" role="button" tabindex="0"
         aria-label="Soziales Engagement – mehr erfahren"
         onkeydown="if(event.key==='Enter')openSozialesModal()">
      <img src="Bilder/Urkunde.jpg" alt="Caritiva-Urkunde 2026 – Elektrotechnik Rakin OHG">
      <div class="urkunde-hover-overlay">
        <svg class="w-10 h-10 text-white opacity-90" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607zM10.5 7.5v6m3-3h-6"/>
        </svg>
        <span class="text-white font-bold text-lg tracking-wide">Mehr erfahren</span>
        <span class="text-white/75 text-sm">Klicken für Details zum Projekt</span>
      </div>
    </div>
"""

rep(old_kachel, '\n', '6e. Urkunden-Kachel entfernt')

# ═══════════════════════════════════════════════════════════════
# SPEICHERN
# ═══════════════════════════════════════════════════════════════
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('═══════════════════════════════════════════')
print('  VERBESSERUNGEN v1 – ERGEBNIS')
print('═══════════════════════════════════════════')
for c in changes:
    print(f'  {c}')
print()
print('Verifikation:')
checks = {
    '30 Rezensionen':            '30 Rezensionen' in html,
    '100+ Counter Target':       'data-target="100"' in html,
    '100+ in Über uns':          '>100+</div>' in html,
    'Btn-Danger immer rot':      'background: #EF4444;\n      color: #fff;\n      border: 2px solid #EF4444' in html,
    'Btn-Danger Glow Hover':     'box-shadow: 0 0 24px rgba(239,68,68' in html,
    '3 Tel-Nummern in Hero':     '0160 9162 8756' in html and '0160 9809 8000' in html and '0151 5124 9333' in html,
    'Herbert Co-Gründer':        'Co-Gründer & Inhaber</p>\n          <p class="text-sm text-muted-light">Elektroinstallation' in html,
    'Helmut Co-Gründer':         'Co-Gründer & Inhaber</p>\n          <p class="text-sm text-muted-light">Sanierung' in html,
    'Christian Co-Gründer':      'Co-Gründer & Inhaber</p>\n          <p class="text-sm text-muted-light">Wallbox' in html,
    '3 Co-Gründer Badge':        '3 Co-Gründer' in html,
    '"gesponsert" statt "bereitgestellt"': 'gesponsert' in html and 'bereitgestellt' not in html,
    'Urkunden-Icon (Siegel)':    'fill="#FBBF24" stroke="#FBBF24"' in html,
    'Soziales-Card klickbar':    'onclick="openSozialesModal()"' in html,
    '"Mehr erfahren" Hinweis':   'Urkunde &amp; Details ansehen' in html,
    'Urkunden-Kachel weg':       'class="mt-6 urkunde-kachel' not in html,
}
print()
for k, v in checks.items():
    print(f'  {"OK  " if v else "FAIL"} - {k}')
