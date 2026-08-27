#!/usr/bin/env python3
"""
CD Boulangerie — chaîne de traitement des photos.

    python3 traiter-medias.py

Ce script prend les photos brutes rangées dans medias/ et produit les
fichiers utilisés par le site (dossier images/).

Ce qu'il fait, dans l'ordre :
  1. recadre au bon format selon l'emplacement (portrait, paysage, carré…)
  2. harmonise l'ambiance : les photos de téléphone sont très chaudes et
     saturées (lumière tungstène des vitrines), le site est crème et sobre.
     On refroidit légèrement, on calme la saturation et on éclaircit.
  3. exporte en .webp haute qualité       -> images/
  4. exporte une version allégée          -> images/inline/
  5. produit le logo à toutes les tailles -> images/logo/

Nécessite Pillow :  pip install Pillow
"""
from pathlib import Path
import sys

try:
    from PIL import Image, ImageEnhance, ImageOps, ImageFilter
except ImportError:
    raise SystemExit("Pillow manquant.  Installez-le :  pip install Pillow")

ROOT = Path(__file__).parent
MEDIAS = ROOT / "medias"
OUT = ROOT / "images"
OUT_INLINE = OUT / "inline"
OUT_LOGO = OUT / "logo"

for d in (OUT, OUT_INLINE, OUT_LOGO):
    d.mkdir(parents=True, exist_ok=True)


# ===========================================================================
#  RÉGLAGES D'AMBIANCE
#  Les photos prises au téléphone dans la boutique sont très chaudes
#  (lampes jaunes) et saturées. Le site est crème, sobre, éditorial.
#  Ces réglages rapprochent les deux sans dénaturer le pain.
# ===========================================================================
AMBIANCE = {
    "temperature":  -0.055,  # < 0 = refroidit (retire le jaune/orange)
    "saturation":    0.86,   # < 1 = calme les couleurs
    "luminosite":    1.09,   # > 1 = éclaircit
    "contraste":     1.05,   # léger galbe
    "nettete":       1.12,   # compense le redimensionnement
    "voile_creme":   0.055,  # voile crème très léger, unifie la série
}

CREME = (248, 246, 240)   # --cream du site

# Formats d'affichage réels sur le site (x2 pour les écrans Retina)
FORMATS = {
    "portrait":     (900, 1125),   # 4:5  — cartes produits
    "portrait_haut": (820, 1100),  # 3:4  — visuel du héros
    "paysage":      (1200, 800),   # 3:2  — blocs alternés
    "pano":         (1500, 845),   # 16:9 — bandeau large
    "carre":        (1100, 1100),  # 1:1  — galerie, citation
}


# ===========================================================================
#  CATALOGUE — quelle photo va où
#  Modifier ce tableau suffit à changer une image du site.
#     nom de sortie : (fichier source, format, dossier de rangement)
# ===========================================================================
CATALOGUE = {
    # --- Boutique / façade -------------------------------------------------
    "devanture":         ("facade-rue.jpg",                  "paysage",       "03-boutique"),
    "boutique-salon":    ("salon-mur-ble.jpg",               "paysage",       "03-boutique"),
    "boutique-comptoir": ("salon-comptoir.jpg",              "paysage",       "03-boutique"),
    "comptoir-vitrine":  ("comptoir-vitrine.jpg",            "paysage",       "03-boutique"),
    "comptoir-vins":     ("comptoir-pains-vins.jpg",         "paysage",       "03-boutique"),
    "vitrine-salee":     ("vitrine-salee.jpg",               "portrait",      "03-boutique"),

    # --- Pains -------------------------------------------------------------
    "hero-vitrine":      ("pains-speciaux-panier.jpg",       "portrait_haut", "04-pains"),
    "pain-levain":       ("pains-grille-refroidissement.jpg","portrait",      "04-pains"),
    "tradition":         ("baguettes-casier.jpg",            "portrait",      "04-pains"),
    "pain-campagne":     ("pain-campagne-panier.jpg",        "paysage",       "04-pains"),
    "pains-speciaux":    ("pains-speciaux-panier.jpg",       "portrait",      "04-pains"),
    "ficelles":          ("ficelles-apero.jpg",              "paysage",       "04-pains"),

    # --- Viennoiseries -----------------------------------------------------
    "croissants":        ("croissants-vitrine.jpg",          "portrait",      "05-viennoiseries"),
    "viennoiseries":     ("viennoiseries-etages.jpg",        "portrait",      "05-viennoiseries"),

    # --- Pâtisseries -------------------------------------------------------
    "patisseries":       ("mignardises-vitrine.jpg",         "portrait",      "06-patisseries"),
    "buches-noel":       ("buches-noel-vitrine.jpg",         "paysage",       "06-patisseries"),
    "piece-montee":      ("piece-montee-mariage.jpg",        "portrait",      "06-patisseries"),

    # --- Snacking / traiteur ----------------------------------------------
    "snacking":          ("comptoir-pains-vins.jpg",         "paysage",       "03-boutique"),
    "traiteur-buffet":   ("plateau-mini-sandwichs.jpg",      "paysage",       "07-snacking-traiteur"),
    "traiteur-verrines": ("verrines-traiteur.jpg",           "portrait",      "07-snacking-traiteur"),

    # --- Fournil -----------------------------------------------------------
    "fournil":           ("four-fournees.jpg",               "pano",          "08-fournil"),
    "faconnage":         ("four-fournees.jpg",               "portrait",      "08-fournil"),
    "produits-locaux":   ("comptoir-vitrine.jpg",            "paysage",       "03-boutique"),
}

