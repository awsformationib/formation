![Logo](images\logo.png)


## 🧩 Fiche Module Standard #5 – `dataclasses`

**Objectif** : Simplifier la déclaration de classes orientées données (comme `Avion`, `Piste`, `Vol`) à l’aide du décorateur `@dataclass`, en réduisant le code sans sacrifier la clarté ni les comportements personnalisés.

---

### 🔎 Question rebond d’introduction

> ✈️ « Si je veux créer une classe juste pour stocker des infos (comme un avion avec immatriculation et modèle), suis-je obligé d’écrire un `__init__`, un `__repr__`, un `__eq__`, etc. à chaque fois ? »

---

### 🧠 Explication & contenu théorique

Le module `dataclasses` permet de :

* créer des classes **orientées données** avec très peu de code
* générer automatiquement `__init__`, `__repr__`, `__eq__`, etc.
* définir des **valeurs par défaut**, des **types**, et des **comportements personnalisés**

#### Exemple minimal :

```
from dataclasses import dataclass

@dataclass
class Avion:
    immatriculation: str
    modele: str
```

Résultat :

* `Avion("F-GKXJ", "A320")` fonctionne sans écrire `__init__`
* `print(avion)` donne : `Avion(immatriculation='F-GKXJ', modele='A320')`

---

### ✈️ Intégration dans `AirOps`

```
from dataclasses import dataclass
from uuid import uuid4

@dataclass
class Avion:
    immatriculation: str
    modele: str
    id: str = str(uuid4())  # Valeur par défaut générée
```

⚠️ Attention : si `uuid4()` est mis directement comme valeur par défaut, il est partagé par tous (piège classique). Utiliser `field(default_factory=...)` pour générer une valeur unique à chaque instance :

```
from dataclasses import dataclass, field
from uuid import uuid4

@dataclass
class Avion:
    immatriculation: str
    modele: str
    id: str = field(default_factory=lambda: str(uuid4()))
```

---

### 🔧 Atelier pratique – `avion_dataclass.py`

1. Réécrire la classe `Avion` avec `@dataclass`
2. Ajouter un champ `id` généré automatiquement avec `uuid4()`
3. Créer 2 avions, les afficher, les comparer
4. Bonus : rendre `Avion` **immuable** (`frozen=True`) pour empêcher la modification après création

---

### 📋 Résumé d’apprentissage

| Élément                      | Avantage                                        | Exemple                                |
| ---------------------------- | ----------------------------------------------- | -------------------------------------- |
| `@dataclass`                 | évite d’écrire `__init__`, `__repr__`, `__eq__` | `@dataclass class Vol:`                |
| `field(default_factory=...)` | valeur générée dynamiquement                    | `id: str = field(default_factory=...)` |
| `frozen=True`                | objet non modifiable                            | `@dataclass(frozen=True)`              |
| Typage                       | plus lisible                                    | `numero: str`                          |

---

### 🧪 Évaluation rapide

1. Quelle est la différence entre `@dataclass` et une classe manuelle ?
2. Que fait `field(default_factory=uuid4)` ?
3. Peut-on ajouter des méthodes dans une `@dataclass` ? (→ Oui, totalement)

