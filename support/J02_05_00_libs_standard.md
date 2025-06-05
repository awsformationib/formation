![Logo](images\logo.png)

## 🧩 Fiche 2.5 – Librairies standard

---

## 🔧 Modules standards Python à intégrer dans le fil rouge (Jour 2)

| Module        | Usage dans `AirOps`                                             | Objectif pédagogique       |
| ------------- | --------------------------------------------------------------- | -------------------------- |
| `datetime`    | gérer heures de départ/arrivée de vol                           | manipulation de date/heure |
| `random`      | simuler génération aléatoire de numéros ou destinations         | tests / simulation         |
| `uuid`        | générer des identifiants uniques (vols, avions, affectations)   | identifiants sûrs          |
| `enum`        | représenter des statuts de vol (`prévu`, `en cours`, `terminé`) | contrôle métier robuste    |
| `dataclasses` | version alternative "propre" d'une classe `Avion`               | allègement de code         |
| `typing`      | annotation des types de méthodes (`-> Vol`)                     | lisibilité et robustesse   |
| `collections` | `namedtuple`, `defaultdict` pour statistiques ou historique     | structures avancées        |
| `pathlib`     | sauvegarder/exporter des rapports de vol ou logs                | manipuler des chemins      |
| `csv`         | générer un rapport CSV des vols du jour                         | export structuré           |
| `json`        | sauvegarder/restaurer la flotte ou les vols                     | persistance de l’état      |

---

## 🔄 Intégration dans les séquences existantes de Jour 2

| Fiche                    | Intégration possible                                            |
| ------------------------ | --------------------------------------------------------------- |
| 2.1 Classe & Instance    | ajouter un `uuid` généré dans `__init__()` de `Avion`           |
| 2.2 Attributs & Méthodes | méthode `decoller()` avec `datetime.now()`                      |
| 2.3 Encapsulation        | validation stricte avec `Enum` pour le statut                   |
| 2.4 Méthodes spéciales   | affichage formaté avec `datetime.strftime()`                    |
| TP inter-objet           | exporter les vols du jour avec `csv` ou `json`                  |
| Bonus                    | remplacer `Vol` ou `Piste` par des `@dataclass` pour simplifier |

---

## 🧪 Exemple : ajout de `datetime` et `uuid` dans la classe `Vol`

```
from datetime import datetime
import uuid

class Vol:
    def __init__(self, numero, destination, avion):
        self.id = uuid.uuid4()
        self.numero = numero
        self.destination = destination
        self.avion = avion
        self.statut = "prévu"
        self.heure_creation = datetime.now()

    def afficher_infos(self):
        print(f"[{self.heure_creation.strftime('%H:%M:%S')}] "
              f"Vol {self.numero} vers {self.destination} – Avion : {self.avion}")
```
