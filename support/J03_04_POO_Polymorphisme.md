![Logo](images\logo.png)

## 🧩 Fiche 3.4 – Polymorphisme et interfaces

---

### **Objectif**

Comprendre le concept de **polymorphisme** en Python, c’est-à-dire la capacité d’utiliser différents objets interchangeablement grâce à une interface ou à des comportements communs, et voir comment cela permet d’écrire du code plus flexible et extensible dans des projets comme `AirOps`.

---

### 🔎 **Définition simple**

Le polymorphisme permet :
✅ D’appeler la même méthode ou utiliser le même nom d’attribut sur **des objets de types différents**.
✅ D’écrire du code générique qui fonctionne avec **plusieurs sous-classes** ou objets, tant qu’ils respectent un comportement attendu.

---

### 🚗 **Analogie quotidienne**

| Concept           | Exemple                                                                                                                         |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Interface commune | On peut “démarrer” une voiture à essence, électrique, ou hybride avec la même clé ou bouton.                                    |
| Polymorphisme     | On peut dire “Cet animal fait un bruit” → un chien aboie, un chat miaule, un oiseau chante. Même commande, actions différentes. |

---

### ✈️ **Exemples dans AirOps**

| Cas polymorphe                                                   | Exemple                                                                                              |
| ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Méthode `presenter()` sur `Pilote`, `AgentSol`                   | Tous deux héritent de `Personnel` mais redéfinissent la méthode pour afficher des infos différentes. |
| Méthode `charger()` sur `AvionPassagers` et `AvionCargo`         | Même nom, comportements adaptés selon le type d’avion.                                               |
| Méthode `generer_rapport()` pour exporter en CSV, JSON, ou texte | Même interface, formats différents.                                                                  |

---

### 🧠 **Pourquoi c’est puissant ?**

✅ On peut écrire **du code générique** qui traite des objets sans savoir leur type exact.
✅ On peut ajouter de nouveaux types d’objets sans modifier le code qui les utilise, tant qu’ils respectent l’interface attendue.
✅ On réduit les conditions `if isinstance(...)` ou `if type(...)`.

---

### 🔧 **Illustration en Python**

```python
class Personnel:
    def presenter(self):
        raise NotImplementedError

class Pilote(Personnel):
    def presenter(self):
        return f"Pilote: Alice"

class AgentSol(Personnel):
    def presenter(self):
        return f"Agent au sol: Bob"

# Code polymorphe
personnels = [Pilote(), AgentSol()]
for p in personnels:
    print(p.presenter())  # Même appel, résultat spécifique
```

---

### ✨ **Polymorphisme sans héritage formel (duck typing)**

En Python, même sans héritage, si un objet a les **bons attributs ou méthodes**, il peut être utilisé de manière polymorphe.

> « If it walks like a duck and quacks like a duck, it’s a duck. »

---

### 📋 **Résumé**

| Concept                       | Description                                                                                   |
| ----------------------------- | --------------------------------------------------------------------------------------------- |
| Polymorphisme via héritage    | Plusieurs sous-classes partagent une interface définie dans la classe parente.                |
| Polymorphisme via duck typing | N’importe quel objet qui respecte l’interface attendue fonctionne, même sans héritage.        |
| Interface explicite           | En Python, on peut utiliser des `abc` (abstract base classes) pour formaliser les interfaces. |

---

### 🔧 **Atelier pratique – `polymorphisme_airops.py`**

1️⃣ Crée une classe parente `Personnel` avec une méthode `presenter()`.
2️⃣ Crée plusieurs sous-classes (`Pilote`, `AgentSol`, `Controleur`) avec des présentations spécifiques.
3️⃣ Écris une fonction générique qui prend une liste mixte de personnels et les affiche tous, sans tester leur type.
4️⃣ Ajoute un objet sans héritage mais qui a aussi une méthode `presenter()`, et montre qu’il fonctionne dans la boucle.

---

### 🧪 **Questions rapides**

1. Quels sont les avantages du duck typing ?
2. Quels risques y a-t-il à utiliser du polymorphisme sans vérifier les signatures ?
3. Comment formaliser une interface en Python pour éviter les erreurs ?

---
