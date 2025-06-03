![Logo](images\logo.png)


## 🧩 Fiche 2.4 – Méthodes spéciales (EXO)

---

## 🧩 Fiche d’exercice – Compléter les méthodes spéciales dans une classe `Vol`

**Objectif pédagogique** : Apprendre à rendre les objets de la classe `Vol` affichables, comparables, triables et utilisables dans un set ou comme clés de dictionnaire.

---

### 🔎 Contexte

> ✈️ Vous avez une liste de vols (`Vol`) à gérer. Pour les afficher correctement, les comparer ou les organiser, vous devez implémenter plusieurs méthodes spéciales. Certaines sont déjà partiellement rédigées, à vous de les compléter.

---

### 📄 Code de départ (`vol_comparable.py` – à compléter)

```python
# vol_comparable.py

class Vol:
    def __init__(self, numero, destination):
        self.numero = numero
        self.destination = destination

    # ✅ A compléter : rendre l’objet lisible par un humain
    def __str__(self):
        pass

    # ✅ A compléter : représentation développeur
    def __repr__(self):
        pass

    # ✅ A compléter : deux vols sont égaux si le numéro est identique
    def __eq__(self, other):
        pass

    # ✅ A compléter : permet de trier les vols
    def __lt__(self, other):
        pass

    # ✅ A compléter : permet l’usage dans un set
    def __hash__(self):
        pass
```

---

### 🧪 Partie test à utiliser

```python
if __name__ == "__main__":
    vols = [
        Vol("AF123", "Lyon"),
        Vol("AF456", "Nice"),
        Vol("AF123", "Paris"),
        Vol("BA789", "Londres"),
    ]

    print("✅ Affichage brut :")
    for vol in vols:
        print(vol)

    print("\n🔢 Tri des vols :")
    for vol in sorted(vols):
        print(repr(vol))

    print("\n🧹 Suppression des doublons via set :")
    vols_uniques = set(vols)
    for vol in vols_uniques:
        print(vol)

    print("\n🔁 Comparaison de deux objets :")
    v1 = Vol("AF123", "Lyon")
    v2 = Vol("AF123", "Paris")
    print("v1 == v2 ?", v1 == v2)
```

---

### 🧠 Objectifs attendus

1. `print(vol)` affiche une phrase lisible du type :
   `Vol AF123 à destination de Lyon`

2. `repr(vol)` donne quelque chose comme :
   `Vol('AF123', 'Lyon')`

3. `vol1 == vol2` est `True` si `numero` est identique

4. Les objets peuvent être ajoutés dans un `set` sans doublon logique

5. La fonction `sorted(vols)` trie les objets par `numero` (ordre alphanumérique)

---

### 📋 Résumé des signatures à compléter

```python
def __str__(self): ...
def __repr__(self): ...
def __eq__(self, other): ...
def __lt__(self, other): ...
def __hash__(self): ...
```
