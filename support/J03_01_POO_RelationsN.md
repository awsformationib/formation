![Logo](images\logo.png)

## 🧩 Fiche 3.1 – Relations entre objets (1-n, n-1, n-n)

---

### **Objectif**

Apprendre à modéliser les **relations complexes entre classes** dans un projet orienté objet :

* **1 → n** : Un objet est lié à plusieurs autres.
* **n → 1** : Plusieurs objets pointent vers un seul.
* **n → n** : Plusieurs objets sont liés de manière croisée, symétrique.

---

### 🔎 **Pourquoi modéliser les relations ?**

Dans un système comme `AirOps`, nous ne manipulons pas des entités isolées :

* Un **avion** réalise plusieurs vols.
* Un **vol** utilise une **piste** spécifique.
* Un **pilote** peut être affecté à plusieurs vols, et inversement.

Bien modéliser ces liens permet :
✅ de **représenter fidèlement** la réalité métier,
✅ de **limiter les erreurs** (par ex. affecter un vol à plusieurs pistes en même temps),
✅ de **naviguer facilement** entre les objets en mémoire.

---

### 🚗 **Analogie quotidienne**

| Relation | Exemple dans la vie réelle                     |
| -------- | ---------------------------------------------- |
| 1 → n    | Une prof a plusieurs étudiants.                |
| n → 1    | Plusieurs commandes vont à une même adresse.   |
| n → n    | Plusieurs acteurs jouent dans plusieurs films. |

---

### 🧠 **Comment coder ces relations ?**

| Relation | Python – modèle typique                                                        |
| -------- | ------------------------------------------------------------------------------ |
| 1 → n    | Une liste dans l’objet racine (`self.vols: List[Vol]`)                         |
| n → 1    | Une référence unique (`vol.piste = Piste(...)`)                                |
| n → n    | Une liste mutuelle ou une classe intermédiaire (`vol.pilotes` + `pilote.vols`) |

---

### ✈️ **Exemple AirOps**

#### Avion et ses vols (1 → n)

```
class Avion:
    def __init__(self, immatriculation):
        self.immatriculation = immatriculation
        self.vols = []  # liste des vols assignés

class Vol:
    def __init__(self, numero, avion):
        self.numero = numero
        self.avion = avion
        avion.vols.append(self)  # on lie l'avion et le vol
```

#### Vol et sa piste (n → 1)

```
class Vol:
    def __init__(self, numero, avion, piste):
        self.numero = numero
        self.avion = avion
        self.piste = piste
```

#### Pilotes et vols (n ↔ n)

```
class Pilote:
    def __init__(self, nom):
        self.nom = nom
        self.vols = []

class Vol:
    def __init__(self, numero, avion, piste):
        self.numero = numero
        self.avion = avion
        self.piste = piste
        self.pilotes = []

    def ajouter_pilote(self, pilote):
        self.pilotes.append(pilote)
        pilote.vols.append(self)
```

---

### 🔧 **Atelier pratique – `relations_airops.py`**

1️⃣ Créez :

* 3 avions, chacun avec 2 vols.
* 3 pilotes, affectés à différents vols.
* 2 pistes, partagées par les vols.

2️⃣ Affichez :

* Tous les vols d’un avion.
* Tous les vols d’un pilote.
* Pour chaque vol : son avion, sa piste et ses pilotes.

---

### 📋 **Résumé d’apprentissage**

| Relation | Pourquoi c’est utile                                          |
| -------- | ------------------------------------------------------------- |
| 1 → n    | Suivre tous les éléments liés à un parent.                    |
| n → 1    | Retrouver rapidement le contexte d’un élément.                |
| n → n    | Modéliser les interactions croisées et éviter la duplication. |

