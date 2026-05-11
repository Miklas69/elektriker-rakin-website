with open('index_website.html', 'r', encoding='utf-8') as f:
    html = f.read()

changes = 0

def rep(old, new, h):
    global changes
    if old in h:
        changes += 1
        return h.replace(old, new)
    else:
        print(f"NICHT GEFUNDEN: {repr(old[:80])}")
        return h

# 1. ROOT VARIABLES
html = rep(
    "      --primary: #F97316;\n      --bg: #0D1117;\n      --surface: #161B22;",
    "      --primary:      #1895BB;\n      --primary-dark: #1571A0;\n      --bg:           #F8F9FA;\n      --surface:      #EEF6F9;\n      --surface-2:    #E0EEF4;\n      --text-dark:    #1A2B35;",
    html)

# 2. BODY TEXT COLOR
html = rep(
    "body { background: var(--bg); color: #F1F5F9;",
    "body { background: var(--bg); color: #1A2B35;",
    html)

# 3. HEADER SCROLLED
html = rep(
    "background: rgba(13,17,23,.95) !important;\n      box-shadow: 0 1px 0 rgba(249,115,22,.15);",
    "background: rgba(248,249,250,.97) !important;\n      box-shadow: 0 1px 0 rgba(24,149,187,.15);",
    html)

# 4. HERO IMAGE + OVERLAY
html = rep(
    "        linear-gradient(to bottom,\n          rgba(13,17,23,.55) 0%,\n          rgba(13,17,23,.70) 60%,\n          rgba(13,17,23,1)   100%),\n        url('https://images.unsplash.com/photo-1621905252507-b35492cc74b4?auto=format&fit=crop&w=1920&q=85');\n      background-size: cover;\n      background-position: center 30%;",
    "        linear-gradient(to bottom,\n          rgba(20,50,65,.50) 0%,\n          rgba(20,50,65,.72) 60%,\n          rgba(20,50,65,.92) 100%),\n        url('Bilder/Herbert_arbeitet.avif');\n      background-size: cover;\n      background-position: center 40%;",
    html)

# 5. GRADIENT TEXT
html = rep(
    "background: linear-gradient(135deg, #F97316, #FBBF24);",
    "background: linear-gradient(135deg, #1895BB, #1E3E4F);",
    html)

# 6. DIVIDER
html = rep(
    ".divider { height:1px; background:linear-gradient(90deg, transparent, rgba(249,115,22,.25), transparent); }",
    ".divider { height:1px; background:linear-gradient(90deg, transparent, rgba(24,149,187,.30), transparent); }",
    html)

# 7. SVC CARD BORDER
html = rep(
    "border: 1px solid rgba(255,255,255,.06);\n      border-radius: 20px;\n      transition: transform .35s ease, box-shadow .35s ease, border-color .35s ease;",
    "border: 1px solid rgba(24,149,187,.15);\n      border-radius: 20px;\n      background: #fff;\n      transition: transform .35s ease, box-shadow .35s ease, border-color .35s ease;",
    html)

# 8. SVC CARD BEFORE BG
html = rep(
    "background: rgba(13,17,23,.80);\n      transition: background .35s ease;\n      z-index: 1;",
    "background: rgba(20,50,65,.72);\n      transition: background .35s ease;\n      z-index: 1;",
    html)

# 9. SVC CARD HOVER
html = rep(
    "border-color: rgba(249,115,22,.5);\n      box-shadow: 0 20px 50px rgba(0,0,0,.5), 0 0 0 1px rgba(249,115,22,.15), 0 0 40px rgba(249,115,22,.08);",
    "border-color: rgba(24,149,187,.5);\n      box-shadow: 0 20px 50px rgba(24,149,187,.18), 0 0 0 1px rgba(24,149,187,.15);",
    html)

# 10. SVC CARD HOVER BEFORE
html = rep(
    ".svc-card:hover::before { background: rgba(13,17,23,.65); }",
    ".svc-card:hover::before { background: rgba(20,50,65,.55); }",
    html)

# 11. SVC ICON HOVER
html = rep(
    ".svc-card:hover .svc-icon { background: rgba(249,115,22,.25); color: #F97316; }",
    ".svc-card:hover .svc-icon { background: rgba(24,149,187,.20); color: #1895BB; }",
    html)

# 12. TRUST ITEM
html = rep(
    ".trust-item { border-left: 3px solid var(--primary); transition: background .3s; }",
    ".trust-item { border-left: 3px solid var(--primary); transition: background .3s; background: #fff; border-radius: 0 8px 8px 0; }",
    html)
html = rep(
    ".trust-item:hover { background: rgba(249,115,22,.04); }",
    ".trust-item:hover { background: rgba(24,149,187,.06); }",
    html)

# 13. PHOTO FRAME OVERLAY
html = rep(
    "background: linear-gradient(135deg, rgba(249,115,22,.1), transparent 60%);",
    "background: linear-gradient(135deg, rgba(24,149,187,.1), transparent 60%);",
    html)

