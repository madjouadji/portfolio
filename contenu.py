# VERSION COMPLÈTE — Toutes les informations qui alimentent ton site.
# Tu peux modifier les textes entre guillemets, puis lancer : python3 build.py
# Pas besoin de modifier le HTML, le CSS ou le JavaScript.

INFOS = {
    "prenom": "Adji",
    "nom_famille": "Madjou",
    "email": "Adji.Madjou@USherbrooke.ca",
    "titre_site": "Adji Madjou | Mathématiques, recherche et enseignement",
    # Adresse publique du site (sert au sitemap, aux liens canoniques et aux aperçus de partage).
    # À modifier si le dépôt GitHub change de nom, par exemple "https://madjouadji.github.io".
    "url_site": "https://madjouadji.github.io/portfolio",
    "presentation_fr": (
        "Doctorant en mathématiques à l'Université de Sherbrooke, je mène des recherches "
        "en géométrie complexe et en géométrie de Poisson. J'accompagne également "
        "des étudiants en calcul et en algèbre linéaire."
    ),
    "presentation_en": (
        "I am a mathematics PhD student at Université de Sherbrooke researching "
        "complex and Poisson geometry. I also support students in calculus "
        "and linear algebra through teaching assistantships."
    ),
    "enseignement_secondaire_fr": (
        "Enseignement des mathématiques, de la physique et de la chimie "
        "au Complexe scolaire protestant Philadelphie et au Complexe Tindjassi "
        "(ANVT), après un stage au Lycée BAMABODOLO, au Togo."
    ),
    "enseignement_secondaire_en": (
        "Teaching mathematics, physics and chemistry at Complexe scolaire "
        "protestant Philadelphie and Complexe Tindjassi (ANVT), following "
        "a teaching internship at Lycée BAMABODOLO in Togo."
    ),
    "recherche_intro_fr": (
        "Mes travaux doctoraux explorent la géométrie complexe et de Poisson, "
        "notamment les groupoïdes symplectiques holomorphes et les structures "
        "hyperkählériennes."
    ),
    "recherche_intro_en": (
        "My doctoral research explores complex and Poisson geometry, "
        "particularly holomorphic symplectic groupoids and hyperkähler structures."
    ),
}

# Une « liste » Python : chaque entrée décrit un cours du site.
COURS = [
    {
        "id": "mat194",
        "code": "MAT194",
        "titre_fr": "Calcul différentiel et intégral",
        "titre_en": "Differential and integral calculus",
        "description_fr": (
            "Auxiliariat d'enseignement : animation de séances d'exercices, "
            "dérivées, optimisation et résolution de problèmes en calcul."
        ),
        "description_en": (
            "Teaching assistantship: facilitating exercise sessions on "
            "derivatives, optimization and calculus problem solving."
        ),
    },
    {
        "id": "mat199",
        "code": "MAT199",
        "titre_fr": "Algèbre linéaire appliquée à l'informatique",
        "titre_en": "Linear algebra for computer science",
        "description_fr": (
            "Auxiliariat d'enseignement : soutien aux étudiants en algèbre "
            "linéaire, matrices, systèmes d'équations et raisonnement mathématique."
        ),
        "description_en": (
            "Teaching assistantship: student support in linear algebra, "
            "matrices, systems of equations and mathematical reasoning."
        ),
    },
]

# Axes de recherche : il s'agit de thèmes, pas de publications déjà parues.
RECHERCHES = [
    {
        "id": "poisson",
        "symbole": "π",
        "titre_fr": "Géométrie de Poisson",
        "titre_en": "Poisson geometry",
        "description_fr": "Structures de Poisson et problèmes géométriques locaux et globaux.",
        "description_en": "Poisson structures and local and global geometric questions.",
    },
    {
        "id": "groupoides",
        "symbole": "Ω",
        "titre_fr": "Groupoïdes symplectiques holomorphes",
        "titre_en": "Holomorphic symplectic groupoids",
        "description_fr": "Constructions et intégration de structures de Poisson holomorphes.",
        "description_en": "Constructing and integrating holomorphic Poisson structures.",
    },
    {
        "id": "hyperkahler",
        "symbole": "∇",
        "titre_fr": "Géométrie hyperkählérienne",
        "titre_en": "Hyperkähler geometry",
        "description_fr": "Étude des structures hyperkählériennes et de leurs liens avec la géométrie complexe.",
        "description_en": "Studying hyperkähler structures and their links to complex geometry.",
    },
]

