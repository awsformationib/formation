![Logo](images\logo.png)


## 🧩 Fiche Module Standard #6 – `typing`

**Objectif** : Utiliser le module `typing` pour annoter les types des attributs, arguments, et valeurs de retour, afin d’améliorer la lisibilité, la robustesse et l’auto-complétion des objets dans les projets Python.

---

### 🔎 Question rebond d’introduction

> ✈️ « Si je lis une méthode `changer_statut(x)` dans une classe, comment puis-je savoir à quoi sert `x` sans lire tout le corps de la fonction ? »

---

### 🧠 Explication & contenu théorique

Le module `typing` permet d’**annoter les types** :

* des attributs dans les classes
* des paramètres et valeurs de retour
* des collections (`List`, `Dict`, `Optional`, etc.)

Cela :

* **n’empêche pas l’exécution** (Python reste dynamique)
* mais **aide les IDE, outils de type-checking (mypy), relectures de code**

#### Exemple simple :

```python
from typing import List, Optional

def get_pilotes_disponibles(code: str) -> List[str]:
    ...

def trouver_piste(numero: str) -> Optional["Piste"]:
    ...
```

---

### ✈️ Intégration dans `AirOps`

#### Exemple dans `vol.py` :

```python
from typing import Optional
from avion import Avion
from enum import Enum

class StatutVol(Enum):
    PREVU = "prévu"
    EN_COURS = "en cours"
    TERMINE = "terminé"

class Vol:
    numero: str
    destination: str
    avion: Avion
    statut: StatutVol
    heure_decollage: Optional[str]  # ISO datetime, pour simplifier ici

    def __init__(self, numero: str, destination: str, avion: Avion):
        self.numero = numero
        self.destination = destination
        self.avion = avion
        self.statut = StatutVol.PREVU
        self.heure_decollage = None

    def changer_statut(self, nouveau: StatutVol) -> None:
        self.statut = nouveau
```

---

### 🔧 Atelier pratique – `typing_airops.py`

> Objectif : Annoter toutes les classes du mini-projet avec `typing`.

1. Annoter les attributs de `Vol`, `Avion`, `Piste`, `Affectation`
2. Annoter les paramètres et valeurs de retour des méthodes :

   * `changer_statut(self, nouveau: StatutVol) -> None`
   * `afficher_infos(self) -> str`
3. Utiliser `List[Vol]` pour stocker des collections de vols
4. Utiliser `Optional[Piste]` pour désigner une piste assignée ou non

---

### 📋 Résumé d’apprentissage

| Élément                 | Annotation      |
| ----------------------- | --------------- |
| Texte                   | `str`           |
| Entier                  | `int`           |
| Objet personnalisé      | `Avion`         |
| Liste de `Vol`          | `List[Vol]`     |
| Valeur absente possible | `Optional[str]` |
| Sans retour             | `-> None`       |

---

### 🧪 Évaluation rapide

1. Que signifie `Optional[Piste]` ?
2. Que renvoie `def foo(x: int) -> str` ?
3. Quelle est la différence entre `List[str]` et `list` ?

---

Souhaites-tu maintenant :

* un **exemple corrigé `typing_airops.py`** montrant l’annotation complète de 2-3 classes ?
* ou que je passe à la **fiche #7 – `collections`** (exploiter `defaultdict`, `namedtuple`, `deque`) ?


**Objectif** : Utiliser le module `typing` pour annoter les types des attributs, arguments, et valeurs de retour, afin d’améliorer la lisibilité, la robustesse et l’auto-complétion des objets dans les projets Python.

---

### 🔎 Question rebond d’introduction

> ✈️ « Si je lis une méthode `changer_statut(x)` dans une classe, comment puis-je savoir à quoi sert `x` sans lire tout le corps de la fonction ? »

---

### 🧠 Explication & contenu théorique

Le module `typing` permet d’**annoter les types** :

* des attributs dans les classes
* des paramètres et valeurs de retour
* des collections (`List`, `Dict`, `Optional`, etc.)

Cela :

* **n’empêche pas l’exécution** (Python reste dynamique)
* mais **aide les IDE, outils de type-checking (mypy), relectures de code**

#### Exemple simple :

```python
from typing import List, Optional

def get_pilotes_disponibles(code: str) -> List[str]:
    ...

def trouver_piste(numero: str) -> Optional["Piste"]:
    ...
```

---

### ✈️ Intégration dans `AirOps`

#### Exemple dans `vol.py` :

```python
from typing import Optional
from avion import Avion
from enum import Enum

class StatutVol(Enum):
    PREVU = "prévu"
    EN_COURS = "en cours"
    TERMINE = "terminé"

class Vol:
    numero: str
    destination: str
    avion: Avion
    statut: StatutVol
    heure_decollage: Optional[str]  # ISO datetime, pour simplifier ici

    def __init__(self, numero: str, destination: str, avion: Avion):
        self.numero = numero
        self.destination = destination
        self.avion = avion
        self.statut = StatutVol.PREVU
        self.heure_decollage = None

    def changer_statut(self, nouveau: StatutVol) -> None:
        self.statut = nouveau
```

---

### 🔧 Atelier pratique – `typing_airops.py`

> Objectif : Annoter toutes les classes du mini-projet avec `typing`.

1. Annoter les attributs de `Vol`, `Avion`, `Piste`, `Affectation`
2. Annoter les paramètres et valeurs de retour des méthodes :

   * `changer_statut(self, nouveau: StatutVol) -> None`
   * `afficher_infos(self) -> str`
3. Utiliser `List[Vol]` pour stocker des collections de vols
4. Utiliser `Optional[Piste]` pour désigner une piste assignée ou non

---

### 📋 Résumé d’apprentissage

| Élément                 | Annotation      |
| ----------------------- | --------------- |
| Texte                   | `str`           |
| Entier                  | `int`           |
| Objet personnalisé      | `Avion`         |
| Liste de `Vol`          | `List[Vol]`     |
| Valeur absente possible | `Optional[str]` |
| Sans retour             | `-> None`       |

---

### 🧪 Évaluation rapide

1. Que signifie `Optional[Piste]` ?
2. Que renvoie `def foo(x: int) -> str` ?
3. Quelle est la différence entre `List[str]` et `list` ?

---
