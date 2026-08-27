# Remise client — CD Boulangerie

## Ce qui est livré

- Site vitrine statique en français, anglais et polonais
- Pages Accueil, Produits, Événements, La Maison, Nos boulangeries et Contact
- Pages légales : Mentions légales, Conditions générales et Confidentialité
- Galerie, menu mobile, liens téléphone, e-mail, WhatsApp et Google Maps
- Images optimisées, polices hébergées localement et fichiers SEO

## Où voir le site

Le site prêt à partager se trouve dans le dossier [`../website/`](../website/).

Pour le tester sur un ordinateur :

```bash
python3 -m http.server 4173 --directory website
```

Puis ouvrir <http://localhost:4173>.

## Mise en ligne

Utiliser **uniquement le contenu du dossier `website/`** comme dossier de publication chez Netlify, Vercel, OVH, Ionos ou un autre hébergeur statique.

Le dossier `source/` contient les fichiers de travail et les médias originaux. Il ne doit pas être configuré comme dossier public.

## Validation indispensable avant la mise en ligne

Les éléments suivants doivent être confirmés par le client :

- [ ] Nom de domaine exact et hébergeur choisi
- [ ] Adresse e-mail de contact : `contact@cdboulangerie.fr`
- [ ] Numéro utilisé par WhatsApp — le site utilise actuellement le numéro fixe
- [ ] Nom exact du compte Instagram, ou décision de supprimer le lien
- [ ] Horaires des deux boutiques, notamment le dimanche après-midi à Montferrat
- [ ] Si une note Google doit être affichée plus tard, fournir la note et le nombre d'avis réels
- [ ] Capital social, numéro de TVA et directeur de publication
- [ ] Nom, adresse et téléphone de l'hébergeur dans les mentions légales
- [ ] Autorisation d'utiliser les logos des partenaires et des communes
- [ ] Dates et événements annoncés
- [ ] Relecture des traductions anglaise et polonaise

## Fonctionnement du formulaire

Le formulaire ouvre le logiciel de messagerie du visiteur avec un message prérempli. Il ne stocke pas les données sur le site, mais il peut ne pas fonctionner si aucun logiciel de messagerie n'est configuré sur l'appareil.

Pour recevoir les demandes directement depuis un formulaire web, remplacer ce fonctionnement par un service de formulaire ou un backend avant la mise en ligne.

## Mise à jour du site

Les textes peuvent être modifiés directement dans les pages HTML de `website/`.

Pour modifier les textes de façon centralisée et régénérer toutes les langues, utiliser les fichiers de `source/`, puis lancer :

```bash
cd source
python3 build-website.py
```

Les consignes de remplacement des photos sont dans [`GUIDE-PHOTOS.md`](GUIDE-PHOTOS.md). Les sources et les droits des logos sont détaillés dans [`ASSET-SOURCES.md`](ASSET-SOURCES.md).
