![Logo](images\logo.png)

## 🧩 Fiche 3.5 – Abstraction et classes abstraites

---

### **Objectif**

Comprendre le concept d’**abstraction** en Python, c’est-à-dire comment définir des comportements attendus sans forcément les implémenter directement, et comment utiliser des **classes abstraites** pour poser des bases solides dans des projets comme `AirOps`.

---

### 🔎 **Définition simple**

✅ L’abstraction consiste à **se concentrer sur l’essentiel** : on définit **ce qu’un objet doit faire**, sans se préoccuper tout de suite de **comment il le fait**.
✅ Une **classe abstraite** est une classe qui définit une interface ou des méthodes à respecter, mais qu’on ne peut pas instancier directement. Elle sert de modèle pour ses sous-classes.

---

### 🚗 **Analogie quotidienne**

| Concept                 | Exemple                                                                                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Classe abstraite        | Un contrat de location : il définit les règles (payer, rendre le bien, respecter les délais), mais ce n’est pas une voiture, ni un appartement concret. |
| Implémentation concrète | Une location de voiture, une location d’appartement : chacune respecte le contrat, mais avec des détails spécifiques.                                   |

---

### ✈️ **Exemples dans AirOps**

| Classe abstraite                                        | Sous-classes concrètes                      |
| ------------------------------------------------------- | ------------------------------------------- |
| `Personnel` (interface : `presenter()`, `identifier()`) | `Pilote`, `AgentSol`, `Controleur`          |
| `RapportExport` (interface : `generer()`)               | `RapportCSV`, `RapportJSON`, `RapportTexte` |
| `Avion` (interface : `capacite()`, `type_moteur()`)     | `AvionPassagers`, `AvionCargo`              |

---

### 🧠 **Pourquoi utiliser l’abstraction ?**

✅ Garantir que toutes les sous-classes implémentent les méthodes importantes.
✅ Rendre le code plus lisible et structuré : on sait à l’avance **ce qu’on peut attendre** d’un objet.
✅ Préparer le terrain pour du polymorphisme robuste.

---

### 🔧 **Illustration en Python**

Avec le module `abc` (abstract base class) :

```
from abc import ABC, abstractmethod

class Personnel(ABC):
    @abstractmethod
    def presenter(self):
        pass

class Pilote(Personnel):
    def presenter(self):
        return "Je suis un pilote."

class AgentSol(Personnel):
    def presenter(self):
        return "Je suis un agent au sol."
```

⚠️ **Remarque** : On ne peut pas créer directement `Personnel()` car c’est une classe abstraite.

---

### ✨ **Avantages pratiques**

✅ Renforce les contraintes de conception.
✅ Clarifie les intentions (les méthodes “à compléter”).
✅ Permet d’éviter les erreurs d’implémentation partielle.

---

### 📋 **Résumé**

| Concept                  | Description                                               |
| ------------------------ | --------------------------------------------------------- |
| Classe abstraite (`ABC`) | Définit une interface sans implémentation.                |
| Méthode abstraite        | Méthode déclarée mais non définie dans la classe parente. |
| Sous-classe concrète     | Hérite de l’abstrait et **fournit l’implémentation**.     |

---

### 🔧 **Atelier pratique – `abstraction_airops.py`**

1️⃣ Crée une classe abstraite `RapportExport` avec une méthode abstraite `generer()`.
2️⃣ Crée trois sous-classes concrètes : `RapportCSV`, `RapportJSON`, `RapportTexte`.
3️⃣ Écris une fonction qui accepte n’importe quel objet `RapportExport` et appelle `generer()`.
4️⃣ Montre qu’on ne peut pas instancier `RapportExport` directement.

---

### 🧪 **Questions rapides**

1. Pourquoi préférer une classe abstraite à un simple “contrat moral” dans la documentation ?
2. Que se passe-t-il si une sous-classe oublie d’implémenter une méthode abstraite ?
3. Est-il possible de mélanger héritage et abstraction (hériter d’une classe concrète et abstraite à la fois) ?

