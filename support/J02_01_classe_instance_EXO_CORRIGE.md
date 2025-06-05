![Logo](images\logo.png)


## 🧩 Fiche – Exercices : Classes simples & Attributs (CORRIGE)

---

### ✅ `piste.py`

```
# piste.py

class Piste:
    def __init__(self, numero, longueur_m, est_occupee=False):
        self.numero = numero
        self.longueur_m = longueur_m
        self.est_occupee = est_occupee

    def afficher_infos(self):
        etat = "occupée" if self.est_occupee else "libre"
        print(f"Piste {self.numero} ({self.longueur_m} m) - État : {etat}")

# Exemple d'utilisation
p1 = Piste("27L", 3900)
p2 = Piste("09R", 3500, est_occupee=True)

p1.afficher_infos()
p2.afficher_infos()
```

---

### ✅ `pilote.py`

```
# pilote.py

class Pilote:
    def __init__(self, nom, prenom, licence):
        self.nom = nom
        self.prenom = prenom
        self.licence = licence

    def nom_complet(self):
        return f"{self.prenom} {self.nom}"

    def afficher_infos(self):
        print(f"Pilote {self.nom_complet()} – Licence : {self.licence}")

# Exemple d'utilisation
p1 = Pilote("Martin", "Jean", "FR-45678")
p2 = Pilote("Dupont", "Anna", "FR-78901")
p3 = Pilote("Klein", "Marc", "DE-12345")

for pilote in [p1, p2, p3]:
    pilote.afficher_infos()
```

---

### ✅ `affectation.py`

```
# affectation.py

from pilote import Pilote
from avion_objet import Avion  # à adapter selon ton import réel


class Affectation:
    def __init__(self, pilote, avion):
        self.pilote = pilote
        self.avion = avion

    def afficher_affectation(self):
        print(
            f"Pilote {self.pilote.nom_complet()} ({self.pilote.licence}) "
            f"affecté à l’avion {self.avion.immatriculation} ({self.avion.__modele})"
        )


# Exemple d'utilisation
if __name__ == "__main__":
    pilote = Pilote("Martin", "Jean", "FR-45678")
    avion = Avion("F-GKXJ", "A320")
    mission = Affectation(pilote, avion)
    mission.afficher_affectation()
```
