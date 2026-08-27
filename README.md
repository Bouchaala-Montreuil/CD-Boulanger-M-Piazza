# CD Boulangerie

Site vitrine statique de CD Boulangerie, disponible en français, anglais et polonais.

## Partager ou mettre en ligne

Le site prêt à être partagé et déployé se trouve dans [`website/`](website/).

- Pour un aperçu local :

  ```bash
  python3 -m http.server 4173 --directory website
  ```

  Puis ouvrir <http://localhost:4173>.

- Pour Netlify, Vercel ou un hébergeur FTP, utiliser `website/` comme dossier de publication.
- Le site ne nécessite ni serveur applicatif, ni base de données, ni installation de dépendances.

## Aperçu public depuis GitHub

Le fichier `index.html` à la racine redirige vers le site prêt à publier. Si GitHub Pages est activé sur la branche `arena/01a04401-cd-boulanger-m-piazza` avec le dossier `/ (root)`, le lien public sera :

<https://bouchaala-montreuil.github.io/CD-Boulanger-M-Piazza/>

## Organisation

```text
.
├── website/       Site généré, prêt à publier
├── source/        Générateur, textes, CSS/JS et médias source
├── docs/          Documents de remise et contrôles avant mise en ligne
└── README.md
```

Le dossier `source/` n'est pas nécessaire pour l'hébergement. Il est conservé pour les futures modifications et la régénération du site.

## Régénérer le site

Depuis le dossier `source/` :

```bash
python3 build-website.py
```

Pour remplacer des photos, modifier d'abord les fichiers dans `source/medias/`, puis lancer :

```bash
cd source
python3 traiter-medias.py
python3 traiter-logos-partenaires.py
python3 build-website.py
```

Pillow est nécessaire uniquement pour retraiter les images : `pip install Pillow`.

## Avant la mise en ligne

Les points listés dans [`docs/CLIENT-HANDOFF.md`](docs/CLIENT-HANDOFF.md) doivent être validés avec le client : coordonnées, horaires, mentions légales, réseaux sociaux et données d'avis.

Ne publier que `website/`. Les médias source, les scripts de génération et les notes de travail ne sont pas requis par l'hébergeur.
