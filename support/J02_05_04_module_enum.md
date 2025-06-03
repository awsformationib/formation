![Logo](images\logo.png)


## 🧩 Fiche Module Standard #4 – `enum`

**Objectif** : Utiliser `enum.Enum` pour définir des **valeurs fixes et nommées** dans les objets Python, afin d’éviter les erreurs de saisie, centraliser les statuts, et fiabiliser la logique métier.

---

### 🔎 Question rebond d’introduction

> ✈️ « Si je code en dur des chaînes comme `'prévu'`, `'en cours'`, `'terminé'` dans les méthodes de mes classes, comment éviter les fautes de frappe et garantir que seules ces valeurs soient utilisées ? »

---

### 🧠 Explication & contenu théorique

Le module `enum` permet de définir des **types énumérés**, c’est-à-dire un ensemble **fermé de valeurs possibles**, clairement nommées, facilement comparables.

#### Exemple :

```python
from enum import Enum

class StatutVol(Enum):
    PREVU = "prévu"
    EN_COURS = "en cours"
    TERMINE = "terminé"
```

* Comparaison sécurisée : `vol.statut == StatutVol.PREVU`
* Valeur de chaîne : `vol.statut.value → "prévu"`

---

### ✈️ Intégration dans `Vol`

```python
from enum import Enum

class StatutVol(Enum):
    PREVU = "prévu"
    EN_COURS = "en cours"
    TERMINE = "terminé"

class Vol:
    def __init__(self, numero, destination, avion):
        self.numero = numero
        self.destination = destination
        self.avion = avion
        self.statut = StatutVol.PREVU

    def changer_statut(self, nouveau_statut):
        if isinstance(nouveau_statut, StatutVol):
            self.statut = nouveau_statut
```

---

### 🔧 Atelier pratique – `vol_enum.py`

1. Créer une énumération `StatutVol` avec 3 statuts

2. Remplacer tous les statuts sous forme de chaîne dans la classe `Vol`

3. Afficher le nom du statut dans `__str__` :

   * `Vol AF123 – Statut : prévu`
   * via `self.statut.value`

4. Bonus :

   * Ajouter un `__str__` à l’`Enum` pour raccourcir l’affichage
   * Utiliser `Enum.auto()` pour simplifier les valeurs (si on n’a pas besoin de chaînes précises)

---

### 📋 Résumé d’apprentissage

| Élément         | Utilisation                  | Avantage                          |
| --------------- | ---------------------------- | --------------------------------- |
| `Enum`          | `StatutVol.EN_COURS`         | Code lisible, sécurisé            |
| `.value`        | `"prévu"`                    | Extraction texte                  |
| Comparaison     | `==`                         | Plus sûr que comparer des strings |
| Contrôle métier | `isinstance(val, StatutVol)` | Validation robuste                |

---

### 🧪 Évaluation rapide

1. Que vaut `StatutVol.PREVU.value` ?
2. Que se passe-t-il si on écrit `vol.statut = "en cours"` au lieu de `StatutVol.EN_COURS` ?
3. Peut-on afficher directement un `Enum` dans une phrase ? (→ `str(statut)` ou `statut.value`)

