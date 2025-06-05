![Logo](images\logo.png)


## 🧩 Fiche 1.4 – Fonctions & portée (aka scope)

**Objectif pédagogique** : Structurer son code avec des fonctions bien conçues, comprendre les mécanismes de portée et les particularités de la signature des fonctions Python.

---

### 🔎 Question rebond d’introduction

> ✈️ « Si je dois réutiliser plusieurs fois une opération sur les vols (par exemple, filtrer ceux à destination de Nice), comment faire pour éviter de réécrire du code ? »

Faire émerger la notion de fonction avec paramètres, valeur de retour, et la portée des variables internes.

---

### 🧠 Explication & contenu théorique

#### 🧩 1. Définir une fonction simple

```
def afficher_vol(vol):
    print(f"Vol {vol['numero']} vers {vol['destination']}")
```

#### 🧩 2. Paramètres positionnels et nommés

```
def message_accueil(nom, aeroport):
    return f"Bienvenue {nom}, vous êtes à {aeroport}."

print(message_accueil("Jean", "CDG"))
print(message_accueil(nom="Anna", aeroport="Lyon"))
```

#### 🧩 3. Valeurs par défaut

```
def annoncer_vol(numero, destination="Inconnue"):
    print(f"Annonce : vol {numero} vers {destination}")
```

#### 🧩 4. `*args` (paramètres multiples positionnels)

```
def addition_vols(*distances):
    return sum(distances)

addition_vols(300, 500, 150)  # => 950
```

#### 🧩 5. `**kwargs` (paramètres nommés optionnels)

```
def info_supplémentaire(**infos):
    for cle, valeur in infos.items():
        print(f"{cle} : {valeur}")

info_supplémentaire(pilote="Martin", avion="A320", piste=4)
```

#### 🧩 6. Portée des variables

```
vol_global = "AF123"

def changer_vol():
    vol_local = "BA456"  # portée locale
    print(vol_local)

changer_vol()
print(vol_global)  # la variable globale n’est pas affectée
```

---

### 🔧 Atelier pratique : `fonctions_vols.py`

> Objectif : structurer plusieurs fonctions autour des opérations courantes sur les vols.

**Consignes** :

1. Créer une fonction `filtrer_par_destination(vols, destination)` → retourne une liste
2. Créer une fonction `compter_vols_par_destination(*vols)` → retourne un dictionnaire `{destination: nb}`
3. Créer une fonction `details_vol(**infos)` → affiche des infos arbitraires sur un vol
4. Créer une fonction `statut_vol(numero, en_retard=False)` → affiche avec valeur par défaut
5. Bonus : utiliser une variable globale et montrer que la modifier localement ne la change pas globalement (sauf avec `global`)

---

### 📋 Résumé d’apprentissage

| Notion             | Syntaxe                   | Exemple        |
| ------------------ | ------------------------- | -------------- |
| Param. positionnel | `def f(x)`                | `f(3)`         |
| Param. nommé       | `def f(x=10)`             | `f(x=15)`      |
| `*args`            | `def f(*a)`               | `f(1,2,3)`     |
| `**kwargs`         | `def f(**k)`              | `f(a=1, b=2)`  |
| Scope              | variable locale ≠ globale | voir ci-dessus |

---

### 🧪 Évaluation rapide (optionnel)

> ❓ Que vaut `a` après l’appel suivant ?

```
a = 5

def test():
    a = 10
    return a

test()
print(a)
```

> ❓ Est-ce possible d’écrire `def f(a=1, b)` ? Pourquoi ?
