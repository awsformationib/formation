
# ✅ Fiche Solution – Atelier CRUD `Vol` avec `mysql-connector-python`

## 📦 Rappel : Classe `Vol`

```
from datetime import datetime

class Vol:
    def __init__(self, numero, destination, avion, statut, heure_creation, heure_decollage, heure_arrivee):
        self.numero = numero
        self.destination = destination
        self.avion = avion
        self.statut = statut
        self.heure_creation = heure_creation
        self.heure_decollage = heure_decollage
        self.heure_arrivee = heure_arrivee
```

---

## 🔌 Connexion MySQL

```
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="votre_mot_de_passe",
        database="formation"
    )
```

---

## 🧱 Fonction `ajouter_vol(vol)`

```
def ajouter_vol(vol: Vol):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = """
        INSERT INTO vols (numero, destination, avion, statut, heure_creation, heure_decollage, heure_arrivee)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            vol.numero,
            vol.destination,
            vol.avion,
            vol.statut,
            vol.heure_creation,
            vol.heure_decollage,
            vol.heure_arrivee
        ))
        conn.commit()
    finally:
        cursor.close()
        conn.close()
```

---

## 📖 Fonction `lister_vols()`

```
def lister_vols():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM vols")
        rows = cursor.fetchall()
        vols = [Vol(*row) for row in rows]
        return vols
    finally:
        cursor.close()
        conn.close()
```

---

## 🔍 Fonction `chercher_vol_par_numero(numero)`

```
def chercher_vol_par_numero(numero: str):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM vols WHERE numero = %s", (numero,))
        row = cursor.fetchone()
        if row:
            return Vol(*row)
        else:
            return None
    finally:
        cursor.close()
        conn.close()
```

---

## 🛠️ Fonction `mettre_a_jour_statut(numero, nouveau_statut)`

```
def mettre_a_jour_statut(numero: str, nouveau_statut: str):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE vols SET statut = %s WHERE numero = %s", (nouveau_statut, numero))
        conn.commit()
    finally:
        cursor.close()
        conn.close()
```

---

## 🗑️ Fonction `supprimer_vol(numero)`

```
def supprimer_vol(numero: str):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM vols WHERE numero = %s", (numero,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()
```

---

## 🔎 Bonus : Recherche par destination (LIKE)

```
def chercher_par_destination(partiel: str):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM vols WHERE destination LIKE %s", ('%' + partiel + '%',))
        rows = cursor.fetchall()
        return [Vol(*row) for row in rows]
    finally:
        cursor.close()
        conn.close()
```