# Photos utilisées pour la citation carrée / la galerie
CARRE = ["pain-levain", "croissants", "patisseries", "fournil"]

# Ces images gardent leurs couleurs d'origine (produits blancs sur fond neutre)
SANS_RETOUCHE = {"traiteur-buffet"}


# ===========================================================================
def refroidir(im, force):
    """Retire la dominante jaune/orange des lampes de vitrine."""
    if force == 0:
        return im
    r, g, b = im.split()
    r = r.point(lambda v: max(0, min(255, int(v * (1 + force)))))
    b = b.point(lambda v: max(0, min(255, int(v * (1 - force * 1.25)))))
    return Image.merge("RGB", (r, g, b))


def voile(im, force, couleur=CREME):
    """Pose un voile crème très léger : unifie toute la série."""
    if force <= 0:
        return im
    calque = Image.new("RGB", im.size, couleur)
    return Image.blend(im, calque, force)


def harmoniser(im, retoucher=True):
    """Applique l'ambiance du site à une photo."""
    im = im.convert("RGB")
    if not retoucher:
        return im
    a = AMBIANCE
    im = refroidir(im, a["temperature"])
    im = ImageEnhance.Color(im).enhance(a["saturation"])
    im = ImageEnhance.Brightness(im).enhance(a["luminosite"])
    im = ImageEnhance.Contrast(im).enhance(a["contraste"])
    im = voile(im, a["voile_creme"])
    return im


def recadrer(im, tw, th):
    """Recadre au centre pour remplir exactement tw x th, sans déformer."""
    w, h = im.size
    cible, actuel = tw / th, w / h
    if actuel > cible:
        nw = int(h * cible)
        im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
    else:
        nh = int(w / cible)
        # cadrage légèrement haut : le sujet est rarement au centre bas
        haut = int((h - nh) * 0.42)
        im = im.crop((0, haut, w, haut + nh))
    return im.resize((tw, th), Image.LANCZOS)


def exporter(im, nom, tw, th, retoucher=True):
    """Produit la version haute qualité + la version allégée."""
    src = harmoniser(im, retoucher)
    grand = recadrer(src.copy(), tw, th)
    grand = ImageEnhance.Sharpness(grand).enhance(AMBIANCE["nettete"])
    f1 = OUT / f"{nom}.webp"
    grand.save(f1, "WEBP", quality=78, method=6)

    m = 720 / max(tw, th)
    iw, ih = (round(tw * m), round(th * m)) if m < 1 else (tw, th)
    petit = recadrer(src.copy(), iw, ih)
    petit = ImageEnhance.Sharpness(petit).enhance(AMBIANCE["nettete"])
    f2 = OUT_INLINE / f"{nom}.webp"
    petit.save(f2, "WEBP", quality=62, method=6)
    return f1.stat().st_size, f2.stat().st_size


