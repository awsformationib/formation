
# 🧩 Étape 3 – Ajouter, modifier, supprimer via API REST (POST/PUT/DELETE)

## 🎯 Objectif

* Ajouter un objet (`POST`)
* Modifier un objet (`PUT`)
* Supprimer un objet (`DELETE`)
* Tous les appels passent via l'API Flask locale (ex: `http://localhost:5000/api/avions`)

---

## 🔁 1. Attendus côté API Flask (convention REST)

| Action                  | Méthode  | URL                | Corps JSON attendu              |
| ----------------------- | -------- | ------------------ | ------------------------------- |
| Obtenir tous les avions | `GET`    | `/api/avions`      | —                               |
| Ajouter un avion        | `POST`   | `/api/avions`      | `{"id": 3, "modele": ..., ...}` |
| Modifier un avion       | `PUT`    | `/api/avions/<id>` | `{"modele": ..., ...}`          |
| Supprimer un avion      | `DELETE` | `/api/avions/<id>` | —                               |

Même structure pour `/api/pilotes` et `/api/vols`.

---

## 🔧 2. Fonctions Python pour l’API

```
import requests

BASE_URL = "http://localhost:5000/api"

# ----- AVIONS -----
def ajouter_avion(avion_data):
    response = requests.post(f"{BASE_URL}/avions", json=avion_data)
    response.raise_for_status()

def modifier_avion(avion_id, avion_data):
    response = requests.put(f"{BASE_URL}/avions/{avion_id}", json=avion_data)
    response.raise_for_status()

def supprimer_avion(avion_id):
    response = requests.delete(f"{BASE_URL}/avions/{avion_id}")
    response.raise_for_status()
```

---

## 🧩 3. Intégration à l’interface

### ✅ a. Ajouter un avion (via formulaire)

* Bouton : `Ajouter un avion`
* Ouvre une `QDialog` avec un `QFormLayout`
* À la validation : appel à `ajouter_avion(...)` + actualisation de la table

### ✅ b. Modifier un avion sélectionné

* Bouton : `Modifier`
* Pré-remplit le formulaire avec les données sélectionnées
* Appelle `modifier_avion(id, ...)` à la soumission

### ✅ c. Supprimer un avion

* Bouton : `Supprimer`
* Supprime la ligne sélectionnée après confirmation `QMessageBox`
* Appelle `supprimer_avion(id)`

---

## 🧱 4. Exemple rapide – formulaire `QDialog` pour ajouter un avion

```
from PySide6.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QLineEdit, QPushButton

class AvionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Ajouter un avion")
        self.layout = QVBoxLayout()
        self.form = QFormLayout()
        self.id_input = QLineEdit()
        self.modele_input = QLineEdit()
        self.desc_input = QLineEdit()
        self.vitesse_input = QLineEdit()

        self.form.addRow("ID", self.id_input)
        self.form.addRow("Modèle", self.modele_input)
        self.form.addRow("Description", self.desc_input)
        self.form.addRow("Vitesse max", self.vitesse_input)
        self.layout.addLayout(self.form)

        btn = QPushButton("Valider")
        btn.clicked.connect(self.submit)
        self.layout.addWidget(btn)
        self.setLayout(self.layout)

    def submit(self):
        avion_data = {
            "id": int(self.id_input.text()),
            "modele": self.modele_input.text(),
            "description": self.desc_input.text(),
            "vitesse_max": int(self.vitesse_input.text())
        }
        try:
            ajouter_avion(avion_data)
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Échec de l’ajout : {e}")
```

---

## ✅ Étapes à suivre côté API Flask

* Côté `@app.route("/api/avions", methods=["POST"])` :

  * Ajouter un avion à la base / structure en mémoire
* Idem pour `PUT` et `DELETE`
* Retourner `JSONResponse(status=201)` ou `204` sans contenu

---

## 🧪 Tests à prévoir

* Création manuelle via l'interface d’un nouvel avion
* Modification d’un avion → vérification sur serveur (ex : avec Postman)
* Suppression et actualisation de la table

