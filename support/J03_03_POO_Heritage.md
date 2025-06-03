![Logo](images\logo.png)

## 🧩 Fiche 3.3 – Héritage et hiérarchies de classes

---

### **Objectif**

Comprendre le concept d’**héritage** en Python, comment créer des sous-classes à partir de classes de base, et pourquoi c’est un outil clé pour organiser et factoriser les comportements communs dans un projet comme `AirOps`.

---

### 🔎 **Définition simple**

L’héritage permet :
✅ De **définir une classe générale** (parente) avec des attributs et des comportements communs.
✅ De créer des **classes spécialisées** (enfants) qui héritent de ces éléments et peuvent **les adapter** (redéfinir, enrichir).

---

### 🚗 **Analogie quotidienne**

| Concept                 | Exemple                                                                |
| ----------------------- | ---------------------------------------------------------------------- |
| Classe parente          | Un véhicule : possède roues, moteur, se déplace.                       |
| Sous-classe             | Une voiture : hérite de véhicule, ajoute “portes”, “coffre”.           |
| Sous-classe spécialisée | Une voiture électrique : hérite de voiture, redéfinit la motorisation. |

---

### 🧠 **Pourquoi utiliser l’héritage ?**

✅ Éviter de répéter le même code dans plusieurs classes.
✅ Factoriser des comportements communs au plus haut niveau.
✅ Organiser le projet en hiérarchies logiques.
✅ Faciliter l’extension future (ajout de nouvelles sous-classes).

---

### ✈️ **Exemples dans AirOps**

| Classe parente | Sous-classes possibles         |
| -------------- | ------------------------------ |
| `Avion`        | `AvionPassagers`, `AvionCargo` |
| `Personnel`    | `Pilote`, `AgentSol`           |
| `Vol`          | `VolPassagers`, `VolCargo`     |

---

### 🔧 **Illustration en Python**

```python
class Avion:
    def __init__(self, immatriculation):
        self.immatriculation = immatriculation

class AvionPassagers(Avion):
    def __init__(self, immatriculation, nb_sieges):
        super().__init__(immatriculation)
        self.nb_sieges = nb_sieges

class AvionCargo(Avion):
    def __init__(self, immatriculation, capacite_tonnes):
        super().__init__(immatriculation)
        self.capacite_tonnes = capacite_tonnes
```

---

### ✨ **Surcharge et extension**

✅ Tu peux **ajouter** de nouveaux attributs.
✅ Tu peux **redéfinir** (override) des méthodes héritées.
✅ Tu peux utiliser `super()` pour réutiliser le comportement de la classe parente.

---

### 📋 **Résumé**

| Concept           | Description                                                                 |
| ----------------- | --------------------------------------------------------------------------- |
| Classe parente    | Contient le comportement général.                                           |
| Sous-classe       | Hérite, enrichit, ou adapte.                                                |
| Héritage multiple | Une classe hérite de plusieurs parents (possible, mais à manier avec soin). |

---

### 🔧 **Atelier pratique – `heritage_airops.py`**

1️⃣ Crée une classe parente `Personnel`.
2️⃣ Crée deux sous-classes : `Pilote` et `AgentSol`, chacune avec ses attributs spécifiques.
3️⃣ Implémente une méthode `presenter()` dans la classe parente, et redéfinis-la différemment dans chaque sous-classe.
4️⃣ Affiche les présentations pour une liste mixte de personnels.

---

### 🧪 **Questions rapides**

1. Dans quels cas l’héritage multiple est-il utile ?
2. Que risque-t-on si on abuse de l’héritage profond (5 niveaux, par exemple) ?
3. Comment choisir entre héritage et composition ?

