![Logo](images\logo.png)
Les **générateurs en Python** sont un outil puissant pour **traiter des données volumineuses de manière paresseuse (lazy)**, c’est-à-dire **sans tout charger en mémoire**. Parfait pour les gros jeux de données !

---

### 🔹 Qu’est-ce qu’un générateur ?

Un **générateur** est une **fonction** qui utilise le mot-clé `yield` au lieu de `return`.
Il ne renvoie pas une valeur unique, mais **produit une séquence de valeurs**, une par une, **à la demande**.

---

### 🔹 Pourquoi c’est utile pour les données ?

Quand on travaille avec **des fichiers volumineux**, comme des CSV ou des logs, les générateurs permettent de **traiter ligne par ligne**, **sans tout charger en RAM**.

---

### ✅ Exemple concret : lire un fichier CSV ligne par ligne avec un générateur

```
def lire_csv_en_generator(nom_fichier):
    with open(nom_fichier, "r", encoding="utf-8") as f:
        for ligne in f:
            # Nettoyage et découpage
            valeurs = ligne.strip().split(",")
            yield valeurs  # renvoie une ligne à la fois
```

Utilisation :

```
for ligne in lire_csv_en_generator("gros_fichier.csv"):
    print(ligne)  # On traite chaque ligne individuellement
```

✔️ **Avantage** : le fichier peut faire 10 Go, ça fonctionnera sans problème mémoire.

---

### 🔹 Exemple avec transformation des données

On veut calculer la moyenne d’une colonne numérique (par exemple la 2e colonne d’un fichier CSV) :

```
def extraire_colonne_generator(nom_fichier, index_colonne):
    with open(nom_fichier, "r", encoding="utf-8") as f:
        for ligne in f:
            try:
                valeurs = ligne.strip().split(",")
                yield float(valeurs[index_colonne])
            except (IndexError, ValueError):
                continue  # Ignore les lignes mal formées

somme = 0
compteur = 0
for valeur in extraire_colonne_generator("gros_fichier.csv", 1):
    somme += valeur
    compteur += 1

print("Moyenne :", somme / compteur if compteur else 0)
```

---

### 🔹 Comparaison avec une liste en mémoire

```
# Inefficace si le fichier est gros :
valeurs = [float(ligne.strip().split(",")[1]) for ligne in open("fichier.csv")]

# Avec un générateur, on ne garde qu'une ligne à la fois en mémoire.
```

---

### 🧠 Astuce bonus : générateur avec `yield from`

Si tu as plusieurs fichiers CSV :

```
def lire_plusieurs_csv(fichiers):
    for nom in fichiers:
        yield from lire_csv_en_generator(nom)
```

---

### 📌 À retenir

| Avantage des générateurs  | Description                                     |
| ------------------------- | ----------------------------------------------- |
| ✅ Mémoire efficace        | Une seule ligne est en mémoire à la fois        |
| ✅ Simple à écrire         | Syntaxe claire avec `yield`                     |
| ✅ Idéal pour le streaming | Traitement de flux continus ou de gros fichiers |
| ✅ Compatible avec `for`   | S’intègre facilement dans les boucles           |

