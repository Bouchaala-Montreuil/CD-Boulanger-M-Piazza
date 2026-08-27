#!/usr/bin/env python3
"""
CD Boulangerie — logos des partenaires.

    python3 traiter-logos-partenaires.py

Prépare les logos affichés dans la section « Ils travaillent avec nous ».

  • Les logos réels (blasons de mairie, EHPAD, La Bastide, Too Good To Go)
    sont détourés, normalisés à la même hauteur optique et exportés en PNG
    transparent.
  • Les partenaires sans logo (crèches, école, catégories génériques)
    reçoivent une pastille dessinée dans le style du site : monogramme
    sur fond crème, filet sauge.

Sources : medias/09-partenaires/sources/
Sortie   : images/partenaires/
"""
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    raise SystemExit("Pillow manquant :  pip install Pillow")

ROOT = Path(__file__).parent
SRC = ROOT / "medias" / "09-partenaires" / "sources"
OUT = ROOT / "images" / "partenaires"
OUT.mkdir(parents=True, exist_ok=True)

# Rendu final : carré, marge de sécurité incluse
BOX = 320          # côté de la vignette exportée
PAD = 26           # marge intérieure

CREME = (248, 246, 240)
INK = (28, 27, 25)
SAGE = (106, 109, 94)


# ---------------------------------------------------------------------------
#  Partenaires disposant d'un vrai logo
#     clé : (fichier source, hauteur optique visée en % de la boîte)
# ---------------------------------------------------------------------------
REELS = {
    "mairie-montferrat":    ("montferrat.svg",   0.86),
    "mairie-figanieres":    ("figanieres.svg",   0.86),
    "mairie-chateaudouble": ("chateaudouble.svg", 0.86),
    "ehpad-figanieres":     ("ehpad.png",        0.74),
    "restaurant-la-bastide":("labastide.png",    0.80),
    "too-good-to-go":       ("toogoodtogo.png",  0.70),
}

# ---------------------------------------------------------------------------
#  Partenaires sans logo : pastille dessinée
#     clé : (monogramme, sous-titre court)
# ---------------------------------------------------------------------------
DESSINES = {
    "creche-figanieres":  ("CF", "Crèche"),
    "creche-montferrat":  ("CM", "Crèche"),
    "ecole-montferrat":   ("EM", "École"),
    "associations":       ("AL", "Assoc."),
    "producteurs-var":    ("PV", "Var"),
    "brasseurs":          ("BP", "Bière"),
}


def charger(nom):
    """Ouvre un SVG (rasterisé) ou un PNG/JPG, en RGBA."""
    f = SRC / nom
    if not f.exists():
        return None
    if f.suffix.lower() == ".svg":
        try:
            import cairosvg, io
            png = cairosvg.svg2png(url=str(f), output_width=900)
            return Image.open(io.BytesIO(png)).convert("RGBA")
        except Exception as e:
            print(f"    ! SVG illisible ({e})")
            return None
    im = Image.open(f)
    if im.mode != "RGBA":
        # Un JPG/PNG opaque sur fond blanc : on rend le blanc transparent
        im = im.convert("RGBA")
        px = im.load()
        w, h = im.size
        for y in range(h):
            for x in range(w):
                r, g, b, a = px[x, y]
                if r > 242 and g > 242 and b > 242:
                    px[x, y] = (r, g, b, 0)
    return im


def detourer(im):
    """Retire les marges transparentes autour du contenu."""
    b = im.getbbox()
    return im.crop(b) if b else im


def poser(im, hauteur_visee):
    """Centre le logo dans une vignette carrée, à hauteur optique constante."""
    im = detourer(im)
    dispo = BOX - PAD * 2
    cible = int(dispo * hauteur_visee)
    # on ajuste sur la plus grande dimension pour ne jamais déborder
    ratio = min(cible / im.height, dispo / im.width)
    nw, nh = max(1, int(im.width * ratio)), max(1, int(im.height * ratio))
    im = im.resize((nw, nh), Image.LANCZOS)

    fond = Image.new("RGBA", (BOX, BOX), (0, 0, 0, 0))
    fond.paste(im, ((BOX - nw) // 2, (BOX - nh) // 2), im)
    return fond


def police(taille):
    for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        if Path(p).exists():
            try:
                return ImageFont.truetype(p, taille)
            except Exception:
                pass
    return ImageFont.load_default()


def pastille(mono, sous_titre):
    """Vignette dessinée pour les partenaires sans logo, au style du site."""
    S = 4                                   # sur-échantillonnage
    im = Image.new("RGBA", (BOX * S, BOX * S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)

    m = PAD * S
    d.ellipse([m, m, BOX * S - m, BOX * S - m],
              outline=SAGE + (150,), width=3 * S)

    f1 = police(int(74 * S * 0.9))
    bb = d.textbbox((0, 0), mono, font=f1)
    d.text(((BOX * S - (bb[2] - bb[0])) / 2 - bb[0],
            BOX * S * 0.34 - bb[1]), mono, font=f1, fill=INK + (255,))

    f2 = police(int(26 * S * 0.9))
    bb2 = d.textbbox((0, 0), sous_titre, font=f2)
    d.text(((BOX * S - (bb2[2] - bb2[0])) / 2 - bb2[0],
            BOX * S * 0.62 - bb2[1]), sous_titre, font=f2, fill=SAGE + (255,))

    return im.resize((BOX, BOX), Image.LANCZOS)


def main():
    print("\nCD Boulangerie — logos partenaires")
    print("=" * 58)
    total = 0

    print("\n  Logos réels")
    for nom, (fichier, h) in REELS.items():
        im = charger(fichier)
        if im is None:
            print(f"    ! {nom:24} source absente ({fichier})")
            continue
        v = poser(im, h)
        f = OUT / f"{nom}.png"
        v.save(f, "PNG", optimize=True)
        total += f.stat().st_size
        print(f"    ✓ {nom:24} {f.stat().st_size // 1024:3} Ko")

    print("\n  Pastilles dessinées (pas de logo existant)")
    for nom, (mono, st) in DESSINES.items():
        v = pastille(mono, st)
        f = OUT / f"{nom}.png"
        v.save(f, "PNG", optimize=True)
        total += f.stat().st_size
        print(f"    ✓ {nom:24} {f.stat().st_size // 1024:3} Ko   [{mono}]")

    print("=" * 58)
    print(f"  {len(REELS) + len(DESSINES)} vignettes · {total // 1024} Ko\n")
    print("Lancez ensuite :  python3 build-website.py\n")


if __name__ == "__main__":
    main()
