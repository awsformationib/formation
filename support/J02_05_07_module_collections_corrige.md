![Logo](images\logo.png)


## 🧩 Fiche Module Standard #7 – `collections`

**Objectif** : Utiliser les structures avancées du module `collections` pour optimiser la manipulation des données dans des contextes orientés objet : statistiques, regroupements, files, objets légers nommés.

---

### 🔎 Question rebond d’introduction

> ✈️ « Et si je voulais organiser automatiquement tous les vols par destination, ou créer une file d’attente des avions au décollage, comment ferais-je sans tout recoder ? »

---

### 🧠 Explication & contenu théorique

Le module `collections` contient plusieurs structures puissantes :

| Structure     | Usage                                           | Exemple                             |
| ------------- | ----------------------------------------------- | ----------------------------------- |
| `defaultdict` | dictionnaire avec valeur par défaut automatique | `defaultdict(list)`                 |
| `deque`       | file d’attente doublement chaînée (FIFO/LIFO)   | `deque([v1, v2])`                   |
| `namedtuple`  | tuple avec noms d’attributs                     | `VolTuple(numero, destination)`     |
| `Counter`     | compter les occurrences d’éléments              | `Counter(["Lyon", "Nice", "Lyon"])` |

---

### ✈️ Intégration dans `AirOps`

#### 1. Grouper les vols par destination avec `defaultdict`

```
from collections import defaultdict

vols_par_destination = defaultdict(list)
for vol in liste_vols:
    vols_par_destination[vol.destination].append(vol)
```

#### 2. Gérer une file d’attente de vols avec `deque`

```
from collections import deque

file_decollage = deque()
file_decollage.append(vol1)
file_decollage.popleft()  # premier à décoller
```

#### 3. Créer une structure légère avec `namedtuple`

```
from collections import namedtuple

VolTuple = namedtuple("VolTuple", ["numero", "destination"])
vol = VolTuple("AF123", "Lyon")
```

#### 4. Statistiques des destinations avec `Counter`

```
from collections import Counter

stats = Counter(vol.destination for vol in liste_vols)
```

---

### 🔧 Atelier pratique – `collections_airops.py`

1. Créer une liste de vols simulés (via `random`)
2. Regrouper les vols par destination avec `defaultdict`
3. Gérer une file de décollage avec `deque` (simuler des décollages)
4. Compter le nombre de vols par ville avec `Counter`
5. Utiliser `namedtuple` pour un export rapide type `(numero, destination)`

---

### 📋 Résumé d’apprentissage

| Élément       | Avantage                            | Idéal pour           |
| ------------- | ----------------------------------- | -------------------- |
| `defaultdict` | plus besoin de `if key not in dict` | regroupements        |
| `deque`       | rapide en append/pop                | file d’attente, pile |
| `namedtuple`  | structure légère lisible            | retour compact       |
| `Counter`     | stats directes sur liste            | fréquences           |

---

### 🧪 Évaluation rapide

1. Que vaut `defaultdict(list)` si on accède à une clé absente ?
2. Quelle structure utiliser pour simuler la tour de contrôle (ordre de décollage) ?
3. Pourquoi `namedtuple` est-il plus sûr et lisible qu’un simple tuple (`("AF123", "Lyon")`) ?
