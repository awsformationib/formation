![Logo](images\logo.png)


## 🧩 Fiche 2.3 – Encapsulation, getters, setters, propriétés (CORRIGE)

* encapsulation stricte des attributs
* propriétés avec validation
* logique métier contrôlée pour le changement de statut
* affichage lisible et clair

---

### ✅ `vol_encapsule.py`

```
# vol_encapsule.py

class Vol:
    STATUTS_AUTORISES = ["prévu", "en cours", "terminé"]
    TRANSITIONS_VALIDES = {
        "prévu": ["en cours"],
        "en cours": ["terminé"],
        "terminé": []
    }

    def __init__(self, numero, destination, avion):
        self.__numero = numero
        self.__destination = destination
        self.__avion = avion  # objet Avion
        self.__statut = "prévu"

    # Propriété lecture seule
    @property
    def numero(self):
        return self.__numero

    # Propriété lecture/écriture
    @property
    def destination(self):
        return self.__destination

    @destination.setter
    def destination(self, nouvelle_destination):
        if isinstance(nouvelle_destination, str) and nouvelle_destination:
            self.__destination = nouvelle_destination
        else:
            raise ValueError("Destination invalide.")

    # Propriété lecture seule
    @property
    def avion(self):
        return self.__avion

    # Propriété lecture seule avec changement via méthode
    @property
    def statut(self):
        return self.__statut

    @property
    def en_cours(self):
        return self.__statut == "en cours"

    def changer_statut(self, nouveau_statut):
        if nouveau_statut not in self.STATUTS_AUTORISES:
            raise ValueError(f"Statut non reconnu : {nouveau_statut}")

        if nouveau_statut in self.TRANSITIONS_VALIDES[self.__statut]:
            self.__statut = nouveau_statut
            print(f"🔄 Statut du vol {self.__numero} changé en : {self.__statut}")
        else:
            print(f"❌ Transition invalide : {self.__statut} → {nouveau_statut}")

    def afficher_infos(self):
        print(f"✈️ Vol {self.__numero} vers {self.__destination} "
              f"[Statut : {self.__statut}] – Avion : {self.__avion.immatriculation}")

# === Exemple d’utilisation ===
if __name__ == "__main__":
    # Classe avion minimale pour tests rapide
    class Avion:
        def __init__(self, immatriculation, modele):
            self.immatriculation = immatriculation
            self.modele = modele

    avion_test = Avion("F-GKXJ", "A320")

    vol1 = Vol("AF123", "Lyon", avion_test)
    vol1.afficher_infos()

    vol1.changer_statut("en cours")
    vol1.afficher_infos()

    vol1.changer_statut("terminé")
    vol1.afficher_infos()

    # Test de transition invalide
    vol1.changer_statut("en cours")  # ❌ interdit

    # Test propriété calculée
    print("En cours ?", vol1.en_cours)  # False
```

---

### ✅ Résultat attendu (extrait) :

```
✈️ Vol AF123 vers Lyon [Statut : prévu] – Avion : F-GKXJ
🔄 Statut du vol AF123 changé en : en cours
✈️ Vol AF123 vers Lyon [Statut : en cours] – Avion : F-GKXJ
🔄 Statut du vol AF123 changé en : terminé
✈️ Vol AF123 vers Lyon [Statut : terminé] – Avion : F-GKXJ
❌ Transition invalide : terminé → en cours
En cours ? False
```
