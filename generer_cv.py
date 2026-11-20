"""Génère ressources/cv/cv-general.pdf à partir de cv_source/cv-general.html (Chrome ou Chromium requis).

Pour modifier le CV : éditer cv_source/cv-general.html, puis lancer : python3 generer_cv.py
Le PDF est publié tel quel sur le site : n'y mettre ni téléphone ni adresse personnelle.
"""
import shutil
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent
SOURCE = RACINE / "cv_source" / "cv-general.html"
SORTIE = RACINE / "ressources" / "cv" / "cv-general.pdf"
CANDIDATS = (
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    shutil.which("google-chrome") or "", shutil.which("chromium") or "", shutil.which("chromium-browser") or "",
)
chrome = next((c for c in CANDIDATS if c and Path(c).exists()), None)
if not chrome:
    sys.exit("Chrome ou Chromium est introuvable.")
SORTIE.parent.mkdir(parents=True, exist_ok=True)
subprocess.run([chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                f"--print-to-pdf={SORTIE}", SOURCE.as_uri()], check=True, capture_output=True)
print("✓ CV généré :", SORTIE)
