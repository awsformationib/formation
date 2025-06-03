![Logo](images\logo.png)


## 🧩 Fiche 1.5 – Modules & scripts

---

### 📁 Structure du dossier

```
aeroport/
├── avions.py
├── vols.py
├── utils.py
└── main.py
```

---

### ✅ `avions.py`

```python
# avions.py

def creer_avion(code):
    """Crée un dictionnaire représentant un avion."""
    return {"immatriculation": code}
```

---

### ✅ `vols.py`

```python
# vols.py

def creer_vol(numero, destination, avion):
    """Crée un dictionnaire représentant un vol avec un avion assigné."""
    return {
        "numero": numero,
        "destination": destination,
        "avion": avion
    }
```

---

### ✅ `utils.py`

```python
# utils.py

def afficher_dict(label, dico):
    """Affiche proprement les éléments d’un dictionnaire."""
    print(f"\n📄 {label} :")
    for cle, valeur in dico.items():
        print(f" - {cle} : {valeur}")
```

---

### ✅ `main.py`

```python
# main.py

from avions import creer_avion
from vols import creer_vol
from utils import afficher_dict

if __name__ == "__main__":
    # Création d’un avion
    avion = creer_avion("F-GKXJ")

    # Création d’un vol associé à cet avion
    vol = creer_vol("AF123", "Toulouse", avion)

    # Affichage des résultats
    afficher_dict("Avion", avion)
    afficher_dict("Vol", vol)
```

---

### ✅ Exécution attendue de `main.py` :

```
📄 Avion :
 - immatriculation : F-GKXJ

📄 Vol :
 - numero : AF123
 - destination : Toulouse
 - avion : {'immatriculation': 'F-GKXJ'}
```
