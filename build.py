"""Génère le site personnel bilingue depuis contenu.py et interface.py, sans serveur Python.

  - français : à la racine du site   (index.html, recherche.html, exposes.html, …)
  - anglais  : dans le dossier en/   (en/index.html, en/research.html, en/talks.html, …)

Le bouton FR | EN du menu passe d'une page à son équivalent dans l'autre langue.
Lancer : python3 lancer_site.py
"""
from datetime import date
from pathlib import Path
from shutil import copy2, copytree, rmtree

from jinja2 import Environment, FileSystemLoader, select_autoescape

import contenu as C
from interface import UI

RACINE = Path(__file__).resolve().parent
DESTINATION = RACINE / "site"
LANGUES = ("fr", "en")

# (clé de page, fichier français, fichier anglais (dans en/), gabarit)
PAGES = (
    ("accueil", "index.html", "index.html", "accueil.html"),
    ("recherche", "recherche.html", "research.html", "recherche.html"),
    ("exposes", "exposes.html", "talks.html", "exposes.html"),
    ("enseignement", "enseignement.html", "teaching.html", "enseignement.html"),
    ("cv", "cv.html", "cv.html", "cv.html"),
)

TRADUCTIONS_MANQUANTES = []


def localiser(valeur, lang, chemin="contenu"):
    """Choisit la version de chaque texte dans la langue demandée.

    Convention de contenu.py : « xxx_fr » + « xxx_en », ou « xxx » (français) + « xxx_en ».
    Le gabarit lit toujours le nom neutre « xxx ». Sans version anglaise, on garde le français
    et on le signale à la fin de la génération.
    """
    if isinstance(valeur, dict):
        bases = {cle[:-3] for cle in valeur if cle.endswith(("_fr", "_en"))}
        resultat = {
            cle: localiser(v, lang, f"{chemin}.{cle}")
            for cle, v in valeur.items() if not cle.endswith(("_fr", "_en"))
        }
        for base in bases:
            francais = valeur.get(base + "_fr", valeur.get(base))
            anglais = valeur.get(base + "_en")
            if lang == "en":
                if anglais is None:
                    TRADUCTIONS_MANQUANTES.append(f"{chemin}.{base}_en")
                choix = anglais if anglais is not None else francais
            else:
                choix = francais if francais is not None else anglais
            resultat[base] = localiser(choix, lang, f"{chemin}.{base}")
        return resultat
    if isinstance(valeur, (list, tuple)):
        return [localiser(v, lang, f"{chemin}[{i}]") for i, v in enumerate(valeur)]
    return valeur


def fichier_page(cle, lang):
    for k, fr, en, _ in PAGES:
        if k == cle:
            return fr if lang == "fr" else en
    raise KeyError(cle)


def url_publique(base, lang, cle):
    """Adresse publique complète d'une page (accueil : adresse du dossier, sans index.html)."""
    dossier = base + ("/" if lang == "fr" else "/en/")
    return dossier + ("" if cle == "accueil" else fichier_page(cle, lang))


