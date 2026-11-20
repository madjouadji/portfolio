"""Génère les deux CV (français et anglais) en PDF avec Chrome ou Chromium.

  cv_source/cv-general.html     -> ressources/cv/cv-general.pdf      (français)
  cv_source/cv-general-en.html  -> ressources/cv/cv-general-en.pdf   (anglais)

Pour modifier un CV : éditer le fichier HTML correspondant, puis lancer : python3 generer_cv.py
Les PDF sont publiés tels quels sur le site : n'y mettre ni téléphone ni adresse personnelle.
"""
import shutil
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent
CVS = (
    (RACINE / "cv_source" / "cv-general.html", RACINE / "ressources" / "cv" / "cv-general.pdf"),
    (RACINE / "cv_source" / "cv-general-en.html", RACINE / "ressources" / "cv" / "cv-general-en.pdf"),
)
CANDIDATS = (
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    shutil.which("google-chrome") or "", shutil.which("chromium") or "", shutil.which("chromium-browser") or "",
)
chrome = next((c for c in CANDIDATS if c and Path(c).exists()), None)
if not chrome:
    sys.exit("Chrome ou Chromium est introuvable.")
for source, sortie in CVS:
    sortie.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={sortie}", source.as_uri()], check=True, capture_output=True)
    print("✓ CV généré :", sortie)
