import json
from pathlib import Path
from random import choice, randint
from uuid import uuid4

# Définition simplifiée
class Vol:
    def __init__(self, numero, destination, statut):
        self.id = str(uuid4())
        self.numero = numero
        self.destination = destination
        self.statut = statut

    def to_dict(self):
        return {
            "id": self.id,
            "numero": self.numero,
            "destination": self.destination,
            "statut": self.statut
        }

# Génération de vols simulés
VILLES = ["Lyon", "Nice", "Toulouse", "Bordeaux", "Lille"]
COMPAGNIES = ["AF", "BA", "LH", "IB"]
STATUTS = ["prévu", "en cours", "terminé"]

def generer_vol():
    numero = f"{choice(COMPAGNIES)}{randint(100,999)}"
    destination = choice(VILLES)
    statut = choice(STATUTS)
    return Vol(numero, destination, statut)

vols = [generer_vol() for _ in range(10)]

# Export JSON avec pathlib
dossier = Path("exports")
dossier.mkdir(exist_ok=True)

chemin_json = dossier / "vols.json"

vols_data = [vol.to_dict() for vol in vols]

with chemin_json.open("w", encoding="utf-8") as f:
    json.dump(vols_data, f, indent=4, ensure_ascii=False)

print(f"✅ Export JSON terminé : {chemin_json}")

# Lecture JSON
if chemin_json.exists():
    with chemin_json.open(encoding="utf-8") as f:
        data = json.load(f)
        print("\n📄 Vols importés depuis le fichier JSON :")
        for vol_dict in data:
            print(f"{vol_dict['numero']} → {vol_dict['destination']} [{vol_dict['statut']}]")
else:
    print("❌ Fichier JSON non trouvé.")
