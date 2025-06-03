![Logo](images\logo.png)


## 🧩 Fiche 1.2 – Conditions, Boucles, Fonctions

**Objectif pédagogique** : Apprendre à structurer la logique métier d’un vol : décision de décollage, gestion des pistes, fonctions de traitement simples.

---

### 🔎 Question rebond d’introduction

> ✈️ « Un avion peut-il décoller immédiatement ? Que faut-il vérifier ? »

Réponses attendues : disponibilité d’une piste, météo, avion prêt, horaires respectés…
Faire émerger la notion de condition, puis de fonction de vérification.

---

### 🧠 Explication & contenu théorique

**Points à aborder** :

* Conditions : `if`, `elif`, `else`
* Booléens, opérateurs logiques : `and`, `or`, `not`
* Boucles : `for`, `while` (focus sur `for`)
* Fonctions : `def`, paramètres, retour avec `return`
* Bonne pratique : 1 fonction = 1 responsabilité

**Exemples en contexte :**

```python
def peut_decoller(piste_libre: bool, carburant_ok: bool) -> bool:
    return piste_libre and carburant_ok

# Simulation
if peut_decoller(True, True):
    print("Décollage autorisé.")
else:
    print("Décollage refusé.")
```

---

### 🔧 Atelier pratique : `gestion_vols.py`

> Objectif : écrire une fonction `peut_decoller` et l’utiliser dans un script simulant plusieurs vols.

**Consignes** :

1. Créer une fonction `peut_decoller(avion_pret: bool, piste_dispo: bool) -> bool`
2. Simuler 3 avions sous forme de dictionnaires :

```python
vols = [
    {"numero": "AF123", "pret": True, "piste": True},
    {"numero": "BA456", "pret": False, "piste": True},
    {"numero": "LH789", "pret": True, "piste": False},
]
```

3. Parcourir la liste avec une boucle `for`
4. Afficher pour chaque vol un message :

```python
"Le vol AF123 peut décoller." ou "Le vol BA456 ne peut pas décoller."
```

**Variante +** :

* Ajouter une fonction `afficher_statut(vol)` qui construit et retourne un message propre pour l’affichage
* Utiliser une boucle `while` avec un compteur si tu veux introduire une alternative

---

### 📋 Résumé d’apprentissage

| Concept            | Exemple                          |
| ------------------ | -------------------------------- |
| Condition simple   | `if avion_pret:`                 |
| Condition combinée | `if avion_pret and piste_dispo:` |
| Boucle `for`       | `for vol in vols:`               |
| Fonction           | `def peut_decoller(...):`        |
| Retour de fonction | `return True`                    |

---

### 🧪 Évaluation rapide (optionnel)

> ❓ Que renvoie cette fonction ?

```python
def test(x):
    if x > 5:
        return "OK"
    return "NON"

test(7)
```

> ❓ Peut-on écrire une condition sans `else` ? Quand cela a-t-il du sens ?

---
