![Logo](images\logo.png)


## 🧩 Fiche 2.3 – Encapsulation, getters, setters, propriétés (ATELIER)

---

```
# avion_etat.py

class Avion:
    def __init__(self, immatriculation, modele):
        self.__immatriculation = immatriculation
        self.__modele = modele
        self.__en_vol = False  # Privé, ne doit pas être modifié directement

    # Propriété en lecture seule pour l'état en vol
    @property
    def en_vol(self):
        return self.__en_vol

    # Propriété pour immatriculation, avec validation
    @property
    def immatriculation(self):
        return self.__immatriculation

    @immatriculation.setter
    def immatriculation(self, nouvelle_valeur):
        if nouvelle_valeur.startswith("F-"):
            self.__immatriculation = nouvelle_valeur
        else:
            raise ValueError("Immatriculation invalide : doit commencer par 'F-'")

    # Méthode métier contrôlant la transition d’état
    def changer_etat_vol(self, action):
        if action == "decoller":
            if not self.__en_vol:
                self.__en_vol = True
                print(f"✈️ L'avion {self.__immatriculation} a décollé.")
            else:
                print(f"⚠️ L'avion {self.__immatriculation} est déjà en vol.")
        elif action == "atterrir":
            if self.__en_vol:
                self.__en_vol = False
                print(f"🛬 L'avion {self.__immatriculation} a atterri.")
            else:
                print(f"⚠️ L'avion {self.__immatriculation} est déjà au sol.")
        else:
            print(f"❓ Action inconnue : {action}")

    def afficher_infos(self):
        etat = "en vol" if self.__en_vol else "au sol"
        print(f"🔍 Avion {self.__immatriculation}, modèle {self.__modele}, actuellement {etat}")

# === Exemple d’utilisation ===
if __name__ == "__main__":
    avion = Avion("F-GKXJ", "A320")

    avion.afficher_infos()
    avion.changer_etat_vol("decoller")
    avion.changer_etat_vol("decoller")
    avion.changer_etat_vol("atterrir")
    avion.afficher_infos()

    print("\n🔧 Test de lecture contrôlée :")
    print("En vol :", avion.en_vol)

    print("\n🔧 Changement d’immatriculation avec validation :")
    avion.immatriculation = "F-HBXO"
    print("Nouvelle immatriculation :", avion.immatriculation)

    # Ligne suivante provoque une erreur volontairement :
    # avion.immatriculation = "XYZ123"

    # Tentative d’accès direct à l’attribut privé :
    print("\n🔒 Tentative d’accès direct à __en_vol :", end=" ")
    try:
        print(avion.__en_vol)
    except AttributeError as e:
        print("ERREUR :", e)
```

---

### ✅ Résultat attendu (extrait) :

```
🔍 Avion F-GKXJ, modèle A320, actuellement au sol
✈️ L'avion F-GKXJ a décollé.
⚠️ L'avion F-GKXJ est déjà en vol.
🛬 L'avion F-GKXJ a atterri.
🔍 Avion F-GKXJ, modèle A320, actuellement au sol

🔧 Test de lecture contrôlée :
En vol : False

🔧 Changement d’immatriculation avec validation :
Nouvelle immatriculation : F-HBXO

🔒 Tentative d’accès direct à __en_vol : ERREUR : 'Avion' object has no attribute '__en_vol'
```
