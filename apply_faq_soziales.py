import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

with open('index_website.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ─── 1. FAQ CSS einfügen ──────────────────────────────────────────────────────
faq_css = """
    /* ── FAQ Accordion ── */
    .faq-item { border-bottom: 1px solid rgba(24,149,187,.15); }
    .faq-item:last-child { border-bottom: none; }
    .faq-btn {
      width: 100%; text-align: left;
      display: flex; align-items: center; justify-content: space-between;
      padding: 1.25rem 0;
      background: none; border: none; cursor: pointer;
      color: #1A2B35; font-size: 1rem; font-weight: 600;
      transition: color .2s;
    }
    .faq-btn:hover { color: #1895BB; }
    .faq-icon {
      width: 1.75rem; height: 1.75rem; flex-shrink: 0;
      border-radius: 50%;
      background: rgba(24,149,187,.10);
      color: #1895BB;
      display: flex; align-items: center; justify-content: center;
      transition: background .25s, transform .3s;
    }
    .faq-btn[aria-expanded="true"] .faq-icon {
      background: #1895BB; color: #fff; transform: rotate(45deg);
    }
    .faq-answer {
      max-height: 0; overflow: hidden;
      transition: max-height .35s ease, padding .35s ease;
      color: #3D5A6A; font-size: 0.95rem; line-height: 1.7;
    }
    .faq-answer.open { max-height: 300px; padding-bottom: 1.25rem; }
"""
html = html.replace(
    "    .star { color: #FBBF24; }\n",
    "    .star { color: #FBBF24; }\n" + faq_css
)
print("FAQ CSS OK")

# ─── 2. SOZIALES ENGAGEMENT + FAQ Sectionen ──────────────────────────────────
neue_sectionen = """

<div class="divider"></div>


<!-- ═══════════════════════════════════════════
     SOZIALES ENGAGEMENT
═══════════════════════════════════════════ -->
<section class="py-16 bg-bg">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="bg-white border border-[#1895BB]/15 rounded-3xl p-8 md:p-12 flex flex-col md:flex-row items-center gap-10 shadow-sm fade-up">

      <!-- Icon / Badge -->
      <div class="flex-shrink-0 text-center">
        <div class="w-24 h-24 rounded-2xl bg-[#EEF6F9] border-2 border-[#1895BB]/20 flex items-center justify-center mx-auto mb-3">
          <svg class="w-12 h-12 text-[#1895BB]" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z"/>
          </svg>
        </div>
        <span class="text-xs font-bold text-[#1895BB] tracking-widest uppercase">Soziales Engagement</span>
      </div>

      <!-- Text -->
      <div class="flex-1 text-center md:text-left">
        <p class="text-xs font-bold text-primary tracking-[.2em] uppercase mb-2">Verantwortung übernehmen</p>
        <h2 class="font-bebas tracking-widest text-[#1E3E4F] mb-3" style="font-size:clamp(1.8rem,4vw,2.8rem)">
          CARITIVA-URKUNDE: FC OBERHINKOFEN
        </h2>
        <p class="text-[#3D5A6A] leading-relaxed mb-4">
          Wir sind überzeugt: Ein gutes Unternehmen trägt auch gesellschaftliche Verantwortung.
          Deshalb hat Elektrotechnik Rakin OHG das <strong class="text-[#1E3E4F]">Rettungsleitsystem für den FC Oberhinkofen e.V.</strong> bereitgestellt –
          ausgezeichnet mit der Caritiva-Urkunde vom 31. März 2026.
        </p>
        <div class="flex flex-wrap gap-3 justify-center md:justify-start">
          <span class="inline-flex items-center gap-2 text-sm font-semibold text-[#1895BB] bg-[#EEF6F9] border border-[#1895BB]/20 rounded-lg px-4 py-2">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" fill-rule="evenodd"/></svg>
            Caritiva-Urkunde 2026
          </span>
          <span class="inline-flex items-center gap-2 text-sm font-semibold text-[#1895BB] bg-[#EEF6F9] border border-[#1895BB]/20 rounded-lg px-4 py-2">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" fill-rule="evenodd"/></svg>
            FC Oberhinkofen e.V.
          </span>
          <span class="inline-flex items-center gap-2 text-sm font-semibold text-[#1895BB] bg-[#EEF6F9] border border-[#1895BB]/20 rounded-lg px-4 py-2">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" fill-rule="evenodd"/></svg>
            Rettungsleitsystem
          </span>
        </div>
      </div>
    </div>
  </div>
</section>


<div class="divider"></div>


<!-- ═══════════════════════════════════════════
     FAQ
═══════════════════════════════════════════ -->
<section class="py-20 bg-bg">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">

    <div class="text-center mb-12 fade-up">
      <p class="text-primary font-bold text-xs tracking-[.2em] uppercase mb-3">Häufige Fragen</p>
      <h2 class="font-bebas tracking-widest text-text mb-4" style="font-size:clamp(2.5rem,5vw,3.5rem)">FAQ</h2>
      <p class="text-muted-light">Antworten auf die häufigsten Fragen rund um unsere Leistungen.</p>
    </div>

    <div class="bg-white border border-[#1895BB]/15 rounded-2xl px-6 md:px-10 py-2 shadow-sm fade-up">

      <div class="faq-item">
        <button class="faq-btn" aria-expanded="false">
          Wie schnell sind Sie bei einem Notfall vor Ort?
          <span class="faq-icon"><svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15"/></svg></span>
        </button>
        <div class="faq-answer">
          In der Regel sind wir innerhalb von 60 Minuten bei Ihnen – in Regensburg und der näheren Umgebung. Unser Notdienst ist 24 Stunden am Tag, 7 Tage die Woche erreichbar, auch an Sonn- und Feiertagen.
        </div>
      </div>

      <div class="faq-item">
        <button class="faq-btn" aria-expanded="false">
          Was kostet ein Notdienst-Einsatz?
          <span class="faq-icon"><svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15"/></svg></span>
        </button>
        <div class="faq-answer">
          Die Kosten hängen vom Umfang des Einsatzes ab. Wir nennen Ihnen vor Beginn der Arbeiten einen transparenten Kostenvoranschlag – keine versteckten Gebühren, keine bösen Überraschungen.
        </div>
      </div>

      <div class="faq-item">
        <button class="faq-btn" aria-expanded="false">
          Installieren Sie Wallboxen für alle Fahrzeugmarken?
          <span class="faq-icon"><svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15"/></svg></span>
        </button>
        <div class="faq-answer">
          Ja – wir sind herstellerunabhängig und installieren Ladestationen für alle gängigen E-Fahrzeuge und Hersteller. Auf Wunsch übernehmen wir auch die Beantragung der KfW-Förderung für Sie.
        </div>
      </div>

      <div class="faq-item">
        <button class="faq-btn" aria-expanded="false">
          Was ist bei einem Zählerschrank-Wechsel zu beachten?
          <span class="faq-icon"><svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15"/></svg></span>
        </button>
        <div class="faq-answer">
          Ein Zählerschrank-Wechsel muss beim Netzbetreiber angemeldet werden und nach DIN VDE Norm ausgeführt sein. Wir übernehmen die komplette Abwicklung – von der Anmeldung über die Installation bis zur Abnahme.
        </div>
      </div>

      <div class="faq-item">
        <button class="faq-btn" aria-expanded="false">
          Arbeiten Sie auch am Wochenende?
          <span class="faq-icon"><svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15"/></svg></span>
        </button>
        <div class="faq-answer">
          Unser Notdienst ist 24/7 verfügbar – auch samstags, sonntags und an Feiertagen. Reguläre Installationsarbeiten und Beratungstermine vereinbaren wir flexibel, gerne auch am Samstag.
        </div>
      </div>

      <div class="faq-item">
        <button class="faq-btn" aria-expanded="false">
          In welchem Gebiet sind Sie tätig?
          <span class="faq-icon"><svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15"/></svg></span>
        </button>
        <div class="faq-answer">
          Unser Hauptgebiet ist Regensburg und die unmittelbare Umgebung. Bei größeren Projekten oder auf Anfrage sind wir auch in einem weiteren Umkreis tätig – sprechen Sie uns einfach an.
        </div>
      </div>

    </div>
  </div>
</section>

"""

# Einfügen: vor dem Notdienst-Banner
insert_marker = '\n\n\n<!-- ═══════════════════════════════════════════\n     NOTDIENST BANNER'
html = html.replace(insert_marker, neue_sectionen + insert_marker)
print("Soziales Engagement + FAQ eingefuegt OK")

# ─── 3. FAQ JAVASCRIPT (vor </body>) ─────────────────────────────────────────
faq_js = """
<script>
// FAQ Accordion
document.querySelectorAll('.faq-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const expanded = btn.getAttribute('aria-expanded') === 'true';
    // Alle schließen
    document.querySelectorAll('.faq-btn').forEach(b => {
      b.setAttribute('aria-expanded', 'false');
      b.nextElementSibling.classList.remove('open');
    });
    // Aktuellen öffnen (wenn war geschlossen)
    if (!expanded) {
      btn.setAttribute('aria-expanded', 'true');
      btn.nextElementSibling.classList.add('open');
    }
  });
});
</script>
"""
html = html.replace('</body>', faq_js + '\n</body>')
print("FAQ JS eingefuegt OK")

# ─── 4. SPEICHERN ─────────────────────────────────────────────────────────────
with open('index_website.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Verifikation
checks = {
    'FAQ CSS':                 '.faq-item {' in html,
    'FAQ Section':             'Häufige Fragen' in html,
    'FAQ 6 Fragen':            html.count('class="faq-btn"') == 6,
    'FAQ JS':                  'faq-btn' in html and 'aria-expanded' in html,
    'Soziales Engagement':     'CARITIVA' in html,
    'FC Oberhinkofen':         'FC Oberhinkofen' in html,
    'Caritiva Urkunde Badge':  'Caritiva-Urkunde 2026' in html,
}
for k, v in checks.items():
    print(f'  {"OK" if v else "FEHLER"} - {k}')
