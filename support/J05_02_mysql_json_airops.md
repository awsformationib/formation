![Logo](images\logo.png)


## 🧩 Fiche participant – Étape 1 : Lire et écrire des vols avec MySQL

---

### 🎯 **Objectif**

Construire une petite application Python qui, à chaque exécution :
✅ Lit les vols existants dans une base MySQL (au démarrage),
✅ Permet d’ajouter un ou plusieurs nouveaux vols (dans le code pour cette version simple),
✅ Écrit les nouvelles données dans la base à la fin,
✅ Utilise un fichier de configuration `.json` (host, user, password, database),
✅ Prend en paramètre l’emplacement de ce fichier `.json` via la ligne de commande.

---

### 📂 **Structure attendue**

```
/projet_airops_etape1
    config.json
    app.py
```

---

### 📄 **Exemple de fichier `config.json`**

```json
{
    "host": "localhost",
    "user": "airops_user",
    "password": "airops_pass",
    "database": "airops"
}
```

---

### 🏗 **Bribes de code pour démarrer**

---

#### 🛠 Étape 1 : Charger la config avec `argparse`

```
import argparse
import json

def charger_config():
    parser = argparse.ArgumentParser(description="AirOps - Étape 1")
    parser.add_argument("--config", required=True, help="Chemin du fichier de configuration JSON")
    args = parser.parse_args()

    with open(args.config, 'r') as f:
        config = json.load(f)
    return config
```

---

#### 🛠 Étape 2 : Se connecter à MySQL

```
import mysql.connector

def connecter_mysql(config):
    conn = mysql.connector.connect(
        host=config['host'],
        user=config['user'],
        password=config['password'],
        database=config['database']
    )
    return conn
```

---

#### 🛠 Étape 3 : Lire les vols

```
def lire_vols(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT numero, destination FROM vols")
    vols = cursor.fetchall()
    for vol in vols:
        print(f"Vol {vol[0]} → {vol[1]}")
```

---

#### 🛠 Étape 4 : Ajouter un vol

> Pour cette version simple, on ajoute des vols directement dans le code (pas encore depuis l’interface utilisateur).

```
def ajouter_vol(conn, numero, destination):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO vols (numero, destination) VALUES (%s, %s)",
        (numero, destination)
    )
    conn.commit()
    print(f"Vol {numero} ajouté vers {destination}")
```

---

### 🔄 **Cycle complet**

1️⃣ Charger la config.
2️⃣ Se connecter à MySQL.
3️⃣ Lire et afficher les vols existants.
4️⃣ Ajouter de nouveaux vols.
5️⃣ Fermer la connexion.

---

### 🧪 **Mini-exercice**

* Créez un fichier `app.py` qui intègre toutes ces étapes.
* Ajoutez **au moins deux vols** au moment de l’insertion (ex. `AF456`, `BA789`).
* Testez que le programme lit les données au départ, et que les nouveaux vols apparaissent dans la base après exécution.

---

### 📋 **Points d’attention**

✅ Pensez à gérer les erreurs (connexion impossible, table manquante, etc.).
✅ Nettoyez vos ressources (fermez les connexions).
✅ Évitez d’insérer des doublons si possible (bonus).
✅ Vérifiez que la structure de la table `vols` existe bien dans MySQL.

---

### 💬 **Prochaines étapes**

Dans les ateliers suivants, nous :
✅ Intégrerons une interface graphique pour voir ces données,
✅ Permettrons de déclencher l’écriture depuis l’interface,
✅ Générerons des rapports PDF automatiques.

