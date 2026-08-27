#!/usr/bin/env python3
"""
CD Boulangerie — générateur du site (FR / EN / PL).

  python3 build.py            -> version autonome à la racine (+ /en, /pl)
  CD_INLINE=0 python3 build.py -> fichiers séparés (styles.css + script.js)
  CD_OUT=dossier ...           -> écrit ailleurs

Les textes vivent dans i18n.py. Les photos dans images/.
"""
import os
import base64
import hashlib
import re
from pathlib import Path
from urllib.parse import quote

from i18n import T, LANGS, check as i18n_check

ROOT = Path(__file__).parent
OUT = Path(os.environ.get("CD_OUT", ROOT))
OUT.mkdir(parents=True, exist_ok=True)


def ver(relpath):
    f = ROOT / relpath
    if not f.exists():
        return relpath
    h = hashlib.md5(f.read_bytes()).hexdigest()[:8]
    return f"{relpath}?v={h}"


def read(relpath):
    f = ROOT / relpath
    return f.read_text(encoding="utf-8") if f.exists() else ""


# --- Mode autonome ----------------------------------------------------------
# Certaines fenêtres d'aperçu n'ouvrent qu'un fichier à la fois et refusent de
# charger styles.css / script.js. Tout intégrer rend chaque page autonome.
INLINE = os.environ.get("CD_INLINE", "1") != "0"

BRAND = "CD Boulangerie"
PHONE_DISPLAY = "09 78 80 63 06"
PHONE_TEL = "+33978806306"
EMAIL = "contact@cdboulangerie.fr"
FACEBOOK = "https://www.facebook.com/CDboulangerie/"
INSTAGRAM = "https://www.instagram.com/cdboulangerie/"
# WhatsApp : numéro au format international, sans + ni espaces.
WHATSAPP_NUM = "33978806306"

# Domaine public du site. Sert aux liens canoniques, au sitemap et aux aperçus de partage.
SITE_URL = os.environ.get("CD_SITE_URL", "https://cd-boulangerie.fr").rstrip("/")
# ---------------------------------------------------------------------------
#  ADRESSES
#  Vérifiées au registre du commerce (RCS Draguignan, SIREN 918 964 834) :
#    siège              6 Rue du Docteur Rayol, 83131 Montferrat
#    2e établissement   7 Place du Caou, 83830 Figanières
# ---------------------------------------------------------------------------
ADDR_MONTFERRAT_RUE = "6 Rue du Dr Rayol"
ADDR_MONTFERRAT_CP = "83131 Montferrat"
ADDR_FIGANIERES_RUE = "7 Place du Caou"
ADDR_FIGANIERES_CP = "83830 Figanières"

# Liens Google Maps. On passe par une recherche sur l'adresse complète :
# c'est la forme la plus robuste — elle fonctionne sur mobile (ouvre l'appli
# Maps) comme sur ordinateur, et ne casse pas si la fiche est modifiée.
MAPS_MONTFERRAT = ("https://www.google.com/maps/search/?api=1&query="
                   + quote(f"CD Boulangerie, {ADDR_MONTFERRAT_RUE}, {ADDR_MONTFERRAT_CP}"))
MAPS_FIGANIERES = ("https://www.google.com/maps/search/?api=1&query="
                   + quote(f"CD Boulangerie, {ADDR_FIGANIERES_RUE}, {ADDR_FIGANIERES_CP}"))

# Itinéraire : ouvre directement le guidage, plus utile qu'une simple fiche.
ITINERAIRE_MONTFERRAT = ("https://www.google.com/maps/dir/?api=1&destination="
                         + quote(f"CD Boulangerie, {ADDR_MONTFERRAT_RUE}, {ADDR_MONTFERRAT_CP}"))
ITINERAIRE_FIGANIERES = ("https://www.google.com/maps/dir/?api=1&destination="
                         + quote(f"CD Boulangerie, {ADDR_FIGANIERES_RUE}, {ADDR_FIGANIERES_CP}"))

PAGES = ["index", "produits", "evenements", "maison", "boulangeries", "contact",
         "mentions", "cgv", "confidentialite"]
# Pages légales : présentes dans le pied de page et le sitemap, mais pas dans
# le menu principal — personne ne visite un site pour lire des CGV.
PAGES_LEGALES = ["mentions", "cgv", "confidentialite"]
NAV_KEYS = [("index", "nav_home"), ("produits", "nav_products"),
            ("evenements", "nav_events"), ("maison", "nav_house"),
            ("boulangeries", "nav_bakeries"), ("contact", "nav_contact")]

# ---------------------------------------------------------------- ICONES ---
ICON_PLUS = ('<svg width="16" height="16" viewBox="0 0 16 16" fill="none" '
             'stroke="currentColor" stroke-width="1.2" aria-hidden="true">'
             '<path d="M8 1v14M1 8h14"/></svg>')
ICON_ARROW = ('<svg width="17" height="17" viewBox="0 0 17 17" fill="none" '
              'stroke="currentColor" stroke-width="1.3" aria-hidden="true">'
              '<path d="M2 15L15 2M15 2H5.5M15 2v9.5"/></svg>')
ICON_UP = ('<svg width="15" height="15" viewBox="0 0 15 15" fill="none" '
           'stroke="currentColor" stroke-width="1.4" aria-hidden="true">'
           '<path d="M7.5 14V1M1.5 7L7.5 1l6 6"/></svg>')

FLAGS = {
    "fr": ('<svg class="flag" viewBox="0 0 3 2" aria-hidden="true">'
           '<rect width="1" height="2" x="0" fill="#0055A4"/>'
           '<rect width="1" height="2" x="1" fill="#FFFFFF"/>'
           '<rect width="1" height="2" x="2" fill="#EF4135"/></svg>'),
    "en": ('<svg class="flag" viewBox="0 0 60 30" aria-hidden="true">'
           '<clipPath id="ukc{u}"><rect width="60" height="30"/></clipPath>'
           '<g clip-path="url(#ukc{u})">'
           '<rect width="60" height="30" fill="#012169"/>'
           '<path d="M0,0 60,30M60,0 0,30" stroke="#FFF" stroke-width="6"/>'
           '<path d="M0,0 60,30M60,0 0,30" stroke="#C8102E" stroke-width="4"/>'
           '<path d="M30,0 V30M0,15 H60" stroke="#FFF" stroke-width="10"/>'
           '<path d="M30,0 V30M0,15 H60" stroke="#C8102E" stroke-width="6"/>'
           '</g></svg>'),
    "pl": ('<svg class="flag" viewBox="0 0 16 10" aria-hidden="true">'
           '<rect width="16" height="5" y="0" fill="#FFFFFF"/>'
           '<rect width="16" height="5" y="5" fill="#DC143C"/></svg>'),
}

ICON_FB = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
           '<path d="M24 12.07C24 5.4 18.63 0 12 0S0 5.4 0 12.07C0 18.1 4.39 23.1 10.13 24v-8.44'
           'H7.08v-3.49h3.05V9.41c0-3.02 1.79-4.69 4.53-4.69 1.31 0 2.68.24 2.68.24v2.97h-1.51'
           'c-1.49 0-1.96.93-1.96 1.89v2.25h3.33l-.53 3.49h-2.8V24C19.61 23.1 24 18.1 24 12.07Z"/>'
           '</svg>')
ICON_IG = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
           '<path d="M12 2.16c3.2 0 3.58.01 4.85.07 1.17.05 1.8.25 2.23.41.56.22.96.48 1.38.9'
           '.42.42.68.82.9 1.38.16.42.36 1.06.41 2.23.06 1.27.07 1.65.07 4.85s-.01 3.58-.07 4.85'
           'c-.05 1.17-.25 1.8-.41 2.23-.22.56-.48.96-.9 1.38-.42.42-.82.68-1.38.9-.42.16-1.06.36-2.23.41'
           '-1.27.06-1.65.07-4.85.07s-3.58-.01-4.85-.07c-1.17-.05-1.8-.25-2.23-.41-.56-.22-.96-.48-1.38-.9'
           '-.42-.42-.68-.82-.9-1.38-.16-.42-.36-1.06-.41-2.23C2.17 15.58 2.16 15.2 2.16 12s.01-3.58.07-4.85'
           'c.05-1.17.25-1.8.41-2.23.22-.56.48-.96.9-1.38.42-.42.82-.68 1.38-.9.42-.16 1.06-.36 2.23-.41'
           'C8.42 2.17 8.8 2.16 12 2.16Z M12 0C8.74 0 8.33.01 7.05.07 5.78.13 4.9.33 4.14.63'
           'c-.79.3-1.46.72-2.13 1.38C1.35 2.68.93 3.35.63 4.14.33 4.9.13 5.78.07 7.05.01 8.33 0 8.74 0 12'
           's.01 3.67.07 4.95c.06 1.27.26 2.15.56 2.91.3.79.72 1.46 1.38 2.13.67.66 1.34 1.08 2.13 1.38'
           '.76.3 1.64.5 2.91.56C8.33 23.99 8.74 24 12 24s3.67-.01 4.95-.07c1.27-.06 2.15-.26 2.91-.56'
           '.79-.3 1.46-.72 2.13-1.38.66-.67 1.08-1.34 1.38-2.13.3-.76.5-1.64.56-2.91.06-1.28.07-1.69.07-4.95'
           's-.01-3.67-.07-4.95c-.06-1.27-.26-2.15-.56-2.91-.3-.79-.72-1.46-1.38-2.13C21.32 1.35 20.65.93 19.86.63'
           'c-.76-.3-1.64-.5-2.91-.56C15.67.01 15.26 0 12 0Z'
           'M12 5.84a6.16 6.16 0 1 0 0 12.32 6.16 6.16 0 0 0 0-12.32Zm0 10.16a4 4 0 1 1 0-8 4 4 0 0 1 0 8Z'
           'M19.85 5.6a1.44 1.44 0 1 1-2.88 0 1.44 1.44 0 0 1 2.88 0Z"/></svg>')
