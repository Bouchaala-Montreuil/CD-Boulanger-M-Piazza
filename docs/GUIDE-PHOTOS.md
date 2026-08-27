# Guide photo — CD Boulangerie

Comment prendre et remplacer les photos du site, avec un simple téléphone.

---

## 1. En une minute

1. Prenez la photo **avec votre téléphone tenu normalement** (pas de zoom).
2. Enregistrez-la dans le bon dossier de `source/medias/` en **gardant exactement
   le même nom de fichier** que la photo à remplacer.
3. Lancez ces deux commandes :

```bash
cd source
python3 traiter-medias.py
python3 build-website.py
```

C'est tout. Le recadrage, les couleurs, la compression et les 27 pages
du site se mettent à jour tout seuls.

> **Ne modifiez jamais les fichiers du dossier `source/images/`** : ils sont
> effacés et régénérés à chaque fois. Travaillez uniquement dans `source/medias/`.

---

## 2. Comment les dossiers sont rangés

```
source/medias/
├── 02-logo/               Logo + carte de visite
├── 03-boutique/           Façade, salon, comptoirs
├── 04-pains/              Pains, baguettes, ficelles
├── 05-viennoiseries/      Croissants, pains au chocolat
├── 06-patisseries/        Bûches, mignardises, pièces montées
├── 07-snacking-traiteur/  Plateaux, verrines, buffets
├── 08-fournil/            Four, fournées, coulisses
└── 09-partenaires/        Logos des partenaires (minoterie…)
```

Le fichier `source/traiter-medias.py` contient un tableau `CATALOGUE` qui dit
quelle photo va à quel endroit du site. Pour **changer l'emplacement**
d'une photo, il suffit d'y modifier une ligne :

```python
"croissants": ("croissants-vitrine.jpg", "portrait", "05-viennoiseries"),
#  ^ nom sur le site   ^ fichier source    ^ format    ^ dossier
```

---

## 3. Les formats — quelle orientation pour quoi

Le site utilise 5 cadrages. **Prenez la photo dans la bonne orientation** :
un recadrage automatique coupe forcément une partie de l'image.

| Format | Orientation | Où c'est utilisé | Tenez le téléphone… |
|---|---|---|---|
| `portrait_haut` | 3:4 debout | grande image d'accueil | **vertical** |
| `portrait` | 4:5 debout | cartes produits, galerie | **vertical** |
| `paysage` | 3:2 couché | blocs alternés | **horizontal** |
| `pano` | 16:9 très large | bandeau pleine largeur | **horizontal** |
| `carre` | 1:1 | galerie, citations | vertical ou horizontal |

**Règle simple :** dans le doute, prenez **verticale**. Une photo verticale
se recadre bien en carré et en portrait ; une photo horizontale ne peut
pas devenir verticale sans perdre la moitié du sujet.

---

## 4. Les bons angles, produit par produit

### 🥖 Les pains
- **De trois quarts, légèrement au-dessus** (environ 45°) — jamais à plat.
- Cherchez la **lumière rasante** : elle révèle la croûte, les grignes,
  la farine. Une lumière de face écrase tout.
- Approchez-vous : **remplissez le cadre** de deux ou trois pains, pas de vingt.
- Une **corbeille en osier ou une planche en bois** en fond fonctionne mieux
  qu'un inox brillant.

### 🥐 Les viennoiseries
- **Au niveau de l'étagère**, pas en plongée depuis le dessus.
- Photographiez **le matin**, quand la vitrine est pleine et le feuilletage brillant.
- Un ou deux croissants au premier plan, le reste flou derrière : c'est ce qui
  donne l'effet « photo de magazine ».

### 🍰 Les pâtisseries
- **En plongée légère** (30–45°) pour montrer le dessus décoré.
- Les vitrines réfléchissent : **placez-vous un peu de côté** pour éviter
  votre reflet et celui des néons.
- Nettoyez la vitre avant. Une trace de doigt se voit énormément en photo.

### 🏠 La boutique
- **Horizontal**, depuis la porte d'entrée ou un angle de la pièce.
- Cadrez de façon à **inclure le comptoir et un peu de plafond** : ça donne
  du volume.
- Éteignez le flash. Les lampes chaudes de la boutique suffisent.

### 🔥 Le fournil
- Ce sont les photos qui **racontent le métier** : les mains, la farine,
  le four ouvert, les fournées sur grille.
- Vertical de préférence.
- N'ayez pas peur du désordre : un fournil trop propre paraît faux.

### 🎂 Traiteur et pièces montées
- **Fond neutre** (nappe blanche, ardoise, planche) : le produit doit ressortir.
- Vertical pour les pièces montées, horizontal pour les plateaux.

---

## 5. Les 7 erreurs qui gâchent une photo

