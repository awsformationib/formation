![Logo](images\logo.png)



## 🐍 **Cheatsheet Python – Du plus simple au plus avancé

---

### 🟢 **1️⃣ Bases fondamentales**

✅ Variables :

```
x = 5
nom = "Alice"
```

✅ Types de base :

```
entier = 10          # int
flottant = 3.14      # float
chaine = "bonjour"   # str
booleen = True       # bool
```

✅ Conditions :

```
if x > 0:
    print("Positif")
elif x < 0:
    print("Négatif")
else:
    print("Zéro")
```

✅ Boucles :

```
for i in range(5):
    print(i)

while x < 10:
    x += 1
```

✅ Fonctions simples :

```
def saluer(nom):
    return f"Bonjour {nom}"
```

---

### 🟡 **2️⃣ Structures plus riches**

✅ Listes :

```
nombres = [1, 2, 3]
nombres.append(4)
```

✅ Dictionnaires :

```
personne = {"nom": "Alice", "age": 30}
print(personne["nom"])
```

✅ Sets :

```
unique = set([1, 2, 2, 3])
```

✅ Tuples :

```
coord = (10, 20)
```

✅ Compréhensions :

```
carrés = [x**2 for x in range(5)]
```

---

### 🟠 **3️⃣ Fonctions avancées**

✅ Paramètres spéciaux :

```
def exemple(a, b=2, *args, **kwargs):
    pass
```

✅ Lambdas :

```
double = lambda x: x * 2
```

✅ Map, Filter, Reduce :

```
list(map(double, [1, 2, 3]))
list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))
```

✅ Générateurs :

```
def compteur():
    for i in range(5):
        yield i
```

---

### 🟣 **4️⃣ Programmation orientée objet (POO)**

✅ Classe simple :

```
class Avion:
    def __init__(self, nom):
        self.nom = nom

    def voler(self):
        print(f"{self.nom} décolle !")
```

✅ Héritage :

```
class AvionCargo(Avion):
    def charger(self):
        print("Chargement...")
```

✅ Méthodes spéciales :

```
def __str__(self):
    return f"Avion: {self.nom}"

def __eq__(self, autre):
    return self.nom == autre.nom
```

---

### 🔵 **5️⃣ Concurrence et asynchrone**

✅ Threads :

```
import threading

def tâche():
    print("Travail en thread")

thread = threading.Thread(target=tâche)
thread.start()
```

✅ Asyncio :

```
import asyncio

async def tâche():
    await asyncio.sleep(1)
    print("Travail async")

asyncio.run(tâche())
```

---

### 🟤 **6️⃣ Bonnes pratiques et patterns**

✅ Décorateurs :

```
def decorateur(f):
    def wrapper():
        print("Avant")
        f()
        print("Après")
    return wrapper

@decorateur
def dire_bonjour():
    print("Bonjour")
```

✅ Contexte (with) :

```
with open("fichier.txt") as f:
    contenu = f.read()
```

✅ Gestion des erreurs :

```
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Erreur : division par zéro")
finally:
    print("Toujours exécuté")
```

---

### 🧩 **7️⃣ Techniques Pythonic (élégance et expressivité)**

✅ **Compréhensions avancées** :

```
pairs = [x for x in range(10) if x % 2 == 0]
dict_inverse = {v: k for k, v in d.items()}
```

✅ **Streams et générateurs** (traiter sans tout charger) :

```
gen = (x**2 for x in range(1000))  # pas de liste en mémoire
```

✅ **Passage d’arguments élégant** :

```
def afficher(nom, age, ville):
    print(nom, age, ville)

infos = {"nom": "Alice", "age": 30, "ville": "Paris"}
afficher(**infos)
```

✅ **Opérateurs spécifiques** :

```
a = [1, 2, 3]
b = [4, 5]
fusion = a + b

x = None
résultat = x or "valeur par défaut"  # opérateur or court-circuité

# Expression ternaire
status = "ok" if condition else "erreur"
```

✅ **Utilisation de enumerate et zip** :

```
for index, valeur in enumerate(['a', 'b', 'c']):
    print(index, valeur)

for nom, age in zip(noms, ages):
    print(nom, age)
```

✅ **Unpacking avancé** :

```
a, *milieu, z = [1, 2, 3, 4, 5]
```

✅ **Any et All pour vérifier des conditions** :

```
any([x > 0 for x in liste])  # au moins un True
all([x > 0 for x in liste])  # tous True
```

---

### 🛑 **8️⃣ Techniques expertes**

✅ Métaclasses :

```
class Meta(type):
    def __new__(cls, name, bases, dct):
        return super().__new__(cls, name, bases, dct)
```

✅ Property :

```
class Personne:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age
```

✅ Slots :

```
class Léger:
    __slots__ = ['a', 'b']
```

✅ Type hinting avancé :

```
from typing import List, Dict

def traiter(données: List[Dict[str, int]]) -> None:
    pass
```

---

### 🌟 **Résumé final**

✅ Python commence simple → évolue vers :

* Des outils d’automatisation puissants,
* Une architecture riche en objets,
* Une expressivité élégante (pythonic),
* Des optimisations poussées pour les experts.
