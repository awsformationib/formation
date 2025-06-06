from pathlib import Path
import csv
from random import choice, randint
from uuid import uuid4

# Définition simplifiée
class Vol:
    def __init__(self, numero, destination, statut):
        self.id = str(uuid4())
        self.numero = numero
        self.destination = destination
        self.statut = statut

    def __str__(self):
        return f"{self.numero} → {self.destination} [{self.statut}]"

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

# Export CSV avec pathlib
dossier = Path("../exports")
dossier.mkdir(exist_ok=True)

chemin_csv = dossier / "vols_jour.csv"

with chemin_csv.open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Numéro", "Destination", "Statut"])
    for vol in vols:
        writer.writerow([vol.id, vol.numero, vol.destination, vol.statut])

print(f"✅ Export terminé : {chemin_csv}")

# Vérifier l’existence
if chemin_csv.exists():
    print(f"✅ Fichier trouvé : {chemin_csv}")

    # Lire et afficher le contenu
    with chemin_csv.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        print("\n📄 Contenu du fichier :")
        for ligne in reader:
            print(ligne)
else:
    print("❌ Fichier non trouvé.")
