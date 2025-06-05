![Logo](images\logo.png)


## 🧩 Fiche participant – Étape 4 : Génération PDF enrichie dans AirOps

---

### 🎯 **Objectif**

Créer une application qui :
✅ Lit les vols depuis MySQL,
✅ Affiche les vols dans une interface PySimpleGUI,
✅ Génère un rapport PDF plus avancé :

* Section résumé (nombre total de vols),
* Liste filtrée (ex. vols vers Paris),
* Format enrichi (tableaux, couleurs, etc.),
  ✅ Utilise de façon **pythonic** :
* Générateurs pour traiter les données,
* Listes en compréhension,
* Fonctions comme `filter()`, `map()`.

---

### 📂 **Structure attendue**

```
/projet_airops_etape4
    config.json
    app_gui_pdf_plus.py
```

---

### 📦 **Prérequis**

Installez les librairies nécessaires :

```
pip install PySimpleGUI weasyprint
```

---

### 🏗 **Bribes de code pour démarrer**

---

#### 🛠 Étape 1 : Préparer les données avec des techniques Pythonic

```
def vols_par_destination(vols, destination="paris"):
    # Liste en compréhension + filtrage
    return [v for v in vols if v[1].lower() == destination.lower()]

def nombres_vols(vols):
    return len(vols)

def vols_formates(vols):
    # Générateur pour produire du texte formaté
    for v in vols:
        yield f"<li>{v[0]} → {v[1]}</li>"
```

---

#### 🛠 Étape 2 : Générer le PDF enrichi

```
from weasyprint import HTML

def generer_rapport_pdf(vols, fichier_pdf="rapport_vols.pdf"):
    total = nombres_vols(vols)
    paris_vols = vols_par_destination(vols)

    html = f"<h1>Rapport des vols</h1>"
    html += f"<p>Total des vols : {total}</p>"
    html += "<h2>Liste complète</h2><ul>"
    html += "".join(vols_formates(vols))
    html += "</ul>"

    html += "<h2>Vols vers Paris</h2><ul>"
    html += "".join(vols_formates(paris_vols))
    html += "</ul>"

    HTML(string=html).write_pdf(fichier_pdf)
    print(f"Rapport généré : {fichier_pdf}")
```

---

#### 🛠 Étape 3 : Intégrer dans l’interface GUI

```
import PySimpleGUI as sg

def afficher_interface(vols):
    layout = [
        [sg.Text("Liste des vols")],
        [sg.Listbox(values=[f"{v[0]} → {v[1]}" for v in vols], size=(40, 10), key='-VOLLIST-')],
        [sg.Button("Rafraîchir"), sg.Button("Générer rapport PDF"), sg.Button("Quitter")]
    ]

    window = sg.Window("AirOps Interface", layout)

    while True:
        event, _ = window.read()
        if event in (sg.WINDOW_CLOSED, "Quitter"):
            break
        if event == "Rafraîchir":
            # TODO: Recharger les vols et mettre à jour la liste
            pass
        if event == "Générer rapport PDF":
            generer_rapport_pdf(vols)
            sg.popup("Rapport PDF généré !", title="Succès")

    window.close()
```

---

### 🧪 **Mini-exercice**

✅ Complétez `app_gui_pdf_plus.py` pour assembler les fonctions,
✅ Utilisez **au moins deux** techniques Pythonic dans le traitement des vols,
✅ Générer un PDF lisible et clair,
✅ Bonus : ajoutez une section colorée ou stylée (avec HTML/CSS simple).

---

### 📋 **Points d’attention**

✅ Testez bien les caractères spéciaux (ex. villes avec accents).
✅ Assurez-vous que le fichier PDF est généré même après plusieurs rafraîchissements.
✅ Protégez la génération contre les listes vides.

---