ICON_WA = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
           '<path d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.17'
           '-.17.2-.35.22-.65.07-.3-.15-1.25-.46-2.38-1.47-.88-.79-1.48-1.76-1.65-2.06-.17-.3-.02-.46.13-.61'
           '.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.61-.92-2.21'
           '-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48s1.06 2.88 1.21 3.08'
           '.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.69.62.71.23 1.36.19 1.87.12.57-.09 1.76-.72 2.01-1.41'
           '.25-.7.25-1.29.17-1.42-.07-.13-.27-.2-.57-.35Z'
           'M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2 22l5.25-1.38c1.45.79 3.08 1.21 4.79 1.21'
           'h.01c5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0 0 12.04 2Z'
           'm5.8 15.71c-.25.7-1.45 1.33-2 1.42-.51.08-1.16.11-1.87-.12a17 17 0 0 1-1.69-.62c-2.98-1.29-4.93-4.29-5.08-4.49'
           '-.15-.2-1.21-1.61-1.21-3.08s.77-2.18 1.04-2.48c.27-.3.59-.37.79-.37h.57c.18.01.43-.07.67.51'
           '.25.6.84 2.06.92 2.21.07.15.12.32.02.52-.1.2-.15.33-.3.5-.15.17-.32.39-.45.52-.15.15-.3.31-.13.61'
           '.17.3.77 1.27 1.65 2.06 1.13 1.01 2.08 1.32 2.38 1.47.3.15.48.13.65-.07.17-.2.74-.87.94-1.17'
           '.2-.3.4-.25.67-.15.27.1 1.73.82 2.03.97.3.15.5.22.57.35.08.13.08.72-.17 1.41Z"/></svg>')

ICON_CHEV = ('<svg class="lang__chev" width="9" height="6" viewBox="0 0 9 6" fill="none" '
             'stroke="currentColor" stroke-width="1.4" aria-hidden="true">'
             '<path d="M1 1l3.5 3.5L8 1"/></svg>')



# ============================================================================
#  Helpers
# ============================================================================
_B64 = {}


def depth(lang):
    """Préfixe de remontée vers la racine ('' pour FR, '../' pour en/pl)."""
    return "" if lang == "fr" else "../"


def asset(path, lang):
    """URL d'un fichier statique depuis une page de langue donnée."""
    if INLINE:
        return path
    return depth(lang) + ver(path)


def img_src(name, lang):
    if not INLINE:
        return depth(lang) + f"images/{name}.webp"
    if name not in _B64:
        f = ROOT / "images/inline" / f"{name}.webp"
        if not f.exists():
            f = ROOT / "images" / f"{name}.webp"
        if not f.exists():
            return ""
        _B64[name] = "data:image/webp;base64," + base64.b64encode(f.read_bytes()).decode("ascii")
    return _B64[name]


# Ordre identique à m_partners dans i18n.py — 12 vignettes.
PARTENAIRES_LOGOS = [
    "mairie-montferrat", "mairie-figanieres", "mairie-chateaudouble",
    "ehpad-figanieres", "creche-figanieres", "creche-montferrat",
    "ecole-montferrat", "restaurant-la-bastide", "associations",
    "producteurs-var", "too-good-to-go", "brasseurs",
]


def partner_src(name, lang):
    """URL d'une vignette partenaire (images/partenaires/)."""
    key = "part:" + name
    if not INLINE:
        return depth(lang) + f"images/partenaires/{name}.png"
    if key not in _B64:
        f = ROOT / "images/partenaires" / f"{name}.png"
        if not f.exists():
            return ""
        _B64[key] = "data:image/png;base64," + base64.b64encode(f.read_bytes()).decode("ascii")
    return _B64[key]


def logo_src(name, lang):
    """URL d'un fichier du logo (images/logo/). Intégré en base64 si besoin."""
    key = "logo:" + name
    if not INLINE:
        return depth(lang) + f"images/logo/{name}.png"
    if key not in _B64:
        f = ROOT / "images/logo" / f"{name}.png"
        if not f.exists():
            return ""
        _B64[key] = "data:image/png;base64," + base64.b64encode(f.read_bytes()).decode("ascii")
    return _B64[key]


def link(page, lang):
    """Lien interne vers une page, dans la langue courante."""
    return f"{page}.html"


def img_size(name):
    """Dimensions réelles — évite les sauts de mise en page (CLS) au chargement."""
    f = ROOT / "images" / f"{name}.webp"
    if not f.exists():
        return None
    try:
        from PIL import Image
        return Image.open(f).size
    except Exception:
        # Lecture minimale de l'en-tête WebP si Pillow est absent
        import struct
        d = f.read_bytes()[:40]
        if d[12:16] == b"VP8X":
            w = int.from_bytes(d[24:27], "little") + 1
            h = int.from_bytes(d[27:30], "little") + 1
            return (w, h)
        return None


_SIZES = {}


def frame(cap, ratio="4x5", tag=None, mod="", img=None, eager=False, lang="fr"):
    tag_html = f'<span class="frame__tag">{tag}</span>' if tag else ""
    if img:
        loading = 'loading="eager" fetchpriority="high"' if eager else 'loading="lazy"'
        if img not in _SIZES:
            _SIZES[img] = img_size(img)
        wh = ""
        if _SIZES[img]:
            wh = f' width="{_SIZES[img][0]}" height="{_SIZES[img][1]}"'
        inner = (f'<img class="frame__img" src="{img_src(img, lang)}"{wh} '
                 f'alt="{cap}" {loading} decoding="async">')
    else:
        inner = (f'<div class="frame__ph"><span class="frame__ico">{ICON_PLUS}</span>'
                 f'<span class="frame__cap">{cap}</span></div>')
    return (f'<figure class="frame frame--{ratio} {mod}">{tag_html}{inner}</figure>')


def marquee(items, ink=False, speed=34):
    dots = '<span class="marquee__dot"></span>'
    content = dots.join(f'<span>{i}</span>' for i in items)
    return (f'<div class="marquee {"marquee--ink" if ink else ""}" data-speed="{speed}" '
            f'aria-hidden="true"><div class="marquee__track">'
            f'<span class="marquee__item">{content}{dots}</span></div></div>')


def wa_link(t):
    """Lien WhatsApp avec message pré-rempli, traduit."""
    return f"https://wa.me/{WHATSAPP_NUM}?text={quote(t['wa_msg'])}"


def social(t, variant="", label=True):
    """Bloc réseaux sociaux réutilisable : Facebook · Instagram · WhatsApp."""
    return f'''<div class="social {variant}">
      <a class="social__link social__link--fb" href="{FACEBOOK}" target="_blank"
         rel="noopener noreferrer" aria-label="Facebook — {BRAND}">{ICON_FB}</a>
      <a class="social__link social__link--ig" href="{INSTAGRAM}" target="_blank"
         rel="noopener noreferrer" aria-label="Instagram — {BRAND}">{ICON_IG}</a>
      <a class="social__link social__link--wa" href="{wa_link(t)}" target="_blank"
         rel="noopener noreferrer" aria-label="WhatsApp — {BRAND}">{ICON_WA}</a>
    </div>'''


def lang_switch(lang, page, t, in_menu=False):
    """Sélecteur de langue. Chaque option pointe vers la même page traduite."""
    items = ""
    for code, name, short, folder in LANGS:
        if code == lang:
            href = f"{page}.html"
        elif lang == "fr":
            href = f"{folder}/{page}.html"
        elif code == "fr":
            href = f"../{page}.html"
        else:
            href = f"../{folder}/{page}.html"
        cur = "true" if code == lang else "false"
        flag = FLAGS[code].replace("{u}", code + ("m" if in_menu else "h"))
        items += (f'<a class="lang__item" href="{href}" hreflang="{code}" '
                  f'aria-current="{cur}" lang="{code}">{flag}<span>{name}</span></a>')

    cur_flag = FLAGS[lang].replace("{u}", lang + ("mb" if in_menu else "hb"))
    cur_short = next(s for c, n, s, f in LANGS if c == lang)
    uid = "langMenu" if in_menu else "langHead"
    return f'''<div class="lang" data-lang>
      <button class="lang__btn" type="button" aria-expanded="false"
              aria-controls="{uid}" aria-label="{t['lang_label']}">
        {cur_flag}<span>{cur_short}</span>{ICON_CHEV}
      </button>
      <div class="lang__list" id="{uid}" role="menu">{items}</div>
    </div>'''


# ============================================================================
#  Chrome
# ============================================================================
def abs_url(lang, page):
    """URL absolue d'une page — nécessaire pour canonical / hreflang / sitemap."""
    folder = next(f for c, n, s, f in LANGS if c == lang)
    return f"{SITE_URL}/{folder + '/' if folder else ''}{page}.html"


