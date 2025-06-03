![Logo](images\logo.png)


## 🧩 Fiche 2.4 – Méthodes spéciales

**Objectif** : Apprendre à rendre ses objets lisibles, comparables, et compatibles avec les structures de données Python comme les `set` ou les clés de dictionnaires.

---

### 🔎 Question rebond d’introduction

> ✈️ « Quand vous affichez un objet dans la console, ou que vous comparez deux objets `Vol`, comment Python sait ce qu’il doit faire ? »

---

### 🧠 Explication & contenu théorique

Les **méthodes spéciales** sont des fonctions prédéfinies que Python appelle **automatiquement** dans certaines situations. Elles commencent et finissent par `__`.

---

### 📦 1. Affichage : `__str__()` vs `__repr__()`

```python
class Avion:
    def __str__(self):
        return f"Avion {self.immatriculation}"

    def __repr__(self):
        return f"Avion('{self.immatriculation}', '{self.modele}')"
```

| Méthode    | Utilisé par           | But                           |
| ---------- | --------------------- | ----------------------------- |
| `__str__`  | `print(obj)`          | Lisible pour les humains      |
| `__repr__` | Console / `repr(obj)` | Lisible pour les développeurs |

---

### 🟰 2. Comparaison : `__eq__()`, `__lt__()`, etc.

```python
def __eq__(self, other):
    return self.numero == other.numero

def __lt__(self, other):
    return self.numero < other.numero
```

| Méthode  | Comparaison |
| -------- | ----------- |
| `__eq__` | `==`        |
| `__ne__` | `!=`        |
| `__lt__` | `<`         |
| `__le__` | `<=`        |
| `__gt__` | `>`         |
| `__ge__` | `>=`        |

---

### 🔐 3. Hashabilité : `__hash__()`

```python
def __hash__(self):
    return hash((self.numero, self.destination))
```

* Permet d’utiliser un objet comme **clé de dictionnaire** ou **élément d’un `set`**
* Doit être cohérent avec `__eq__` : deux objets égaux doivent avoir le même `hash`

---

### 🔧 Atelier pratique : `vol_comparable.py`

> Objectif : créer une classe `Vol` qui :

* s’affiche joliment
* peut être comparée à d’autres
* peut être mise dans un `set`

**Consignes** :

1. Reprendre la classe `Vol`
2. Ajouter :

   * `__str__()` → humain
   * `__repr__()` → développeur
   * `__eq__()` → deux vols sont égaux s’ils ont le même numéro
   * `__lt__()` → tri par numéro
   * `__hash__()` → pour l’ajout dans un set
3. Créer une liste de vols + un set de vols
4. Trier les vols, afficher, dédupliquer via set

---

### 📋 Résumé d’apprentissage

| Dunder     | Utilité                        | Exemple                  |
| ---------- | ------------------------------ | ------------------------ |
| `__str__`  | Affichage `print()`            | `"Vol AF123 vers Nice"`  |
| `__repr__` | Debug / logs                   | `"Vol('AF123', 'Nice')"` |
| `__eq__`   | Comparaison `==`               | `vol1 == vol2`           |
| `__lt__`   | Tri avec `sorted()`            | `sorted(vols)`           |
| `__hash__` | Utilisation dans `set`, `dict` | `set([vol1, vol2])`      |

---

### 🧪 Évaluation rapide (optionnel)

1. Quelle est la différence entre `__str__()` et `__repr__()` ?
2. Que permet l’ajout de `__lt__()` dans une classe ?
3. Pourquoi faut-il implémenter `__hash__()` avec `__eq__()` ?
