![Logo](images\logo.png)

## 🧩 Fiche Module Standard #9 – `csv` + `pathlib`

**Objectif** : Combiner l’utilisation de `csv` et `pathlib` pour exporter proprement les données `AirOps` (vols, avions, affectations) dans des répertoires dédiés, avec des chemins robustes et des fichiers compatibles Excel ou d’autres outils.

---

### 🔎 Question rebond d’introduction

> ✈️ « Si je veux que mon application crée automatiquement un répertoire `exports` et y dépose un fichier CSV contenant les vols du jour, comment éviter les erreurs de chemin et générer un fichier structuré et lisible sans dépendances externes ? »

---

### 🧠 Explication & contenu théorique

#### `pathlib` :

* Manipuler les chemins de fichiers et répertoires
* Créer des dossiers au besoin (`mkdir(exist_ok=True)`)
* Joindre des segments facilement (`/`)

#### `csv` :

* Écrire des fichiers tabulaires, ligne par ligne ou via dictionnaire
* Lire des fichiers existants pour les réimporter dans l’application
* Compatible avec Excel, LibreOffice, pandas, etc.

---

### ✈️ Intégration pratique combinée

Exporter les vols du jour dans un sous-dossier `exports` :

```python
from pathlib import Path
import csv

def exporter_vols_csv(vols, nom_fichier: str = "vols_jour.csv") -> None:
    dossier = Path("exports")
    dossier.mkdir(exist_ok=True)

    chemin = dossier / nom_fichier

    with chemin.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Numéro", "Destination", "Statut"])
        for vol in vols:
            writer.writerow([vol.id, vol.numero, vol.destination, vol.statut.value])

    print(f"✅ Export terminé : {chemin}")
```

---

### 🔧 Atelier pratique – `export_csv_pathlib_airops.py`

1. Créer un sous-dossier `exports` s’il n’existe pas
2. Générer une liste de 10 vols simulés (avec `random`, `uuid`)
3. Exporter ces vols dans `exports/vols_jour.csv`
4. Vérifier l’existence du fichier avec `.exists()`
5. Relire le fichier CSV et afficher son contenu dans la console

---

### 📋 Résumé d’apprentissage

| Élément          | Fonction clé                   | Exemple                     |
| ---------------- | ------------------------------ | --------------------------- |
| Dossier          | `Path("exports")`              | créer/référencer un dossier |
| Fichier complet  | `Path("exports") / "vols.csv"` | chemin complet              |
| Création dossier | `.mkdir(exist_ok=True)`        | créer sans erreur           |
| Écriture CSV     | `csv.writer(f)`                | écrire en-têtes + lignes    |
| Lecture CSV      | `csv.reader(f)`                | lire ligne par ligne        |

---

### 🧪 Évaluation rapide

1. Pourquoi préférer `Path /` à la concaténation manuelle de chaînes pour créer un chemin ?
2. Quelle précaution prendre pour éviter les lignes vides avec `csv` ?
3. Comment vérifier que le fichier CSV a bien été généré avant de le relire ?