def jsonld(t, lang, page):
    """Données structurées : aide Google à afficher horaires, adresse et avis."""
    import json
    hours = [
        {"@type": "OpeningHoursSpecification",
         "dayOfWeek": ["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
         "opens": "07:00", "closes": "13:30"},
        {"@type": "OpeningHoursSpecification",
         "dayOfWeek": ["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
         "opens": "16:30", "closes": "19:00"},
        {"@type": "OpeningHoursSpecification",
         "dayOfWeek": "Sunday", "opens": "07:00", "closes": "13:30"},
    ]
    # Figanières ferme plus tôt le dimanche (13h au lieu de 13h30)
    hours_fig = [
        {"@type": "OpeningHoursSpecification",
         "dayOfWeek": ["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
         "opens": "07:00", "closes": "13:30"},
        {"@type": "OpeningHoursSpecification",
         "dayOfWeek": ["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
         "opens": "16:30", "closes": "19:00"},
        {"@type": "OpeningHoursSpecification",
         "dayOfWeek": "Sunday", "opens": "07:00", "closes": "13:00"},
    ]
    data = {
        "@context": "https://schema.org",
        "@type": "Bakery",
        "name": BRAND,
        "description": t["meta"][page][1].replace("&amp;", "&"),
        "url": abs_url(lang, page),
        "image": f"{SITE_URL}/images/og-cover.jpg",
        "telephone": PHONE_TEL,
        "email": EMAIL,
        "priceRange": "€",
        "servesCuisine": "Bakery",
        "address": {"@type": "PostalAddress", "streetAddress": ADDR_MONTFERRAT_RUE,
                    "addressLocality": "Montferrat", "postalCode": "83131",
                    "addressRegion": "Var", "addressCountry": "FR"},
        "geo": {"@type": "GeoCoordinates", "latitude": 43.6469, "longitude": 6.5122},
        "hasMap": MAPS_MONTFERRAT,
        "openingHoursSpecification": hours,
        # sameAs : dit à Google que ces comptes appartiennent bien à la maison.
        # C'est ce qui relie le site, la fiche Google et les réseaux sociaux.
        "sameAs": [FACEBOOK, INSTAGRAM],
        # Ne pas ajouter de note ici sans chiffres Google confirmés.
        # Une donnée structurée inventée peut nuire au référencement.
        # Le 2e point de vente : sans cela Google ignore la boutique de Figanières.
        "department": [{
            "@type": "Bakery",
            "name": f"{BRAND} — Figanières",
            "telephone": PHONE_TEL,
            "priceRange": "€",
            "image": f"{SITE_URL}/images/og-cover.jpg",
            "address": {"@type": "PostalAddress", "streetAddress": ADDR_FIGANIERES_RUE,
                        "addressLocality": "Figanières", "postalCode": "83830",
                        "addressRegion": "Var", "addressCountry": "FR"},
            "geo": {"@type": "GeoCoordinates", "latitude": 43.5906, "longitude": 6.4283},
            "hasMap": MAPS_FIGANIERES,
            "openingHoursSpecification": hours_fig,
        }],
    }
    return ('<script type="application/ld+json">'
            + json.dumps(data, ensure_ascii=False, separators=(",", ":"))
            + '</script>')


# --- Polices ----------------------------------------------------------------
# Elles sont hébergées avec le site : plus aucun appel à Google Fonts, donc
# plus de fuite d'adresse IP vers Google (RGPD) ni de connexion tierce.
# On précharge les deux fichiers réellement critiques au premier écran :
# le Garamond du titre et le Work Sans du texte. Sans cela le navigateur ne
# les découvre qu'après avoir lu le CSS, ce qui décale l'affichage.
FONTS_PRELOAD = ["EB_Garamond_500_latin.woff2", "Work_Sans_400_latin.woff2"]


def fonts_head(lang):
    if INLINE:
        # En mode autonome les polices sont intégrées en base64 dans le CSS :
        # rien à précharger, tout est déjà là.
        return ""
    out = []
    for f in FONTS_PRELOAD:
        # PAS de ?v=hash ici : styles.css appelle url('fonts/…') sans paramètre.
        # Deux URL différentes = deux téléchargements du même fichier.
        out.append(f'<link rel="preload" href="{depth(lang)}fonts/{f}" '
                   f'as="font" type="font/woff2" crossorigin>')
    return "\n".join(out)


_CSS_CACHE = {}


def css_autonome():
    """CSS avec les polices en base64.

    En mode autonome la page est ouverte seule : un url('fonts/…') ne se
    résout pas et le navigateur retombe sur Times New Roman. On remplace donc
    chaque référence par le fichier lui-même, encodé en base64.
    Le résultat est mis en cache : sinon on relirait 14 fichiers par page,
    donc 252 fois pour les 27 pages.
    """
    if "v" in _CSS_CACHE:
        return _CSS_CACHE["v"]
    css = read("styles.css")

    def remplacer(m):
        f = ROOT / "fonts" / m.group(1)
        if not f.exists():
            return m.group(0)
        b64 = base64.b64encode(f.read_bytes()).decode()
        return f"url(data:font/woff2;base64,{b64}) format('woff2')"

    css = re.sub(r"url\('fonts/([^']+)'\) format\('woff2'\)", remplacer, css)
    _CSS_CACHE["v"] = css
    return css


def head(t, lang, page):
    title, desc = t["meta"][page]
    css = ("<style>\n" + css_autonome() + "\n</style>") if INLINE \
        else f'<link rel="stylesheet" href="{asset("styles.css", lang)}">'

    # hreflang : indique à Google les versions équivalentes.
    # URL absolues : les chemins relatifs sont ignorés par les moteurs.
    alts = ""
    for code, name, short, folder in LANGS:
        alts += f'<link rel="alternate" hreflang="{code}" href="{abs_url(code, page)}">\n'
    alts += f'<link rel="alternate" hreflang="x-default" href="{abs_url("fr", page)}">\n'
    alts += f'<link rel="canonical" href="{abs_url(lang, page)}">\n'

    og_img = f"{SITE_URL}/images/og-cover.jpg"
    social_meta = f'''<meta property="og:url" content="{abs_url(lang, page)}">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:image" content="{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{BRAND} — {t['b_img_1']}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{og_img}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="author" content="{BRAND}">
{jsonld(t, lang, page)}'''

    return f'''<!doctype html>
<html lang="{t['html_lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#F8F6F0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:locale" content="{t['locale']}">
{social_meta}
{alts}{fonts_head(lang)}
<script>document.documentElement.className+=' js';</script>
{css}
<link rel="icon" type="image/png" sizes="32x32" href="{logo_src('favicon-32', lang)}">
<link rel="icon" type="image/png" sizes="16x16" href="{logo_src('favicon-16', lang)}">
<link rel="apple-touch-icon" href="{logo_src('apple-touch-icon', lang)}">
</head>
<body data-page="{page}" data-lang="{lang}">
<div class="grain" aria-hidden="true"></div>
<div class="prog" id="prog" aria-hidden="true"></div>
<a class="skip" href="#main">{t['skip']}</a>'''


def loader(t, lang):
    letters = "".join(
        f'<span style="--i:{i}">{"&nbsp;" if c == " " else c}</span>'
        for i, c in enumerate(BRAND))
    steps = " · ".join(t["load_steps"])

    # Grains de farine qui retombent en fond. Valeurs figées (pas de random)
    # pour que le HTML soit identique à chaque génération.
    import random
    rnd = random.Random(7)
    dust = "".join(
        f'<i style="--x:{rnd.randint(2, 98)}%;--s:{rnd.choice([2, 3, 3, 4, 5])}px;'
        f'--d:{rnd.uniform(5.5, 11):.1f}s;--dl:{rnd.uniform(0, 8):.1f}s;'
        f'--dx:{rnd.randint(-40, 40)}px"></i>'
        for _ in range(26))

    return f'''
<template id="loaderTpl">
<div class="loader" id="loader" role="status" aria-label="{t['loading']}">
  <div class="loader__top"><span>{BRAND}</span><span>Var — 83</span></div>
  <div class="loader__dust" aria-hidden="true">{dust}</div>

  <div class="loader__c">
    <div class="loader__seal">
      <svg class="loader__ring" viewBox="0 0 100 100" aria-hidden="true">
        <circle class="ring-bg"/>
        <circle class="ring-fg" id="loaderRing"/>
      </svg>
      <img class="loader__logo" src="{logo_src('logo-clair-512', lang)}"
           alt="" width="512" height="518" decoding="async">
    </div>
    <span class="loader__name" aria-hidden="true">{letters}</span>
    <div class="loader__bar"><div class="loader__fill" id="loaderFill"></div></div>
    <div class="loader__meta">
      <span class="loader__step" id="loaderStep" data-steps="{steps}">{t['load_steps'][0]}</span>
      <span id="loaderPct">000</span>
    </div>
  </div>
  <div class="loader__f"><span>{t['load_where']}</span><span>{t['load_who']}</span></div>
</div>
</template>

<div class="curtain" id="curtain" aria-hidden="true">
  <div class="curtain__in">
    <span class="curtain__l">{t['loading']}</span>
    <span class="curtain__t" id="curtainTitle">{BRAND}</span>
    <span class="curtain__dots"><i></i><i></i><i></i></span>
  </div>
</div>'''


def header(t, lang, page):
    links = ""
    for pg, key in NAV_KEYS[:-1]:
        cur = ' aria-current="page"' if pg == page else ''
        label = t[key]
        links += (f'<a class="nav__link" href="{pg}.html"{cur}>'
                  f'<span class="nav__flip"><span>{label}</span>'
                  f'<span aria-hidden="true">{label}</span></span></a>')

    menu_links = "".join(
        f'<a class="menu__link" href="{pg}.html"><span>0{i+1}</span>{t[key]}</a>'
        for i, (pg, key) in enumerate(NAV_KEYS))

    return f'''
<header class="header" id="header">
  <div class="header__in">
    <a class="brand" href="index.html" aria-label="{BRAND}">
      <span class="brand__mark">
        <img class="brand__logo brand__logo--dark" src="{logo_src('logo-256', lang)}"
             alt="" width="256" height="259" decoding="async">
        <img class="brand__logo brand__logo--light" src="{logo_src('logo-clair-256', lang)}"
             alt="" width="256" height="259" decoding="async" aria-hidden="true">
      </span>
      <span>
        <span class="brand__name">{BRAND}</span>
        <span class="brand__sub">{t['brand_sub']}</span>
      </span>
    </a>
    <nav class="nav" aria-label="{t['menu_label']}">{links}</nav>
    <div class="header__side">
      {social(t)}
      {lang_switch(lang, page, t)}
      <a class="btn btn--sm" href="contact.html">{t['nav_order']}</a>
      <button class="burger" id="burger" type="button" aria-label="{t['menu_label']}"
              aria-expanded="false" aria-controls="menu"><span></span><span></span></button>
    </div>
  </div>
</header>

<nav class="menu" id="menu" aria-hidden="true" aria-label="{t['menu_label']}">
  <div class="menu__nav">{menu_links}</div>
  <div class="menu__foot">
    <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
    <a href="mailto:{EMAIL}">{EMAIL}</a>
    <div style="margin-top:1.2rem">{social(t)}</div>
    {lang_switch(lang, page, t, in_menu=True)}
  </div>
</nav>

<aside class="social-rail" id="socialRail" aria-label="{t['follow']}">{social(t)}</aside>'''


def upnext(t, label, title, href):
    return f'''
<a class="upnext" href="{href}">
  <div class="wrap upnext__in">
    <div><span class="tw upnext__l">{label}</span>
      <div class="upnext__t" style="margin-top:.7rem">{title}</div></div>
    <span class="upnext__ico">{ICON_ARROW}</span>
  </div>
</a>'''


def footer(t, lang):
    nav_links = "".join(f'<li class="footer__li"><a href="{pg}.html">{t[key]}</a></li>'
                        for pg, key in NAV_KEYS)
    return f'''
<footer class="footer">
  <div class="wrap">
    <div class="footer__grid">
      <div>
        <div class="h3" style="letter-spacing:-.03em">{BRAND}</div>
        <p class="body-lg" style="color:rgba(248,246,240,.62); margin-top:.9rem; max-width:34ch; font-size:.98rem">
          {t['f_tagline']}
        </p>
        <div class="follow" style="margin-top:1.6rem">
          <span class="follow__label">{t['follow']}</span>
          {social(t)}
        </div>
      </div>
      <div>
        <div class="footer__t">{t['f_nav']}</div>
        <ul>{nav_links}</ul>
      </div>
      <div>
        <div class="footer__t">{t['f_find']}</div>
        <ul>
          <li class="footer__li"><a href="{MAPS_MONTFERRAT}" target="_blank" rel="noopener noreferrer">{ADDR_MONTFERRAT_RUE}<br>{ADDR_MONTFERRAT_CP}</a></li>
          <li class="footer__li" style="margin-top:1rem"><a href="{MAPS_FIGANIERES}" target="_blank" rel="noopener noreferrer">{ADDR_FIGANIERES_RUE}<br>{ADDR_FIGANIERES_CP}</a></li>
        </ul>
      </div>
      <div>
        <div class="footer__t">{t['f_contact']}</div>
        <ul>
          <li class="footer__li"><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
          <li class="footer__li"><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li class="footer__li"><a href="{wa_link(t)}" target="_blank" rel="noopener noreferrer">WhatsApp</a></li>
          <li class="footer__li"><a href="{FACEBOOK}" target="_blank" rel="noopener">Facebook</a></li>
          <li class="footer__li"><a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__word" aria-hidden="true">Boulangerie</div>
    <div class="footer__bar">
      <span>© <span data-year>2026</span> {BRAND}</span>
      <span>{t['f_craft']}</span>
      <nav class="footer__legal" aria-label="{t['nav_legal']}">
        <a href="mentions.html">{t['nav_legal']}</a>
        <a href="cgv.html">{t['nav_cgv']}</a>
        <a href="confidentialite.html">{t['nav_privacy']}</a>
      </nav>
    </div>
  </div>
</footer>'''


def overlays(t, lang):
    js = ("<script>\n" + read("script.js") + "\n</script>") if INLINE \
        else f'<script src="{asset("script.js", lang)}"></script>'
    return f'''
<div class="lb" id="lb" role="dialog" aria-modal="true" aria-label="{t['gallery']}" aria-hidden="true">
  <div class="lb__bar">
    <span class="lb__cap" id="lbIdx">01 / 01</span>
    <button class="lb__btn" id="lbClose" type="button" aria-label="{t['close']}">
      <svg width="15" height="15" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M1 1l13 13M14 1L1 14"/></svg>
    </button>
  </div>
  <div class="lb__stage" id="lbStage"><div class="lb__box" id="lbBox"></div></div>
  <div class="lb__nav">
    <button class="lb__btn" id="lbPrev" type="button" aria-label="{t['prev']}">
      <svg width="15" height="15" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M9.5 1L3 7.5 9.5 14"/></svg>
    </button>
    <span class="lb__cap" id="lbCap"></span>
    <button class="lb__btn" id="lbNext" type="button" aria-label="{t['next']}">
      <svg width="15" height="15" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M5.5 1L12 7.5 5.5 14"/></svg>
    </button>
  </div>
</div>
<button class="totop" id="toTop" type="button" aria-label="{t['top']}">{ICON_UP}</button>
{js}
</body>
</html>'''


# ============================================================================
#  Contenu des pages
# ============================================================================
def page_home(t, lang):
    F = lambda *a, **k: frame(*a, lang=lang, **k)
    return f'''
<section class="hero">
  <div class="hero__bg" aria-hidden="true" data-para="6"></div>
  <div class="wrap hero__in">
    <div class="hero__grid">
      <div>
        <div class="eyebrow" data-entrance data-reveal="fade"><span class="tw">{t['h_eyebrow']}</span></div>
        <h1 class="display hero__title" data-entrance data-split="48">
          {t['h_title_1']} <em>{t['h_title_2']}</em>
        </h1>
        <div class="hero__foot">
          <p class="lead" data-entrance data-reveal style="--rd:120ms">{t['h_lead']}</p>
          <div class="hero__actions" data-entrance data-reveal style="--rd:220ms">
            <a class="btn" href="produits.html">{t['h_cta1']}</a>
            <a class="btn btn--ghost" href="boulangeries.html">{t['h_cta2']}</a>
          </div>
        </div>
      </div>
      <div class="hero__visual" data-entrance data-reveal="scale">
        {F(t['h_img_hero'], "3x4", mod="frame--r", img="hero-vitrine", eager=True)}
      </div>
    </div>
  </div>
  <div class="cue" aria-hidden="true">
    <span class="tw tw--mute">{t['scroll']}</span><span class="cue__line"></span>
  </div>
</section>

{marquee(t['mq_home'])}

<section class="section">
  <div class="wrap">
    <div class="head">
      <div class="head__aside"><div class="eyebrow"><span class="tw">{t['h_s1_eyebrow']}</span></div></div>
      <div>
        <h2 class="h2" data-split="42">{t['h_s1_title']}</h2>
        <p class="lead" data-reveal style="--rd:160ms; margin-top:1.4rem">{t['h_s1_lead']}</p>
      </div>
    </div>
    <div class="grid g-3" data-stagger="120">
      <div data-reveal>
        <div class="mask">{F(t['h_img_levain'], "4x5", tag=t['h_tag_sig'], img="pain-levain")}</div>
        <div style="display:flex; justify-content:space-between; align-items:baseline; gap:1rem; margin-top:1.1rem">
          <h3 class="h3">{t['h_c1_t']}</h3><span class="num">{t['h_c1_n']}</span>
        </div>
        <p class="card__d" style="margin-top:.5rem">{t['h_c1_d']}</p>
      </div>
      <div data-reveal>
        <div class="mask">{F(t['h_img_trad'], "4x5", img="tradition")}</div>
        <div style="display:flex; justify-content:space-between; align-items:baseline; gap:1rem; margin-top:1.1rem">
          <h3 class="h3">{t['h_c2_t']}</h3><span class="num">{t['h_c2_n']}</span>
        </div>
        <p class="card__d" style="margin-top:.5rem">{t['h_c2_d']}</p>
      </div>
      <div data-reveal>
        <div class="mask">{F(t['h_img_croissants'], "4x5", tag=t['h_tag_morning'], img="croissants")}</div>
        <div style="display:flex; justify-content:space-between; align-items:baseline; gap:1rem; margin-top:1.1rem">
          <h3 class="h3">{t['h_c3_t']}</h3><span class="num">{t['h_c3_n']}</span>
        </div>
        <p class="card__d" style="margin-top:.5rem">{t['h_c3_d']}</p>
      </div>
    </div>
    <div style="margin-top:clamp(2.4rem,5vw,3.6rem)" data-reveal>
      <a class="alink" href="produits.html">{t['h_all']} <span class="alink__ico">{ICON_ARROW}</span></a>
    </div>
  </div>
</section>

<section class="section section--ink">
  <div class="wrap">
    <div class="grid g-12" style="align-items:end">
      <div class="col-7">
        <div class="eyebrow"><span class="tw">{t['h_q_eyebrow']}</span></div>
        <blockquote class="quote__t" data-split="40">{t['h_quote']}</blockquote>
        <div class="quote__by" data-reveal style="--rd:200ms">
          <div class="tw tw--mute" style="color:var(--sage-soft)">{t['h_q_by']}</div>
        </div>
      </div>
      <div class="col-4 start-9" data-reveal="right" style="--rd:140ms">
        <div class="mask">{F(t['h_img_fournil'], "1x1", img="fournil-carre")}</div>
      </div>
    </div>
    <div class="stats" style="margin-top:clamp(3rem,7vw,5.5rem)" data-stagger="110">
      <div class="stat" data-reveal><div class="stat__v"><span data-count="36">0</span> h</div><div class="stat__l">{t['h_st1']}</div></div>
      <div class="stat" data-reveal><div class="stat__v"><span data-count="2">0</span></div><div class="stat__l">{t['h_st2']}</div></div>
      <div class="stat" data-reveal><div class="stat__v"><span data-count="3">0</span></div><div class="stat__l">{t['h_st3']}</div></div>
      <div class="stat" data-reveal><div class="stat__v"><span data-count="100" data-suffix="%">0</span></div><div class="stat__l">{t['h_st4']}</div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="feat">
      <div class="feat__media" data-reveal="left"><div class="mask">{F(t['h_img_faconnage'], "3x2", img="faconnage")}</div></div>
      <div class="feat__body">
        <div class="eyebrow"><span class="tw">{t['h_s2_eyebrow']}</span></div>
        <h2 class="h2" data-split="40">{t['h_s2_title_1']} <br>{t['h_s2_title_2']}</h2>
        <p class="body-lg" data-reveal style="--rd:160ms; margin-top:1.3rem">{t['h_s2_text']}</p>
        <div style="margin-top:2rem; --rd:240ms" data-reveal>
          <a class="alink" href="maison.html">{t['h_s2_link']} <span class="alink__ico">{ICON_ARROW}</span></a>
        </div>
      </div>
    </div>
    <div class="feat feat--flip">
      <div class="feat__media" data-reveal="right"><div class="mask">{F(t['h_img_devanture'], "3x2", img="devanture")}</div></div>
      <div class="feat__body">
        <div class="eyebrow"><span class="tw">{t['h_s3_eyebrow']}</span></div>
        <h2 class="h2" data-split="40">{t['h_s3_title_1']} <br>{t['h_s3_title_2']}</h2>
        <p class="body-lg" data-reveal style="--rd:160ms; margin-top:1.3rem">{t['h_s3_text']}</p>
        <div style="margin-top:2rem" data-reveal>
          <a class="alink" href="boulangeries.html">{t['h_s3_link']} <span class="alink__ico">{ICON_ARROW}</span></a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="head">
      <div class="head__aside"><div class="eyebrow"><span class="tw">{t['h_s4_eyebrow']}</span></div></div>
      <div><h2 class="h2" data-split="42">{t['h_s4_title']}</h2></div>
    </div>
    <div class="grid g-3" data-stagger="110">
      <article class="card" data-reveal><span class="card__n">/ 01</span><h3 class="card__t">{t['h_e1_t']}</h3><p class="card__d">{t['h_e1_d']}</p></article>
      <article class="card" data-reveal><span class="card__n">/ 02</span><h3 class="card__t">{t['h_e2_t']}</h3><p class="card__d">{t['h_e2_d']}</p></article>
      <article class="card" data-reveal><span class="card__n">/ 03</span><h3 class="card__t">{t['h_e3_t']}</h3><p class="card__d">{t['h_e3_d']}</p></article>
    </div>
  </div>
</section>'''


GAL_CATS = ["pains", "pains", "pains", "viennoiseries", "viennoiseries", "viennoiseries",
            "patisseries", "patisseries", "patisseries", "snacking", "snacking", "locaux"]
GAL_IMGS = ["pain-levain", "tradition", "pain-campagne",
            "croissants", "viennoiseries", "hero-vitrine",
            "patisseries", "buches-noel", "piece-montee",
            "snacking", "traiteur-buffet", "comptoir-vins"]


def page_produits(t, lang):
    F = lambda *a, **k: frame(*a, lang=lang, **k)
    rows = "".join(
        f'<div class="row" data-reveal><span class="row__n"><span>{i+1:02d}</span>'
        f'<span class="row__arw">&rarr;</span></span><span class="row__t">{n}</span>'
        f'<span class="row__d">{d}</span><span class="row__m">{m}</span></div>'
        for i, (n, d, m) in enumerate(t["p_rows"]))

    gal = "".join(
        f'<button class="gal__i" type="button" data-cat="{GAL_CATS[i]}" data-cap="{cap}" '
        f'data-reveal aria-label="{t["p_zoom"]} : {cap}">{F(cap, "1x1", img=GAL_IMGS[i])}</button>'
        for i, cap in enumerate(t["p_gal"]))

    return f'''
<section class="section" style="padding-top:calc(var(--header-h) + clamp(3rem,7vw,6rem))">
  <div class="wrap">
    <div class="eyebrow" data-entrance data-reveal="fade"><span class="tw">{t['p_eyebrow']}</span></div>
    <h1 class="h1" data-entrance data-split="45">{t['p_title_1']}<br>{t['p_title_2']}</h1>
    <p class="lead" data-entrance data-reveal style="--rd:180ms; margin-top:1.6rem">{t['p_lead']}</p>
  </div>
</section>

{marquee(t['mq_prod'], ink=True, speed=30)}

<section class="section">
  <div class="wrap">
    <div class="head">
      <div class="head__aside"><div class="eyebrow"><span class="tw">{t['p_s1_eyebrow']}</span></div></div>
      <div><h2 class="h2" data-split="40">{t['p_s1_title']}</h2></div>
    </div>
    <div class="rows" data-stagger="70">{rows}</div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="head">
      <div class="head__aside"><div class="eyebrow"><span class="tw">{t['p_s2_eyebrow']}</span></div></div>
      <div><h2 class="h2" data-split="40">{t['p_s2_title']}</h2></div>
    </div>
    <div class="grid g-2" style="gap:clamp(2rem,4vw,3.4rem)" data-stagger="130">
      <div data-reveal>
        <div class="mask">{F(t['p_img_vienn'], "3x2", img="viennoiseries")}</div>
        <h3 class="h3" style="margin-top:1.2rem">{t['p_cat1_t']}</h3>
        <p class="card__d" style="margin-top:.6rem">{t['p_cat1_d']}</p>
      </div>
      <div data-reveal>
        <div class="mask">{F(t['p_img_patis'], "3x2", img="patisseries")}</div>
        <h3 class="h3" style="margin-top:1.2rem">{t['p_cat2_t']}</h3>
        <p class="card__d" style="margin-top:.6rem">{t['p_cat2_d']}</p>
      </div>
      <div data-reveal>
        <div class="mask">{F(t['p_img_snack'], "3x2", img="traiteur-buffet")}</div>
        <h3 class="h3" style="margin-top:1.2rem">{t['p_cat3_t']}</h3>
        <p class="card__d" style="margin-top:.6rem">{t['p_cat3_d']}</p>
      </div>
      <div data-reveal>
        <div class="mask">{F(t['p_img_local'], "3x2", img="comptoir-vins")}</div>
        <h3 class="h3" style="margin-top:1.2rem">{t['p_cat4_t']}</h3>
        <p class="card__d" style="margin-top:.6rem">{t['p_cat4_d']}</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="head">
      <div class="head__aside"><div class="eyebrow"><span class="tw">{t['p_s3_eyebrow']}</span></div></div>
      <div>
        <h2 class="h2" data-split="40">{t['p_s3_title']}</h2>
        <p class="lead" data-reveal style="--rd:140ms; margin-top:1.2rem">{t['p_s3_lead']}</p>
      </div>
    </div>
    <div class="filters" style="margin-bottom:clamp(1.6rem,3vw,2.4rem)" data-reveal>
      <button class="pill" type="button" data-filter="all" aria-pressed="true">{t['p_f_all']}</button>
      <button class="pill" type="button" data-filter="pains" aria-pressed="false">{t['p_f_breads']}</button>
      <button class="pill" type="button" data-filter="viennoiseries" aria-pressed="false">{t['p_f_vienn']}</button>
      <button class="pill" type="button" data-filter="patisseries" aria-pressed="false">{t['p_f_patis']}</button>
      <button class="pill" type="button" data-filter="snacking" aria-pressed="false">{t['p_f_snack']}</button>
      <button class="pill" type="button" data-filter="locaux" aria-pressed="false">{t['p_f_local']}</button>
    </div>
    <div class="gal" id="gal" data-stagger="60">{gal}</div>
  </div>
</section>

<section class="section section--ink section--tight">
  <div class="wrap">
    <div class="grid g-12" style="align-items:center; row-gap:2rem">
      <div class="col-7">
        <h2 class="h2" data-split="40">{t['p_cta_title']}</h2>
        <p class="lead" data-reveal style="--rd:150ms; margin-top:1.2rem">{t['p_cta_lead']}</p>
      </div>
      <div class="col-4 start-9" data-reveal="right">
        <a class="btn btn--light btn--wide" href="contact.html">{t['p_cta_btn']}</a>
        <a class="btn btn--ghost btn--wide" style="margin-top:.7rem; color:var(--cream); border-color:rgba(248,246,240,.28)" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
        <div style="margin-top:1.4rem; display:flex; justify-content:center">{social(t)}</div>
      </div>
    </div>
  </div>
</section>'''


def page_maison(t, lang):
    F = lambda *a, **k: frame(*a, lang=lang, **k)
    rows = "".join(
        f'<div class="row" data-reveal><span class="row__n"><span>{i+1:02d}</span>'
        f'<span class="row__arw">&rarr;</span></span><span class="row__t">{n}</span>'
        f'<span class="row__d">{d}</span><span class="row__m">{m}</span></div>'
        for i, (n, d, m) in enumerate(t["m_rows"]))
    parts = ""
    for i, p in enumerate(t["m_partners"]):
        slug = PARTENAIRES_LOGOS[i] if i < len(PARTENAIRES_LOGOS) else ""
        src = partner_src(slug, lang) if slug else ""
        vignette = (f'<img class="part__logo" src="{src}" alt="" width="320" height="320" '
                    f'loading="lazy" decoding="async">') if src else ""
        parts += (f'<div class="part"><span class="part__n">/ {i+1:02d}</span>'
                  f'{vignette}<span class="part__t">{p}</span></div>')

    return f'''
<section class="section" style="padding-top:calc(var(--header-h) + clamp(3rem,7vw,6rem)); padding-bottom:clamp(2.5rem,5vw,4rem)">
  <div class="wrap">
    <div class="eyebrow" data-entrance data-reveal="fade"><span class="tw">{t['m_eyebrow']}</span></div>
    <h1 class="h1" data-entrance data-split="45">{t['m_title_1']}<br>{t['m_title_2']}</h1>
    <p class="lead" data-entrance data-reveal style="--rd:180ms; margin-top:1.6rem">{t['m_lead']}</p>
  </div>
</section>

<div class="wrap" data-reveal="scale">
  <div class="mask">{F(t['m_img_fournil'], "16x9", mod="frame--soft", img="fournil", eager=True)}</div>
</div>

{marquee(t['mq_maison'], speed=32)}

<section class="section">
  <div class="wrap">
    <div class="head">
      <div class="head__aside"><div class="eyebrow"><span class="tw">{t['m_s1_eyebrow']}</span></div></div>
      <div><h2 class="h2" data-split="40">{t['m_s1_title']}</h2></div>
    </div>
    <div class="rows" data-stagger="80">{rows}</div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="feat">
      <div class="feat__media" data-reveal="left"><div class="mask">{F(t['m_img_petrissage'], "4x5", img="pain-levain")}</div></div>
      <div class="feat__body">
        <div class="eyebrow"><span class="tw">{t['m_s2_eyebrow']}</span></div>
        <h2 class="h2" data-split="40">{t['m_s2_title_1']} <br>{t['m_s2_title_2']}</h2>
        <p class="body-lg" data-reveal style="--rd:160ms; margin-top:1.3rem">{t['m_s2_text']}</p>
        <div class="acc" style="margin-top:2.2rem" data-reveal>
          <div class="acc__i">
            <button class="acc__b" type="button" aria-expanded="false" aria-controls="a1">{t['m_a1_t']}<span class="acc__ico"></span></button>
            <div class="acc__p" id="a1"><div class="acc__c">{t['m_a1_d']}</div></div>
          </div>
          <div class="acc__i">
            <button class="acc__b" type="button" aria-expanded="false" aria-controls="a2">{t['m_a2_t']}<span class="acc__ico"></span></button>
            <div class="acc__p" id="a2"><div class="acc__c">{t['m_a2_d']}</div></div>
          </div>
          <div class="acc__i">
            <button class="acc__b" type="button" aria-expanded="false" aria-controls="a3">{t['m_a3_t']}<span class="acc__ico"></span></button>
            <div class="acc__p" id="a3"><div class="acc__c">{t['m_a3_d']}</div></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="head">
      <div class="head__aside"><div class="eyebrow"><span class="tw">{t['m_s3_eyebrow']}</span></div></div>
      <div>
        <h2 class="h2" data-split="40">{t['m_s3_title']}</h2>
        <p class="lead" data-reveal style="--rd:150ms; margin-top:1.2rem">{t['m_s3_lead']}</p>
      </div>
    </div>
    <div class="parts" data-reveal>{parts}</div>
  </div>
</section>

<section class="section section--ink section--tight">
  <div class="wrap wrap--narrow" style="text-align:center">
    <blockquote class="quote__t" data-split="40" style="max-width:26ch; margin-inline:auto">{t['m_quote']}</blockquote>
    <div class="tw" style="margin-top:2rem; color:var(--sage-soft)" data-reveal>{BRAND}</div>
    <div style="margin-top:1.8rem; display:flex; justify-content:center" data-reveal>{social(t)}</div>
  </div>
</section>'''


def page_boulangeries(t, lang):
    F = lambda *a, **k: frame(*a, lang=lang, **k)
    return f'''
<section class="section" style="padding-top:calc(var(--header-h) + clamp(3rem,7vw,6rem)); padding-bottom:clamp(2.5rem,5vw,4rem)">
  <div class="wrap">
    <div class="eyebrow" data-entrance data-reveal="fade"><span class="tw">{t['b_eyebrow']}</span></div>
    <h1 class="h1" data-entrance data-split="45">{t['b_title_1']}<br>{t['b_title_2']}</h1>
    <p class="lead" data-entrance data-reveal style="--rd:180ms; margin-top:1.6rem">{t['b_lead']}</p>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="grid g-2" style="gap:clamp(2.4rem,5vw,4rem)" data-stagger="140">
      <article class="loc" data-reveal>
        <div class="mask">{F(t['b_img_1'], "3x2", img="devanture", eager=True)}</div>
        <div class="loc__head" style="margin-top:1.6rem">
          <h2 class="h3">Montferrat</h2><span class="tw">{t['b_badge']}</span>
        </div>
        <div class="loc__list">
          <div class="loc__r"><span class="loc__k">{t['b_addr']}</span><span class="loc__v"><a class="alink" style="font-size:inherit" href="{MAPS_MONTFERRAT}" target="_blank" rel="noopener noreferrer">{ADDR_MONTFERRAT_RUE}<br>{ADDR_MONTFERRAT_CP}</a></span></div>
          <div class="loc__r"><span class="loc__k">{t['b_tue_sat']}</span><span class="loc__v">07:00 – 13:30 · 16:30 – 19:00</span></div>
          <div class="loc__r"><span class="loc__k">{t['b_sun']}</span><span class="loc__v">07:00 – 13:30 · 16:30 – 19:00</span></div>
          <div class="loc__r"><span class="loc__k">{t['b_mon']}</span><span class="loc__v" style="color:var(--ember)">{t['b_closed']}</span></div>
          <div class="loc__r"><span class="loc__k">{t['b_phone']}</span><span class="loc__v"><a class="alink" style="font-size:inherit" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></span></div>
        </div>
        <div style="display:flex; gap:.7rem; flex-wrap:wrap; margin-top:1.8rem">
          <a class="btn btn--sm" href="{ITINERAIRE_MONTFERRAT}" target="_blank" rel="noopener noreferrer">{t['b_route']}</a>
          <a class="btn btn--ghost btn--sm" href="contact.html">{t['b_contact']}</a>
        </div>
      </article>

      <article class="loc" data-reveal>
        <div class="mask">{F(t['b_img_2'], "3x2", img="boutique-comptoir", eager=True)}</div>
        <div class="loc__head" style="margin-top:1.6rem">
          <h2 class="h3">Figanières</h2><span class="tw">{t['b_badge']}</span>
        </div>
        <div class="loc__list">
          <div class="loc__r"><span class="loc__k">{t['b_addr']}</span><span class="loc__v"><a class="alink" style="font-size:inherit" href="{MAPS_FIGANIERES}" target="_blank" rel="noopener noreferrer">{ADDR_FIGANIERES_RUE}<br>{ADDR_FIGANIERES_CP}</a></span></div>
          <div class="loc__r"><span class="loc__k">{t['b_tue_sat']}</span><span class="loc__v">07:00 – 13:30 · 16:30 – 19:00</span></div>
          <div class="loc__r"><span class="loc__k">{t['b_sun']}</span><span class="loc__v">07:00 – 13:00</span></div>
          <div class="loc__r"><span class="loc__k">{t['b_mon']}</span><span class="loc__v" style="color:var(--ember)">{t['b_closed']}</span></div>
          <div class="loc__r"><span class="loc__k">{t['b_phone']}</span><span class="loc__v"><a class="alink" style="font-size:inherit" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></span></div>
        </div>
        <div style="display:flex; gap:.7rem; flex-wrap:wrap; margin-top:1.8rem">
          <a class="btn btn--sm" href="{ITINERAIRE_FIGANIERES}" target="_blank" rel="noopener noreferrer">{t['b_route']}</a>
          <a class="btn btn--ghost btn--sm" href="contact.html">{t['b_contact']}</a>
        </div>
      </article>
    </div>
    <p class="note" style="margin-top:2rem" data-reveal>{t['b_note']}{PHONE_DISPLAY}.</p>
  </div>
</section>

{marquee(t['mq_boul'], ink=True, speed=28)}

<section class="section">
  <div class="wrap">
    <div class="head">
      <div class="head__aside"><div class="eyebrow"><span class="tw">{t['b_s2_eyebrow']}</span></div></div>
      <div><h2 class="h2" data-split="40">{t['b_s2_title']}</h2></div>
    </div>
    <div class="grid g-3" data-stagger="110">
      <article class="card" data-reveal><span class="card__n">/ 01</span><h3 class="card__t">{t['b_k1_t']}</h3><p class="card__d">{t['b_k1_d']}</p></article>
      <article class="card" data-reveal><span class="card__n">/ 02</span><h3 class="card__t">{t['b_k2_t']}</h3><p class="card__d">{t['b_k2_d']}</p></article>
      <article class="card" data-reveal><span class="card__n">/ 03</span><h3 class="card__t">{t['b_k3_t']}</h3><p class="card__d">{t['b_k3_d']}</p></article>
    </div>
  </div>
</section>'''


def page_contact(t, lang):
    faq = ""
    for i, (q, a) in enumerate(t["c_faq"]):
        faq += (f'<div class="acc__i">'
                f'<button class="acc__b" type="button" aria-expanded="false" aria-controls="q{i+1}">'
                f'{q}<span class="acc__ico"></span></button>'
                f'<div class="acc__p" id="q{i+1}"><div class="acc__c">{a}</div></div></div>')

    return f'''
<section class="section" style="padding-top:calc(var(--header-h) + clamp(3rem,7vw,6rem)); padding-bottom:clamp(2.5rem,5vw,4rem)">
  <div class="wrap">
    <div class="eyebrow" data-entrance data-reveal="fade"><span class="tw">{t['c_eyebrow']}</span></div>
    <h1 class="h1" data-entrance data-split="45">{t['c_title_1']}<br>{t['c_title_2']}</h1>
    <p class="lead" data-entrance data-reveal style="--rd:180ms; margin-top:1.6rem">{t['c_lead']}</p>
  </div>
</section>

{marquee(t['mq_contact'], ink=True, speed=30)}

<section class="section" style="padding-top:clamp(3rem,6vw,5rem)">
  <div class="wrap">
    <div class="grid g-12" style="gap:clamp(2.5rem,5vw,4.5rem)">
      <div class="col-7" data-reveal>
        <div class="eyebrow"><span class="tw">{t['c_form']}</span></div>
        <form id="contactForm" novalidate
              data-err="{t['c_err']}" data-opening="{t['c_opening']}"
              data-subject="{t['c_subject']}" data-mail="{EMAIL}"
              data-lname="{t['c_qa_phone']}">
          <div class="field">
            <label class="field__l" for="f-nom">{t['c_name']}</label>
            <input class="field__i" id="f-nom" name="nom" type="text" autocomplete="name" placeholder="{t['c_name_ph']}" required>
            <span class="field__bar"></span>
          </div>
          <div class="field">
            <label class="field__l" for="f-tel">{t['c_tel']}</label>
            <input class="field__i" id="f-tel" name="tel" type="tel" autocomplete="tel" placeholder="{t['c_tel_ph']}">
            <span class="field__bar"></span>
          </div>
          <div class="field">
            <label class="field__l" for="f-msg">{t['c_msg']}</label>
            <textarea class="field__i" id="f-msg" name="message" rows="5" placeholder="{t['c_msg_ph']}" required></textarea>
            <span class="field__bar"></span>
          </div>
          <button class="btn" type="submit">{t['c_send']}</button>
          <p class="formmsg" id="formMsg" role="status"></p>
          <p class="note" style="margin-top:1.4rem">{t['c_note']}</p>
        </form>
      </div>

      <div class="col-4 start-9" data-reveal="right" style="--rd:140ms">
        <div class="eyebrow"><span class="tw">{t['c_direct']}</span></div>
        <div class="qa">
          <a class="qa__i" href="tel:{PHONE_TEL}">
            <span><span class="qa__k">{t['c_qa_phone']}</span><br><span class="qa__v">{PHONE_DISPLAY}</span></span>
            <span class="alink__ico">{ICON_ARROW}</span></a>
          <a class="qa__i" href="mailto:{EMAIL}">
            <span><span class="qa__k">{t['c_qa_mail']}</span><br><span class="qa__v">{EMAIL}</span></span>
            <span class="alink__ico">{ICON_ARROW}</span></a>
          <a class="qa__i" href="{FACEBOOK}" target="_blank" rel="noopener">
            <span><span class="qa__k">{t['c_qa_fb']}</span><br><span class="qa__v">CDboulangerie</span></span>
            <span class="alink__ico">{ICON_ARROW}</span></a>
          <a class="qa__i" href="{INSTAGRAM}" target="_blank" rel="noopener">
            <span><span class="qa__k">{t['c_qa_ig']}</span><br><span class="qa__v">@cdboulangerie</span></span>
            <span class="alink__ico">{ICON_ARROW}</span></a>
          <a class="qa__i" href="{wa_link(t)}" target="_blank" rel="noopener noreferrer">
            <span><span class="qa__k">{t['c_qa_wa']}</span><br><span class="qa__v">{PHONE_DISPLAY}</span></span>
            <span class="alink__ico">{ICON_ARROW}</span></a>
          <a class="qa__i" href="{ITINERAIRE_MONTFERRAT}" target="_blank" rel="noopener noreferrer">
            <span><span class="qa__k">{t['c_qa_route']}</span><br><span class="qa__v">Montferrat</span></span>
            <span class="alink__ico">{ICON_ARROW}</span></a>
          <a class="qa__i" href="{ITINERAIRE_FIGANIERES}" target="_blank" rel="noopener noreferrer">
            <span><span class="qa__k">{t['c_qa_route']}</span><br><span class="qa__v">Figanières</span></span>
            <span class="alink__ico">{ICON_ARROW}</span></a>
        </div>
        <div style="margin-top:2.4rem">
          <div class="tw tw--ink" style="margin-bottom:1rem">{t['c_hours']}</div>
          <div class="loc__list" style="border-top:1px solid var(--line)">
            <div class="loc__r"><span class="loc__k">{t['b_tue_sat']}</span><span class="loc__v">07:00 — 13:30 · 16:30 — 19:00</span></div>
            <div class="loc__r"><span class="loc__k">{t['b_sun']}</span><span class="loc__v">07:00 — 13:30</span></div>
            <div class="loc__r"><span class="loc__k">{t['b_mon']}</span><span class="loc__v" style="color:var(--ember)">{t['b_closed']}</span></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="head">
      <div class="head__aside"><div class="eyebrow"><span class="tw">{t['c_faq_eyebrow']}</span></div></div>
      <div><h2 class="h2" data-split="40">{t['c_faq_title']}</h2></div>
    </div>
    <div class="acc" data-reveal>{faq}</div>
  </div>
</section>'''


def page_evenements(t, lang):
    F = lambda *a, **k: frame(*a, lang=lang, **k)
    rows = "".join(
        f'<div class="row" data-reveal><span class="row__n"><span>{i+1:02d}</span>'
        f'<span class="row__arw">&rarr;</span></span><span class="row__t">{n}</span>'
        f'<span class="row__d">{d}</span><span class="row__m">{m}</span></div>'
        for i, (n, d, m) in enumerate(t["e_rows"]))

    return f'''
<section class="section" style="padding-top:calc(var(--header-h) + clamp(3rem,7vw,6rem)); padding-bottom:clamp(2.5rem,5vw,4rem)">
  <div class="wrap">
    <div class="eyebrow" data-entrance data-reveal="fade"><span class="tw">{t['e_eyebrow']}</span></div>
    <h1 class="h1" data-entrance data-split="45">{t['e_title_1']}<br>{t['e_title_2']}</h1>
    <p class="lead" data-entrance data-reveal style="--rd:180ms; margin-top:1.6rem">{t['e_lead']}</p>
  </div>
</section>

<div class="wrap" data-reveal="scale">
  <div class="mask">{F(t['e_img_hero'], "16x9", mod="frame--soft", img="boutique-salon", eager=True)}</div>
</div>

{marquee(t['mq_events'], speed=32)}

<!-- Calendrier -->
<section class="section">
  <div class="wrap">
    <div class="head">
      <div class="head__aside"><div class="eyebrow"><span class="tw">{t['e_s1_eyebrow']}</span></div></div>
      <div>
        <h2 class="h2" data-split="40">{t['e_s1_title']}</h2>
        <p class="lead" data-reveal style="--rd:150ms; margin-top:1.2rem">{t['e_s1_lead']}</p>
      </div>
    </div>
    <div class="rows" data-stagger="70">{rows}</div>
  </div>
</section>

<!-- Sur demande -->
<section class="section section--alt">
  <div class="wrap">
    <div class="feat">
      <div class="feat__media" data-reveal="left">
        <div class="mask">{F(t['e_img_buffet'], "3x2", img="traiteur-buffet")}</div>
      </div>
      <div class="feat__body">
        <div class="eyebrow"><span class="tw">{t['e_s2_eyebrow']}</span></div>
        <h2 class="h2" data-split="40">{t['e_s2_title_1']} <br>{t['e_s2_title_2']}</h2>
        <p class="body-lg" data-reveal style="--rd:160ms; margin-top:1.3rem">{t['e_s2_text']}</p>
        <div style="margin-top:2rem; --rd:240ms" data-reveal>
          <a class="alink" href="contact.html">{t['p_cta_btn']} <span class="alink__ico">{ICON_ARROW}</span></a>
        </div>
      </div>
    </div>

    <div class="grid g-3" style="margin-top:clamp(3rem,6vw,5rem)" data-stagger="110">
      <article class="card" data-reveal><span class="card__n">/ 01</span><h3 class="card__t">{t['e_c1_t']}</h3><p class="card__d">{t['e_c1_d']}</p></article>
      <article class="card" data-reveal><span class="card__n">/ 02</span><h3 class="card__t">{t['e_c2_t']}</h3><p class="card__d">{t['e_c2_d']}</p></article>
      <article class="card" data-reveal><span class="card__n">/ 03</span><h3 class="card__t">{t['e_c3_t']}</h3><p class="card__d">{t['e_c3_d']}</p></article>
    </div>
  </div>
</section>

<!-- Suivez-nous -->
<section class="section section--ink">
  <div class="wrap">
    <div class="grid g-12" style="align-items:center; row-gap:2.2rem">
      <div class="col-7">
        <div class="eyebrow"><span class="tw">{t['e_s3_eyebrow']}</span></div>
        <h2 class="h2" data-split="40">{t['e_s3_title']}</h2>
        <p class="lead" data-reveal style="--rd:150ms; margin-top:1.2rem">{t['e_s3_text']}</p>
        <p class="note" style="margin-top:1.6rem; color:var(--sage-soft)" data-reveal>{t['e_note']}</p>
      </div>
      <div class="col-4 start-9" data-reveal="right">
        <a class="btn btn--light btn--wide" href="{FACEBOOK}" target="_blank" rel="noopener noreferrer">{t['e_cta_fb']}</a>
        <a class="btn btn--ghost btn--wide" style="margin-top:.7rem; color:var(--cream); border-color:rgba(248,246,240,.28)"
           href="{INSTAGRAM}" target="_blank" rel="noopener noreferrer">{t['e_cta_ig']}</a>
        <a class="btn btn--ghost btn--wide" style="margin-top:.7rem; color:var(--cream); border-color:rgba(248,246,240,.28)"
           href="{wa_link(t)}" target="_blank" rel="noopener noreferrer">{t['e_cta_wa']}</a>
        <div style="margin-top:1.6rem; display:flex; justify-content:center">{social(t)}</div>
      </div>
    </div>
  </div>
</section>'''


# ------------------------------------------------------------ PAGES LEGALES ---
# Ces trois pages partagent la même mise en page : un titre, un chapô, puis une
# suite de sections numérotées. Elles sont volontairement sobres : on vient y
# chercher une information précise, pas une expérience.

def _bloc_defs(paires):
    """Liste de définitions (libellé / valeur) — pour l'éditeur et l'hébergeur."""
    out = ""
    for k, v in paires:
        out += (f'<div class="qa"><div class="qa__k">{k}</div>'
                f'<div class="qa__v">{v}</div></div>')
    return f'<div class="legal__defs">{out}</div>'


def _paras(txt):
    """Un texte peut contenir des sauts de ligne doubles : autant de paragraphes."""
    return "".join(f'<p class="legal__p">{p.strip()}</p>'
                   for p in txt.split("\n\n") if p.strip())


def _section(num, titre, corps, delai=0):
    return f'''
  <section class="legal__s" data-reveal style="--rd:{delai}ms">
    <div class="legal__num">{num:02d}</div>
    <div class="legal__body">
      <h2 class="h3 legal__t">{titre}</h2>
      {corps}
    </div>
  </section>'''


def _page_legale(t, lang, eyebrow, titre1, titre2, lead, sections, encart=None):
    """Ossature commune aux trois pages légales."""
    from datetime import date
    corps = ""
    for i, (titre, contenu) in enumerate(sections, start=1):
        corps += _section(i, titre, contenu, delai=min(i * 40, 240))

    bloc_encart = ""
    if encart:
        bloc_encart = f'''
  <div class="legal__hl" data-reveal>
    <div class="tw tw--ink">{encart[0]}</div>
    <p class="legal__hl-p">{encart[1]}</p>
  </div>'''

    return f'''
<section class="section" style="padding-top:calc(var(--header-h) + clamp(3rem,7vw,6rem)); padding-bottom:clamp(2rem,4vw,3rem)">
  <div class="wrap wrap--narrow">
    <div class="eyebrow" data-entrance data-reveal="fade"><span class="tw">{eyebrow}</span></div>
    <h1 class="h1" data-entrance data-split="45">{titre1}<br>{titre2}</h1>
    <p class="lead" data-entrance data-reveal style="--rd:180ms; margin-top:1.6rem">{lead}</p>
    <p class="legal__date" data-reveal style="--rd:240ms">{t['lg_updated']} : {date.today().strftime('%d/%m/%Y')}</p>
  </div>
</section>

<div class="section" style="padding-top:0; padding-bottom:var(--sec)">
  <div class="wrap wrap--narrow">
{bloc_encart}
    <div class="legal">{corps}</div>
  </div>
</div>'''


def page_mentions(t, lang):
    s = [
        (t['lg_s1_t'], _bloc_defs(t['lg_s1_b'])),
        (t['lg_s2_t'], _bloc_defs(t['lg_s2_b'])),
        (t['lg_s3_t'], _paras(t['lg_s3_p'])),
        (t['lg_s4_t'], _paras(t['lg_s4_p'])),
        (t['lg_s5_t'], _paras(t['lg_s5_p'])),
        (t['lg_s6_t'], _paras(t['lg_s6_p'])),
        (t['lg_s7_t'], _paras(t['lg_s7_p'])
            + f'''<div class="legal__links">
                 <a class="link" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
                 <a class="link" href="mailto:{EMAIL}">{EMAIL}</a>
               </div>'''),
    ]
    return _page_legale(t, lang, t['lg_eyebrow'], t['lg_title_1'], t['lg_title_2'],
                        t['lg_lead'], s)


def page_cgv(t, lang):
    s = [
        (t['cg_s1_t'], _paras(t['cg_s1_p'])),
        (t['cg_s2_t'], _paras(t['cg_s2_p'])),
        (t['cg_s3_t'], _paras(t['cg_s3_p'])),
        (t['cg_s4_t'], _paras(t['cg_s4_p'])),
        (t['cg_s5_t'], _paras(t['cg_s5_p']) + _bloc_defs(t['cg_s5_b'])),
        (t['cg_s6_t'], _paras(t['cg_s6_p'])),
        (t['cg_s7_t'], _paras(t['cg_s7_p'])),
        (t['cg_s8_t'], _paras(t['cg_s8_p'])),
        (t['cg_s9_t'], _paras(t['cg_s9_p'])),
        (t['cg_s10_t'], _paras(t['cg_s10_p'])),
        (t['cg_s11_t'], _paras(t['cg_s11_p'])),
        (t['cg_s12_t'], _paras(t['cg_s12_p'])),
    ]
    return _page_legale(t, lang, t['cg_eyebrow'], t['cg_title_1'], t['cg_title_2'],
                        t['cg_lead'], s, encart=(t['cg_intro_t'], t['cg_intro_p']))


def page_confidentialite(t, lang):
    s = [
        (t['pv_s1_t'], _paras(t['pv_s1_p'])),
        (t['pv_s2_t'], _bloc_defs(t['pv_s2_b'])),
        (t['pv_s3_t'], _paras(t['pv_s3_p'])),
        (t['pv_s4_t'], _paras(t['pv_s4_p'])),
        (t['pv_s5_t'], _paras(t['pv_s5_p'])),
        (t['pv_s6_t'], _paras(t['pv_s6_p'])),
        (t['pv_s7_t'], _paras(t['pv_s7_p'])),
    ]
    return _page_legale(t, lang, t['pv_eyebrow'], t['pv_title_1'], t['pv_title_2'],
                        t['pv_lead'], s, encart=(t['pv_hl_t'], t['pv_hl_p']))


BUILDERS = {
    "index": page_home,
    "produits": page_produits,
    "evenements": page_evenements,
    "maison": page_maison,
    "boulangeries": page_boulangeries,
    "contact": page_contact,
    "mentions": page_mentions,
    "cgv": page_cgv,
    "confidentialite": page_confidentialite,
}

NEXT = {
    "index": ("produits", "nav_products", "up_next"),
    "produits": ("evenements", "nav_events", "up_next"),
    "evenements": ("maison", "nav_house", "up_next"),
    "maison": ("boulangeries", "nav_bakeries", "up_next"),
    "boulangeries": ("contact", "nav_contact", "up_next"),
    "contact": ("index", "nav_home", "back"),
    # Les pages légales renvoient à l'accueil : ce sont des culs-de-sac
    # volontaires, on n'y enchaîne pas une visite.
    "mentions": ("index", "nav_home", "back"),
    "cgv": ("index", "nav_home", "back"),
    "confidentialite": ("index", "nav_home", "back"),
}


def build_page(lang, page, outdir):
    t = T[lang]
    nxt_page, nxt_key, nxt_label = NEXT[page]
    html = (head(t, lang, page)
            + loader(t, lang)
            + header(t, lang, page)
            + f'\n<main id="main">\n{BUILDERS[page](t, lang)}\n</main>\n'
            + upnext(t, t[nxt_label], t[nxt_key], f"{nxt_page}.html")
            + footer(t, lang)
            + overlays(t, lang))
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / f"{page}.html").write_text(html, encoding="utf-8")
    return len(html)


def write_seo_files():
    """sitemap.xml + robots.txt — indispensables pour le référencement."""
    from datetime import date
    today = date.today().isoformat()

    urls = ""
    for code, name, short, folder in LANGS:
        for pg in PAGES:
            alts = "".join(
                f'\n    <xhtml:link rel="alternate" hreflang="{c}" href="{abs_url(c, pg)}"/>'
                for c, n, s, f in LANGS)
            prio = "1.0" if pg == "index" else "0.8"
            urls += (f'  <url>\n    <loc>{abs_url(code, pg)}</loc>'
                     f'\n    <lastmod>{today}</lastmod>'
                     f'\n    <changefreq>monthly</changefreq>'
                     f'\n    <priority>{prio}</priority>{alts}\n  </url>\n')

    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
        '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + urls + '</urlset>\n', encoding="utf-8")

    (OUT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")


if __name__ == "__main__":
    problems = i18n_check()
    if problems:
        print("\n⚠ Problèmes de traduction :")
        for p in problems:
            print("   " + p)

    print("\nCD Boulangerie — build\n" + "-" * 40)
    total = 0
    for code, name, short, folder in LANGS:
        outdir = OUT if code == "fr" else OUT / folder
        sizes = [build_page(code, pg, outdir) for pg in PAGES]
        total += sum(sizes)
        loc = "/" if code == "fr" else f"/{folder}/"
        print(f"  ✓ {name:9} {loc:6} {len(PAGES)} pages   {sum(sizes)//1024} KB")
    write_seo_files()
    print("  ✓ sitemap.xml + robots.txt")
    print("-" * 40)
    print(f"  {len(LANGS) * len(PAGES)} pages · {total//1024} KB\nDone.\n")
