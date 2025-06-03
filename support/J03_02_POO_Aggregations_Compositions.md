![Logo](images\logo.png)

## 🧩 Fiche 3.2 – Agrégation vs Composition

---

### **Objectif**

Comprendre la différence entre **agrégation** et **composition**, deux formes clés de relations entre objets, et savoir quand les utiliser dans un projet Python orienté objet comme `AirOps`.

---

### 🔎 **Définition simple**

| Terme           | Définition                                                                                                  |
| --------------- | ----------------------------------------------------------------------------------------------------------- |
| **Agrégation**  | Relation **faible** : l’objet “contient” ou “référence” un autre, mais l’autre peut exister indépendamment. |
| **Composition** | Relation **forte** : l’objet “possède” l’autre, qui ne peut exister sans lui.                               |

---

### 🚗 **Analogie quotidienne**

| Concept         | Exemple                                                                                        |
| --------------- | ---------------------------------------------------------------------------------------------- |
| **Agrégation**  | Une école a plusieurs professeurs → si l’école ferme, les professeurs continuent d’exister.    |
| **Composition** | Une maison a des pièces → si la maison est détruite, les pièces n’ont plus de sens séparément. |

---

### ✈️ **Exemples dans AirOps**

| Relation                                                                                                  | Type        |
| --------------------------------------------------------------------------------------------------------- | ----------- |
| Un avion dessert plusieurs vols → les vols peuvent exister même si l’avion change.                        | Agrégation  |
| Un vol possède un plan de vol interne (objet PlanDeVol spécifique) → ce plan n’a de sens que pour ce vol. | Composition |

---

### 🧠 **Comment les représenter en Python ?**

| Type        | Illustration code                                                                         |
| ----------- | ----------------------------------------------------------------------------------------- |
| Agrégation  | `self.vols: List[Vol]` → l’avion contient des références aux vols.                        |
| Composition | `self.plan = PlanDeVol(...)` → l’objet interne est créé et géré uniquement par le parent. |

---

### 🔧 **Quand choisir l’un ou l’autre ?**

| Question à se poser                                                            | Si oui →    |
| ------------------------------------------------------------------------------ | ----------- |
| L’objet peut-il exister seul, sans le parent ?                                 | Agrégation  |
| L’objet est-il “une partie de” son parent, au point qu’il disparaît avec lui ? | Composition |

---

### ✨ **Impact sur la conception**

✅ **Agrégation** :

* Favorise la modularité.
* Permet de partager un même objet entre plusieurs parents (par ex. un pilote sur plusieurs vols).

✅ **Composition** :

* Renforce l’intégrité des données.
* Simplifie les dépendances : on sait que l’objet interne dépend totalement du parent.

---

### 📋 **Résumé**

| Dimension    | Agrégation  | Composition       |
| ------------ | ----------- | ----------------- |
| Lien         | Faible      | Fort              |
| Cycle de vie | Indépendant | Dépendant         |
| Exemple      | Avion → Vol | Vol → Plan de vol |

---

### 🔧 **Atelier pratique – `aggregation_composition_airops.py`**

1️⃣ Modéliser l’agrégation :

* Lier plusieurs vols à un avion (via une liste).

2️⃣ Modéliser la composition :

* Créer un objet `PlanDeVol` interne à chaque vol, qui disparaît si le vol est supprimé.

3️⃣ Afficher :

* La liste des vols d’un avion.
* Le plan détaillé d’un vol.

---

### 🧪 **Questions rapides**

1. Peut-on passer d’une agrégation à une composition sans tout casser ?
2. Quels risques y a-t-il à mal modéliser une relation comme trop forte (composition) ?
3. Comment factoriser du code si plusieurs objets composés partagent des comportements similaires ?
