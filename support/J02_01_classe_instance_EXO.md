![Logo](images\logo.png)


## 🧩 Fiche – Exercices : Classes simples & Attributs

**Objectif** : S’exercer à la création de classes, l’instanciation et la manipulation d’attributs d’objets en autonomie.

---

### 🔎 Question d’amorce

> ✈️ « On sait maintenant créer des objets comme `Avion`. Et si je vous donnais quelques objets à modéliser rapidement ? À vous de jouer. »

---

### 🎯 Exercice 1 – Classe `Piste`

**Objectif** : Créer une classe représentant une piste d’atterrissage.

**Consignes** :

* Créer une classe `Piste` avec :

  * un attribut `numero` (ex. `"27L"`)
  * un attribut `longueur_m` (en mètres)
  * un attribut `est_occupee` (booléen)
* Créer deux pistes différentes
* Afficher leurs informations manuellement avec `print(...)`

**Bonus** : Ajouter une méthode `afficher_infos()` dans la classe

---

### 🎯 Exercice 2 – Classe `Pilote`

**Objectif** : Créer une classe représentant un pilote.

**Consignes** :

* Créer une classe `Pilote` avec :

  * un attribut `nom`
  * un attribut `prenom`
  * un attribut `licence` (ex. `"FR-45678"`)
* Créer une liste de 3 pilotes
* Afficher nom complet + licence pour chacun

---

### 🎯 Exercice 3 – Classe `Affectation`

**Objectif** : Créer une classe de liaison entre un pilote et un avion.

**Consignes** :

* Créer une classe `Affectation` avec :

  * un attribut `avion` (objet de type `Avion`)
  * un attribut `pilote` (objet de type `Pilote`)
* Créer une méthode `afficher_affectation()` qui affiche :

```
Pilote Martin (FR-45678) affecté à l’avion F-GKXJ (A320)
```

---

### 🧪 Mini-synthèse d’application

1. Créer 1 pilote et 1 avion
2. Créer une affectation entre les deux
3. Appeler la méthode `afficher_affectation()`

---

### 📋 Rappel des outils à utiliser

* `class NomDeClasse:`
* `def __init__(self, ...)`
* `self.attribut = ...`
* `obj = NomDeClasse(...)`
* `obj.attribut`
