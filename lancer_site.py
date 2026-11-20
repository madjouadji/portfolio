"""Une seule commande pour reconstruire et ouvrir le site personnel."""
from pathlib import Path
import webbrowser
from build import construire_site

if __name__ == "__main__":
    construire_site()
    page = Path(__file__).resolve().parent / "site" / "index.html"
    webbrowser.open(page.as_uri())
    print("✅ Site ouvert. Actualise la page si nécessaire.")
