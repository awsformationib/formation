from collections import defaultdict, deque, namedtuple, Counter
from random import choice, randint
from uuid import uuid4

# Définition minimale pour les besoins du test
class Vol:
    def __init__(self, numero, destination):
        self.id = str(uuid4())
        self.numero = numero
        self.destination = destination

    def __str__(self):
        return f"{self.numero} → {self.destination}"

# Génération de vols simulés
VILLES = ["Lyon", "Nice", "Toulouse", "Lille", "Bordeaux"]
COMPAGNIES = ["AF", "BA", "LH", "IB"]

def generer_vol():
    numero = f"{choice(COMPAGNIES)}{randint(100,999)}"
    destination = choice(VILLES)
    return Vol(numero, destination)

vols = [generer_vol() for _ in range(15)]

# 1. Grouper les vols par destination
vols_par_destination = defaultdict(list)
for vol in vols:
    vols_par_destination[vol.destination].append(vol)

# 2. File d’attente avec deque
file_decollage = deque(v for v in vols if v.destination == "Lyon")

# 3. Statistiques avec Counter
statistiques = Counter(vol.destination for vol in vols)

# 4. Export simplifié avec namedtuple
VolTuple = namedtuple("VolTuple", ["numero", "destination"])
vols_tuples = [VolTuple(vol.numero, vol.destination) for vol in vols]

# Affichage des résultats
print("✈️ Vols par destination :")
for ville, vols_liste in vols_par_destination.items():
    print(f"{ville} ({len(vols_liste)} vols)")

print("\n🛫 File de décollage pour Lyon :")
while file_decollage:
    vol = file_decollage.popleft()
    print(f"Décollage de {vol}")

print("\n📊 Statistiques globales :")
for ville, count in statistiques.items():
    print(f"{ville} : {count} vols")

print("\n📋 Export simple des vols :")
for v in vols_tuples[:5]:
    print(v)
