![Logo](images\logo.png)


## 🧩 Fiche 2.1 – Classe & Instance (ATELIER)

```python
# avion_objet.py

class Avion:
    def __init__(self, immatriculation, modele):
        """Initialise un nouvel avion avec une immatriculation et un modèle."""
        self.immatriculation = immatriculation
        self.modele = modele

    def afficher_infos(self):
        """Affiche les informations de l’avion."""
        print(f"Avion {self.immatriculation}, modèle {self.modele}")

# Création de deux avions
avion1 = Avion("F-GKXJ", "A320")
avion2 = Avion("F-HBXO", "B737")

# Affichage des informations
avion1.afficher_infos()
avion2.afficher_infos()
```

---

### ✅ Résultat attendu à l’exécution :

```
Avion F-GKXJ, modèle A320
Avion F-HBXO, modèle B737
```
