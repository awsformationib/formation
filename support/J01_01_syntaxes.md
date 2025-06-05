![Logo](images\logo.png)


## 🧩 Fiche 1.1 – Variables, Types et Opérateurs

**Objectif pédagogique** : Savoir représenter les données de base d’un vol en Python à l’aide des variables, des types simples et des opérateurs.

---

### 🔎 Question rebond d’introduction

> ✈️ « Si je devais stocker les informations essentielles d’un vol dans un programme, quelles seraient-elles ? Et comment les représenter en Python ? »

Laisser les stagiaires proposer : numéro de vol, ville de départ, heure, statut, etc. Puis faire émerger les types (`str`, `int`, `float`, `bool`, `datetime`).

---

### 🧠 Explication & contenu théorique

**Points à aborder** :

* Déclaration et nommage des variables
* Types de base : `int`, `float`, `str`, `bool`
* Opérateurs classiques : `+`, `-`, `*`, `/`, `%`, `==`, `!=`, `>`, `<`, etc.
* Concaténation et interpolation de chaînes (`f-strings`)
* Conversion de types (`int()`, `str()`…)

**Exemples en contexte** :

```
numero_vol = "AF1234"
ville_depart = "Paris"
ville_arrivee = "Toulouse"
heure_depart = "10:30"
distance_km = 604.3
en_retard = True
```

```
message = f"Le vol {numero_vol} part de {ville_depart} à {heure_depart}."
print(message)
```

---

### 🔧 Atelier pratique : `vol_basique.py`

> Objectif : créer un petit script qui affiche les infos d’un vol dans une phrase.

**Consignes** :

1. Créer un fichier `vol_basique.py`
2. Définir 6 variables avec des données simples :

   * Numéro de vol
   * Ville de départ
   * Ville d’arrivée
   * Heure de départ
   * Distance en km
   * En retard (booléen)
3. Afficher un message formaté du type :

```
"Le vol AF1234 part de Paris à 10:30 en direction de Toulouse (604.3 km). Statut : En retard."
```

**Variante niveau +** :

* Ajouter une variable `vitesse_kmh`
* Calculer le temps estimé de vol : `temps_h = distance_km / vitesse_kmh`
* Afficher aussi cette info dans le message

---

### 📋 Résumé d’apprentissage

| Concept        | Exemple                  |
| -------------- | ------------------------ |
| Variable       | `ville_depart = "Paris"` |
| Type numérique | `distance = 604.3`       |
| Booléen        | `en_retard = True`       |
| f-string       | `f"Vol {numero}"`        |
| Opérateur      | `distance / vitesse`     |

---

### 🧪 Évaluation rapide (optionnel)

> ❓ Que donne cette ligne ?

```
print("Vol" + " " + str(123))
```

> ❓ Peut-on faire : `"AF" + 1234` ? Pourquoi ou pourquoi pas ?

