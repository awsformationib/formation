![Logo](images\logo.png)


## 🧩 Fiche Module Standard #6 – `typing` (CORRIGE)

Voici un **exemple corrigé complet `typing_airops.py`**, avec des annotations de type appliquées aux classes `Avion`, `Piste`, `Vol` et `Affectation` dans le contexte du projet `AirOps`.

Ce fichier regroupe les classes essentielles, avec l'utilisation de `typing` pour :

* les attributs de classe
* les paramètres de méthodes
* les types de retour
* les cas optionnels (`Optional`)
* les collections (`List`)

---

### ✅ `typing_airops.py`

```python
from __future__ import annotations  # permet l’utilisation de types avant leur définition
from typing import Optional
from enum import Enum
from dataclasses import dataclass, field
from uuid import uuid4
from datetime import datetime


# --- ENUM pour statut de vol ---
class StatutVol(Enum):
    PREVU = "prévu"
    EN_COURS = "en cours"
    TERMINE = "terminé"


# --- AVION ---
@dataclass
class Avion:
    immatriculation: str
    modele: str
    id: str = field(default_factory=lambda: str(uuid4()))

    def __str__(self) -> str:
        return f"{self.immatriculation} ({self.modele})"


# --- PISTE ---
@dataclass
class Piste:
    numero: str
    longueur: int
    occupee: bool = False

    def occuper(self) -> None:
        self.occupee = True

    def liberer(self) -> None:
        self.occupee = False

    def __str__(self) -> str:
        etat = "occupée" if self.occupee else "libre"
        return f"Piste {self.numero} ({self.longueur}m) – {etat}"


# --- VOL ---
class Vol:
    numero: str
    destination: str
    avion: Avion
    statut: StatutVol
    heure_decollage: Optional[datetime]
    heure_arrivee: Optional[datetime]

    def __init__(self, numero: str, destination: str, avion: Avion):
        self.numero = numero
        self.destination = destination
        self.avion = avion
        self.statut = StatutVol.PREVU
        self.heure_decollage = None
        self.heure_arrivee = None

    def changer_statut(self, nouveau: StatutVol) -> None:
        self.statut = nouveau

    def decoller(self) -> None:
        self.heure_decollage = datetime.now()
        self.changer_statut(StatutVol.EN_COURS)

    def atterrir(self) -> None:
        self.heure_arrivee = datetime.now()
        self.changer_statut(StatutVol.TERMINE)

    def duree_vol(self) -> Optional[float]:
        if self.heure_decollage and self.heure_arrivee:
            return (self.heure_arrivee - self.heure_decollage).total_seconds()
        return None

    def __str__(self) -> str:
        return f"Vol {self.numero} vers {self.destination} [{self.statut.value}] – {self.avion}"


# --- AFFECTATION ---
class Affectation:
    vol: Vol
    piste: Piste

    def __init__(self, vol: Vol, piste: Piste):
        self.vol = vol
        self.piste = piste

    def effectuer(self) -> None:
        if not self.piste.occupee and self.vol.statut == StatutVol.PREVU:
            self.piste.occuper()
            self.vol.decoller()

    def liberer(self) -> None:
        self.vol.atterrir()
        self.piste.liberer()

    def __str__(self) -> str:
        return f"Affectation : {self.vol.numero} ←→ {self.piste.numero}"


# --- Exemple de tests ---
if __name__ == "__main__":
    avion = Avion("F-GKXJ", "A320")
    piste = Piste("27L", 3900)
    vol = Vol("AF123", "Lyon", avion)
    affectation = Affectation(vol, piste)

    print(vol)
    affectation.effectuer()
    print(vol)
    affectation.liberer()
    print(vol)
```

---

### ✅ Résumé des annotations utilisées :

| Élément             | Exemple                               |
| ------------------- | ------------------------------------- |
| Objet simple        | `avion: Avion`                        |
| Enum                | `statut: StatutVol`                   |
| Valeur optionnelle  | `heure_decollage: Optional[datetime]` |
| Méthode sans retour | `-> None`                             |
| Méthode avec retour | `-> Optional[float]`                  |

---