# 14. EMERGENCY SECTION
html = rep(
    "        linear-gradient(135deg, rgba(249,115,22,.12) 0%, rgba(234,68,10,.06) 100%),\n        #0D1117;\n      border-top: 1px solid rgba(249,115,22,.2);\n      border-bottom: 1px solid rgba(249,115,22,.2);",
    "        linear-gradient(135deg, rgba(239,68,68,.08) 0%, rgba(220,38,38,.04) 100%),\n        #1A2B35;\n      border-top: 1px solid rgba(239,68,68,.25);\n      border-bottom: 1px solid rgba(239,68,68,.25);",
    html)

# 15. FORM FIELDS
html = rep(
    "background: rgba(255,255,255,.04);\n      border: 1px solid rgba(255,255,255,.1);\n      color: #F1F5F9;",
    "background: #fff;\n      border: 1px solid #CBD5E1;\n      color: #1A2B35;",
    html)
html = rep(
    ".form-field:focus { border-color: var(--primary); box-shadow: 0 0 0 3px rgba(249,115,22,.12); }",
    ".form-field:focus { border-color: var(--primary); box-shadow: 0 0 0 3px rgba(24,149,187,.12); }",
    html)
html = rep(
    "select.form-field option { background: #161B22; }",
    "select.form-field option { background: #fff; color: #1A2B35; }",
    html)

# 16. BTN PRIMARY HOVER
html = rep(
    "background: #EA6C0A;\n      box-shadow: 0 8px 30px rgba(249,115,22,.35);",
    "background: #1571A0;\n      box-shadow: 0 8px 30px rgba(24,149,187,.35);",
    html)

# 17. LOGOS (nav + footer)
html = html.replace(
    'src="Bilder/Logo.png" alt="Elektrotechnik Rakin Logo" class="h-10 w-auto object-contain"',
    'src="Bilder/Logo_SVG.svg" alt="Elektrotechnik Rakin Logo" class="h-10 w-auto object-contain"'
)
html = html.replace(
    'src="Bilder/Logo.png" alt="Elektrotechnik Rakin Logo" class="h-9 w-auto object-contain"',
    'src="Bilder/Logo_SVG.svg" alt="Elektrotechnik Rakin Logo" class="h-9 w-auto object-contain"'
)

# 18. ADD TAILWIND OVERRIDE BLOCK
overrides = """
    /* ══════════════════════════════════════════
       LIGHT DESIGN: Tailwind compiled overrides
    ══════════════════════════════════════════ */
    .bg-bg        { background-color: #F8F9FA !important; }
    .bg-surface   { background-color: #EEF6F9 !important; }
    .bg-surface-2 { background-color: #E0EEF4 !important; }
    .bg-primary   { background-color: #1895BB !important; }
    .text-text         { color: #1A2B35 !important; }
    .text-muted        { color: #5A7A8A !important; }
    .text-muted-light  { color: #3D5A6A !important; }
    .text-primary      { color: #1895BB !important; }
    .text-primary-dark { color: #1571A0 !important; }
    .border-primary    { border-color: #1895BB !important; }

    /* Header: immer hell */
    #main-header {
      background: rgba(248,249,250,.92) !important;
      border-bottom: 1px solid rgba(24,149,187,.15) !important;
      backdrop-filter: blur(12px);
    }
    #mobile-menu { background: #fff !important; }

    /* Hero: Text bleibt weiss auf dunklem Overlay */
    .hero-img h1,
    .hero-img > div p,
    .hero-img .fade-up { color: #fff !important; }
    .hero-img .text-muted-light { color: #CBD8E0 !important; }
    .hero-img .text-primary { color: #5DD4F0 !important; }
    .hero-img .text-muted { color: #CBD8E0 !important; }

    /* Trust-pills im Hero */
    .hero-img .bg-white\\/\\[\\.05\\] { background: rgba(255,255,255,.12) !important; }

    /* Review-Karten */
    .review-card {
      background: #fff !important;
      border: 1px solid rgba(24,149,187,.12) !important;
      box-shadow: 0 2px 12px rgba(24,149,187,.06);
    }

    /* Hintergrund-Blobs anpassen */
    .bg-primary\\/10 { background-color: rgba(24,149,187,.08) !important; }
    .bg-copper\\/10  { background-color: rgba(30,62,79,.06)   !important; }

    /* Gradient Badge-Farben */
    .from-primary\\/60 { --tw-gradient-from: rgba(24,149,187,.6) !important; }
    .from-copper       { --tw-gradient-from: #1E3E4F !important; }
    .from-primary      { --tw-gradient-from: #1895BB !important; }
    .to-copper         { --tw-gradient-to: #1E3E4F !important; }
    .to-primary\\/60   { --tw-gradient-to: rgba(24,149,187,.6) !important; }

    /* Bewertungs-Sterne bleiben gelb */
    .text-\\[\\#FBBF24\\] { color: #FBBF24 !important; }

    /* Scrollbar */
    ::-webkit-scrollbar-thumb { background: #1895BB !important; }
"""

html = html.replace(
    "    .star { color: #FBBF24; }\n</style>",
    "    .star { color: #FBBF24; }\n" + overrides + "</style>"
)

print(f"Ersetzungen durchgefuehrt: {changes}")
with open('index_website.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Datei gespeichert.")