# ===========================================================================
#  LOGO
# ===========================================================================
def traiter_logo():
    """Découpe les marges vides et exporte toutes les tailles utiles."""
    src = MEDIAS / "02-logo" / "logo-cd.png"
    if not src.exists():
        src = MEDIAS / "01-originaux" / "cdlogotransparent.png"
    if not src.exists():
        print("  ! logo introuvable")
        return

    im = Image.open(src).convert("RGBA")
    bbox = im.getbbox()          # retire les marges transparentes
    if bbox:
        im = im.crop(bbox)

    total = 0
    # PNG transparents, pour un usage sur fond clair ou foncé
    for taille in (1024, 512, 256, 128, 64):
        c = im.copy()
        c.thumbnail((taille, taille), Image.LANCZOS)
        f = OUT_LOGO / f"logo-{taille}.png"
        c.save(f, "PNG", optimize=True)
        total += f.stat().st_size

    # Favicons
    for taille, nom in ((32, "favicon-32.png"), (16, "favicon-16.png"),
                        (180, "apple-touch-icon.png")):
        c = im.copy()
        c.thumbnail((taille, taille), Image.LANCZOS)
        if nom == "apple-touch-icon.png":
            # iOS n'aime pas la transparence : fond crème
            fond = Image.new("RGBA", (taille, taille), (248, 246, 240, 255))
            fond.paste(c, ((taille - c.width) // 2, (taille - c.height) // 2), c)
            c = fond.convert("RGB")
        f = OUT_LOGO / nom
        c.save(f, "PNG", optimize=True)
        total += f.stat().st_size

    # favicon.ico multi-tailles
    ico = im.copy()
    ico.thumbnail((64, 64), Image.LANCZOS)
    ico.save(ROOT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])

    print(f"  ✓ logo : {len(list(OUT_LOGO.glob('*')))} fichiers · {total // 1024} Ko"
          f"  (source {im.width}x{im.height})")


def traiter_logo_partenaire():
    """Logo du meunier partenaire (Minoterie du Trièves)."""
    src = MEDIAS / "09-partenaires" / "minoterie-du-trieves.png"
    if not src.exists():
        src = MEDIAS / "01-originaux" / "logo-minoterie-vectoriel-MARRON-1.png"
    if not src.exists():
        return
    im = Image.open(src).convert("RGBA")
    b = im.getbbox()
    if b:
        im = im.crop(b)
    im.thumbnail((360, 360), Image.LANCZOS)
    f = OUT_LOGO / "partenaire-minoterie.png"
    im.save(f, "PNG", optimize=True)
    print(f"  ✓ logo partenaire : {f.stat().st_size // 1024} Ko")


# ===========================================================================
def main():
    if not MEDIAS.exists():
        raise SystemExit("Dossier medias/ introuvable.")

    print("\nCD Boulangerie — traitement des médias")
    print("=" * 62)

    gros = petit = 0
    faits, manquants = 0, []

    for nom, (fichier, fmt, dossier) in CATALOGUE.items():
        src = MEDIAS / dossier / fichier
        if not src.exists():
            src = MEDIAS / "01-originaux" / fichier
        if not src.exists():
            manquants.append(f"{nom} ({fichier})")
            continue

        tw, th = FORMATS[fmt]
        try:
            im = Image.open(src)
            im = ImageOps.exif_transpose(im)     # respecte l'orientation EXIF
        except Exception as e:
            manquants.append(f"{nom} — illisible ({e})")
            continue

        a, b = exporter(im, nom, tw, th, retoucher=(nom not in SANS_RETOUCHE))
        gros += a; petit += b; faits += 1
        print(f"  ✓ {nom:20} {fmt:14} {tw}x{th:<5} {a // 1024:4} Ko")

    # versions carrées pour la galerie
    for nom in CARRE:
        entry = CATALOGUE.get(nom)
        if not entry:
            continue
        fichier, _, dossier = entry
        src = MEDIAS / dossier / fichier
        if not src.exists():
            src = MEDIAS / "01-originaux" / fichier
        if not src.exists():
            continue
        im = ImageOps.exif_transpose(Image.open(src))
        tw, th = FORMATS["carre"]
        a, b = exporter(im, f"{nom}-carre", tw, th)
        gros += a; petit += b; faits += 1
        print(f"  ✓ {nom + '-carre':20} {'carre':14} {tw}x{th:<5} {a // 1024:4} Ko")

    print("-" * 62)
    traiter_logo()
    traiter_logo_partenaire()

    # image de partage (Open Graph 1200x630)
    dev = OUT / "devanture.webp"
    if dev.exists():
        og = Image.open(dev).convert("RGB")
        og = recadrer(og, 1200, 630)
        og.save(OUT / "og-cover.jpg", "JPEG", quality=76,
                optimize=True, progressive=True)
        print(f"  ✓ og-cover.jpg : {(OUT / 'og-cover.jpg').stat().st_size // 1024} Ko")

    print("=" * 62)
    print(f"  {faits} photos · site {gros // 1024} Ko · intégré {petit // 1024} Ko")
    if manquants:
        print("\n  ⚠ introuvables :")
        for m in manquants:
            print("     -", m)
    print("\nLancez ensuite :  python3 build-website.py\n")


if __name__ == "__main__":
    main()
