# 🛫 ALTERNATIVE Atelier CRUD SqlLite – Python 

### ✅ 1. Création de la base et de la table `vols` en SQLite

```
import sqlite3
from datetime import datetime

# Connexion à la base SQLite
conn = sqlite3.connect("vols.db")
cursor = conn.cursor()

# Création de la table conforme à ta structure
cursor.execute("""
CREATE TABLE IF NOT EXISTS vols (
    numero TEXT PRIMARY KEY,
    destination TEXT,
    avion TEXT,
    statut TEXT,
    heure_creation TEXT,
    heure_decollage TEXT,
    heure_arrivee TEXT
)
""")
conn.commit()
```

> En SQLite, on utilise `TEXT` pour les dates/heure au format ISO (ex: `'2025-06-05 08:45:00'`) — SQLite ne possède pas un type `DATETIME` natif strict comme MySQL.

---

### ✅ 2. Classe Python `Vol`

```
class Vol:
    def __init__(self, numero, destination, avion, statut,
                 heure_creation, heure_decollage, heure_arrivee):
        self.numero = numero
        self.destination = destination
        self.avion = avion
        self.statut = statut
        self.heure_creation = heure_creation
        self.heure_decollage = heure_decollage
        self.heure_arrivee = heure_arrivee
```

---

### ✅ 3. Fonction d’insertion

```
def enregistrer_vol(vol: Vol):
    cursor.execute("""
    INSERT INTO vols (numero, destination, avion, statut, 
                      heure_creation, heure_decollage, heure_arrivee)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        vol.numero, vol.destination, vol.avion, vol.statut,
        vol.heure_creation, vol.heure_decollage, vol.heure_arrivee
    ))
    conn.commit()
```

---

### ✅ 4. Exemple d’utilisation

```
v = Vol(
    numero="AF456",
    destination="Tokyo",
    avion="Boeing 777",
    statut="programmé",
    heure_creation=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    heure_decollage="2025-06-06 14:00:00",
    heure_arrivee="2025-06-07 06:30:00"
)

enregistrer_vol(v)

# Affichage
cursor.execute("SELECT * FROM vols")
for row in cursor.fetchall():
    print(row)

conn.close()
```

---

### ℹ️ Remarques pédagogiques

* Tu peux utiliser `datetime.strptime(...)` pour parser des dates au besoin.
* Pour des projets réels, pense à convertir `heure_*` en objets `datetime` à la lecture pour mieux les manipuler.
* SQLite est tolérant sur les types, mais mieux vaut standardiser les formats (`%Y-%m-%d %H:%M:%S`).

---
