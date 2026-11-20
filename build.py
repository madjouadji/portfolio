"""Génère un vrai site multipage depuis contenu.py, sans serveur Python.

Lancer : python3 lancer_site.py
Les liens du menu ouvrent des fichiers HTML distincts.
"""
from pathlib import Path
from shutil import copy2, copytree, rmtree
from datetime import date
from jinja2 import Environment, FileSystemLoader, select_autoescape
from contenu import (INFOS, COURS, RECHERCHES, PARCOURS, CV, EXPOSES, DISTINCTIONS, MEMOIRES, COMPETENCES_ACADEMIQUES, COURS_COMPLEMENTAIRES, EXPERIENCES_ACADEMIQUES, TRAVAIL_ANTERIEUR, AUXILIARIATS)

RACINE = Path(__file__).resolve().parent
DESTINATION = RACINE / "site"

PAGES = (
    ("index.html", "accueil.html", "accueil"),
    ("recherche.html", "recherche.html", "recherche"),
    ("exposes.html", "exposes.html", "exposes"),
    ("cv.html", "cv.html", "cv"),
    ("enseignement.html", "enseignement.html", "enseignement"),
)


def construire_site():
    if DESTINATION.exists():
        rmtree(DESTINATION)  # Ce répertoire est toujours recréé : ne pas y éditer les fichiers.
    DESTINATION.mkdir(parents=True)
    env = Environment(
        loader=FileSystemLoader(RACINE / "templates"),
        autoescape=select_autoescape(["html"]),
    )
    donnees = {
        **INFOS, "annee": date.today().year,
        "cours": COURS, "recherches": RECHERCHES,
        "parcours": PARCOURS, "cvs": [c for c in CV if (RACINE / "ressources" / "cv" / c["fichier"]).exists()],
        "exposes": EXPOSES, "distinctions": DISTINCTIONS,
        "memoires": MEMOIRES, "competences_academiques": COMPETENCES_ACADEMIQUES,
        "cours_complementaires": COURS_COMPLEMENTAIRES,
        "experiences_academiques": EXPERIENCES_ACADEMIQUES, "travail_anterieur": TRAVAIL_ANTERIEUR, "auxiliariats": AUXILIARIATS,
        "portrait_disponible": (RACINE / "ressources" / "assets" / "portrait.jpg").exists(),
        "url_site": INFOS["url_site"].rstrip("/"),
    }
    for nom, modele, actif in PAGES:
        html = env.get_template(modele).render(**donnees, page_active=actif, page_fichier=nom)
        (DESTINATION / nom).write_text(html, encoding="utf-8")
    copy2(RACINE / "ressources" / "styles.css", DESTINATION / "styles.css")
    copytree(RACINE / "ressources" / "assets", DESTINATION / "assets", dirs_exist_ok=True)
    copytree(RACINE / "ressources" / "cv", DESTINATION / "cv", dirs_exist_ok=True)
    (DESTINATION / ".nojekyll").touch()
    base = INFOS["url_site"].rstrip("/")
    aujourd_hui = date.today().isoformat()
    entrees = "\n".join(
        f"  <url><loc>{base}/{'' if nom == 'index.html' else nom}</loc><lastmod>{aujourd_hui}</lastmod>"
        f"<priority>{'1.0' if nom == 'index.html' else '0.7'}</priority></url>"
        for nom, _, _ in PAGES
    )
    (DESTINATION / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + entrees + "\n</urlset>\n", encoding="utf-8")
    (DESTINATION / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {base}/sitemap.xml\n", encoding="utf-8")
    print("✓ Site personnel créé avec 5 pages indépendantes :")
    for nom, _, _ in PAGES:
        print("  - site/" + nom)
    print("Ouvre site/index.html ou lance python3 lancer_site.py")


if __name__ == "__main__":
    construire_site()