# Parcours : une entrée = une ligne sur la frise chronologique.
PARCOURS = [
    {
        "id": "doctorat", "annees_fr": "2025 — aujourd'hui", "annees_en": "2025 — present",
        "titre_fr": "Doctorat en mathématiques", "titre_en": "PhD in Mathematics",
        "lieu_fr": "Université de Sherbrooke · Canada", "lieu_en": "Université de Sherbrooke · Canada",
    },
    {
        "id": "iqucode", "annees_fr": "Depuis l'automne 2026", "annees_en": "Since fall 2026",
        "titre_fr": "Microprogramme IQuCode — informatique quantique", "titre_en": "IQuCode microprogram — quantum computing",
        "lieu_fr": "Institut quantique, Université de Sherbrooke · Canada", "lieu_en": "Institut quantique, Université de Sherbrooke · Canada",
    },
    {
        "id": "nantes", "annees_fr": "2024 — 2025", "annees_en": "2024 — 2025",
        "titre_fr": "Master 2 en mathématiques fondamentales", "titre_en": "Master 2 in Fundamental Mathematics",
        "lieu_fr": "Nantes Université · France", "lieu_en": "Nantes Université · France",
    },
    {
        "id": "ugb", "annees_fr": "2022 — 2024", "annees_en": "2022 — 2024",
        "titre_fr": "Études de master en mathématiques", "titre_en": "Graduate studies in Mathematics",
        "lieu_fr": "Université Gaston Berger · Sénégal", "lieu_en": "Université Gaston Berger · Senegal",
    },
    {
        "id": "kara", "annees_fr": "2019", "annees_en": "2019",
        "titre_fr": "Licence en mathématiques", "titre_en": "Bachelor's degree in Mathematics",
        "lieu_fr": "Université de Kara · Togo", "lieu_en": "Université de Kara · Togo",
    },
]

# Compétences de tutorat : sélectionne seulement les matières que tu maîtrises.
TUTORAT = [
    {
        "id": "calcul", "symbole": "∫", "niveau_fr": "CÉGEP · UNIVERSITÉ", "niveau_en": "COLLEGE · UNIVERSITY",
        "titre_fr": "Calcul différentiel et intégral", "titre_en": "Differential & integral calculus",
        "description_fr": "Limites, dérivées, intégrales, optimisation et résolution de problèmes.",
        "description_en": "Limits, derivatives, integrals, optimization and problem solving.",
    },
    {
        "id": "algebre", "symbole": "A", "niveau_fr": "CÉGEP · UNIVERSITÉ", "niveau_en": "COLLEGE · UNIVERSITY",
        "titre_fr": "Algèbre linéaire", "titre_en": "Linear algebra",
        "description_fr": "Matrices, systèmes linéaires, espaces vectoriels et applications.",
        "description_en": "Matrices, linear systems, vector spaces and applications.",
    },
    {
        "id": "secondaire", "symbole": "x²", "niveau_fr": "SECONDAIRE", "niveau_en": "SECONDARY SCHOOL",
        "titre_fr": "Mathématiques au secondaire", "titre_en": "Secondary mathematics",
        "description_fr": "Algèbre, fonctions, géométrie et préparation aux évaluations.",
        "description_en": "Algebra, functions, geometry and exam preparation.",
    },
]

# Projets présentés comme explorations, pas comme logiciels déjà publiés.
PROJETS = [
    {
        "id": "simulateur", "numero": "01", "technos": "PYTHON · NUMPY",
        "titre_fr": "Simulateur quantique en Python", "titre_en": "Python quantum simulator",
        "description_fr": "Projet d'apprentissage autour des portes quantiques, des états de qubits et de la simulation de circuits.",
        "description_en": "Learning project exploring quantum gates, qubit states and circuit simulation.",
        "statut_fr": "Projet d'apprentissage", "statut_en": "Learning project",
    },
    {
        "id": "site", "numero": "02", "technos": "PYTHON · JINJA2 · WEB",
        "titre_fr": "Ce site, généré avec Python", "titre_en": "This website, generated with Python",
        "description_fr": "Un projet personnel pour structurer mes activités scientifiques et pédagogiques et pratiquer Python.",
        "description_en": "A personal project for presenting my research and teaching while practicing Python.",
        "statut_fr": "Projet personnel", "statut_en": "Personal project",
    },
]

# CV téléchargeable : un seul document, le CV général (ressources/cv/cv-general.pdf, généré par generer_cv.py).
CV = [
    {"fichier": "cv-general.pdf", "titre_fr": "CV — Curriculum vitæ complet", "titre_en": "CV — Full curriculum vitae"},
]


# DEBUT AJOUT CV2026 — données du CV académique et informations du 14 novembre 2026
# Tu peux modifier les textes des listes ci-dessous dans ce même fichier.
INFOS["presentation_fr"] = (
    "Doctorant en mathématiques à l'Université de Sherbrooke, sous la direction de "
    "Maxence Mayrand, je travaille en géométrie complexe, en géométrie de Poisson "
    "et sur les groupoïdes symplectiques holomorphes. "
    "Je participe aussi à l'enseignement universitaire des mathématiques."
)
INFOS["presentation_en"] = (
    "I am a PhD student in Mathematics at Université de Sherbrooke, supervised by "
    "Maxence Mayrand. My research focuses on complex geometry, Poisson geometry, "
    "and holomorphic symplectic groupoids. I also work as a mathematics teaching assistant."
)
INFOS["recherche_intro_fr"] = (
    "Mes recherches portent sur la géométrie complexe et l'intégration de structures "
    "de Poisson holomorphes par des groupoïdes symplectiques. "
    "Je m'intéresse également aux structures hyperkählériennes et à leurs constructions locales."
)

