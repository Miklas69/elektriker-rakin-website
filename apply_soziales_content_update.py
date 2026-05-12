import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

with open('index_website.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ══════════════════════════════════════════════════════════════
# Ersetzt den Platzhaltertext im Soziales-Modal mit echten
# Inhalten aus der Präsentation "Leitsystem_FC_Oberhinkofen"
# ══════════════════════════════════════════════════════════════

# ─── 1. FC Oberhinkofen Kachel – Text ────────────────────────────────────────
old_fc_text = """          <p class="text-[#3D5A6A] text-sm leading-relaxed">
            Der FC Oberhinkofen e.V. ist ein gemeinnütziger Sportverein aus der Region Regensburg.
            Als lokaler Partner unterstützt Elektrotechnik Rakin OHG den Verein aktiv – weil
            gesellschaftliches Engagement für uns genauso wichtig ist wie fachliche Exzellenz.
          </p>"""

new_fc_text = """          <p class="text-[#3D5A6A] text-sm leading-relaxed mb-3">
            Der FC Oberhinkofen e.V. feiert sein <strong class="text-[#1E3E4F]">75-jähriges Jubiläum</strong> –
            ein traditionsreicher Sportverein aus der Region Regensburg mit einem breiten Angebot für die ganze Familie.
          </p>
          <ul class="text-sm text-[#3D5A6A] space-y-1">
            <li class="flex items-center gap-2"><span class="w-1.5 h-1.5 rounded-full bg-[#1895BB] flex-shrink-0"></span>Fußball &amp; Juniorenfußball</li>
            <li class="flex items-center gap-2"><span class="w-1.5 h-1.5 rounded-full bg-[#1895BB] flex-shrink-0"></span>Fitness &amp; Gymnastik</li>
            <li class="flex items-center gap-2"><span class="w-1.5 h-1.5 rounded-full bg-[#1895BB] flex-shrink-0"></span>Dart (DC Robin Hood)</li>
            <li class="flex items-center gap-2"><span class="w-1.5 h-1.5 rounded-full bg-[#1895BB] flex-shrink-0"></span>Freizeitsport &amp; Stockschießen</li>
            <li class="flex items-center gap-2"><span class="w-1.5 h-1.5 rounded-full bg-[#1895BB] flex-shrink-0"></span>Neu: CenterBall (centerball.eu)</li>
          </ul>"""

if old_fc_text in html:
    html = html.replace(old_fc_text, new_fc_text)
    print("FC Oberhinkofen Text aktualisiert OK")
else:
    print("FEHLER: FC Text nicht gefunden!")

# ─── 2. Rettungsleitsystem Kachel – Text ─────────────────────────────────────
old_rls_text = """          <p class="text-[#3D5A6A] text-sm leading-relaxed">
            Ein Rettungsleitsystem sorgt im Notfall für eine schnelle und sichere Evakuierung –
            durch klar gekennzeichnete Fluchtwege, Notbeleuchtung und Orientierungshilfen.
            Elektrotechnik Rakin OHG hat dieses System für den FC Oberhinkofen e.V.
            vollständig geplant und installiert.
          </p>"""

new_rls_text = """          <p class="text-[#3D5A6A] text-sm leading-relaxed mb-3">
            Herzprobleme im Sport nehmen zu – und im Notfall zählt jede Sekunde.
            Erste Hilfe und Defibrillation müssen innerhalb von <strong class="text-[#1E3E4F]">3–5 Minuten</strong> erfolgen.
            Das RLS (RettungsLeitSystem) mit Notfallkoffer &amp; AED macht genau das möglich.
          </p>
          <ul class="text-sm text-[#3D5A6A] space-y-1">
            <li class="flex items-center gap-2"><span class="w-1.5 h-1.5 rounded-full bg-[#1895BB] flex-shrink-0"></span>Automatischer Notruf 112 beim Öffnen</li>
            <li class="flex items-center gap-2"><span class="w-1.5 h-1.5 rounded-full bg-[#1895BB] flex-shrink-0"></span>AED-Defibrillator &amp; Erste-Hilfe-Set</li>
            <li class="flex items-center gap-2"><span class="w-1.5 h-1.5 rounded-full bg-[#1895BB] flex-shrink-0"></span>Anleitung per Freisprechanlage</li>
            <li class="flex items-center gap-2"><span class="w-1.5 h-1.5 rounded-full bg-[#1895BB] flex-shrink-0"></span>TÜV-geprüft · 15 Jahre Garantie</li>
          </ul>"""

if old_rls_text in html:
    html = html.replace(old_rls_text, new_rls_text)
    print("Rettungsleitsystem Text aktualisiert OK")
else:
    print("FEHLER: RLS Text nicht gefunden!")

# ─── 3. Caritiva Details – Urkunden-Text ergänzen ────────────────────────────
old_caritiva = """      <div class="bg-gradient-to-r from-[#EEF6F9] to-[#F8F9FA] border border-[#1895BB]/20 rounded-2xl p-5 mb-8">
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
      </div>"""

new_caritiva = """      <div class="bg-gradient-to-r from-[#EEF6F9] to-[#F8F9FA] border border-[#1895BB]/20 rounded-2xl p-5 mb-8">
        <p class="text-xs font-bold text-[#1895BB] tracking-[.2em] uppercase mb-3">Offizielle Auszeichnung</p>
        <div class="flex flex-wrap gap-6 text-sm text-[#3D5A6A] mb-4">
          <div>
            <span class="font-semibold text-[#1E3E4F] block">Ausgestellt von</span>
            CARITIVA GmbH, Montabaur
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
        <p class="text-sm text-[#3D5A6A] italic border-l-2 border-[#1895BB]/40 pl-3">
          „Dank Ihrer Mithilfe konnte das Rettungsleitsystem für den FC Oberhinkofen e.V. bereitgestellt werden.
          Wir wünschen Ihnen und Ihrem Unternehmen viel Erfolg."
          <span class="block mt-1 text-xs text-[#5A7A8A] not-italic">— CARITIVA, Urkunde vom 31.03.2026</span>
        </p>
      </div>"""

if old_caritiva in html:
    html = html.replace(old_caritiva, new_caritiva)
    print("Caritiva Details aktualisiert OK")
else:
    print("FEHLER: Caritiva Block nicht gefunden!")

# ─── 4. Lebensretter-Tafel Info zwischen Galerie und CTA einfügen ─────────────
old_gallery_end = """      <!-- CTA -->
      <div class="flex flex-wrap gap-3 pt-4 border-t border-[#1895BB]/15">"""

new_gallery_end = """      <!-- Lebensretter-Tafel Info -->
      <div class="bg-[#1E3E4F] rounded-2xl p-5 mb-8 text-white">
        <div class="flex items-start gap-4">
          <div class="w-10 h-10 rounded-xl bg-white/10 flex items-center justify-center flex-shrink-0 mt-0.5">
            <svg class="w-5 h-5 text-[#5DD4F0]" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M9 12h3.75M9 15h3.75M9 18h3.75m3 .75H18a2.25 2.25 0 002.25-2.25V6.108c0-1.135-.845-2.098-1.976-2.192a48.424 48.424 0 00-1.123-.08m-5.801 0c-.065.21-.1.433-.1.664 0 .414.336.75.75.75h4.5a.75.75 0 00.75-.75 2.25 2.25 0 00-.1-.664m-5.8 0A2.251 2.251 0 0113.5 2.25H15c1.012 0 1.867.668 2.15 1.586m-5.8 0c-.376.023-.75.05-1.124.08C9.095 4.01 8.25 4.973 8.25 6.108V8.25m0 0H4.875c-.621 0-1.125.504-1.125 1.125v11.25c0 .621.504 1.125 1.125 1.125h9.75c.621 0 1.125-.504 1.125-1.125V9.375c0-.621-.504-1.125-1.125-1.125H8.25zM6.75 12h.008v.008H6.75V12zm0 3h.008v.008H6.75V15zm0 3h.008v.008H6.75V18z"/>
            </svg>
          </div>
          <div>
            <p class="font-bold text-white mb-1">Die Lebensretter-Tafel (1,90 × 1,20 m)</p>
            <p class="text-white/75 text-sm leading-relaxed">
              Direkt am Sportplatz des FC Oberhinkofen aufgestellt – mit dem Logo und Namen von
              <strong class="text-[#5DD4F0]">Elektrotechnik Rakin OHG</strong> als Sponsor auf der Förderertafel.
              Sichtbarkeit für Verein, Besucher und die gesamte Region.
            </p>
          </div>
        </div>
      </div>

      <!-- CTA -->
      <div class="flex flex-wrap gap-3 pt-4 border-t border-[#1895BB]/15">"""

if old_gallery_end in html:
    html = html.replace(old_gallery_end, new_gallery_end)
    print("Lebensretter-Tafel Info eingefuegt OK")
else:
    print("FEHLER: CTA-Marker nicht gefunden!")

# ─── 5. SPEICHERN ─────────────────────────────────────────────────────────────
with open('index_website.html', 'w', encoding='utf-8') as f:
    f.write(html)

checks = {
    '75 Jahre FC':              '75-jähriges Jubiläum' in html,
    'CenterBall':               'CenterBall' in html,
    '3-5 Minuten':              '3–5 Minuten' in html,
    'TÜV-geprüft':              'TÜV-geprüft' in html,
    'Notruf 112':               'Notruf 112' in html,
    'Urkunden-Zitat':           'Dank Ihrer Mithilfe' in html,
    'CARITIVA GmbH Montabaur':  'CARITIVA GmbH, Montabaur' in html,
    'Lebensretter-Tafel Info':  '1,90 × 1,20 m' in html,
}
print()
for k, v in checks.items():
    print(f'  {"OK" if v else "FEHLER"} - {k}')
