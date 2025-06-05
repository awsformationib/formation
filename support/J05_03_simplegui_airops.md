![Logo](images\logo.png)


## 🧩 Fiche participant – Étape 2 : Intégrer une interface graphique simple avec PySimpleGUI

---

### 🎯 **Objectif**

Créer une petite application Python qui :
✅ Se connecte à la base MySQL (comme en étape 1),
✅ Récupère la liste des vols,
✅ Affiche les vols dans une **interface graphique simple** avec **PySimpleGUI**,
✅ Ajoute un bouton “Rafraîchir” pour recharger les données depuis la base.

---

### 📂 **Structure attendue**

```
/projet_airops_etape2
    config.json
    app_gui.py
```

---

### 📦 **Prérequis**

Installez PySimpleGUI :

```
pip install PySimpleGUI
```

---

### 🏗 **Bribes de code pour démarrer**

---

#### 🛠 Étape 1 : Charger la config et connecter MySQL

Réutilisez les fonctions déjà vues dans l’étape 1 :

```
import argparse
import json
import mysql.connector

def charger_config():
    parser = argparse.ArgumentParser(description="AirOps - Étape 2")
    parser.add_argument("--config", required=True, help="Chemin du fichier JSON")
    args = parser.parse_args()
    with open(args.config, 'r') as f:
        return json.load(f)

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

#### 🛠 Étape 2 : Lire les vols

```
def lire_vols(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT numero, destination FROM vols")
    return cursor.fetchall()
```

---

#### 🛠 Étape 3 : Créer l’interface avec PySimpleGUI

```
import PySimpleGUI as sg

def afficher_interface(vols):
    layout = [
        [sg.Text("Liste des vols")],
        [sg.Listbox(values=[f"{v[0]} → {v[1]}" for v in vols], size=(40, 10), key='-VOLLIST-')],
        [sg.Button("Rafraîchir"), sg.Button("Quitter")]
    ]

    window = sg.Window("AirOps Interface", layout)

    while True:
        event, _ = window.read()
        if event in (sg.WINDOW_CLOSED, "Quitter"):
            break
        if event == "Rafraîchir":
            # TODO: Recharger les vols et mettre à jour la liste
            pass

    window.close()
```

---

### 🔄 **Cycle complet**

1️⃣ Charger la config,
2️⃣ Se connecter à MySQL,
3️⃣ Récupérer et afficher les vols dans l’interface,
4️⃣ Rafraîchir les données sur demande.

---

### 🧪 **Mini-exercice**

* Créez un fichier `app_gui.py` qui intègre toutes ces étapes.
* Remplacez le `pass` dans le bouton “Rafraîchir” pour qu’il recharge vraiment les vols.
* Testez l’application avec :

```
python app_gui.py --config config.json
```

---

### 📋 **Points d’attention**

✅ Vérifiez que vous fermez la connexion MySQL proprement.
✅ Affichez un message clair si la connexion échoue.
✅ Bonus : ajoutez une couleur spéciale pour les vols vers une destination spécifique (ex. Paris).

---

### 💬 **Prochaines étapes**

Dans l’étape suivante, nous :
✅ Générerons un rapport PDF à partir des données affichées.
✅ Ajouterons un bouton dans l’interface pour déclencher cette génération.

---
