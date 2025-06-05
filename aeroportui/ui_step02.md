
# 🔄 Étape 2 (version REST) – Chargement des données via une API Flask locale

## 🎯 Objectif

* Interroger une API REST Flask locale (ex : `http://localhost:5000/api/avions`)
* Récupérer les données au format JSON
* Créer les objets Python `Avion`, `Pilote`, `Vol`
* Afficher ces objets dans l’interface PySide6

---

## 🛠️ 1. Endpoints attendus côté API Flask

| Objet   | Endpoint REST                       | Méthode HTTP | Format de retour attendu                          |
| ------- | ----------------------------------- | ------------ | ------------------------------------------------- |
| Avions  | `http://localhost:5000/api/avions`  | `GET`        | `application/json` — `[{"id":..., "modele":...}]` |
| Pilotes | `http://localhost:5000/api/pilotes` | `GET`        | idem                                              |
| Vols    | `http://localhost:5000/api/vols`    | `GET`        | idem                                              |

---

## 📦 2. Ajout de dépendance côté PySide6

```
pip install requests
```

---

## 📥 3. Fonctions de chargement via HTTP

```
import requests
from models import Avion, Pilote, Vol

BASE_URL = "http://localhost:5000/api"

def charger_avions():
    response = requests.get(f"{BASE_URL}/avions")
    response.raise_for_status()
    return [Avion(**a) for a in response.json()]

def charger_pilotes():
    response = requests.get(f"{BASE_URL}/pilotes")
    response.raise_for_status()
    return [Pilote(**p) for p in response.json()]

def charger_vols():
    response = requests.get(f"{BASE_URL}/vols")
    response.raise_for_status()
    return [Vol(**v) for v in response.json()]
```

---

## 🖥️ 4. Utilisation dans `MainWindow`

Identique à l'étape précédente : on appelle `charger_avions()`, `charger_pilotes()` et `charger_vols()` dans `__init__`, et on affiche ensuite les objets avec `QTableWidget`.

Tu peux également :

* Afficher un message d’erreur si `requests.get()` échoue (`try/except`)
* Afficher un popup (`QMessageBox`) si l’API est inaccessible

---

## 🧪 Exemple avec gestion d’erreur API

```
from PySide6.QtWidgets import QMessageBox

try:
    self.avions = charger_avions()
except requests.exceptions.RequestException as e:
    QMessageBox.critical(self, "Erreur", f"Impossible de charger les avions : {e}")
    self.avions = []
```

---
