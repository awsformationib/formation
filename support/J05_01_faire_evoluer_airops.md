![Logo](images\logo.png)


## 🧩 Plan de la journée finale – Projet AirOps évolué

---

### 🎯 **Objectif général**

Faire évoluer le projet fil rouge AirOps pour :
✅ Lire et écrire des données dans une base MySQL,
✅ Afficher les résultats dans une interface graphique simple,
✅ Générer un rapport PDF automatisé,
✅ Le tout structuré en ateliers progressifs.

Chaque atelier apportera une nouvelle brique et permettra aux participants de pratiquer sur un projet complet et réaliste.

---

### 🏗 **Étape 1 – Connexion MySQL (lecture)**

✅ **Objectif :** Se connecter à une base MySQL contenant les données de vols et avions, et les lire dans Python.

| Contenu atelier                                                         |
| ----------------------------------------------------------------------- |
| Installer `mysql-connector-python` ou `SQLAlchemy`.                     |
| Écrire une fonction Python qui récupère la liste des vols depuis MySQL. |
| Afficher les résultats dans la console pour vérification.               |

**Bribe de départ :**

```python
import mysql.connector

def get_vols():
    conn = mysql.connector.connect(
        host="localhost", user="user", password="pass", database="airops"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT numero, destination FROM vols")
    return cursor.fetchall()
```

---

### 🏗 **Étape 2 – Écriture MySQL (ajout ou mise à jour)**

✅ **Objectif :** Permettre d’ajouter un nouveau vol ou de mettre à jour son statut directement depuis Python.

| Contenu atelier                                                |
| -------------------------------------------------------------- |
| Écrire une fonction Python pour insérer un vol.                |
| Écrire une fonction Python pour mettre à jour un vol existant. |
| Valider que les modifications apparaissent dans la base.       |

**Bribe de départ :**

```python
def ajouter_vol(numero, destination):
    cursor.execute(
        "INSERT INTO vols (numero, destination) VALUES (%s, %s)",
        (numero, destination)
    )
    conn.commit()
```

---

### 🏗 **Étape 3 – Interface graphique simple**

✅ **Objectif :** Afficher les informations de vols dans une petite interface GUI.

| Contenu atelier                                            |
| ---------------------------------------------------------- |
| Utiliser `tkinter` (simple), `PySimpleGUI`, ou `PySide6`.  |
| Créer une fenêtre listant les vols récupérés.              |
| Ajouter un bouton “Rafraîchir” pour recharger les données. |

**Bribe de départ (tkinter) :**

```python
import tkinter as tk

root = tk.Tk()
root.title("AirOps")

label = tk.Label(root, text="Liste des vols")
label.pack()

# Afficher les vols ici

root.mainloop()
```

---

### 🏗 **Étape 4 – Génération de rapport PDF**

✅ **Objectif :** Générer un fichier PDF contenant un résumé des vols, à partir des données récupérées.

| Contenu atelier                                                           |
| ------------------------------------------------------------------------- |
| Utiliser `reportlab` ou `WeasyPrint`.                                     |
| Générer un fichier `rapport_vols.pdf` listant les vols.                   |
| Ajouter des sections (total des vols, répartition par destination, etc.). |

**Bribe de départ (WeasyPrint) :**

```python
from weasyprint import HTML

html = "<h1>Rapport des vols</h1><ul>"
for vol in vols:
    html += f"<li>{vol}</li>"
html += "</ul>"

HTML(string=html).write_pdf("rapport_vols.pdf")
```

---

### 🏗 **Étape 5 – Atelier final combiné**

✅ **Objectif :** Assembler tout :

* Lire depuis MySQL,
* Afficher dans l’interface graphique,
* Générer un rapport PDF avec un bouton,
* Vérifier que les mises à jour se répercutent partout.

| Contenu atelier                                                         |
| ----------------------------------------------------------------------- |
| Lancer l’interface graphique.                                           |
| Charger les vols depuis la base.                                        |
| Permettre à l’utilisateur de générer un rapport PDF depuis l’interface. |

**Question rebond :**
👉 Comment organiser les fichiers et modules pour garder un code lisible et maintenable ?
👉 Quels sont les pièges classiques quand on combine interface, base de données et génération de documents ?

---

### 🧪 **Idées bonus pour aller plus loin**

✅ Ajouter un filtre dans l’interface (par destination, par statut).
✅ Générer des graphiques (avec `matplotlib`) dans le rapport PDF.
✅ Écrire des tests automatisés pour les fonctions MySQL.
✅ Ajouter une authentification simple dans l’interface.

---