| ❌ À éviter | ✅ À faire |
|---|---|
| **Flash** | Lumière naturelle ou lampes de la boutique |
| **Zoom numérique** | Avancez physiquement |
| **Photo de loin** avec tout le magasin | Remplissez le cadre avec 2–3 produits |
| **Vitre sale ou reflets** | Nettoyez, décalez-vous de côté |
| **Contre-jour** (fenêtre derrière le produit) | Lumière de côté ou de trois quarts |
| **Photo penchée** | Activez la grille de l'appareil photo |
| **Mode portrait / filtres** | Photo normale : le site fait déjà les retouches |

---

## 6. Réglages du téléphone

**iPhone**
- Réglages → Appareil photo → **Formats → « Le plus compatible »**
  (sinon les photos sont en HEIC, que le script ne lit pas).
- Activez **Réglages → Appareil photo → Grille**.
- Appuyez sur le produit à l'écran pour faire la mise au point,
  puis glissez vers le bas si c'est trop clair.

**Android**
- Activez la **grille** et le format **JPEG** (pas RAW).
- Résolution maximale : **12 Mpx suffit largement**.
- Désactivez les modes « embellissement » et les filtres.

**Dans tous les cas**
- Essuyez l'objectif avec un chiffon — c'est la cause n°1 des photos floues.
- Prenez **3 ou 4 photos** du même produit sous des angles différents,
  vous choisirez après.

---

## 7. Tailles et poids

Vous n'avez **rien à calculer** : le script s'occupe de tout.

| | Photo d'origine | Après traitement |
|---|---|---|
| Dimensions | 3000 × 4000 px | 900 × 1125 px |
| Poids | 3 à 4 Mo | 60 à 250 Ko |

**Ce qui compte, c'est la photo de départ :**
- Minimum **1500 px** sur le petit côté (tout téléphone récent dépasse ça).
- Format **JPG** ou **PNG**. Pas de HEIC, pas de RAW.
- N'envoyez pas une photo déjà réduite reçue par WhatsApp : WhatsApp
  compresse énormément. **Utilisez le fichier original** ou envoyez-le
  « en tant que document ».

---

## 8. Ce que le script fait automatiquement

Les photos de vitrine sont très **jaunes et saturées** à cause des lampes.
Le site, lui, est crème et sobre. Le script rapproche les deux :

- refroidit légèrement (retire l'excès d'orange)
- calme la saturation (−14 %)
- éclaircit (+9 %)
- pose un voile crème très léger qui **unifie toute la série**
- renforce la netteté après redimensionnement
- exporte en `.webp` (2 à 3 fois plus léger qu'un JPG)

Pour ajuster l'intensité, ouvrez `source/traiter-medias.py` et modifiez le bloc
`AMBIANCE` en haut du fichier :

```python
AMBIANCE = {
    "temperature":  -0.055,  # plus négatif = plus froid
    "saturation":    0.86,   # 1.0 = couleurs d'origine
    "luminosite":    1.09,   # 1.0 = luminosité d'origine
    "contraste":     1.05,
    "nettete":       1.12,
    "voile_creme":   0.055,  # 0 = pas de voile
}
```

Certaines photos (fond blanc, plateaux traiteur) ne doivent pas être
retouchées : ajoutez leur nom dans `SANS_RETOUCHE`.

---

## 9. Ajouter une photo à un nouvel emplacement

1. Rangez la photo dans le bon dossier de `source/medias/`.
2. Ajoutez une ligne au `CATALOGUE` de `source/traiter-medias.py` :
   ```python
   "ma-nouvelle-photo": ("mon-fichier.jpg", "portrait", "04-pains"),
   ```
3. Utilisez-la dans `source/build.py` :
   ```python
   {F("Description de la photo", "4x5", img="ma-nouvelle-photo")}
   ```
4. Depuis la racine du projet : `cd source && python3 traiter-medias.py && python3 build-website.py`

> La **description** devient le texte alternatif : elle est lue par les
> personnes malvoyantes et par Google. Décrivez ce qu'on voit vraiment,
> en français, en quelques mots.

---

## 10. Le logo

Le logo est généré à toutes les tailles depuis `source/medias/02-logo/logo-cd.png`.

| Fichier | Usage |
|---|---|
| `logo-1024 / 512 / 256 / 128 / 64.png` | site, en-tête, réseaux |
| `logo-clair-*.png` | version pour fonds sombres (trait crème) |
| `favicon-16 / 32.png` | onglet du navigateur |
| `apple-touch-icon.png` | raccourci iPhone/iPad |
| `favicon.ico` | vieux navigateurs |

**Pour remplacer le logo :** déposez le nouveau fichier PNG **à fond
transparent** dans `source/medias/02-logo/logo-cd.png`, puis relancez
`cd source && python3 traiter-medias.py`. Toutes les tailles sont recalculées,
y compris la version claire pour les fonds sombres.

Le script **recadre automatiquement les marges vides** autour du logo :
inutile de le préparer, déposez-le tel quel.
