![Logo](images\logo.png)


## 🧩 Challenge – Techniques avancées Python derrière les packages externes

---

### 🎯 **Objectif**

Comprendre que beaucoup de packages externes Python reposent sur des **mécanismes avancés du langage** :
✅ Décorateurs
✅ Générateurs
✅ Itérateurs
✅ Héritage
✅ Duck typing
✅ Méthodes spéciales (`__eq__`, `__hash__`, etc.)

Avant de les réutiliser dans nos projets, il est essentiel de **démystifier** ces concepts.
Nous allons les explorer ensemble, puis les utiliser dans un **atelier pratique / jeu de défi** sur AirOps.

---

### 🔍 **Pourquoi c’est important ?**

Les bibliothèques modernes comme :

* `rich` (console stylée)
* `click` ou `typer` (command-line interfaces)
* `pandas` (traitement de données)
* `fastapi` (API web)
  … exploitent ces techniques pour rendre leur code **modulaire, élégant, réutilisable et performant**.

Quand vous les utilisez, vous **bénéficiez déjà** de :

* Méthodes **décorées** pour enrichir les comportements.
* Objets **itérables** pour parcourir des ensembles complexes.
* **Générateurs** pour travailler en flux sans tout garder en mémoire.
* Interfaces **polymorphes** et **duck typing** pour une compatibilité souple.
* **Méthodes spéciales** pour rendre les objets comparables, triables, ou utilisables dans des ensembles.

---

### 🛠 **Rappel rapide des concepts**

| Concept                | Description simple                                                                                            |
| ---------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Décorateur**         | Une fonction qui “enveloppe” une autre fonction pour enrichir son comportement.                               |
| **Générateur**         | Une fonction qui produit des valeurs à la demande (avec `yield`), sans tout calculer à l’avance.              |
| **Itérateur**          | Un objet qu’on peut parcourir élément par élément (implémente `__iter__` et `__next__`).                      |
| **Héritage**           | Une sous-classe reprend et adapte le comportement d’une classe parente.                                       |
| **Duck typing**        | Peu importe le type exact : si ça se comporte comme l’objet attendu, ça fonctionne.                           |
| **Méthodes spéciales** | Fonctions magiques (ex. `__eq__`, `__lt__`, `__hash__`) qui permettent de comparer, trier, hacher vos objets. |

---

### ✨ **Focus : Méthodes spéciales**

Les méthodes spéciales (ou dunders) permettent à vos objets d’être :
✅ Comparables (`__eq__`, `__lt__`, `__gt__`)
✅ Utilisables dans des ensembles ou comme clés (`__hash__`)
✅ Représentables joliment (`__str__`, `__repr__`)
✅ Clonables (`__copy__`)
✅ Contextualisables (`__enter__`, `__exit__`)

---

### 📦 **Exemples appliqués AirOps**

| Méthode spéciale | Exemple                                                           |
| ---------------- | ----------------------------------------------------------------- |
| `__eq__`         | Permettre de comparer deux vols : `vol1 == vol2`.                 |
| `__lt__`         | Trier les vols par numéro : `sorted(liste_vols)`.                 |
| `__hash__`       | Mettre des objets avion dans un `set` pour éviter les doublons.   |
| `__str__`        | Afficher un résumé lisible : `print(vol) → Vol AF123 vers Paris`. |

---

### ✈️ **Comment ça peut s’appliquer à AirOps ?**

| AirOps simplifié                      | Avec techniques avancées                                              |
| ------------------------------------- | --------------------------------------------------------------------- |
| Une fonction simple `afficher_vols()` | Un décorateur `@logger` qui trace les appels                          |
| Une liste de vols calculée            | Un générateur qui produit les vols éligibles à l’export               |
| Parcours manuel des objets            | Utilisation d’un itérateur custom pour filtrer les avions par statut  |
| Classes simples                       | Sous-classes spécialisées avec héritage multiple                      |
| Type strict (`Vol`)                   | Duck typing : tout objet avec `.numero` et `.destination` est accepté |
| Comparaison manuelle                  | `__eq__` et `__lt__` pour comparer et trier les vols directement      |

---

### 🎮 **Atelier / Gaming proposé**

Nous allons former des **équipes ou binômes** pour relever un mini-défi autour d’AirOps :
✅ Chaque équipe doit enrichir le projet avec **au moins deux** de ces techniques avancées.
✅ On propose une **liste de défis à choisir** :

* Ajouter un décorateur pour logguer les actions.
* Créer un générateur pour les prochains départs.
* Implémenter un itérateur pour parcourir les pistes disponibles.
* Utiliser l’héritage pour créer des variantes spécialisées de `Vol`.
* Ajouter `__eq__` et `__lt__` pour comparer et trier les objets AirOps.
* Accepter un nouvel objet externe (via duck typing) dans le système.

Temps imparti : **1h – 1h30**, avec présentation finale.

---

### 🧪 **Questions de préparation**

1. Pourquoi certains packages préfèrent un décorateur plutôt qu’un simple appel fonctionnel ?
2. Dans quels cas un générateur est-il plus efficace qu’une liste complète ?
3. Comment le duck typing améliore-t-il l’interopérabilité entre bibliothèques ?
4. Pourquoi `__eq__` + `__hash__` doivent-ils être cohérents pour utiliser un objet dans un `set` ?
5. Que gagne-t-on à rendre ses objets triables avec `__lt__` dans un projet métier ?

---
