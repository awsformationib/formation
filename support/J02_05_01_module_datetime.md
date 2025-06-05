![Logo](images\logo.png)

## 🧩 Fiche Module Standard #1 – `datetime`

**Objectif** : Savoir utiliser le module `datetime` pour gérer les dates et heures dans un projet Python orienté objet.

---

### 🔎 Question rebond d’introduction

> ✈️ « Si je veux enregistrer l'heure exacte de création d’un vol ou suivre son heure de décollage et d'atterrissage, comment faire sans calculer manuellement l'heure ? »

---

### 🧠 Explication & contenu théorique

Le module `datetime` permet de :

* manipuler des objets **date**, **heure** et **datetime**
* calculer des **durées**
* afficher des dates sous forme lisible

#### Exemples :

```
from datetime import datetime

# Heure actuelle
now = datetime.now()

# Affichage formaté
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# Durée entre deux moments
start = datetime.now()
# ... traitement ...
end = datetime.now()
duree = end - start
print(duree.total_seconds(), "secondes écoulées")
```

---

### 🛫 Intégration dans `Vol`

```
from datetime import datetime

class Vol:
    def __init__(self, numero, destination, avion):
        self.numero = numero
        self.destination = destination
        self.avion = avion
        self.statut = "prévu"
        self.heure_creation = datetime.now()
        self.heure_decollage = None
        self.heure_arrivee = None

    def decoller(self):
        self.heure_decollage = datetime.now()
        self.statut = "en cours"

    def atterrir(self):
        self.heure_arrivee = datetime.now()
        self.statut = "terminé"

    def duree_de_vol(self):
        if self.heure_decollage and self.heure_arrivee:
            return self.heure_arrivee - self.heure_decollage
        return None
```

---

### 🔧 Atelier pratique – `vol_datetime.py`

1. Créer un vol, afficher son heure de création
2. Simuler un décollage (attendre quelques secondes)
3. Simuler un atterrissage
4. Afficher la **durée du vol** (en secondes)
5. Afficher la date/heure dans un format lisible

---

### 📋 Résumé d’apprentissage

| Concept        | Code                    | Résultat              |
| -------------- | ----------------------- | --------------------- |
| Heure actuelle | `datetime.now()`        | `2025-05-22 14:12:45` |
| Format lisible | `dt.strftime(...)`      | `Vol créé à 14h12`    |
| Durée          | `end - start`           | `0:01:02.123456`      |
| Conversion     | `delta.total_seconds()` | `62.12`               |

---

### 🧪 Évaluation rapide

1. Que fait `datetime.now()` ?
2. À quoi sert `strftime()` ?
3. Pourquoi utiliser `total_seconds()` ?