def construire_site():
    if DESTINATION.exists():
        rmtree(DESTINATION)  # Ce répertoire est toujours recréé : ne pas y éditer les fichiers.
    DESTINATION.mkdir(parents=True)
    (DESTINATION / "en").mkdir()
    env = Environment(
        loader=FileSystemLoader(RACINE / "templates"),
        autoescape=select_autoescape(["html"]),
    )
    base = C.INFOS["url_site"].rstrip("/")
    contenu = {
        **C.INFOS, "recherches": C.RECHERCHES, "parcours": C.PARCOURS, "cvs_source": C.CV,
        "exposes": C.EXPOSES, "distinctions": C.DISTINCTIONS, "memoires": C.MEMOIRES,
        "experiences_academiques": C.EXPERIENCES_ACADEMIQUES, "travail_anterieur": C.TRAVAIL_ANTERIEUR,
        "auxiliariats": C.AUXILIARIATS,
    }
    portrait = (RACINE / "ressources" / "assets" / "portrait.jpg").exists()
    manquants_cv = []

    for lang in LANGUES:
        donnees = localiser(contenu, lang)
        donnees["url_site"] = base  # sans « / » final
        cvs = []
        for document in donnees.pop("cvs_source"):
            if (RACINE / "ressources" / "cv" / document["fichier"]).exists():
                cvs.append(document)
            else:
                manquants_cv.append(document["fichier"])
        nom = f"{donnees['prenom']} {donnees['nom_famille']}"
        dossier = DESTINATION if lang == "fr" else DESTINATION / "en"
        prefixe = "" if lang == "fr" else "../"  # chemin vers styles.css, assets/ et cv/
        liens = {cle: (fr if lang == "fr" else en) for cle, fr, en, _ in PAGES}
        for cle, fr, en, modele in PAGES:
            html = env.get_template(modele).render(
                **donnees, cvs=cvs, nom=nom, annee=date.today().year, portrait_disponible=portrait,
                ui=UI[lang], lang=lang, pre=prefixe, liens=liens, page_active=cle,
                lien_autre_langue=("en/" + en) if lang == "fr" else ("../" + fr),
                url_page=url_publique(base, lang, cle),
                url_fr=url_publique(base, "fr", cle), url_en=url_publique(base, "en", cle),
                url_accueil=url_publique(base, lang, "accueil"),
            )
            (dossier / (fr if lang == "fr" else en)).write_text(html, encoding="utf-8")

    copy2(RACINE / "ressources" / "styles.css", DESTINATION / "styles.css")
    copytree(RACINE / "ressources" / "js", DESTINATION / "js", dirs_exist_ok=True)
    copytree(RACINE / "ressources" / "assets", DESTINATION / "assets", dirs_exist_ok=True)
    copytree(RACINE / "ressources" / "cv", DESTINATION / "cv", dirs_exist_ok=True)
    # Fichiers de validation (Google Search Console) : copiés à la racine du site, à ne jamais supprimer.
    verification = RACINE / "ressources" / "verification"
    if verification.is_dir():
        for fichier in verification.iterdir():
            if fichier.is_file():
                copy2(fichier, DESTINATION / fichier.name)
    (DESTINATION / ".nojekyll").touch()

    # Plan du site : chaque page dans les deux langues, avec ses équivalents (hreflang).
    aujourd_hui = date.today().isoformat()
    entrees = []
    for lang in LANGUES:
        for cle, _, _, _ in PAGES:
            alternatives = "".join(
                f'\n    <xhtml:link rel="alternate" hreflang="{autre}" href="{url_publique(base, autre, cle)}"/>'
                for autre in LANGUES
            ) + f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{url_publique(base, "fr", cle)}"/>'
            entrees.append(
                f"  <url>\n    <loc>{url_publique(base, lang, cle)}</loc>\n    <lastmod>{aujourd_hui}</lastmod>"
                f"\n    <priority>{'1.0' if cle == 'accueil' else '0.7'}</priority>{alternatives}\n  </url>"
            )
    (DESTINATION / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(entrees) + "\n</urlset>\n", encoding="utf-8")
    (DESTINATION / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {base}/sitemap.xml\n", encoding="utf-8")

    print("✓ Site personnel bilingue créé : 5 pages en français et 5 pages en anglais")
    for _, fr, _, _ in PAGES:
        print("  - site/" + fr)
    for _, _, en, _ in PAGES:
        print("  - site/en/" + en)
    for fichier in sorted(set(manquants_cv)):
        print(f"⚠ CV absent : ressources/cv/{fichier} (lance python3 generer_cv.py)")
    for chemin in sorted(set(TRADUCTIONS_MANQUANTES)):
        print(f"⚠ Traduction anglaise manquante : {chemin}")
    print("Ouvre site/index.html ou lance python3 lancer_site.py")


if __name__ == "__main__":
    construire_site()
