![Logo](images\logo.png)


## 🧩 Fiche 2.2 – Attributs & Méthodes

**Objectif pédagogique** : Comprendre comment ajouter des comportements aux objets Python à l’aide de méthodes, bien manipuler les attributs d’instance, et découvrir les particularités Python comme les méthodes de classe (`@classmethod`) et statiques (`@staticmethod`).

---

### 🔎 Question rebond d’introduction

> ✈️ « Si un avion peut décoller ou atterrir, comment le représenter dans notre programme sans avoir à le coder à chaque fois à l’extérieur ? »

---

### 🧠 Explication & contenu théorique

#### 1. Méthodes liées à l’instance (méthodes classiques)

```python
class Avion:
    def __init__(self, immatriculation):
        self.immatriculation = immatriculation
        self.en_vol = False

    def decoller(self):
        self.en_vol = True

    def atterrir(self):
        self.en_vol = False
```

* `self` est toujours le **premier paramètre** des méthodes d’instance
* on accède aux **attributs de l’objet** avec `self.nom_attribut`

---

#### 2. Attributs d’instance vs attributs de classe

```python
class Avion:
    type_appareil = "Avion"  # attribut de classe (partagé)

    def __init__(self, immatriculation):
        self.immatriculation = immatriculation  # attribut d'instance
```

* L’attribut `type_appareil` est **commun à tous les objets**
* Les attributs définis dans `__init__` sont **propres à chaque objet**

---

#### 3. Méthodes de classe (`@classmethod`)

```python
class Avion:
    compteur = 0

    def __init__(self, immatriculation):
        self.immatriculation = immatriculation
        Avion.compteur += 1

    @classmethod
    def combien_de_avions(cls):
        return cls.compteur
```

* `@classmethod` utilise `cls` au lieu de `self`
* elle agit sur la **classe elle-même**, pas sur une instance

---

#### 4. Méthodes statiques (`@staticmethod`)

```python
class Avion:
    @staticmethod
    def aide():
        print("Un avion est un appareil capable de voler.")
```

* Ne reçoit ni `self` ni `cls`
* Utile pour des **utilitaires** liés à la classe mais indépendants de toute instance

---

### 🔧 Atelier pratique : `avion_actions.py`

1. Reprendre la classe `Avion`
2. Ajouter :

   * Un attribut `en_vol` initialisé à `False`
   * Deux méthodes : `decoller()` et `atterrir()`
3. Ajouter :

   * Un attribut de classe `compteur` pour compter le nombre d’avions créés
   * Une méthode de classe `afficher_compteur()` qui affiche ce nombre
4. Ajouter une méthode statique `afficher_aide()` expliquant ce qu’est un avion
5. Tester tous les comportements dans un `main`

---

### 📋 Résumé d’apprentissage

| Élément             | Exemple                | Particularité         |
| ------------------- | ---------------------- | --------------------- |
| Méthode d’instance  | `def decoller(self)`   | Accès à `self`        |
| Attribut d’instance | `self.en_vol`          | Propre à chaque objet |
| Attribut de classe  | `Avion.compteur`       | Partagé par tous      |
| Méthode de classe   | `@classmethod` + `cls` | Agit sur la classe    |
| Méthode statique    | `@staticmethod`        | Indépendante          |

---

### 🧪 Évaluation rapide (optionnel)

> ❓ Quelle est la différence entre une méthode statique et une méthode de classe ?
> ❓ À quel moment préférer un attribut de classe plutôt qu’un attribut d’instance ?
> ❓ Que renvoie cette ligne : `Avion.afficher_compteur()` si aucun avion n’a été créé ?

---
