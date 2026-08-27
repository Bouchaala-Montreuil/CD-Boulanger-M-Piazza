# Source du site

Ce dossier contient les fichiers éditables et les médias originaux. Il n'est pas nécessaire pour publier le site : l'hébergeur doit utiliser le dossier `../website/`.

## Générer le site

Depuis ce dossier :

```bash
python3 build-website.py
```

Le script génère les 27 pages françaises, anglaises et polonaises dans `../website/` et y copie les feuilles de style, le JavaScript, les polices et les images optimisées.

## Mettre à jour les images

1. Remplacer ou ajouter les fichiers dans `medias/`.
2. Lancer `python3 traiter-medias.py`.
3. Si nécessaire, lancer `python3 traiter-logos-partenaires.py`.
4. Lancer `python3 build-website.py`.

Le site conserve les noms de fichiers de sortie utilisés par les pages HTML. Les fichiers de `images/` sont des fichiers générés : ils ne doivent pas être modifiés à la main.

Les notes de remise et les droits des logos sont dans `../docs/`.
