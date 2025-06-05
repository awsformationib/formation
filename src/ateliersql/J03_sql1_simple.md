
# 🛫 Atelier CRUD MySQL – Python & `mysql-connector-python`

## 🎯 Objectif

Manipuler une base de données MySQL sans ORM à l’aide de requêtes SQL directes pour effectuer les opérations CRUD sur des objets `Vol`.

## 🧱 Prérequis

* Base MySQL `formation` accessible
* Table `vols` existante ou à créer (voir plus bas)
* Module Python `mysql-connector-python` installé (`pip install mysql-connector-python`)
* Notions de base en SQL

## 📋 Structure attendue pour la table `vols`

```sql
CREATE TABLE vols (
    numero VARCHAR(10) PRIMARY KEY,
    destination VARCHAR(50),
    avion VARCHAR(50),
    statut VARCHAR(20),
    heure_creation DATETIME,
    heure_decollage DATETIME,
    heure_arrivee DATETIME
);
```

---

## 🧩 Classe Python `Vol`

```
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

## 🔌 Connexion à la base

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

## 🧪 Tâches demandées

### 1️⃣ **Créer un vol**

Écrire une fonction `ajouter_vol(vol: Vol)` qui insère un vol en base.

### 2️⃣ **Lire tous les vols**

Écrire une fonction `lister_vols()` qui retourne tous les vols sous forme de liste d’objets `Vol`.

### 3️⃣ **Chercher un vol par numéro**

Écrire une fonction `chercher_vol_par_numero(numero: str)`.

### 4️⃣ **Mettre à jour un vol (statut ou horaires)**

Écrire une fonction `mettre_a_jour_statut(numero: str, nouveau_statut: str)`.

### 5️⃣ **Supprimer un vol**

Écrire une fonction `supprimer_vol(numero: str)`.

---

## 🧪 Exemple d’appel

```
from datetime import datetime

v1 = Vol("AF123", "Tokyo", "Boeing 777", "prévu",
         datetime.now(), None, None)

ajouter_vol(v1)
vol = chercher_vol_par_numero("AF123")
print(vol.destination)
mettre_a_jour_statut("AF123", "décollé")
supprimer_vol("AF123")
```

---

## 🔍 Astuces pour les participants

* Utilisez `cursor.execute(...)` avec des **paramètres (%s)** pour éviter les injections SQL.
* Gérez bien la **fermeture** du curseur et de la connexion (`cursor.close()`, `conn.close()`).
* Utilisez des blocs `try/except` pour capturer les erreurs de connexion ou requête.
* Transformez les résultats SQL (`fetchall()`) en objets `Vol`.

---

## 📌 Bonus (optionnel)

* Permettre une **recherche partielle** par destination (`LIKE '%tokyo%'`)
* Ajouter une fonction de **pagination** (retourner X vols à la fois)
