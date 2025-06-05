![Logo](images\logo.png)


## 🧩 Fiche 1.3 – Listes, Dictionnaires, Tuples, Ensembles

**Objectif pédagogique** : Savoir manipuler les structures de données fondamentales de Python pour stocker, organiser, rechercher et transformer les données liées aux vols.

---

### 🔎 Question rebond d’introduction

> ✈️ « Si je veux gérer tous les vols d’une journée dans un aéroport, quel type de structure utiliseriez-vous ? Et si je veux connaître tous les avions immatriculés ? »

Faire émerger les besoins : collections ordonnées (liste), associations clé-valeur (dictionnaire), groupes sans doublons (set), données figées (tuple).

---

### 🧠 Explication & contenu théorique

| Structure                 | Description                            | Exemple                                            |
| ------------------------- | -------------------------------------- | -------------------------------------------------- |
| **Liste** (`list`)        | Collection ordonnée et modifiable      | `vols = ["AF123", "LH456"]`                        |
| **Dictionnaire** (`dict`) | Association clé → valeur               | `vol = {"numero": "AF123", "destination": "Nice"}` |
| **Tuple** (`tuple`)       | Données groupées, immuables            | `coords = (43.6, 1.4)`                             |
| **Ensemble** (`set`)      | Collection non ordonnée, sans doublons | `immatriculations = {"F-GKXJ", "F-HBXO"}`          |

**Notions-clés à démontrer** :

* Création, ajout, suppression
* Accès aux éléments
* Itérations avec `for`
* Conditions d’appartenance (`in`)
* Transformation entre types (`list()`, `set()`, `dict()`)

---

### 🔧 Atelier pratique : `analyse_flotte.py`

> Objectif : manipuler plusieurs structures pour représenter et interroger une flotte d’avions et leurs vols.

**Consignes** :

1. Créer une **liste de dictionnaires**, chaque dictionnaire représentant un vol :

```
vols = [
    {"numero": "AF123", "destination": "Nice", "immatriculation": "F-GKXJ"},
    {"numero": "LH456", "destination": "Berlin", "immatriculation": "D-ABCD"},
    {"numero": "BA789", "destination": "Londres", "immatriculation": "G-EUPT"},
    {"numero": "AF124", "destination": "Nice", "immatriculation": "F-GKXJ"},
]
```

2. Extraire **toutes les immatriculations distinctes** (avec `set`)
3. Compter **le nombre de vols vers chaque destination** (avec un dictionnaire)
4. Créer une **fonction `afficher_vol(vol)`** prenant un dictionnaire et affichant proprement les infos
5. Bonus : créer une liste de tuples `(numero_vol, destination)`

---

### 📋 Résumé d’apprentissage

| Structure | Action clé           | Exemple                    |
| --------- | -------------------- | -------------------------- |
| `list`    | Ajouter              | `vols.append(nouveau_vol)` |
| `dict`    | Accès valeur         | `vol["destination"]`       |
| `tuple`   | Groupement simple    | `("AF123", "Nice")`        |
| `set`     | Retirer les doublons | `set(immatriculations)`    |

---

### 🧪 Évaluation rapide (optionnel)

> ❓ Quelle sont les différences entre **liste** , **tuple** , **set** et **dict**?
> ❓ Peut-on modifier un tuple ? Pourquoi l’utiliser ?

---
