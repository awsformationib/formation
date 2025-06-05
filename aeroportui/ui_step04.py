# dialogs.py

from PySide6.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QMessageBox

class AvionDialog(QDialog):
    def __init__(self, avion=None, on_submit=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Avion")
        self.on_submit = on_submit
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

        if avion:
            self.id_input.setText(str(avion.id))
            self.modele_input.setText(avion.modele)
            self.desc_input.setText(avion.description)
            self.vitesse_input.setText(str(avion.vitesse_max))

    def submit(self):
        try:
            avion_data = {
                "id": int(self.id_input.text()),
                "modele": self.modele_input.text(),
                "description": self.desc_input.text(),
                "vitesse_max": int(self.vitesse_input.text())
            }
            if self.on_submit:
                self.on_submit(avion_data)
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Erreur", str(e))


class PiloteDialog(QDialog):
    def __init__(self, pilote=None, on_submit=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Pilote")
        self.on_submit = on_submit
        self.layout = QVBoxLayout()
        self.form = QFormLayout()

        self.id_input = QLineEdit()
        self.nom_input = QLineEdit()
        self.licence_input = QLineEdit()

        self.form.addRow("ID", self.id_input)
        self.form.addRow("Nom", self.nom_input)
        self.form.addRow("Licence", self.licence_input)

        self.layout.addLayout(self.form)
        btn = QPushButton("Valider")
        btn.clicked.connect(self.submit)
        self.layout.addWidget(btn)
        self.setLayout(self.layout)

        if pilote:
            self.id_input.setText(str(pilote.id))
            self.nom_input.setText(pilote.nom)
            self.licence_input.setText(pilote.licence)

    def submit(self):
        try:
            pilote_data = {
                "id": int(self.id_input.text()),
                "nom": self.nom_input.text(),
                "licence": self.licence_input.text()
            }
            if self.on_submit:
                self.on_submit(pilote_data)
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Erreur", str(e))


class VolDialog(QDialog):
    def __init__(self, vol=None, on_submit=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Vol")
        self.on_submit = on_submit
        self.layout = QVBoxLayout()
        self.form = QFormLayout()

        self.numero_input = QLineEdit()
        self.destination_input = QLineEdit()
        self.statut_input = QLineEdit()
        self.decollage_input = QLineEdit()
        self.arrivee_input = QLineEdit()
        self.avion_id_input = QLineEdit()
        self.pilote_id_input = QLineEdit()

        self.form.addRow("Numéro", self.numero_input)
        self.form.addRow("Destination", self.destination_input)
        self.form.addRow("Statut", self.statut_input)
        self.form.addRow("Heure de décollage", self.decollage_input)
        self.form.addRow("Heure d'arrivée", self.arrivee_input)
        self.form.addRow("Avion ID", self.avion_id_input)
        self.form.addRow("Pilote ID", self.pilote_id_input)

        self.layout.addLayout(self.form)
        btn = QPushButton("Valider")
        btn.clicked.connect(self.submit)
        self.layout.addWidget(btn)
        self.setLayout(self.layout)

        if vol:
            self.numero_input.setText(vol.numero)
            self.destination_input.setText(vol.destination)
            self.statut_input.setText(vol.statut)
            self.decollage_input.setText(vol.heure_decollage)
            self.arrivee_input.setText(vol.heure_arrivee)
            self.avion_id_input.setText(str(vol.avion_id))
            self.pilote_id_input.setText(str(vol.pilote_id))

    def submit(self):
        try:
            vol_data = {
                "numero": self.numero_input.text(),
                "destination": self.destination_input.text(),
                "statut": self.statut_input.text(),
                "heure_decollage": self.decollage_input.text(),
                "heure_arrivee": self.arrivee_input.text(),
                "avion_id": int(self.avion_id_input.text()),
                "pilote_id": int(self.pilote_id_input.text())
            }
            if self.on_submit:
                self.on_submit(vol_data)
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Erreur", str(e))
