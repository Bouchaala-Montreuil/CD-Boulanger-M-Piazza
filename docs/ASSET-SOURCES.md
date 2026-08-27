# Logos des partenaires — origine et droits

Section « Ils travaillent avec nous » de la page **La Maison**.

---

## Logos réels trouvés (6)

| Partenaire | Source | Licence / statut |
|---|---|---|
| Mairie de Montferrat | Wikimedia Commons — blason officiel | **CC BY-SA 4.0** |
| Mairie de Figanières | Wikimedia Commons — blason officiel | **CC BY-SA 3.0** |
| Mairie de Châteaudouble | Wikimedia Commons — blason officiel | **CC BY-SA 3.0** |
| EHPAD de Figanières | ehpad-lepredelaroque.fr (site officiel) | logo de l'établissement |
| Restaurant La Bastide | labastide83.com (site officiel) | logo de l'établissement |
| Too Good To Go | toogoodtogo.com — **pack presse officiel** | usage presse autorisé |

Les fichiers d'origine sont conservés dans `../source/medias/09-partenaires/sources/`.

### ⚠️ Point juridique à régler avant la mise en ligne

Les **blasons municipaux** viennent de Wikimedia sous licence CC BY-SA :
leur réutilisation est libre, mais ces licences demandent en principe de
**créditer l'auteur**. En pratique, pour trois petits blasons dans une
grille de partenaires, personne ne le fait — mais si vous voulez être
irréprochable, ajoutez une ligne en pied de page ou dans les mentions
légales :

> Blasons des communes : Wikimedia Commons, CC BY-SA.

Plus important : **afficher le logo d'un partenaire suppose son accord.**
Un blason municipal ou le logo d'un restaurant ne s'utilisent pas librement
à des fins commerciales, même si le fichier est techniquement accessible.

**Recommandation :** demandez un accord écrit (un simple e-mail suffit) à
chacune des six structures. C'est rapide, et cela protège la boulangerie.
Le logo **Too Good To Go** est le seul dont l'usage est explicitement
prévu par la marque via son pack presse.

---

## Partenaires sans logo (6)

Ces entités **n'ont aucun logo** — vérifié, ce n'est pas un oubli :

| Partenaire | Pourquoi |
|---|---|
| Crèche de Figanières | structure municipale, pas d'identité propre |
| Crèche de Montferrat | structure municipale, pas d'identité propre |
| École de Montferrat | école publique (Éducation nationale) |
| Associations locales | **catégorie générique**, pas une entité |
| Producteurs du Var | **catégorie générique**, pas une entité |
| Brasseurs partenaires | **catégorie générique**, pas une entité |

Plutôt que de laisser six cases vides, elles reçoivent une **pastille
dessinée** dans le style du site : monogramme sur cercle sauge.
La grille reste homogène.

**Si le client obtient un vrai logo** (par exemple le nom du brasseur
partenaire), voir la marche à suivre plus bas.

---

## Remplacer ou ajouter un logo

1. Déposez le fichier dans `../source/medias/09-partenaires/sources/`
   (PNG transparent de préférence, ou SVG).
2. Ouvrez `../source/traiter-logos-partenaires.py` et déclarez-le dans `REELS` :

   ```python
   REELS = {
       "brasseurs": ("mon-brasseur.png", 0.78),
       #  ^ nom de sortie   ^ fichier      ^ hauteur optique (0.7 à 0.9)
   }
   ```
3. Retirez la même clé du dictionnaire `DESSINES` juste en dessous.
4. Relancez :

   ```bash
   cd source
   python3 traiter-logos-partenaires.py
   python3 build-website.py
   ```

Le script détoure automatiquement les marges vides, normalise la taille
et rend le blanc transparent sur les JPEG.

### Changer l'ordre ou les noms

L'ordre des vignettes suit la liste `PARTENAIRES_LOGOS` dans `../source/build.py`,
qui doit correspondre **ligne pour ligne** à `m_partners` dans `../source/i18n.py`
(les 3 langues). Si vous ajoutez un partenaire, pensez aux deux fichiers.

---

## Rendu

Les blasons sont colorés, le site est sobre : ils sont **légèrement
désaturés au repos** et reprennent toute leur couleur au survol, quand
la tuile passe au noir. C'est ce qui permet de mélanger des blasons
héraldiques rouges et or avec un design crème sans que ça jure.
