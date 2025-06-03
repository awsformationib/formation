![Logo](images\logo.png)


## 🧩 Fiche Module Standard #5 – `dataclasses` CORRIGE

### ✅ `avion_dataclass.py`

```python
from dataclasses import dataclass, field
from uuid import uuid4

@dataclass
class Avion:
    immatriculation: str
    modele: str
    id: str = field(default_factory=lambda: str(uuid4()))

# Option bonus : version immuable
# @dataclass(frozen=True)
# class Avion:
#     immatriculation: str
#     modele: str
#     id: str = field(default_factory=lambda: str(uuid4()))

# === Exemple d'utilisation ===

if __name__ == "__main__":
    avion1 = Avion("F-GKXJ", "A320")
    avion2 = Avion("F-HBXO", "B737")
    avion3 = Avion("F-GKXJ", "A320")  # Même données que avion1 mais id différent

    print("✈️ Avions créés :")
    print(avion1)
    print(avion2)
    print(avion3)

    print("\n🔍 Comparaisons :")
    print("avion1 == avion2 ?", avion1 == avion2)
    print("avion1 == avion3 ?", avion1 == avion3)  # False car id différent

    print("\n🔒 ID uniques :")
    print(avion1.id)
    print(avion3.id)

    # Démonstration d'utilisation dans un set (grâce à __hash__)
    print("\n📦 Ajout dans un set :")
    flotte = {avion1, avion2, avion3}
    for a in flotte:
        print(a)
```

---

### ✅ Résultat attendu (extrait)

```
✈️ Avions créés :
Avion(immatriculation='F-GKXJ', modele='A320', id='b1d...')
Avion(immatriculation='F-HBXO', modele='B737', id='c7a...')
Avion(immatriculation='F-GKXJ', modele='A320', id='d5e...')

🔍 Comparaisons :
avion1 == avion2 ? False
avion1 == avion3 ? False

🔒 ID uniques :
b1d...c7a...d5e...

📦 Ajout dans un set :
Avion(immatriculation='F-HBXO', modele='B737', id='...')
...
```

---
