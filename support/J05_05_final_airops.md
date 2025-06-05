![Logo](images\logo.png)


## 🏁 Fiche participant – Étape finale : AirOps complet

---

### 🎯 **Objectif final**

Assembler une application Python complète qui :
✅ Lit et écrit des vols dans MySQL,
✅ Affiche les vols dans une interface graphique moderne,
✅ Rafraîchit dynamiquement les données,
✅ Génère un rapport PDF enrichi avec résumé et listes filtrées,
✅ Utilise des techniques Pythonic élégantes,
✅ Suit une architecture modulaire et maintenable.

---

### 📂 **Structure attendue**

```
/air_ops_final
    config.json
    app.py
    /modules
        db.py
        gui.py
        reporting.py
        utils.py
```

---

### 🏗 **Modules à assembler**

---

#### 📦 `db.py` (module base de données)

✅ Se connecter à MySQL,
✅ Lire les vols,
✅ Ajouter un vol,
✅ Mettre à jour les informations si nécessaire.

```
import mysql.connector

def connecter(config):
    return mysql.connector.connect(
        host=config['host'],
        user=config['user'],
        password=config['password'],
        database=config['database']
    )

def lire_vols(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT numero, destination FROM vols")
    return cursor.fetchall()

def ajouter_vol(conn, numero, destination):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO vols (numero, destination) VALUES (%s, %s)",
        (numero, destination)
    )
    conn.commit()
```

---

#### 📦 `gui.py` (module interface graphique)

✅ Afficher les vols,
✅ Boutons : Rafraîchir, Générer rapport, Quitter.

```
import PySimpleGUI as sg

def afficher_interface(vols, callbacks):
    layout = [
        [sg.Text("Liste des vols")],
        [sg.Listbox(values=[f"{v[0]} → {v[1]}" for v in vols], size=(40, 10), key='-VOLLIST-')],
        [sg.Button("Rafraîchir"), sg.Button("Générer rapport PDF"), sg.Button("Quitter")]
    ]

    window = sg.Window("AirOps Final", layout)

    while True:
        event, _ = window.read()
        if event in (sg.WINDOW_CLOSED, "Quitter"):
            break
        if event == "Rafraîchir":
            callbacks['rafraichir']()
        if event == "Générer rapport PDF":
            callbacks['generer_rapport']()

    window.close()
```

---

#### 📦 `reporting.py` (module rapport PDF)

✅ Générer un rapport enrichi :

* Total des vols,
* Liste complète,
* Liste filtrée (ex. vers Paris).

```
from weasyprint import HTML

def generer_rapport(vols, fichier_pdf="rapport_final.pdf"):
    total = len(vols)
    paris_vols = [v for v in vols if v[1].lower() == "paris"]

    html = f"<h1>Rapport AirOps</h1><p>Total des vols : {total}</p><h2>Liste complète</h2><ul>"
    html += "".join(f"<li>{v[0]} → {v[1]}</li>" for v in vols)
    html += "</ul><h2>Vols vers Paris</h2><ul>"
    html += "".join(f"<li>{v[0]} → {v[1]}</li>" for v in paris_vols)
    html += "</ul>"

    HTML(string=html).write_pdf(fichier_pdf)
```

---

#### 📦 `utils.py` (module utilitaires)

✅ Charger la config,
✅ Préparer des traitements Pythonic (générateurs, map, filter…).

```
import argparse
import json

def charger_config():
    parser = argparse.ArgumentParser(description="AirOps Final")
    parser.add_argument("--config", required=True, help="Chemin du fichier JSON")
    args = parser.parse_args()
    with open(args.config, 'r') as f:
        return json.load(f)
```

---

### 🔗 **Fichier principal `app.py`**

Assemble tout :
✅ Charge la config,
✅ Connecte la base,
✅ Rafraîchit les vols,
✅ Branche les callbacks.

```
from modules.db import connecter, lire_vols
from modules.gui import afficher_interface
from modules.reporting import generer_rapport
from modules.utils import charger_config

def main():
    config = charger_config()
    conn = connecter(config)
    vols = lire_vols(conn)

    def rafraichir():
        nonlocal vols
        vols = lire_vols(conn)
        print("Vols rafraîchis")

    def generer():
        generer_rapport(vols)
        print("Rapport généré")

    afficher_interface(vols, {'rafraichir': rafraichir, 'generer_rapport': generer})
    conn.close()

if __name__ == "__main__":
    main()
```

---

### 🧪 **Défi final**

✅ Complétez chaque module,
✅ Testez le projet complet,
✅ Présentez une mini-démo aux autres participants,
✅ Bonus : ajoutez une fonctionnalité originale (export CSV, filtrage avancé, graphes, etc.).
