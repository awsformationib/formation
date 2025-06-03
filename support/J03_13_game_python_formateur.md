![Logo](images\logo.png)

# Challenge – Techniques avancées Python derrière les packages externes

> **Public :** participants formation Python POO  
> **But :** relier les concepts avancés (décorateurs, générateurs, itérateurs, héritage, duck typing, méthodes spéciales) aux packages externes et préparer un atelier AirOps.

---

## 🎯 Objectif

- Découvrir **pourquoi** ces techniques sont utilisées partout (packages, framework)
- Savoir **créer et utiliser** chaque construction avancée :
  1. Décorateur
  2. Générateur
  3. Itérateur
  4. Héritage
  5. Duck typing
  6. Méthodes spéciales (`__eq__`, `__lt__`, `__hash__`, …)
- Se préparer à un **atelier/gaming** d’extension du projet **AirOps**.

---

## 🔍 Pourquoi c’est important ?

Les paquets populaires (`rich`, `typer`, `pandas`, `fastapi`…) reposent sur ces concepts pour être :

* **Flexibles** (duck typing)
* **Performants** (générateurs)
* **Élégants** (décorateurs)
* **Extensibles** (héritage + méthodes spéciales)

Comprendre ces briques vous aidera à **lire, débugguer et étendre** tout écosystème Python.

---

## 🛠 Rappel & mode d’emploi

1 : **Décorateur** | Définir une fonction qui prend une fonction et retourne une nouvelle fonction.
```
def logger(func):
    def wrapper(*a, **k):
        print(f"▶ {func.__name__}")
        return func(*a, **k)
    return wrapper
```
2 : **Générateur** | Ajouter `yield` dans une fonction pour produire un **flux**.
```
def vols_prets(vols):
    for v in vols:
        if v.statut == 'prévu':
            yield v
``` 
> Parcourir : `for v in vols_prets(liste):` sans charger tout en mémoire. |

3 : **Itérateur** | Implémenter `__iter__` **et** `__next__` dans une classe.
```
class PistesLibres:
    def __init__(self, pistes):
        self.pistes = [p for p in pistes if not p.occupee]
    def __iter__(self):
        return iter(self.pistes)
```
> Se comporte comme une liste : `for p in PistesLibres(pistes): ...` |

4 : **Héritage** | Déclarer une sous‐classe qui étend la classe parente.
```
class VolPassagers(Vol):
    def embarquer(self): ...
```
> Réutiliser / redéfinir méthodes, appeler `super()`. |

5 : **Duck typing** | Aucune syntaxe spéciale : un objet « quack » suffit.
```
def affiche(obj):
    print(obj.numero)
```
> Tant qu’un objet possède `.numero`, il est accepté.

6 : **Méthodes spéciales** | Ajouter des dunders pour enrichir le comportement.
```
class Vol:
    def __eq__(self, other):
        return self.numero == other.numero
    def __lt__(self, other):
        return self.numero < other.numero
    def __hash__(self):
        return hash(self.numero)
``` 
→ Comparaison `==`, tri `sorted(vols)`, mise en `set`

---

## ✈️ Application directe à **AirOps**

- **Décorateur** : `@logger` sur `decoller()`, crée un journal d’action.  
- **Générateur** : `vols_prets()` renvoie au fil de l’eau les vols encore “prévu”.  
- **Itérateur** : `PistesLibres(pistes)` permet `for piste in PistesLibres(...)`.  
- **Héritage** : `VolCargo` et `VolPassagers` héritent de `Vol`.  
- **Duck typing** : accepter un objet `VolExterne` d’un autre module s’il expose `.numero` & `.destination`.  
- **Dunders** : trier les vols, éviter les doublons dans des `set`.

---

## 🧪 Questions de réflexion

1. Quand un décorateur est‑il plus indiqué qu’une simple fonction enveloppante ?  
2. Quels gains mémoire apporte un générateur dans la gestion d’une grosse liste de vols ?  
3. Comment garantir que `__eq__` et `__hash__` restent cohérents ?  
4. Pourquoi le duck typing facilite‑t‑il l’intégration de packages tiers ?  
5. Quels pièges à éviter avec l’héritage multiple ?

---

## ✋ Conseils formateur

- Encouragez les participants à **tester rapidement** chaque concept avec un snippet isolé.  
- Soulignez l’importance de **petites étapes** : décorateur simple → version enrichie.  
- Reliez toujours au **cas métier** AirOps pour donner du sens.

---