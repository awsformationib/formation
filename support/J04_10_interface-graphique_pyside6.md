
# 🖼️ Fiche pratique – Comprendre et utiliser **PySide6**

## 📦 1. Qu’est-ce que PySide6 ?

PySide6 est le **binding officiel de Qt 6 pour Python**, proposé par Qt Group. Il permet de construire des **interfaces graphiques modernes, modulaires et multiplateformes** en Python.

* Alternative directe à PyQt6 (mais sous licence LGPL gratuite).
* Très utilisé pour créer des logiciels interactifs (scientifiques, techniques, métiers).
* Intègre tout le système de **widgets**, **layouts**, **signaux/slots** et **QML (facultatif)**.

---

## 🧱 2. Structure générale d’une application PySide6

```python
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

app = QApplication(sys.argv)                   # 1. Application Qt
window = QMainWindow()                         # 2. Fenêtre principale
button = QPushButton("Cliquez ici")            # 3. Widget
window.setCentralWidget(button)                # 4. Placement du widget
window.show()                                  # 5. Affichage
sys.exit(app.exec())                           # 6. Boucle événementielle
```

---

## 📐 3. Les composants de base

| Élément                                    | Description                                              |
| ------------------------------------------ | -------------------------------------------------------- |
| `QApplication`                             | Gère l’application (événements, arguments, etc.)         |
| `QWidget`                                  | Composant de base de toute interface                     |
| `QMainWindow`                              | Fenêtre principale avec barre de menus, status bar, etc. |
| `QDialog`                                  | Fenêtre secondaire modale (formulaire, message, etc.)    |
| `QLayout`                                  | Système de disposition (VBox, HBox, Grid, Form…)         |
| `QPushButton`, `QLabel`, `QLineEdit`, etc. | Widgets courants                                         |

---

## 📦 4. Organisation typique d’un projet PySide6

```
mon_projet/
├── main.py              # Point d’entrée
├── windows/
│   └── main_window.py   # Classe QMainWindow personnalisée
├── dialogs/
│   └── edit_dialog.py   # Boîtes de dialogue
├── widgets/
│   └── custom_table.py  # Composants spécialisés
├── models/
│   └── avion.py         # Données métier
```

---

## 🔁 5. Signaux & Slots : la mécanique des interactions

Qt fonctionne sur un modèle **signal → slot** (observateur).

```python
from PySide6.QtWidgets import QPushButton

btn = QPushButton("Valider")
btn.clicked.connect(ma_fonction)  # Quand cliqué, exécute ma_fonction
```

On peut connecter un signal à :

* une fonction lambda,
* une méthode,
* un slot Qt (`close`, `setText`, etc.).

---

## 🖼️ 6. Layouts : gérer l’agencement

```python
from PySide6.QtWidgets import QVBoxLayout, QWidget

widget = QWidget()
layout = QVBoxLayout(widget)
layout.addWidget(QPushButton("OK"))
layout.addWidget(QPushButton("Annuler"))
```

> Ne jamais positionner des éléments avec `.move()` ou `.resize()` dans une vraie appli : utilise toujours des `QLayout`.

---

## 📋 7. Dialogs : créer des formulaires

```python
from PySide6.QtWidgets import QDialog, QFormLayout, QLineEdit, QPushButton

class MonDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formulaire")
        layout = QFormLayout()
        self.nom_input = QLineEdit()
        layout.addRow("Nom :", self.nom_input)
        bouton = QPushButton("OK")
        bouton.clicked.connect(self.accept)
        layout.addWidget(bouton)
        self.setLayout(layout)
```

---

## 📚 8. Concepts importants à connaître

| Concept              | Utilité principale                                                    |
| -------------------- | --------------------------------------------------------------------- |
| **Layouts**          | Gestion automatique des positions/tailles                             |
| **Signaux/Slots**    | Communication entre composants                                        |
| **Custom Widgets**   | Personnaliser le comportement graphique                               |
| **Model/View**       | Gérer des listes, tableaux, données (ex. `QTableWidget`, `QListView`) |
| **Stylesheets**      | Personnaliser le rendu avec une syntaxe CSS Qt (`setStyleSheet`)      |
| **Timers / Threads** | Exécuter des actions différées ou en parallèle (`QTimer`, `QThread`)  |

---

## 🧪 9. Tester une app PySide6

* `pytest-qt` : permet de simuler des clics, entrées clavier, etc.
* `QTest` : module PyQt/PySide pour tests bas niveau

---

## 🛠️ 10. Pour aller plus loin

| Ressource               | Lien                                                                                                         |
| ----------------------- | ------------------------------------------------------------------------------------------------------------ |
| Doc officielle PySide6  | [https://doc.qt.io/qtforpython-6/index.html](https://doc.qt.io/qtforpython-6/index.html)                     |
| Exemples Qt pour Python | [https://github.com/qt/qtforpython/tree/main/examples](https://github.com/qt/qtforpython/tree/main/examples) |
| Tutoriels avancés       | [https://realpython.com/python-pyqt-gui/](https://realpython.com/python-pyqt-gui/)                           |

