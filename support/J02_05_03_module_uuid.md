![Logo](images\logo.png)


## 🧩 Fiche Module Standard #3 – `uuid`

**Objectif** : Utiliser le module `uuid` pour attribuer des identifiants uniques non ambigus à chaque instance d’objet (vol, avion, affectation…).

---

### 🔎 Question rebond d’introduction

> ✈️ « Si je veux m’assurer que chaque vol, chaque avion ou chaque affectation possède un identifiant unique (même si deux objets ont le même nom ou numéro), comment faire simplement ? »

---

### 🧠 Explication & contenu théorique

Le module `uuid` permet de générer des **identifiants universellement uniques**. Il est très utile pour :

* différencier deux objets ayant des attributs identiques (ex. deux vols "AF123")
* indexer des objets dans une base de données ou un système distribué
* garantir l’unicité sans avoir à gérer manuellement les ID

#### Exemple :

```
import uuid

id_unique = uuid.uuid4()
print(id_unique)  # Exemple : 20a62738-79aa-4c77-a4f3-e73f13b9dc9c
```

---

### ✈️ Intégration dans le projet `AirOps`

Ajouter un identifiant unique dans chaque objet `Avion` ou `Vol` :

```
import uuid

class Avion:
    def __init__(self, immatriculation, modele):
        self.id = uuid.uuid4()
        self.immatriculation = immatriculation
        self.modele = modele
```

Affichage possible dans `__repr__()` ou lors de l’export (CSV, JSON).

---

### 🔧 Atelier pratique – `vol_uuid.py`

1. Ajouter un attribut `id` à la classe `Vol` généré par `uuid.uuid4()`
2. Modifier `__repr__()` pour inclure l’ID
3. Créer plusieurs vols ayant le même `numero` mais des `uuid` différents
4. Ajouter un test d’égalité avec `==` basé sur `numero` seulement → montrer que `uuid` garantit l’unicité même si logique métier ≠

---

### 📋 Résumé d’apprentissage

| Fonction           | Usage                                  | Exemple                        |
| ------------------ | -------------------------------------- | ------------------------------ |
| `uuid.uuid4()`     | Génère un identifiant aléatoire unique | `'c913…b7f2'`                  |
| Attribut `self.id` | Ajouté à `Vol`, `Avion`, `Affectation` | `self.id = uuid.uuid4()`       |
| Affichage          | Utiliser dans `__repr__()` ou logs     | `Vol('AF123', 'Nice', id=...)` |

---

### 🧪 Évaluation rapide

1. Que garantit `uuid.uuid4()` ?
2. Peut-on utiliser cet identifiant dans un set ? (Oui, il est hashable)
3. Quelle est la différence entre `numero` et `uuid` dans une classe métier ?

---
