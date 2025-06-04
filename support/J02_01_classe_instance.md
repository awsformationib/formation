![Logo](images\logo.png)


## 🧩 Fiche 2.1 – Classe & Instance

**Objectif pédagogique** : Comprendre comment créer ses propres types d’objets à l’aide de classes, les instancier, et manipuler leurs attributs dans le cadre de la gestion d’une flotte d’avions.

---

### 🔎 Question rebond d’introduction

> ✈️ « Si un avion a une immatriculation et un modèle, et qu’il doit être manipulé souvent, comment éviter de gérer ces infos sous forme de simples dictionnaires ? »

Faire émerger la notion de **classe** comme plan de construction, et d’**objet** comme instance concrète.

---

### 🧠 Explication & contenu théorique

#### 1. Définir une classe

```
class Avion:
    pass
```

#### 2. Ajouter un constructeur `__init__`

```
class Avion:
    def __init__(self, immatriculation, modele):
        self.immatriculation = immatriculation
        self.modele = modele
```

* `__init__` : méthode appelée automatiquement à l’instanciation
* `self` : référence à l’objet lui-même
* `self.immatriculation` : création d’un **attribut d’instance**

#### 3. Créer une instance

```
a1 = Avion("F-GKXJ", "A320")
print(a1.immatriculation)  # → "F-GKXJ"
```

---

### 🔧 Atelier pratique : `avion_objet.py`

> Objectif : créer une classe `Avion`, l’instancier, accéder à ses attributs.

**Consignes :**

1. Créer une classe `Avion` avec deux attributs : `immatriculation` et `modele`
2. Dans le `main`, créer deux avions distincts
3. Afficher leurs attributs
4. Ajouter une méthode `afficher_infos()` dans la classe qui affiche les deux infos

---

### 🧪 Exemple attendu :

```python
Avion F-GKXJ, modèle A320
Avion F-HBXO, modèle B737
```

---

### 📋 Résumé d’apprentissage

| Élément             | Exemple                      |
| ------------------- | ---------------------------- |
| Déclaration         | `class Avion:`               |
| Constructeur        | `def __init__(self, ...)`    |
| Attribut d’instance | `self.immatriculation = ...` |
| Instanciation       | `avion1 = Avion(...)`        |
| Accès               | `avion1.modele`              |

---

### 🧪 Évaluation rapide (optionnel)

**❓ Que fait le code suivant ?**

```python
class Vol:
    def __init__(self, numero):
        self.numero = numero

v = Vol("AF123")
print(v.numero)
```

**❓ Peut-on créer un objet sans `__init__` ?**

---
