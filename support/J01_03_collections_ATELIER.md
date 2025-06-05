![Logo](images\logo.png)


## 🧩 Fiche 1.3 – Listes, Dictionnaires, Tuples, Ensembles (ATELIER)

```
# analyse_flotte.py

# Liste de vols (chaque vol est un dictionnaire)
vols = [
    {"numero": "AF123", "destination": "Nice", "immatriculation": "F-GKXJ"},
    {"numero": "LH456", "destination": "Berlin", "immatriculation": "D-ABCD"},
    {"numero": "BA789", "destination": "Londres", "immatriculation": "G-EUPT"},
    {"numero": "AF124", "destination": "Nice", "immatriculation": "F-GKXJ"},
]

# 1. Extraire toutes les immatriculations distinctes
immatriculations_uniques = {vol["immatriculation"] for vol in vols}

print("Immatriculations distinctes :")
for immat in immatriculations_uniques:
    print("-", immat)

# 2. Compter les vols par destination
compteur_destinations = {}

for vol in vols:
    destination = vol["destination"]
    if destination in compteur_destinations:
        compteur_destinations[destination] += 1
    else:
        compteur_destinations[destination] = 1

print("\nNombre de vols par destination :")
for ville, nb in compteur_destinations.items():
    print(f"- {ville} : {nb} vol(s)")

# 3. Fonction d’affichage d’un vol
def afficher_vol(vol):
    print(f"Vol {vol['numero']} vers {vol['destination']} - immatriculation {vol['immatriculation']}")

print("\nAffichage détaillé des vols :")
for vol in vols:
    afficher_vol(vol)

# 4. Liste de tuples (numero, destination)
vols_simplifies = [(vol["numero"], vol["destination"]) for vol in vols]

print("\nVols simplifiés (tuples) :")
for numero, dest in vols_simplifies:
    print(f"- {numero} -> {dest}")
```

---

### Résultat attendu (exemple) :

```
Immatriculations distinctes :
- F-GKXJ
- D-ABCD
- G-EUPT

Nombre de vols par destination :
- Nice : 2 vol(s)
- Berlin : 1 vol(s)
- Londres : 1 vol(s)

Affichage détaillé des vols :
Vol AF123 vers Nice - immatriculation F-GKXJ
Vol LH456 vers Berlin - immatriculation D-ABCD
Vol BA789 vers Londres - immatriculation G-EUPT
Vol AF124 vers Nice - immatriculation F-GKXJ

Vols simplifiés (tuples) :
- AF123 -> Nice
- LH456 -> Berlin
- BA789 -> Londres
- AF124 -> Nice
```
