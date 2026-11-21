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

## Design (novembre 2026)

- **Mode jour uniquement**, sur une seule surface continue : aucune bordure ni bloc séparé entre les sections.
- **Fond fixe** : crème doré (jaune) avec des reflets d'automne de Sherbrooke (érable, ocre, vert mousse).
- **Couleurs** : orange-rouge et vert (inspirés de la palette d'Anthropic) pour les accents, bleus pour les liens
  (variables en tête de `ressources/styles.css`).
- **Animations** (`ressources/js/site.js`, comme sur le site de Yassine) : entrée en cascade du contenu,
  apparition du portrait, trait sous le nom, trait du menu qui suit la souris, menu collant,
  barre de lecture, copie du courriel en un clic.
- L'ancien design est conservé dans `_sauvegarde_design_avant_refonte/`.

## Pages générées (chacune est un fichier HTML séparé)

Après `python3 build.py`, le dossier `site/` contient :
`index.html`, `recherche.html`, `exposes.html`, `enseignement.html`, `cv.html`,
et en anglais `en/index.html`, `en/research.html`, `en/talks.html`, `en/teaching.html`, `en/cv.html`,
plus `sitemap.xml`, `robots.txt`, le fichier de validation Google, `styles.css`, `js/site.js`, `assets/`, `cv/`.

## Google Search Console (apparaître dans Google)

1. Ouvrir https://search.google.com/search-console et choisir la propriété
   **Préfixe de l'URL** : `https://madjouadji.github.io/portfolio/`.
2. Validation : le fichier `google0715c4e7b75eb266.html` (dans `ressources/verification/`) est publié
   à la racine du site ; cliquer sur « Valider ».
3. Menu **Sitemaps** → saisir `sitemap.xml` → **Envoyer**.
   Adresse complète : `https://madjouadji.github.io/portfolio/sitemap.xml` (10 pages, FR + EN).
4. Facultatif : **Inspection de l'URL** → coller l'adresse de l'accueil → « Demander l'indexation ».

Remarque : comme le site est dans un sous-dossier (`/portfolio/`), Google ne lit pas son `robots.txt` ;
c'est l'envoi du sitemap dans la Search Console (étape 3) qui compte.
