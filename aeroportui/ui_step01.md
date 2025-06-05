
# 🧭 Objectif du projet

Créer une interface graphique pour :

* Visualiser une **liste d’avions**
* Visualiser et lier des **vols** à des **pilotes** et **avions**
* Afficher les détails de chaque vol

---

## 🗂️ Modèle de données

```
class Avion:
    def __init__(self, id, modele, description, vitesse_max):
        self.id = id
        self.modele = modele
        self.description = description
        self.vitesse_max = vitesse_max

class Pilote:
    def __init__(self, id, nom, licence):
        self.id = id
        self.nom = nom
        self.licence = licence

class Vol:
    def __init__(self, numero, destination, statut, heure_decollage, heure_arrivee, avion_id, pilote_id):
        self.numero = numero
        self.destination = destination
        self.statut = statut
        self.heure_decollage = heure_decollage
        self.heure_arrivee = heure_arrivee
        self.avion_id = avion_id
        self.pilote_id = pilote_id
```

---

## 🧱 Étapes du projet

### ✅ **Étape 1 – Structure minimale de l’interface**

* Créer une fenêtre principale avec PySide6 (ou PyQt6)
* Ajouter un `QTabWidget` avec 3 onglets : `Avions`, `Pilotes`, `Vols`
* Afficher des données factices dans chaque onglet via `QTableWidget`

🎯 Objectif : architecture générale de l’UI, affichage des objets

---

### ✅ **Étape 2 – Lecture depuis un fichier JSON ou CSV**

* Charger la liste des objets (Avion, Pilote, Vol) depuis un fichier
* Afficher dynamiquement les données dans les tables
* Lier les données aux objets Python

🎯 Objectif : séparation modèle / vue + interaction réelle

---

### ✅ **Étape 3 – Fiche de détail + formulaire d’ajout**

* Ajouter un bouton "Détails" → ouvre un `QDialog` avec les infos complètes de l’objet sélectionné
* Ajouter un bouton "Ajouter un avion/pilote/vol" → ouvre un formulaire
* Le formulaire envoie les données et met à jour la liste

🎯 Objectif : interaction avec les objets + input utilisateur

---

### ✅ **Étape 4 – Liaisons entre objets**

* Dans l’onglet Vols :

  * Afficher non seulement `avion_id`, mais aussi `modele` de l’avion
  * Afficher le nom du pilote à partir de `pilote_id`
* Utiliser un `QComboBox` pour sélectionner un pilote ou un avion dans le formulaire Vol

🎯 Objectif : relations inter-objets et affichage enrichi

---

### ✅ **Étape 5 – Améliorations graphiques**

* Mise en page propre avec `QVBoxLayout` / `QFormLayout`
* Tri par colonnes, recherche simple (`QLineEdit` + filtre)
* Affichage conditionnel : statut de vol coloré (ex : "prévu", "décollé", "annulé")

🎯 Objectif : expérience utilisateur + esthétique

---

### ✅ **Étape 6 – Export et persistance**

* Sauvegarder les objets dans un fichier `.json` à la fermeture
* Recharger automatiquement les données à l’ouverture
* (optionnel) Support d’une base SQLite

🎯 Objectif : persistance des données

---

## 💡 Option avancée : architecture MVC

* Modèle : objets Python
* Vue : `QWidget`, `QDialog`, `QTableWidget`
* Contrôleur : fonctions de mise à jour, lecture, liaison

---

## 🧪 Départ rapide – Exemple d’interface (Étape 1)

```
from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion des vols")
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        self.setup_tabs()

    def setup_tabs(self):
        self.tabs.addTab(self.create_table_widget("Avions", ["ID", "Modèle", "Vitesse"]), "Avions")
        self.tabs.addTab(self.create_table_widget("Pilotes", ["ID", "Nom", "Licence"]), "Pilotes")
        self.tabs.addTab(self.create_table_widget("Vols", ["Numéro", "Destination", "Avion", "Pilote"]), "Vols")

    def create_table_widget(self, title, headers):
        widget = QWidget()
        layout = QVBoxLayout()
        table = QTableWidget(0, len(headers))
        table.setHorizontalHeaderLabels(headers)
        layout.addWidget(table)
        widget.setLayout(layout)
        return widget

app = QApplication(sys.argv)
window = MainWindow()
window.resize(800, 600)
window.show()
sys.exit(app.exec())
```
