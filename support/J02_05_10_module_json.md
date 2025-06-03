![Logo](images\logo.png)

## 🧩 Fiche Module Standard #10 – `json`

**Objectif** : Utiliser le module `json` pour sérialiser (exporter) et désérialiser (importer) des données structurées au format JSON, afin de sauvegarder/restaurer facilement l’état des objets du projet `AirOps`.

---

### 🔎 Question rebond d’introduction

> ✈️ « Si je veux sauvegarder non seulement une liste de vols, mais aussi tous les détails de leurs avions, horaires et statuts, dans un format lisible, portable et réutilisable par d’autres systèmes, comment faire ? »

---

### 🧠 Explication & contenu théorique

Le module `json` permet :

* d’**écrire** des données Python sous forme de texte au format JSON
* de **lire** des fichiers JSON pour reconstruire des objets Python
* de partager des données facilement entre systèmes

#### Exemple d’écriture :

```python
import json

data = {"numero": "AF123", "destination": "Lyon"}
with open("vol.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)
```

#### Exemple de lecture :

```python
with open("vol.json", encoding="utf-8") as f:
    data = json.load(f)
    print(data["numero"])
```

⚠️ Attention : les objets complexes (par ex. `datetime`, `Enum`, ou objets personnalisés) doivent être transformés en types simples (`str`, `int`, `dict`, `list`) avant d’être passés à `json.dump()`.

---

### ✈️ Intégration dans `AirOps`

Exporter une liste de vols :

```python
import json
from pathlib import Path

def exporter_vols_json(vols, chemin_fichier="exports/vols.json") -> None:
    path = Path(chemin_fichier)
    path.parent.mkdir(exist_ok=True)

    vols_data = [
        {
            "id": vol.id,
            "numero": vol.numero,
            "destination": vol.destination,
            "statut": vol.statut.value if hasattr(vol.statut, "value") else vol.statut
        }
        for vol in vols
    ]

    with path.open("w", encoding="utf-8") as f:
        json.dump(vols_data, f, indent=4, ensure_ascii=False)

    print(f"✅ Export JSON terminé : {path}")
```

---

### 🔧 Atelier pratique – `export_json_airops.py`

1. Générer une liste de 10 vols simulés
2. Exporter les données dans `exports/vols.json`
3. Vérifier manuellement le fichier (ouvrir dans un éditeur texte)
4. Lire à nouveau le fichier et reconstruire une liste d’objets Python simples (dicts)
5. Afficher chaque vol depuis les données lues

---

### 📋 Résumé d’apprentissage

| Fonction             | Usage                    | Exemple                              |
| -------------------- | ------------------------ | ------------------------------------ |
| `json.dump()`        | écrire en JSON           | `json.dump(data, f, indent=4)`       |
| `json.load()`        | lire du JSON             | `data = json.load(f)`                |
| `ensure_ascii=False` | conserver les accents    | `json.dump(..., ensure_ascii=False)` |
| Conversion           | transformer avant export | objets → dictionnaires               |

---

### 🧪 Évaluation rapide

1. Pourquoi doit-on convertir les objets complexes avant de les passer à `json.dump()` ?
2. Que fait l’argument `indent=4` ?
3. Quelle est la différence entre `json.dump()` et `json.dumps()` ?

