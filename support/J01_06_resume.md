![Logo](images\logo.png)


# 📘 Fiche Récapitulatif – Fin de Journée 

### 🎯 Objectif : Valider les acquis fondamentaux de la syntaxe Python et des bases structurantes pour aborder la POO dès le jour 2.

---

## 🧩 Concepts-clés vus aujourd’hui

| Thème               | Concepts essentiels                              | Exemple                          |
| ------------------- | ------------------------------------------------ | -------------------------------- |
| **Syntaxe de base** | Variables, types (`int`, `str`, `float`, `bool`) | `distance_km = 604.3`            |
| **Conditions**      | `if`, `elif`, `else`, booléens                   | `if en_retard:`                  |
| **Boucles**         | `for`, `while`                                   | `for vol in vols:`               |
| **Fonctions**       | Paramètres, `return`, portée                     | `def peut_decoller():`           |
| **Arguments**       | Positionnels, nommés, `*args`, `**kwargs`        | `def f(a, b=2, *args, **kwargs)` |
| **Collections**     | `list`, `dict`, `tuple`, `set`                   | `set(immats)`                    |
| **Modularisation**  | Fichiers, `import`, `__main__`                   | `from avions import ...`         |

---

## ✅ Quiz de fin de journée (10 points)

> **Règle** : 1 point par bonne réponse. Corrigé à l’oral ou en groupe.

---

### 🔢 Q1 – Types & Variables

**1.** Que va afficher ce code ?

```
a = 10
b = "10"
print(a + int(b))
```

---

### 🔁 Q2 – Conditions

**2.** Complète la condition pour que le vol ne décolle que si l’avion est prêt **et** une piste est disponible :

```
if ____________:
    print("Décollage autorisé")
```

---

### 🔃 Q3 – Boucles

**3.** Quelle boucle utiliseriez-vous pour traiter une file d’attente de vols **jusqu’à épuisement** de la liste ?

a) `for`
b) `while`
c) `repeat`
d) `foreach`

---

### 🔧 Q4 – Fonctions

**4.** Que fait ce code ?

```
def f(x=5):
    return x * 2

print(f())
print(f(3))
```

---

### ✨ Q5 – `*args` et `**kwargs`

**5.** Quel est le résultat ?

```
def fusion(*args):
    return " ".join(args)

print(fusion("AF123", "vers", "Nice"))
```

---

### 📦 Q6 – Listes & Sets

**6.** Quelle est la différence principale entre une `list` et un `set` en Python ?

---

### 📦 Q7 – Dictionnaires

**7.** Comment accéder à la valeur `"Nice"` dans ce dictionnaire ?

```
vol = {"numero": "AF123", "destination": "Nice"}
```

---

### 📂 Q8 – Modules

**8.** Que fait la ligne suivante ?

```
if __name__ == "__main__":
```

---

### 🧠 Q9 – Portée

**9.** Que vaut `a` à la fin ?

```
a = 10

def change():
    a = 5

change()
print(a)
```

---

### 📂 Q10 – Import

**10.** Quelle est la différence entre :

```
import avions
```

et

```
from avions import creer_avion
```
