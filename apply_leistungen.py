import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

with open('index_website.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ─── 1. MODAL + WHATSAPP CSS einfügen (vor </style>) ─────────────────────────
modal_css = """
    /* ── Modal ── */
    .modal-overlay {
      position: fixed; inset: 0; z-index: 1000;
      background: rgba(10,20,30,.75);
      backdrop-filter: blur(6px);
      display: flex; align-items: center; justify-content: center;
      padding: 1rem;
      opacity: 0; pointer-events: none;
      transition: opacity .3s ease;
    }
    .modal-overlay.open { opacity: 1; pointer-events: all; }
    .modal-box {
      background: #fff;
      border-radius: 24px;
      max-width: 560px; width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      position: relative;
      transform: translateY(20px);
      transition: transform .3s ease;
      box-shadow: 0 32px 80px rgba(0,0,0,.25);
    }
    .modal-overlay.open .modal-box { transform: translateY(0); }
    .modal-img { width: 100%; height: 220px; object-fit: cover; border-radius: 24px 24px 0 0; }
    .modal-img-placeholder {
      width: 100%; height: 160px;
      background: linear-gradient(135deg, #EEF6F9, #D0E8F2);
      border-radius: 24px 24px 0 0;
      display: flex; align-items: center; justify-content: center;
      color: #1895BB; font-size: 3rem;
    }
    .modal-body { padding: 2rem; }
    .modal-close {
      position: absolute; top: 1rem; right: 1rem;
      width: 2.25rem; height: 2.25rem;
      border-radius: 50%;
      background: rgba(255,255,255,.9);
      border: none; cursor: pointer;
      display: flex; align-items: center; justify-content: center;
      font-size: 1.25rem; color: #1E3E4F;
      box-shadow: 0 2px 8px rgba(0,0,0,.15);
      transition: background .2s;
      z-index: 10;
    }
    .modal-close:hover { background: #fff; }

    /* ── Nebenleistungen (kein Bild) ── */
    .svc-secondary {
      background: #fff;
      border: 1px solid rgba(24,149,187,.15);
      border-radius: 20px;
      padding: 1.75rem;
      cursor: pointer;
      transition: transform .3s ease, box-shadow .3s ease, border-color .3s ease;
      display: flex; flex-direction: column; gap: 0.75rem;
    }
    .svc-secondary:hover {
      transform: translateY(-4px);
      border-color: rgba(24,149,187,.4);
      box-shadow: 0 16px 40px rgba(24,149,187,.12);
    }
    .svc-secondary .svc-icon {
      width: 2.75rem; height: 2.75rem;
      border-radius: 0.75rem;
      background: rgba(24,149,187,.1);
      color: #1895BB;
      display: flex; align-items: center; justify-content: center;
      transition: background .3s;
    }
    .svc-secondary:hover .svc-icon { background: rgba(24,149,187,.2); }
    .svc-secondary h3 { font-size: 1.1rem; font-weight: 700; color: #1A2B35; }
    .svc-secondary p  { font-size: 0.875rem; color: #5A7A8A; line-height: 1.6; }
    .svc-secondary .svc-arrow { color: #1895BB; margin-top: auto; }

    /* ── WhatsApp Floating Button ── */
    .wa-btn {
      position: fixed; bottom: 1.75rem; right: 1.75rem;
      width: 3.5rem; height: 3.5rem;
      background: #25D366;
      border-radius: 50%;
      display: flex; align-items: center; justify-content: center;
      box-shadow: 0 4px 20px rgba(37,211,102,.4);
      z-index: 999;
      transition: transform .2s, box-shadow .2s;
    }
    .wa-btn:hover {
      transform: scale(1.1);
      box-shadow: 0 6px 28px rgba(37,211,102,.55);
    }
    .wa-btn svg { width: 1.875rem; height: 1.875rem; }
    .wa-tooltip {
      position: absolute; right: 4.25rem; top: 50%;
      transform: translateY(-50%);
      background: #1A2B35; color: #fff;
      font-size: 0.8rem; font-weight: 600;
      padding: 0.4rem 0.85rem;
      border-radius: 8px; white-space: nowrap;
      opacity: 0; pointer-events: none;
      transition: opacity .2s;
    }
    .wa-btn:hover .wa-tooltip { opacity: 1; }
"""
html = html.replace("    .star { color: #FBBF24; }\n",
                    "    .star { color: #FBBF24; }\n" + modal_css)
print("CSS eingefuegt OK")

# ─── 2. NEUE LEISTUNGEN SECTION ───────────────────────────────────────────────
old_section_start = '<!-- ═══════════════════════════════════════════\n     LEISTUNGEN – Image Cards\n═══════════════════════════════════════════ -->'
old_section_end   = '\n\n\n<div class="divider"></div>'

neue_leistungen = '''<!-- ═══════════════════════════════════════════
     LEISTUNGEN
═══════════════════════════════════════════ -->
<section id="leistungen" class="py-24 bg-bg">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">

    <div class="mb-14 fade-up">
      <p class="text-primary font-bold text-xs tracking-[.2em] uppercase mb-3">Was wir für Sie tun</p>
      <h2 class="font-bebas tracking-widest text-text mb-4" style="font-size:clamp(2.5rem,6vw,4rem)">UNSERE LEISTUNGEN</h2>
      <p class="text-muted-light max-w-lg">Von der Notfall-Entstörung bis zur modernen Energielösung – wir decken alle Bereiche ab.</p>
    </div>

    <!-- ── HAUPTLEISTUNGEN ── -->
    <p class="text-xs font-bold text-primary tracking-[.2em] uppercase mb-5 fade-up">Hauptleistungen</p>
    <div class="grid sm:grid-cols-3 gap-6 mb-10">

      <!-- Notdienst -->
      <div class="svc-card cursor-pointer min-h-[340px] fade-up"
           data-modal="notdienst">
        <div class="svc-bg" style="background-image:url('Bilder/notdienst.png')"></div>
        <div class="svc-default">
          <span class="inline-block text-xs font-bold text-white/80 tracking-widest uppercase mb-2">24/7 verfügbar</span>
          <h3 class="text-2xl font-bold text-white">Elektriker-Notdienst</h3>
        </div>
        <div class="svc-content">
          <div>
            <div class="svc-icon">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126zM12 15.75h.007v.008H12v-.008z"/></svg>
            </div>
            <h3 class="text-xl font-bold text-white mb-2">Elektriker-Notdienst</h3>
            <p class="text-sm leading-relaxed" style="color:rgba(255,255,255,.90)">Stromausfall, Kurzschluss, defekte Sicherungen – wir sind 24/7 für Sie da, auch an Sonn- und Feiertagen.</p>
          </div>
          <span class="svc-arrow mt-4 text-sm font-semibold flex items-center gap-2">
            Details ansehen <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
          </span>
        </div>
      </div>

      <!-- Wallbox -->
      <div class="svc-card cursor-pointer min-h-[340px] fade-up delay-1"
           data-modal="wallbox">
        <div class="svc-bg" style="background-image:url('Bilder/wallbox.avif')"></div>
        <div class="svc-default">
          <span class="inline-block text-xs font-bold text-white/80 tracking-widest uppercase mb-2">KfW-förderungsfähig</span>
          <h3 class="text-2xl font-bold text-white">Wallbox-Installation</h3>
        </div>
        <div class="svc-content">
          <div>
            <div class="svc-icon">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M21 10.5h.375c.621 0 1.125.504 1.125 1.125v2.25c0 .621-.504 1.125-1.125 1.125H21M3.75 18h15A2.25 2.25 0 0021 15.75v-6a2.25 2.25 0 00-2.25-2.25h-15A2.25 2.25 0 001.5 9.75v6A2.25 2.25 0 003.75 18zM3 12h18"/></svg>
            </div>
            <h3 class="text-xl font-bold text-white mb-2">Wallbox-Installation</h3>
            <p class="text-sm leading-relaxed" style="color:rgba(255,255,255,.90)">E-Ladestation für Zuhause oder Gewerbe – fachgerecht installiert, alle Hersteller, KfW-förderungsfähig.</p>
          </div>
          <span class="svc-arrow mt-4 text-sm font-semibold flex items-center gap-2">
            Details ansehen <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
          </span>
        </div>
      </div>

      <!-- Zählerschrank -->
      <div class="svc-card cursor-pointer min-h-[340px] fade-up delay-2"
           data-modal="zaehler">
        <div class="svc-bg" style="background-image:url('Bilder/kasten.avif')"></div>
        <div class="svc-default">
          <span class="inline-block text-xs font-bold text-white/80 tracking-widest uppercase mb-2">Norm-konform</span>
          <h3 class="text-2xl font-bold text-white">Zählerschränke & Unterverteiler</h3>
        </div>
        <div class="svc-content">
          <div>
            <div class="svc-icon">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6A2.25 2.25 0 016 3.75h2.25A2.25 2.25 0 0110.5 6v2.25a2.25 2.25 0 01-2.25 2.25H6a2.25 2.25 0 01-2.25-2.25V6zM3.75 15.75A2.25 2.25 0 016 13.5h2.25a2.25 2.25 0 012.25 2.25V18a2.25 2.25 0 01-2.25 2.25H6A2.25 2.25 0 013.75 18v-2.25zM13.5 6a2.25 2.25 0 012.25-2.25H18A2.25 2.25 0 0120.25 6v2.25A2.25 2.25 0 0118 10.5h-2.25a2.25 2.25 0 01-2.25-2.25V6zM13.5 15.75a2.25 2.25 0 012.25-2.25H18a2.25 2.25 0 012.25 2.25V18A2.25 2.25 0 0118 20.25h-2.25A2.25 2.25 0 0113.5 18v-2.25z"/></svg>
            </div>
            <h3 class="text-xl font-bold text-white mb-2">Zählerschränke & Unterverteiler</h3>
            <p class="text-sm leading-relaxed" style="color:rgba(255,255,255,.90)">Neubau, Erneuerung oder Erweiterung – wir planen und installieren Ihre Elektroverteilung normkonform nach DIN VDE.</p>
          </div>
          <span class="svc-arrow mt-4 text-sm font-semibold flex items-center gap-2">
            Details ansehen <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
          </span>
        </div>
      </div>

    </div>

    <!-- ── NEBENLEISTUNGEN ── -->
    <p class="text-xs font-bold text-muted tracking-[.2em] uppercase mb-5 fade-up">Weitere Leistungen</p>
    <div class="grid sm:grid-cols-3 gap-4 mb-12">

      <!-- Balkonkraftwerk -->
      <div class="svc-secondary fade-up" data-modal="balkon">
        <div class="svc-icon">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 3v2.25m6.364.386l-1.591 1.591M21 12h-2.25m-.386 6.364l-1.591-1.591M12 18.75V21m-4.773-4.227l-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0z"/></svg>
        </div>
        <h3>Balkonkraftwerk</h3>
        <p>Montage und normgerechter Anschluss Ihrer Mini-Solaranlage – schnell und sicher.</p>
        <span class="svc-arrow text-sm font-semibold flex items-center gap-1">
          Mehr erfahren <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
        </span>
      </div>

      <!-- Elektro-Hausservice -->
      <div class="svc-secondary fade-up delay-1" data-modal="hausservice">
        <div class="svc-icon">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25"/></svg>
        </div>
        <h3>Elektro-Hausservice</h3>
        <p>Leuchtmittel wechseln, Herd anschließen, Steckdosen tauschen, Bewegungsmelder – alles aus einer Hand.</p>
        <span class="svc-arrow text-sm font-semibold flex items-center gap-1">
          Mehr erfahren <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
        </span>
      </div>

      <!-- Elektroinstallation -->
      <div class="svc-secondary fade-up delay-2" data-modal="installation">
        <div class="svc-icon">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M11.42 15.17L17.25 21A2.652 2.652 0 0021 17.25l-5.877-5.877M11.42 15.17l2.496-3.03c.317-.384.74-.626 1.208-.766M11.42 15.17l-4.655 5.653a2.548 2.548 0 11-3.586-3.586l6.837-5.63m5.108-.233c.55-.164 1.163-.188 1.743-.14a4.5 4.5 0 004.486-6.336l-3.276 3.277a3.004 3.004 0 01-2.25-2.25l3.276-3.276a4.5 4.5 0 00-6.336 4.486c.091 1.076-.071 2.264-.904 2.95l-.102.085m-1.745 1.437L5.909 7.5H4.5L2.25 3.75l1.5-1.5L7.5 4.5v1.409l4.26 4.26m-1.745 1.437l1.745-1.437m6.615 8.206L15.75 15.75M4.867 19.125h.008v.008h-.008v-.008z"/></svg>
        </div>
        <h3>Elektroinstallation</h3>
        <p>Planung und Umsetzung für Neu- und Altbau – von der Steckdose bis zur Gesamtverkabelung.</p>
        <span class="svc-arrow text-sm font-semibold flex items-center gap-1">
          Mehr erfahren <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
        </span>
      </div>

    </div>

    <div class="mt-4 text-center fade-up">
      <a href="#kontakt" class="inline-flex items-center gap-2 bg-surface border border-primary/30 hover:border-primary text-primary font-semibold px-8 py-3.5 rounded-xl transition-all hover:bg-primary/5">
        Alle Leistungen anfragen
        <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
      </a>
    </div>
  </div>
</section>'''

# Find and replace the leistungen section
start_idx = html.find(old_section_start)
end_idx   = html.find(old_section_end, start_idx) + len(old_section_end)
html = html[:start_idx] + neue_leistungen + '\n\n\n<div class="divider"></div>' + html[end_idx:]
print("Leistungen Section ersetzt OK")

# ─── 3. MODAL HTML vor </body> einfügen ──────────────────────────────────────
modal_html = '''
<!-- ═══════════════════════════════════════════
     MODAL – Leistungsdetails
═══════════════════════════════════════════ -->
<div id="svc-modal" class="modal-overlay" role="dialog" aria-modal="true">
  <div class="modal-box">
    <button class="modal-close" id="modal-close-btn" aria-label="Schließen">&times;</button>
    <img id="modal-img" class="modal-img" src="" alt="" style="display:none">
    <div id="modal-img-placeholder" class="modal-img-placeholder">
      <svg width="48" height="48" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3.75 13.5l10.5-11.25L12 10.5h8.25L9.75 21.75 12 13.5H3.75z"/></svg>
    </div>
    <div class="modal-body">
      <p id="modal-tag" class="text-xs font-bold text-primary tracking-widest uppercase mb-2"></p>
      <h3 id="modal-title" class="font-bebas tracking-widest text-[#1E3E4F] mb-3" style="font-size:2rem"></h3>
      <p id="modal-desc" class="text-[#3D5A6A] leading-relaxed mb-6"></p>
      <div class="flex flex-wrap gap-3">
        <a href="tel:+491609162876"
           class="flex items-center gap-2 bg-[#1895BB] hover:bg-[#1571A0] text-white font-bold px-6 py-3 rounded-xl transition-all">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
          Jetzt anrufen
        </a>
        <a href="https://wa.me/491609162876"
           class="flex items-center gap-2 bg-[#25D366] hover:bg-[#1ebe59] text-white font-bold px-6 py-3 rounded-xl transition-all">
          <svg class="w-5 h-5" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
          WhatsApp
        </a>
      </div>
    </div>
  </div>
</div>

<!-- ── WhatsApp Floating Button ── -->
<a href="https://wa.me/491609162876" class="wa-btn" target="_blank" rel="noopener" aria-label="WhatsApp schreiben">
  <span class="wa-tooltip">WhatsApp schreiben</span>
  <svg viewBox="0 0 24 24" fill="white"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
</a>

<!-- ── Modal JavaScript ── -->
<script>
const modalData = {
  notdienst: {
    tag: '24/7 Notdienst',
    title: 'Elektriker-Notdienst',
    desc: 'Bei einem Elektriker-Notfall zählt jede Minute. Elektrotechnik Rakin ist rund um die Uhr – auch an Sonn- und Feiertagen – für Sie erreichbar. Ob Stromausfall, Kurzschluss, defekte Sicherungen oder gefährliche Funken: Wir sind schnell vor Ort und beheben das Problem fachgerecht und dauerhaft.',
    img: 'Bilder/notdienst.png'
  },
  wallbox: {
    tag: 'KfW-förderungsfähig',
    title: 'Wallbox-Installation',
    desc: 'Wir installieren Ladestationen für Elektrofahrzeuge bei Ihnen zu Hause oder in Ihrem Betrieb – herstellerunabhängig und normkonform. Auf Wunsch übernehmen wir die gesamte Abwicklung: von der Planung über den Netzantrag bis zur KfW-Förderung.',
    img: 'Bilder/wallbox.avif'
  },
  zaehler: {
    tag: 'DIN VDE normkonform',
    title: 'Zählerschränke & Unterverteiler',
    desc: 'Ob Neubau, Sanierung oder Erweiterung: Wir planen und installieren Zählerschränke und Unterverteiler nach aktuellen DIN VDE Normen. Für mehr Sicherheit, mehr Kapazität und eine zukunftssichere Elektroverteilung in Ihrem Gebäude.',
    img: 'Bilder/kasten.avif'
  },
  balkon: {
    tag: 'Erneuerbare Energie',
    title: 'Balkonkraftwerk',
    desc: 'Balkonkraftwerke sind eine einfache Möglichkeit, eigenen Solarstrom zu erzeugen. Wir übernehmen die professionelle Montage und den normgerechten elektrischen Anschluss – schnell, sicher und mit allem was dazu gehört.',
    img: 'Bilder/panele.avif'
  },
  hausservice: {
    tag: 'Für Zuhause',
    title: 'Elektro-Hausservice',
    desc: 'Kleine Elektroarbeiten, die sich summieren: Leuchtmittel wechseln, einen Herd oder Geschirrspüler anschließen, Steckdosen oder Schalter tauschen, Bewegungsmelder montieren. Wir erledigen das zuverlässig – kein Auftrag ist zu klein.',
    img: null
  },
  installation: {
    tag: 'Neu- & Altbau',
    title: 'Elektroinstallation',
    desc: 'Von der einzelnen Steckdose bis zur kompletten Gebäudeverkabelung: Wir planen und installieren Elektroleitungen für Neu- und Altbauten. Sauber verlegt, normkonform ausgeführt und auf Ihre Bedürfnisse abgestimmt.',
    img: 'Bilder/installation.jpg'
  }
};

const modal    = document.getElementById('svc-modal');
const mTitle   = document.getElementById('modal-title');
const mDesc    = document.getElementById('modal-desc');
const mImg     = document.getElementById('modal-img');
const mPlaceh  = document.getElementById('modal-img-placeholder');
const mTag     = document.getElementById('modal-tag');
const closeBtn = document.getElementById('modal-close-btn');

function openModal(id) {
  const d = modalData[id];
  if (!d) return;
  mTag.textContent   = d.tag;
  mTitle.textContent = d.title;
  mDesc.textContent  = d.desc;
  if (d.img) {
    mImg.src = d.img; mImg.alt = d.title;
    mImg.style.display = 'block';
    mPlaceh.style.display = 'none';
  } else {
    mImg.style.display = 'none';
    mPlaceh.style.display = 'flex';
  }
  modal.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeModal() {
  modal.classList.remove('open');
  document.body.style.overflow = '';
}

document.querySelectorAll('[data-modal]').forEach(el => {
  el.addEventListener('click', () => openModal(el.dataset.modal));
});
closeBtn.addEventListener('click', closeModal);
modal.addEventListener('click', e => { if (e.target === modal) closeModal(); });
document.addEventListener('keydown', e => { if (e.key === 'Escape') closeModal(); });
</script>
'''

html = html.replace('</body>', modal_html + '\n</body>')
print("Modal + WhatsApp eingefuegt OK")

with open('index_website.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Gespeichert!")
