
# 🧱 Fiche – Widgets PySide6 : Utilité, usage & signaux/slots

| Widget           | Utilité principale                               | Exemple d'utilisation                                  | Signaux utiles                                     |
| ---------------- | ------------------------------------------------ | ------------------------------------------------------ | -------------------------------------------------- |
| `QPushButton`    | Bouton déclencheur                               | `btn = QPushButton("Valider")`                         | `clicked`, `pressed`, `released`, `toggled`        |
| `QLabel`         | Affichage de texte ou image                      | `label = QLabel("Nom :")`                              | — (affichage uniquement)                           |
| `QLineEdit`      | Champ de texte sur une ligne                     | `champ = QLineEdit()`                                  | `textChanged`, `returnPressed`, `editingFinished`  |
| `QTextEdit`      | Zone de texte multilignes                        | `zone = QTextEdit()`                                   | `textChanged`                                      |
| `QCheckBox`      | Case à cocher                                    | `case = QCheckBox("Accepter")`                         | `toggled`, `stateChanged`                          |
| `QRadioButton`   | Choix exclusif parmi plusieurs                   | `radio = QRadioButton("Option 1")`                     | `toggled`                                          |
| `QComboBox`      | Liste déroulante                                 | `combo = QComboBox(); combo.addItems(["A", "B", "C"])` | `currentIndexChanged`, `activated`, `highlighted`  |
| `QSpinBox`       | Champ numérique (entier)                         | `spin = QSpinBox(); spin.setRange(0, 100)`             | `valueChanged`                                     |
| `QDoubleSpinBox` | Champ numérique (flottant)                       | `dspin = QDoubleSpinBox(); dspin.setDecimals(2)`       | `valueChanged`                                     |
| `QSlider`        | Curseur horizontal ou vertical                   | `slider = QSlider(Qt.Horizontal)`                      | `valueChanged`, `sliderMoved`, `sliderReleased`    |
| `QProgressBar`   | Affichage d’une progression                      | `bar = QProgressBar(); bar.setValue(50)`               | — (piloté manuellement)                            |
| `QListWidget`    | Liste simple avec éléments sélectionnables       | `liste = QListWidget(); liste.addItem("Élément 1")`    | `itemClicked`, `currentRowChanged`                 |
| `QTableWidget`   | Tableau interactif avec cellules modifiables     | `table = QTableWidget(3, 2)`                           | `cellClicked`, `itemChanged`, `currentCellChanged` |
| `QDateEdit`      | Sélecteur de date                                | `date = QDateEdit(); date.setCalendarPopup(True)`      | `dateChanged`                                      |
| `QTimeEdit`      | Sélecteur d’heure                                | `time = QTimeEdit()`                                   | `timeChanged`                                      |
| `QDateTimeEdit`  | Sélecteur de date+heure                          | `dt = QDateTimeEdit()`                                 | `dateTimeChanged`                                  |
| `QTabWidget`     | Panneaux avec onglets                            | `tabs = QTabWidget(); tabs.addTab(widget, "Titre")`    | `currentChanged`                                   |
| `QStackedWidget` | Conteneur d’affichage d’une seule page à la fois | `stack = QStackedWidget(); stack.setCurrentIndex(0)`   | — (piloté par index)                               |
| `QGroupBox`      | Regrouper visuellement des widgets               | `gbox = QGroupBox("Paramètres"); gbox.setLayout(...)`  | —                                                  |
| `QFrame`         | Cadre visuel (ligne, panneau...)                 | `frame = QFrame(); frame.setFrameShape(QFrame.Box)`    | —                                                  |
| `QFileDialog`    | Dialogue de sélection de fichiers                | `filename, _ = QFileDialog.getOpenFileName()`          | — (utilisation via méthode statique)               |
| `QMessageBox`    | Affichage de message, confirmation, erreur       | `QMessageBox.information(self, "Titre", "Message")`    | —                                                  |

---

## 🧩 Exemple : connexion de signaux/slots

```python
from PySide6.QtWidgets import QPushButton, QLineEdit

champ = QLineEdit()
btn = QPushButton("Valider")

# Connecter un slot natif
btn.clicked.connect(lambda: print("Clic détecté"))

# Connecter une fonction personnalisée
def afficher():
    print("Texte : ", champ.text())

champ.returnPressed.connect(afficher)
```

---

## 🧰 Slots fréquemment utilisés (à connecter)

| Slot cible             | Effet déclenché                                                 | Exemple                                                          |
| ---------------------- | --------------------------------------------------------------- | ---------------------------------------------------------------- |
| `setText(str)`         | Change le texte d’un `QLabel`, `QLineEdit`, etc.                | `champ.textChanged.connect(label.setText)`                       |
| `setValue(int)`        | Met à jour un `QProgressBar`, `QSlider`, `QSpinBox`             | `slider.valueChanged.connect(bar.setValue)`                      |
| `setEnabled(bool)`     | Active ou désactive un widget                                   | `checkbox.toggled.connect(btn.setEnabled)`                       |
| `setVisible(bool)`     | Rend visible/invisible                                          | `case.toggled.connect(widget.setVisible)`                        |
| `clear()`              | Vide une zone de texte ou liste                                 | `btn.clicked.connect(liste.clear)`                               |
| `close()`              | Ferme une fenêtre ou un dialogue                                | `btn_annuler.clicked.connect(dialog.close)`                      |
| `setCurrentIndex(int)` | Change d’onglet ou de page dans `QComboBox`, `QTabWidget`, etc. | `btn.clicked.connect(lambda: tabs.setCurrentIndex(1))`           |
| `setChecked(bool)`     | Coche ou décoche une `QCheckBox`                                | `btn.clicked.connect(lambda: cb.setChecked(True))`               |
| `append(str)`          | Ajoute du texte à un `QTextEdit`                                | `btn.clicked.connect(lambda: textedit.append("Log..."))`         |
| `selectAll()`          | Sélectionne tout le texte d’un champ                            | `champ.focusInEvent = lambda e: champ.selectAll()`               |
| `setFocus()`           | Donne le focus clavier à un widget                              | `btn.clicked.connect(champ.setFocus)`                            |
| `setStyleSheet(str)`   | Change l’apparence (CSS Qt)                                     | `btn.clicked.connect(lambda: label.setStyleSheet("color:red"))`  |
| `scrollToItem(item)`   | Force un scroll dans une `QListWidget`                          | `list.itemClicked.connect(lambda item: list.scrollToItem(item))` |

---

## 🛠️ Customisation visuelle

```python
btn.setStyleSheet("background-color: #007ACC; color: white; font-weight: bold;")
```
