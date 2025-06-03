![Logo](images\logo.png)


---

## ✈️ Extensions fil rouge AirOps avec librairies externes

---

### 🌟 **Extension 1 : Enrichir l’affichage console avec `rich`**

| Objectif | Rendre les sorties terminal plus agréables et informatives. |
| -------- | ----------------------------------------------------------- |

✅ Installer :

```bash
pip install rich
```

✅ Exemple d’intégration :

```python
from rich.console import Console
from rich.table import Table

console = Console()
table = Table(title="Résumé des vols AirOps")

table.add_column("Numéro de vol", justify="center")
table.add_column("Avion")
table.add_column("Destination")
table.add_column("Statut")

table.add_row("AF123", "A320", "Paris", "[green]À l’heure[/green]")
table.add_row("AF124", "A320", "Londres", "[yellow]Retardé[/yellow]")

console.print(table)
```

✅ **Valeur pédagogique :**
Les participants voient immédiatement comment passer de `print()` brut à un affichage structuré et coloré.
Cela ouvre la discussion sur la lisibilité et l’UX des outils CLI.

---

### 🌟 **Extension 2 : Connecter une API externe avec `requests`**

| Objectif | Simuler une intégration API, par exemple pour obtenir la météo d’un aéroport. |
| -------- | ----------------------------------------------------------------------------- |

✅ Installer :

```bash
pip install requests
```

✅ Exemple d’intégration :

```python
import requests

def get_meteo_ville(ville):
    response = requests.get(f"https://wttr.in/{ville}?format=3")
    if response.status_code == 200:
        return response.text
    else:
        return "Météo indisponible"

print(get_meteo_ville("Paris"))
```

✅ **Valeur pédagogique :**
Les participants découvrent comment faire une requête HTTP simple, parser un résultat, et intégrer une donnée dynamique au projet.
C’est un excellent tremplin vers des discussions plus larges : authentification API, formats JSON, etc.

---

### 🌟 **Extension 3 : Analyser des statistiques avec `pandas`**

| Objectif | Faire des calculs simples (retards moyens, ponctualité) sur les données AirOps. |
| -------- | ------------------------------------------------------------------------------- |

✅ Installer :

```bash
pip install pandas
```

✅ Exemple d’intégration :

```python
import pandas as pd

# Exemple de dataset minimal
data = {
    'vol': ['AF123', 'AF124', 'BA200'],
    'retard_minutes': [0, 15, 30]
}

df = pd.DataFrame(data)
retard_moyen = df['retard_minutes'].mean()

print(f"Retard moyen : {retard_moyen:.1f} minutes")
```

✅ **Valeur pédagogique :**
Les participants touchent du doigt le potentiel de Pandas pour explorer, transformer et analyser les données.
Cela ouvre des pistes vers des analyses plus complexes (groupby, merges, filtrage).

---

---

### 📦 Résumé des extensions

| Extension          | Librairie  | Apport                                                                 |
| ------------------ | ---------- | ---------------------------------------------------------------------- |
| Affichage enrichi  | `rich`     | Mieux présenter les résultats et rapports en console.                  |
| API externe        | `requests` | Connecter AirOps à un service externe, ajouter de la valeur dynamique. |
| Analyse de données | `pandas`   | Explorer les performances et statistiques métiers.                     |

---