# Précisions sur les intitulés de diplômes à partir du CV universitaire.
for diplome in PARCOURS:
    if diplome["id"] == "ugb":
        diplome["titre_fr"] = "Master en mathématiques appliquées — géométrie, algèbre et applications"
    if diplome["id"] == "kara":
        diplome["annees_fr"] = "2016 — 2019"
        diplome["titre_fr"] = "Licence en mathématiques appliquées"

EXPERIENCES_ACADEMIQUES = [
    {"date": "Depuis 2025", "titre": "Auxiliaire d'enseignement", "lieu": "Université de Sherbrooke · mathématiques", "detail": "Séances d'exercices, suivi des étudiants et correction de travaux et examens."},
    {"date": "2020–2022", "titre": "Enseignant de mathématiques au secondaire", "lieu": "Togo", "detail": "Enseignement, préparation de cours et accompagnement pédagogique des élèves."},
]

TRAVAIL_ANTERIEUR = [
    {"titre": "Étude du paludisme chez les enfants de moins de cinq ans et chimioprévention du paludisme saisonnier", "contexte": "Rapport de stage de licence · Université de Kara, Togo"},
]

COURS_COMPLEMENTAIRES = [
    {"code": "MAT298", "titre": "Calcul vectoriel", "precision": "Auxiliariat d'enseignement · automne 2025", "url": ""},
    {"code": "MAT401-AB", "titre": "Géométrie euclidienne et non euclidienne", "precision": "Cours mentionné dans mon parcours", "url": ""},
    {"code": "MAT901", "titre": "Notions fondamentales de calcul intégral", "precision": "Cours mentionné dans mon parcours", "url": ""},
]

EXPOSES = [
    {
        "annee": "2026", "date": "30 avril 2026",
        "titre": "Construction locale de métriques hyperkählériennes au voisinage de sous-variétés lagrangiennes complexes",
        "contexte": "Examen général oral · Département de mathématiques, Université de Sherbrooke",
        "url": "https://www.usherbrooke.ca/mathematiques/actualites/evenements/details/58350",
    },
    {"annee": "2025", "date": "2025", "titre": "Théorème de Lefschetz difficile", "contexte": "Séminaire des doctorants · Université de Sherbrooke", "url": ""},
    {"annee": "2024", "date": "2024", "titre": "Approximation diophantienne", "contexte": "Séminaire des étudiants · Nantes Université", "url": ""},
    {"annee": "2024", "date": "2024", "titre": "Champs de vecteurs et nombre d'Euler", "contexte": "Séminaire des étudiants · Nantes Université", "url": ""},
    {"annee": "", "date": "Soutenance de master", "titre": "Étude des solutions du flot de Kähler–Ricci sur une variété kählérienne compacte", "contexte": "Mémoire de master · Nantes Université", "url": ""},
    {"annee": "2024", "date": "2024", "titre": "Code de Hamming", "contexte": "Séminaire des étudiants · Université Gaston Berger, Sénégal", "url": ""},
    {"annee": "2024", "date": "2024", "titre": "Décodage par tableau standard", "contexte": "Séminaire de mathématiques · Université Gaston Berger, Sénégal", "url": ""},
    {"annee": "2023", "date": "2023", "titre": "Fonctions à sens unique", "contexte": "Séminaire des étudiants · Université Gaston Berger, Sénégal", "url": ""},
]

DISTINCTIONS = [
    {"annee": "2024–2025", "titre": "Bourse d'excellence de master Henri Lebesgue", "detail": "Centre Henri Lebesgue · Nantes Université, France · 10 000 €", "url": "https://federation-henri-lebesgue.fr/D%C3%A9fiMath-bourses"},
    {"annee": "2025", "titre": "Prix de major de promotion", "detail": "UFR des sciences et technologies · Université Gaston Berger, Sénégal", "url": ""},
]

MEMOIRES = [
    {"titre": "Flot de Kähler–Ricci sur une variété kählérienne compacte", "contexte": "Mémoire de master · Nantes Université · 2024–2025"},
    {"titre": "Sommes et produits de modules singuliers", "contexte": "Mémoire de master · Université Gaston Berger · 2022–2024"},
]

COMPETENCES_ACADEMIQUES = [
    "Géométrie complexe et symplectique", "Analyse et algèbre linéaire",
    "Python et calcul scientifique", "LaTeX, Excel, SPSS et SQL",
    "Cryptographie et codes correcteurs", "Analyse de données, français et anglais",
]
# FIN AJOUT CV2026

# Auxiliariats d'enseignement, par ordre chronologique (page Enseignement et CV).
AUXILIARIATS = [
    {"code": "MAT298", "titre": "Calcul vectoriel", "session": "Automne 2025"},
    {"code": "MAT401-AB", "titre": "Géométrie euclidienne et non euclidienne", "session": "Hiver 2026"},
    {"code": "MAT901", "titre": "Notions fondamentales de calcul intégral", "session": "Été 2026"},
    {"code": "MAT194", "titre": "Calcul différentiel et intégral", "session": "Automne 2026"},
    {"code": "MAT199", "titre": "Algèbre linéaire appliquée à l'informatique", "session": "Automne 2026"},
]
