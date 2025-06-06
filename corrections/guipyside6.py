from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,
    QHBoxLayout, QGridLayout, QLineEdit, QMessageBox
)
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # --- Zone centrale avec des boutons dans une grille
        grid_layout = QGridLayout()
        self.buttons = []
        self.setWindowTitle("Exemple P6 - Layouts + Events")
        self.setMinimumSize(200, 100)

        # --- Layout principal (vertical)
        main_layout = QVBoxLayout()

        # --- Zone supérieure avec un label et un champ texte (horizontal)
        top_layout = QHBoxLayout()
        self.label = QLabel("Entrez votre nom :")
        self.input = QLineEdit()
        self.input.textChanged.connect(self.on_text_changed)
        top_layout.addWidget(self.label)
        top_layout.addWidget(self.input)
        main_layout.addLayout(top_layout)

        for i in range(2):
            for j in range(2):
                btn = QPushButton(f"Bouton {i},{j}")
                btn.setMinimumSize(50, 40)
                btn.setMaximumSize(200, 80)
                btn.clicked.connect(self.on_button_clicked)
                btn.enterEvent = self.make_hover_event(btn)
                self.buttons.append(btn)
                grid_layout.addWidget(btn, i, j)

        main_layout.addLayout(grid_layout)

        # --- Zone inférieure avec un bouton "OK"
        bottom_layout = QHBoxLayout()
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.show_message)
        bottom_layout.addStretch()
        bottom_layout.addWidget(self.ok_button)
        main_layout.addLayout(bottom_layout)

        self.setLayout(main_layout)

    def on_button_clicked(self):
        sender = self.sender()
        sender.setText("Cliqué !")

    def make_hover_event(self, btn):
        def on_hover(event):
            btn.setStyleSheet("background-color: lightblue")
        return on_hover

    def on_text_changed(self, text):
        self.label.setText(f"Bonjour, {text} !")

    def show_message(self):
        QMessageBox.information(self, "Info", "Vous avez cliqué sur OK")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
