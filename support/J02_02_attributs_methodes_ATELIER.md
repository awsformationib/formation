![Logo](images\logo.png)


## 🧩 Fiche 2.2 – Attributs & Méthodes (ATELIER)

---

```python
# avion_actions.py

class Avion:
    # Attribut de classe (partagé par toutes les instances)
    compteur = 0

    def __init__(self, immatriculation, modele):
        self.immatriculation = immatriculation  # Attribut d'instance
        self.modele = modele
        self.en_vol = False  # L’avion est au sol par défaut

        # Mise à jour du compteur à chaque création d'avion
        Avion.compteur += 1

    # Méthodes d'instance
    def decoller(self):
        if not self.en_vol:
            self.en_vol = True
            print(f"✈️ L'avion {self.immatriculation} a décollé.")
        else:
            print(f"⚠️ L'avion {self.immatriculation} est déjà en vol.")

    def atterrir(self):
        if self.en_vol:
            self.en_vol = False
            print(f"🛬 L'avion {self.immatriculation} a atterri.")
        else:
            print(f"⚠️ L'avion {self.immatriculation} est déjà au sol.")

    def afficher_etat(self):
        etat = "en vol" if self.en_vol else "au sol"
        print(f"🔍 Avion {self.immatriculation} ({self.modele}) est actuellement {etat}.")

    # Méthode de classe
    @classmethod
    def afficher_compteur(cls):
        print(f"📊 Nombre total d'avions créés : {cls.compteur}")

    # Méthode statique
    @staticmethod
    def afficher_aide():
        print("ℹ️ Un avion est un appareil capable de décoller et d'atterrir. Utilisez les méthodes .decoller() et .atterrir().")

# === Exemple d'utilisation ===
if __name__ == "__main__":
    # Appel de la méthode statique sans instance
    Avion.afficher_aide()

    # Création de deux avions
    a1 = Avion("F-GKXJ", "A320")
    a2 = Avion("F-HBXO", "B737")

    # Affichage état initial
    a1.afficher_etat()
    a2.afficher_etat()

    # Décollage du premier avion
    a1.decoller()
    a1.afficher_etat()

    # Tentative de décollage déjà en vol
    a1.decoller()

    # Atterrissage
    a1.atterrir()
    a1.afficher_etat()

    # Affichage du compteur global via méthode de classe
    Avion.afficher_compteur()
```

---

### ✅ Résultat attendu (extrait) :

```
ℹ️ Un avion est un appareil capable de décoller et d'atterrir. Utilisez les méthodes .decoller() et .atterrir().
🔍 Avion F-GKXJ (A320) est actuellement au sol.
🔍 Avion F-HBXO (B737) est actuellement au sol.
✈️ L'avion F-GKXJ a décollé.
🔍 Avion F-GKXJ (A320) est actuellement en vol.
⚠️ L'avion F-GKXJ est déjà en vol.
🛬 L'avion F-GKXJ a atterri.
🔍 Avion F-GKXJ (A320) est actuellement au sol.
📊 Nombre total d'avions créés : 2
```
