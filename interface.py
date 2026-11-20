"""Textes de l'interface (menu, titres, boutons) en français et en anglais.

Le contenu personnel (présentation, exposés, parcours, cours…) est dans contenu.py.
Ici, {nom} est remplacé à la génération par le nom complet.
Pour ajouter une langue, il faudrait ajouter une entrée dans UI et dans LANGUES (build.py).
"""

UI = {
    "fr": {
        "html_lang": "fr",
        "og_locale": "fr_CA",
        "og_locale_alt": "en_CA",
        "skip": "Aller au contenu",
        "brand_role": "Mathématiques · Université de Sherbrooke",
        "aria_nav": "Navigation principale",
        "aria_menu": "Ouvrir le menu",
        "aria_lang": "Langue",
        "autre_langue": {"nom": "English", "aria": "Switch to English"},
        "nav": {
            "accueil": "Accueil", "recherche": "Recherche", "exposes": "Exposés",
            "enseignement": "Enseignement", "cv": "CV",
        },
        "job": "Doctorant en mathématiques",
        "knows": [
            "Géométrie complexe", "Géométrie de Poisson",
            "Groupoïdes symplectiques holomorphes", "Géométrie hyperkählérienne",
        ],
        "accueil": {
            "titre_complet": "{nom} — Doctorant en mathématiques, Université de Sherbrooke",
            "description": (
                "Site d'{nom}, doctorant en mathématiques à l'Université de Sherbrooke : géométrie complexe, "
                "géométrie de Poisson, groupoïdes symplectiques holomorphes. Recherche, exposés, enseignement et CV."
            ),
            "kicker": "Doctorant en mathématiques",
            "alt_portrait": "Portrait d'{nom}, doctorant en mathématiques à l'Université de Sherbrooke",
            "institution": "Institution", "institution_valeur": "Université de Sherbrooke, Québec",
            "direction": "Direction", "direction_valeur": "Maxence Mayrand",
            "domaines": "Domaines", "domaines_valeur": "Géométrie complexe · Géométrie de Poisson",
            "courriel": "Courriel",
            "bouton_recherche": "Mes recherches", "bouton_cv": "Curriculum vitæ",
            "themes": "Thèmes de recherche", "exposes_recents": "Exposés récents", "distinctions": "Distinctions",
            "tous_exposes": "Tous les exposés →", "parcours_complet": "Parcours complet →",
        },
        "recherche": {
            "titre": "Recherche",
            "description": (
                "Recherche d'{nom} : géométrie complexe, géométrie de Poisson, groupoïdes symplectiques "
                "holomorphes et structures hyperkählériennes, Université de Sherbrooke."
            ),
            "kicker": "Recherche", "h1": "Recherche", "memoires": "Mémoires",
        },
        "exposes": {
            "titre": "Exposés",
            "description": (
                "Exposés et séminaires d'{nom} : géométrie hyperkählérienne, théorème de Lefschetz difficile, "
                "approximation diophantienne, codes correcteurs."
            ),
            "kicker": "Exposés", "h1": "Exposés et séminaires",
        },
        "enseignement": {
            "titre": "Enseignement",
            "description": (
                "Enseignement d'{nom} : auxiliaire d'enseignement en mathématiques à l'Université de Sherbrooke "
                "(calcul, algèbre linéaire, géométrie) et ancien professeur au secondaire."
            ),
            "kicker": "Enseignement", "h1": "Auxiliaire d'enseignement",
            "sous_titre": "Département de mathématiques, Université de Sherbrooke",
            "note": "Auparavant : professeur de mathématiques, de physique et de chimie au secondaire (Togo, 2020 – 2022).",
        },
        "cv": {
            "titre": "Curriculum vitæ",
            "description": (
                "Curriculum vitæ d'{nom} : formation (Sherbrooke, Nantes, Université Gaston Berger, Kara), "
                "expérience en enseignement, distinctions et compétences."
            ),
            "kicker": "Curriculum vitæ", "h1": "Parcours", "telecharger": "Télécharger le CV (PDF)",
            "formation": "Formation", "experience": "Expérience", "distinctions": "Bourses et distinctions",
        },
    },
    "en": {
        "html_lang": "en",
        "og_locale": "en_CA",
        "og_locale_alt": "fr_CA",
        "skip": "Skip to main content",
        "brand_role": "Mathematics · Université de Sherbrooke",
        "aria_nav": "Main navigation",
        "aria_menu": "Open menu",
        "aria_lang": "Language",
        "autre_langue": {"nom": "Français", "aria": "Passer en français"},
        "nav": {
            "accueil": "Home", "recherche": "Research", "exposes": "Talks",
            "enseignement": "Teaching", "cv": "CV",
        },
        "job": "PhD student in mathematics",
        "knows": [
            "Complex geometry", "Poisson geometry",
            "Holomorphic symplectic groupoids", "Hyperkähler geometry",
        ],
        "accueil": {
            "titre_complet": "{nom} — PhD student in mathematics, Université de Sherbrooke",
            "description": (
                "Website of {nom}, PhD student in mathematics at Université de Sherbrooke: complex geometry, "
                "Poisson geometry, holomorphic symplectic groupoids. Research, talks, teaching and CV."
            ),
            "kicker": "PhD student in mathematics",
            "alt_portrait": "Portrait of {nom}, PhD student in mathematics at Université de Sherbrooke",
            "institution": "Institution", "institution_valeur": "Université de Sherbrooke, Quebec",
            "direction": "Supervisor", "direction_valeur": "Maxence Mayrand",
            "domaines": "Fields", "domaines_valeur": "Complex geometry · Poisson geometry",
            "courriel": "Email",
            "bouton_recherche": "My research", "bouton_cv": "Curriculum vitae",
            "themes": "Research topics", "exposes_recents": "Recent talks", "distinctions": "Awards",
            "tous_exposes": "All talks →", "parcours_complet": "Full background →",
        },
        "recherche": {
            "titre": "Research",
            "description": (
                "Research of {nom}: complex geometry, Poisson geometry, holomorphic symplectic groupoids "
                "and hyperkähler structures, Université de Sherbrooke."
            ),
            "kicker": "Research", "h1": "Research", "memoires": "Theses",
        },
        "exposes": {
            "titre": "Talks",
            "description": (
                "Talks and seminars by {nom}: hyperkähler geometry, hard Lefschetz theorem, "
                "Diophantine approximation, error-correcting codes."
            ),
            "kicker": "Talks", "h1": "Talks and seminars",
        },
        "enseignement": {
            "titre": "Teaching",
            "description": (
                "Teaching by {nom}: teaching assistant in mathematics at Université de Sherbrooke "
                "(calculus, linear algebra, geometry) and former secondary school teacher."
            ),
            "kicker": "Teaching", "h1": "Teaching assistant",
            "sous_titre": "Department of Mathematics, Université de Sherbrooke",
            "note": "Previously: secondary school teacher of mathematics, physics and chemistry (Togo, 2020 – 2022).",
        },
        "cv": {
            "titre": "Curriculum vitae",
            "description": (
                "Curriculum vitae of {nom}: education (Sherbrooke, Nantes, Université Gaston Berger, Kara), "
                "teaching experience, awards and skills."
            ),
            "kicker": "Curriculum vitae", "h1": "Background", "telecharger": "Download CV (PDF)",
            "formation": "Education", "experience": "Experience", "distinctions": "Scholarships and awards",
        },
    },
}
