![Logo](images\logo.png)


## 🧩 Fiche 2.3 – Encapsulation, getters, setters, propriétés

**Objectif** : Protéger les données internes d’une classe, utiliser les conventions Python pour l'encapsulation, et maîtriser les propriétés avec `@property` et `@setter`.

---

### 🔎 Question rebond d’introduction

> ✈️ « Si un avion change d’état (ex. passe en vol) à cause d’un bug ou d’un script extérieur, comment s’assurer que cela reste contrôlé dans votre application ? »

Faire émerger les risques liés à l’accès direct aux attributs (`obj.attr = …`) et introduire les bonnes pratiques d’encapsulation.

---

### 🧠 Explication & contenu théorique

#### 1. Encapsulation en Python : pas d'interdiction, mais des conventions

| Syntaxe       | But                                | Exemple                       |
| ------------- | ---------------------------------- | ----------------------------- |
| `self.nom`    | Public (accès libre)               | `avion.nom = "A320"`          |
| `self._etat`  | Protégé (usage interne recommandé) | `avion._etat = "maintenance"` |
| `self.__code` | Privé (name mangling)              | `avion._Avion__code`          |

---

#### 2. Getters / Setters manuels

```python
class Avion:
    def __init__(self, immat):
        self.__immatriculation = immat

    def get_immatriculation(self):
        return self.__immatriculation

    def set_immatriculation(self, nouvelle_valeur):
        if nouvelle_valeur.startswith("F-"):
            self.__immatriculation = nouvelle_valeur
```

---

#### 3. Utiliser `@property` et `@<attr>.setter`

```python
class Avion:
    def __init__(self, immat):
        self.__immatriculation = immat

    @property
    def immatriculation(self):
        return self.__immatriculation

    @immatriculation.setter
    def immatriculation(self, valeur):
        if valeur.startswith("F-"):
            self.__immatriculation = valeur
        else:
            raise ValueError("Immatriculation invalide")
```

Utilisation :

```python
a = Avion("F-GKXJ")
print(a.immatriculation)       # getter
a.immatriculation = "F-HBXO"   # setter
```

---

### 🔧 Atelier pratique : `avion_etat.py`

> Objectif : Encapsuler proprement les données critiques d’un avion et fournir des méthodes d’accès contrôlées.

**Consignes :**

1. Créer une classe `Avion` avec les attributs suivants en **privé** :

   * `__immatriculation`
   * `__modele`
   * `__en_vol`
2. Créer les **propriétés** suivantes :

   * `immatriculation` (lecture + écriture avec validation)
   * `en_vol` (lecture seule)
3. Ajouter une méthode `changer_etat_vol()` qui permet de passer de `au sol` à `en vol`, mais uniquement via une logique métier contrôlée.
4. Tenter d’afficher directement `avion.__en_vol` : pourquoi cela échoue ?

---

### 📋 Résumé d’apprentissage

| Élément           | Exemple                               |
| ----------------- | ------------------------------------- |
| Attribut privé    | `self.__en_vol`                       |
| Getter classique  | `def get_immat(self):`                |
| `@property`       | `@property def immat(self):`          |
| `@setter`         | `@immat.setter def immat(self, val):` |
| Protection métier | `if valeur.startswith(...)`           |

---

### 🧪 Évaluation rapide (optionnel)

> ❓ Que signifie `@property` en Python ?
> ❓ Que se passe-t-il si on écrit `avion.__en_vol = True` ?
> ❓ Pourquoi les doubles underscores rendent l’attribut inaccessible directement ?
