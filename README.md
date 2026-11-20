# Site personnel — Adji Madjou (français / anglais)

Site statique généré en Python (Jinja2), **bilingue** : chaque page existe en français et en anglais,
et le bouton **FR | EN** du menu passe d'une langue à l'autre.

| Page | Français (racine du site) | Anglais (dossier `en/`) |
|---|---|---|
| Accueil | `index.html` | `en/index.html` |
| Recherche | `recherche.html` | `en/research.html` |
| Exposés | `exposes.html` | `en/talks.html` |
| Enseignement | `enseignement.html` | `en/teaching.html` |
| CV | `cv.html` | `en/cv.html` |

## Modifier le contenu

- **Textes personnels** (présentation, parcours, exposés, cours, distinctions…) : `contenu.py`.
  Chaque texte existe en deux versions :
  - `titre_fr` + `titre_en` (champs doubles), ou
  - `titre` (français) + `titre_en` (anglais).

  Quand tu ajoutes un exposé ou un cours, écris donc les deux versions.
  Si une version anglaise manque, la page anglaise affiche le français et `python3 build.py`
  affiche un avertissement `⚠ Traduction anglaise manquante`.
- **Textes de l'interface** (menu, titres de page, boutons, descriptions pour Google) : `interface.py`.
- **Mise en page** : `templates/` (un gabarit par page, commun aux deux langues) et `ressources/styles.css`.
- **Photo** : `ressources/assets/portrait.jpg`.

## Voir le site en local

```bash
python3 -m pip install -r requirements.txt
python3 lancer_site.py
```

Le dossier `site/` est régénéré à chaque exécution : ne pas y modifier de fichiers.

## CV (deux PDF)

- `cv_source/cv-general.html` → `ressources/cv/cv-general.pdf` (français)
- `cv_source/cv-general-en.html` → `ressources/cv/cv-general-en.pdf` (anglais)

Après une modification : `python3 generer_cv.py` (Chrome ou Chromium requis), puis publier.
La page française propose le CV français, la page anglaise le CV anglais.

## Publication (GitHub Pages)

Chaque envoi sur la branche `main` déclenche `.github/workflows/pages.yml`, qui exécute
`python build.py` puis publie le dossier `site/`.

Réglage unique sur GitHub : **Settings → Pages → Build and deployment → Source : GitHub Actions**.

## Référencement

`build.py` génère `sitemap.xml` (les deux langues, avec leurs équivalents `hreflang`) et `robots.txt`.
Chaque page déclare son adresse canonique et ses versions française et anglaise.
Le fichier `ressources/verification/google….html` valide le site dans Google Search Console : ne pas le supprimer.

## Données publiques

Tout ce qui se trouve dans `ressources/` (photo, CV PDF) est téléchargeable par tous les visiteurs
une fois le site publié : n'y mettre ni téléphone ni adresse personnelle.
