
# ✅ Plan de test complet pour le projet Avion-Pilote-Vol

## 🧪 Partie 1 – Tests unitaires des objets `Avion`, `Pilote`, `Vol`

📁 Dossier recommandé : `tests/unit/`

### 1.1 Structure `pytest`

```
pip install pytest
```

**tests/unit/test\_avion.py**

```
from models import Avion

def test_avion_creation():
    a = Avion(1, "A320", "Court-courrier", 850)
    assert a.id == 1
    assert a.modele == "A320"
    assert a.description == "Court-courrier"
    assert a.vitesse_max == 850
```

**tests/unit/test\_pilote.py**

```
from models import Pilote

def test_pilote_creation():
    p = Pilote(2, "Durand", "XYZ999")
    assert p.id == 2
    assert p.nom == "Durand"
    assert p.licence == "XYZ999"
```

**tests/unit/test\_vol.py**

```
from models import Vol

def test_vol_creation():
    v = Vol("AF123", "Tokyo", "prévu", "2025-06-01T10:00", "2025-06-01T18:30", 1, 2)
    assert v.numero == "AF123"
    assert v.destination == "Tokyo"
    assert v.statut == "prévu"
    assert v.avion_id == 1
    assert v.pilote_id == 2
```

---

## 🔗 Partie 2 – Tests d’intégration avec l’API Flask (endpoints REST)

📁 Dossier recommandé : `tests/integration/`

```
pip install pytest requests
```

**tests/integration/test\_api\_avion.py**

```
import requests

BASE = "http://localhost:5000/api/avions"

def test_get_avions():
    response = requests.get(BASE)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_post_avion():
    avion = {"id": 99, "modele": "TestModel", "description": "Test", "vitesse_max": 900}
    response = requests.post(BASE, json=avion)
    assert response.status_code == 201

def test_put_avion():
    update = {"modele": "UpdatedModel"}
    response = requests.put(f"{BASE}/99", json=update)
    assert response.status_code == 200

def test_delete_avion():
    response = requests.delete(f"{BASE}/99")
    assert response.status_code in (204, 200)
```

> Répéter la même logique pour `pilotes` et `vols` dans leurs fichiers dédiés.

---

## 🧪 Partie 3 – Tests de bout-en-bout (End-to-End)

Objectif : vérifier qu’un ajout d’avion via l’API est **visible dans l’interface PySide6** (nécessite test manuel ou `pytest-qt` pour automatiser GUI).

```
pip install pytest-qt
```

(Optionnel, je peux te fournir un exemple de test avec `QTest` si tu veux automatiser l'UI.)

---

## 📂 Structure de projet recommandée

```
vols_gui_project/
├── models.py
├── main.py
├── dialogs.py
├── api_server.py
├── tests/
│   ├── unit/
│   │   ├── test_avion.py
│   │   ├── test_pilote.py
│   │   └── test_vol.py
│   └── integration/
│       ├── test_api_avion.py
│       ├── test_api_pilote.py
│       └── test_api_vol.py
```

---
