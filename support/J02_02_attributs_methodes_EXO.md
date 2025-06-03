![Logo](images\logo.png)


## 🧩 Fiche 2.2 – Attributs & Méthodes (EXO)

Voici une **fiche d’exercice libre avec erreurs à corriger**, conçue pour renforcer la compréhension des **attributs et méthodes d’objet**, tout en développant l’esprit critique sur le code.

---

## 🧩 Fiche d’exercice – Corriger une classe mal écrite

**Objectif pédagogique** : Identifier et corriger des erreurs courantes dans une classe Python mal conçue (mauvais usage de `self`, oubli du constructeur, confusion entre méthodes et fonctions, etc.)

---

### 🔎 Mise en situation

> ✈️ « Un développeur junior vous a transmis une classe `Avion` pour la simulation de notre flotte… mais elle ne fonctionne pas comme prévu. À vous de la corriger. »

---

### 🔧 Code à corriger (fichier `avion_bogue.py`)

```python
# avion_bogue.py

class Avion:

    compteur = 0

    def init(self, code, modele):
        immatriculation = code
        modele = modele
        en_vol = False

    def decoller():
        en_vol = True

    def atterrir():
        en_vol = False

    def afficher_etat():
        if en_vol:
            print("L'avion est en vol.")
        else:
            print("L'avion est au sol.")

    def afficher_compteur():
        print("Nombre total d'avions :", Avion.compteur)
```

---

### 🛠️ Tâches demandées

Corrige ce code en :

1. Corrigeant les erreurs :

   * Mauvais nom du constructeur
   * Attributs non liés à `self`
   * Méthodes manquant `self`
   * Mauvaise gestion de la portée des variables

2. Améliorant la clarté :

   * Ajouter un affichage de l’immatriculation dans `afficher_etat()`
   * Ajouter une méthode de classe pour `afficher_compteur()`

3. Bonus :

   * Empêcher un avion de décoller s’il est déjà en vol
   * Ajouter une méthode statique `aide()` expliquant ce qu’est un avion

---

### 🧠 Points de vigilance

| Problème                           | Exemple erroné           | Correction                    |
| ---------------------------------- | ------------------------ | ----------------------------- |
| Constructeur mal nommé             | `def init(...)`          | `def __init__(...)`           |
| Attributs non stockés              | `immatriculation = code` | `self.immatriculation = code` |
| Manque de `self` dans les méthodes | `def decoller():`        | `def decoller(self):`         |
| Variable hors portée               | `en_vol = True`          | `self.en_vol = True`          |

---

### 🧪 Évaluation finale

1. Que se passe-t-il si on oublie le `self` dans une méthode ?
2. Quelle est la différence entre `self.attribut` et `Attribut` tout court ?
3. Pourquoi utiliser un `@classmethod` pour un compteur d’objets ?

