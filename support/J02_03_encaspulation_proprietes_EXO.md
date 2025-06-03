![Logo](images\logo.png)


## 🧩 Fiche 2.3 – Encapsulation, getters, setters, propriétés (EXO)

---

## 🧩 Exercice libre – Créer une classe `Vol` bien encapsulée

**Objectif pédagogique** : Créer une classe `Vol` qui applique toutes les bonnes pratiques vues : encapsulation des attributs, usage de propriétés (`@property`, `@setter`), validation métier, et affichage personnalisé.

---

### 🔎 Enoncé

> ✈️ Un vol comporte un numéro, une destination, un avion, et un statut (`prévu`, `en cours`, `terminé`).
> Vous devez créer une classe **robuste**, avec :

* Attributs protégés
* Accès contrôlés
* Affichage lisible
* Validation des transitions d’état

---

### 🎯 Spécifications de la classe `Vol`

1. **Attributs (privés)** :

   * `__numero` : code vol ex. `"AF123"`
   * `__destination` : ville ou code aéroport
   * `__avion` : objet `Avion`
   * `__statut` : `"prévu"` par défaut ; doit évoluer proprement

2. **Propriétés obligatoires** :

   * `numero` (lecture seule)
   * `destination` (lecture/écriture libre)
   * `avion` (lecture seule)
   * `statut` (lecture, mais **écriture contrôlée**)

3. **Méthodes** :

   * `changer_statut(nouveau_statut)` : change le statut si transition autorisée (`"prévu"` → `"en cours"` → `"terminé"`)
   * `afficher_infos()` : affiche une ligne type :
     `✈️ Vol AF123 vers Lyon [Statut : en cours] – Avion : F-GKXJ`

4. **Bonus** :

   * Refuser les transitions invalides (ex : `"terminé"` → `"en cours"`)
   * Utiliser une propriété calculée : `en_cours` → booléen selon le statut

---

### 📋 Exemple attendu

```python
vol1 = Vol("AF123", "Lyon", avion)
vol1.afficher_infos()
vol1.changer_statut("en cours")
vol1.afficher_infos()
vol1.changer_statut("terminé")
```

---

### 🧠 Points d’évaluation

| Cible         | Question                                                       |
| ------------- | -------------------------------------------------------------- |
| Encapsulation | Les attributs sont-ils en `__privé` ?                          |
| Propriétés    | Les accès sont-ils contrôlés ?                                 |
| Validation    | La méthode `changer_statut()` vérifie-t-elle les transitions ? |
| Affichage     | L’affichage est-il lisible et pertinent ?                      |

---
