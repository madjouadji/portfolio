# Site personnel — Adji Madjou

Site statique généré en Python (Jinja2) : cinq pages — accueil, recherche, exposés, enseignement, CV.

## Modifier le contenu

Tout le texte est dans `contenu.py` (présentation, cours, recherche, parcours, exposés, distinctions).
Les gabarits HTML sont dans `templates/`, le style dans `ressources/styles.css`,
la photo dans `ressources/assets/portrait.jpg`, les CV dans `ressources/cv/`.

## Voir le site en local

```bash
python3 -m pip install -r requirements.txt
python3 lancer_site.py
```

Le dossier `site/` est régénéré à chaque exécution : ne pas y modifier de fichiers.

## Publication (GitHub Pages)

Chaque envoi sur la branche `main` déclenche `.github/workflows/pages.yml`, qui exécute
`python build.py` puis publie le dossier `site/`.

Réglage unique sur GitHub : **Settings → Pages → Build and deployment → Source : GitHub Actions**.

## Données publiques

Tout ce qui se trouve dans `ressources/` (photo, CV PDF) est téléchargeable par tous les visiteurs
une fois le site publié.
