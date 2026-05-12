import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

with open('index_website.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ══════════════════════════════════════════════════════════════
# BILDNAMEN – hier anpassen wenn User andere Namen hochlädt
# ══════════════════════════════════════════════════════════════
IMG_VEREIN      = 'Bilder/fc_verein.jpg'        # Foto FC Oberhinkofen
IMG_LEITSYSTEM  = 'Bilder/leitsystem.jpg'        # Foto Rettungsleitsystem
IMG_URKUNDE     = 'Bilder/Urkunde.jpg'           # bereits vorhanden ✅

# ─── 1. CSS ───────────────────────────────────────────────────────────────────
neue_css = """
    /* ── Urkunden-Kachel ── */
    .urkunde-kachel {
      position: relative;
      overflow: hidden;
      border-radius: 16px;
      cursor: pointer;
      border: 2px solid rgba(24,149,187,.18);
      transition: border-color .3s, box-shadow .3s;
    }
    .urkunde-kachel:hover {
      border-color: rgba(24,149,187,.50);
      box-shadow: 0 12px 40px rgba(24,149,187,.15);
    }
    .urkunde-kachel img {
      width: 100%;
      max-height: 280px;
      object-fit: cover;
      display: block;
      transition: transform .4s ease;
    }
    .urkunde-kachel:hover img { transform: scale(1.04); }
    .urkunde-hover-overlay {
      position: absolute;
      inset: 0;
      background: rgba(20,50,65,.65);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: .75rem;
      opacity: 0;
      transition: opacity .3s ease;
    }
    .urkunde-kachel:hover .urkunde-hover-overlay { opacity: 1; }

    /* ── Soziales Modal (breiter als Leistungs-Modal) ── */
    .soziales-modal-box {
      background: #fff;
      border-radius: 24px;
      max-width: 820px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      position: relative;
      transform: translateY(20px);
      transition: transform .3s ease;
      box-shadow: 0 32px 80px rgba(0,0,0,.28);
    }
    #soziales-modal.open .soziales-modal-box { transform: translateY(0); }

    /* Galerie-Grid im Modal */
    .soz-gallery {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 1rem;
    }
    .soz-gallery img {
      width: 100%; height: 180px;
      object-fit: cover;
      border-radius: 12px;
      border: 1px solid rgba(24,149,187,.15);
    }
"""

html = html.replace(
    "    .star { color: #FBBF24; }\n",
    "    .star { color: #FBBF24; }\n" + neue_css
)
print("CSS OK")

# ─── 2. URKUNDEN-KACHEL in Soziales-Section einfügen ─────────────────────────
# Wir ersetzen den schließenden Tag der bestehenden Section
old_section_end = """      </div>
    </div>
  </div>
</section>


<div class="divider"></div>


<!-- ═══════════════════════════════════════════
     FAQ"""

new_section_end = f"""      </div>
    </div>

    <!-- Urkunden-Kachel -->
    <div class="mt-6 urkunde-kachel fade-up" onclick="openSozialesModal()" role="button" tabindex="0"
         aria-label="Soziales Engagement – mehr erfahren"
         onkeydown="if(event.key==='Enter')openSozialesModal()">
      <img src="{IMG_URKUNDE}" alt="Caritiva-Urkunde 2026 – Elektrotechnik Rakin OHG">
      <div class="urkunde-hover-overlay">
        <svg class="w-10 h-10 text-white opacity-90" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607zM10.5 7.5v6m3-3h-6"/>
        </svg>
        <span class="text-white font-bold text-lg tracking-wide">Mehr erfahren</span>
        <span class="text-white/75 text-sm">Klicken für Details zum Projekt</span>
      </div>
    </div>

  </div>
</section>


<div class="divider"></div>


<!-- ═══════════════════════════════════════════
     FAQ"""

if old_section_end in html:
    html = html.replace(old_section_end, new_section_end)
    print("Urkunden-Kachel eingefuegt OK")
else:
    print("FEHLER: Marker fuer Soziales-Section-Ende nicht gefunden!")

# ─── 3. SOZIALES MODAL HTML (vor </body>) ─────────────────────────────────────
soziales_modal = f"""
<!-- ═══════════════════════════════════════════
     SOZIALES ENGAGEMENT MODAL
═══════════════════════════════════════════ -->
<div id="soziales-modal" class="modal-overlay" role="dialog" aria-modal="true" aria-labelledby="soz-modal-title">
  <div class="soziales-modal-box">

    <!-- Schließen-Button -->
    <button onclick="closeSozialesModal()"
            class="absolute top-4 right-4 z-10 w-9 h-9 rounded-full bg-[#EEF6F9] hover:bg-[#1895BB] hover:text-white text-[#1E3E4F] flex items-center justify-center text-xl font-bold transition-colors"
            aria-label="Schließen">
      &times;
    </button>

    <!-- Header-Bild: Urkunde -->
    <div class="relative overflow-hidden rounded-t-3xl" style="max-height:260px">
      <img src="{IMG_URKUNDE}" alt="Caritiva-Urkunde 2026" class="w-full object-cover" style="max-height:260px">
      <div class="absolute inset-0 bg-gradient-to-t from-[#1E3E4F]/80 to-transparent flex items-end p-8">
        <div>
          <p class="text-[#5DD4F0] text-xs font-bold tracking-[.2em] uppercase mb-1">Soziales Engagement</p>
          <h2 id="soz-modal-title" class="font-bebas tracking-widest text-white" style="font-size:clamp(1.8rem,4vw,2.4rem)">
            CARITIVA-URKUNDE: FC OBERHINKOFEN
          </h2>
        </div>
      </div>
    </div>

    <!-- Inhalt -->
    <div class="p-7 md:p-10">

      <!-- Kacheln: Über den Verein + Rettungsleitsystem -->
      <div class="grid md:grid-cols-2 gap-6 mb-8">

        <!-- Über FC Oberhinkofen -->
        <div class="bg-[#F8F9FA] border border-[#1895BB]/15 rounded-2xl p-5">
          <div class="flex items-center gap-3 mb-3">
            <div class="w-9 h-9 rounded-xl bg-[#EEF6F9] flex items-center justify-center flex-shrink-0">
              <svg class="w-5 h-5 text-[#1895BB]" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" d="M18 18.72a9.094 9.094 0 003.741-.479 3 3 0 00-4.682-2.72m.94 3.198l.001.031c0 .225-.012.447-.037.666A11.944 11.944 0 0112 21c-2.17 0-4.207-.576-5.963-1.584A6.062 6.062 0 016 18.719m12 0a5.971 5.971 0 00-.941-3.197m0 0A5.995 5.995 0 0012 12.75a5.995 5.995 0 00-5.058 2.772m0 0a3 3 0 00-4.681 2.72 8.986 8.986 0 003.74.477m.94-3.197a5.971 5.971 0 00-.94 3.197"/>
              </svg>
            </div>
            <h3 class="font-bold text-[#1E3E4F] text-base">FC Oberhinkofen e.V.</h3>
          </div>
          <p class="text-[#3D5A6A] text-sm leading-relaxed">
            Der FC Oberhinkofen e.V. ist ein gemeinnütziger Sportverein aus der Region Regensburg.
            Als lokaler Partner unterstützt Elektrotechnik Rakin OHG den Verein aktiv – weil
            gesellschaftliches Engagement für uns genauso wichtig ist wie fachliche Exzellenz.
          </p>
        </div>

        <!-- Rettungsleitsystem -->
        <div class="bg-[#F8F9FA] border border-[#1895BB]/15 rounded-2xl p-5">
          <div class="flex items-center gap-3 mb-3">
            <div class="w-9 h-9 rounded-xl bg-[#EEF6F9] flex items-center justify-center flex-shrink-0">
              <svg class="w-5 h-5 text-[#1895BB]" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9.594 3.94c.09-.542.56-.94 1.11-.94h2.593c.55 0 1.02.398 1.11.94l.213 1.281c.063.374.313.686.645.87.074.04.147.083.22.127.325.196.72.257 1.075.124l1.217-.456a1.125 1.125 0 011.37.49l1.296 2.247a1.125 1.125 0 01-.26 1.431l-1.003.827c-.293.241-.438.613-.43.992a7.723 7.723 0 010 .255c-.008.378.137.75.43.991l1.004.827c.424.35.534.955.26 1.43l-1.298 2.247a1.125 1.125 0 01-1.369.491l-1.217-.456c-.355-.133-.75-.072-1.076.124a6.47 6.47 0 01-.22.128c-.331.183-.581.495-.644.869l-.213 1.281c-.09.543-.56.94-1.11.94h-2.594c-.55 0-1.019-.398-1.11-.94l-.213-1.281c-.062-.374-.312-.686-.644-.87a6.52 6.52 0 01-.22-.127c-.325-.196-.72-.257-1.076-.124l-1.217.456a1.125 1.125 0 01-1.369-.49l-1.297-2.247a1.125 1.125 0 01.26-1.431l1.004-.827c.292-.24.437-.613.43-.991a6.932 6.932 0 010-.255c.007-.38-.138-.751-.43-.992l-1.004-.827a1.125 1.125 0 01-.26-1.43l1.297-2.247a1.125 1.125 0 011.37-.491l1.216.456c.356.133.751.072 1.076-.124.072-.044.146-.086.22-.128.332-.183.582-.495.644-.869l.214-1.28z"/>
                <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
              </svg>
            </div>
            <h3 class="font-bold text-[#1E3E4F] text-base">Das Rettungsleitsystem</h3>
          </div>
          <p class="text-[#3D5A6A] text-sm leading-relaxed">
            Ein Rettungsleitsystem sorgt im Notfall für eine schnelle und sichere Evakuierung –
            durch klar gekennzeichnete Fluchtwege, Notbeleuchtung und Orientierungshilfen.
            Elektrotechnik Rakin OHG hat dieses System für den FC Oberhinkofen e.V.
            vollständig geplant und installiert.
          </p>
        </div>
      </div>

      <!-- Caritiva-Details -->
      <div class="bg-gradient-to-r from-[#EEF6F9] to-[#F8F9FA] border border-[#1895BB]/20 rounded-2xl p-5 mb-8">
        <p class="text-xs font-bold text-[#1895BB] tracking-[.2em] uppercase mb-3">Offizielle Auszeichnung</p>
        <div class="flex flex-wrap gap-6 text-sm text-[#3D5A6A]">
          <div>
            <span class="font-semibold text-[#1E3E4F] block">Ausgestellt von</span>
            CARITIVA (gemeinnützige Organisation)
          </div>
          <div>
            <span class="font-semibold text-[#1E3E4F] block">Datum</span>
            31. März 2026
          </div>
          <div>
            <span class="font-semibold text-[#1E3E4F] block">Referenznummer</span>
            P24-500966-27363
          </div>
        </div>
      </div>

      <!-- Bildergalerie -->
      <p class="text-xs font-bold text-[#1895BB] tracking-[.2em] uppercase mb-4">Eindrücke vom Projekt</p>
      <div class="soz-gallery mb-8">
        <img src="{IMG_VEREIN}" alt="FC Oberhinkofen e.V."
             onerror="this.style.display='none'">
        <img src="{IMG_LEITSYSTEM}" alt="Rettungsleitsystem Installation"
             onerror="this.style.display='none'">
        <img src="{IMG_URKUNDE}" alt="Caritiva-Urkunde 2026">
      </div>

      <!-- CTA -->
      <div class="flex flex-wrap gap-3 pt-4 border-t border-[#1895BB]/15">
        <a href="tel:+491609162876"
           class="flex items-center gap-2 bg-[#1895BB] hover:bg-[#1571A0] text-white font-bold px-5 py-2.5 rounded-xl transition-all text-sm">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
          Jetzt anrufen
        </a>
        <a href="https://www.fc-oberhinkofen.de" target="_blank" rel="noopener"
           class="flex items-center gap-2 border border-[#1895BB] text-[#1895BB] hover:bg-[#EEF6F9] font-bold px-5 py-2.5 rounded-xl transition-all text-sm">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13.19 8.688a4.5 4.5 0 011.242 7.244l-4.5 4.5a4.5 4.5 0 01-6.364-6.364l1.757-1.757m13.35-.622l1.757-1.757a4.5 4.5 0 00-6.364-6.364l-4.5 4.5a4.5 4.5 0 001.242 7.244"/></svg>
          FC Oberhinkofen Website
        </a>
      </div>

    </div>
  </div>
</div>
"""

html = html.replace('</body>', soziales_modal + '\n</body>')
print("Soziales Modal HTML eingefuegt OK")

# ─── 4. JAVASCRIPT ────────────────────────────────────────────────────────────
soziales_js = """
<script>
// ── Soziales Modal ────────────────────────────────────────────
const sozialesModal = document.getElementById('soziales-modal');

function openSozialesModal() {
  sozialesModal.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeSozialesModal() {
  sozialesModal.classList.remove('open');
  document.body.style.overflow = '';
}

// Klick auf Overlay-Hintergrund schließt Modal
sozialesModal.addEventListener('click', e => {
  if (e.target === sozialesModal) closeSozialesModal();
});

// Escape-Taste schließt Modal
document.addEventListener('keydown', e => {
  if (e.key === 'Escape' && sozialesModal.classList.contains('open')) {
    closeSozialesModal();
  }
});
</script>
"""

html = html.replace('</body>', soziales_js + '\n</body>')
print("Soziales Modal JS eingefuegt OK")

# ─── 5. SPEICHERN + VERIFIKATION ──────────────────────────────────────────────
with open('index_website.html', 'w', encoding='utf-8') as f:
    f.write(html)

checks = {
    'CSS urkunde-kachel':       '.urkunde-kachel {' in html,
    'CSS soziales-modal-box':   '.soziales-modal-box {' in html,
    'Urkunden-Kachel HTML':     'openSozialesModal' in html,
    'Soziales Modal HTML':      'id="soziales-modal"' in html,
    'Caritiva Details':         'P24-500966' in html,
    'FC Oberhinkofen Text':     'gemeinnütziger Sportverein' in html,
    'Rettungsleitsystem Text':  'Evakuierung' in html,
    'Bildergalerie':            'soz-gallery' in html,
    'JS openSozialesModal':     'function openSozialesModal' in html,
    'JS closeSozialesModal':    'function closeSozialesModal' in html,
}

print()
for k, v in checks.items():
    print(f'  {"OK" if v else "FEHLER"} - {k}')
