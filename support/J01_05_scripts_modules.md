![Logo](images\logo.png)


## 🧩 Fiche 1.5 – Modules & scripts

**Objectif pédagogique** : Organiser son code Python en plusieurs fichiers pour le rendre plus lisible, réutilisable et structuré dès le début du projet fil rouge.

---

### 🔎 Question rebond d’introduction

> ✈️ « Si je veux séparer la gestion des avions, des vols, des pistes, etc., comment faire pour garder mon code propre sans tout mettre dans un seul fichier ? »

Faire émerger : la notion de **modularisation**, de **fichier importable**, d’entrée principale du script avec `if __name__ == "__main__":`.

---

### 🧠 Explication & contenu théorique

| Notion               | Description                  | Exemple                       |
| -------------------- | ---------------------------- | ----------------------------- |
| `import`             | Importer un module standard  | `import math`                 |
| `from module import` | Import ciblé                 | `from random import randint`  |
| Module personnel     | Fichier `.py` dans le projet | `import avions`               |
| `__name__`           | Point d’entrée principal     | `if __name__ == "__main__":`  |
| Chemin relatif       | Structure projet             | `projet/avions.py`, `vols.py` |

#### Organisation typique :

```
aeroport/
├── avions.py
├── vols.py
├── utils.py
└── main.py
```

**Exemple simple :**

**`avions.py`**

```
def creer_avion(code):
    return {"immatriculation": code}
```

**`main.py`**

```
from avions import creer_avion

if __name__ == "__main__":
    a1 = creer_avion("F-GKXJ")
    print("Avion créé :", a1)
```

---

### 🔧 Atelier pratique : `aeroport/`

> Objectif : structurer un mini-projet en 3 modules avec un fichier principal.

**Consignes** :

1. Créer un dossier `aeroport/` contenant 4 fichiers :

   * `avions.py` : fonction `creer_avion(code)`
   * `vols.py` : fonction `creer_vol(numero, destination, avion)`
   * `utils.py` : fonction `afficher_dict(label, dico)`
   * `main.py` : point d’entrée du script
2. Dans `main.py`, importer les fonctions et :

   * Créer un avion avec `creer_avion()`
   * Créer un vol avec `creer_vol()`
   * Afficher les deux avec `afficher_dict()`

---

### 📋 Résumé d’apprentissage

| Concept             | Exemple                                 |
| ------------------- | --------------------------------------- |
| Import standard     | `import os`                             |
| Import projet       | `from avions import creer_avion`        |
| Structure modulaire | `main.py` importe `avions.py`           |
| `__name__`          | Empêche exécution lors de l'import      |
| Réutilisabilité     | Plusieurs scripts → un projet structuré |

---

### 🧪 Évaluation rapide (optionnel)

> ❓ Que se passe-t-il si on exécute un module directement alors qu'il n’a pas de `if __name__ == "__main__"` ?
> ❓ Quelle est la différence entre `import avions` et `from avions import creer_avion` ?
