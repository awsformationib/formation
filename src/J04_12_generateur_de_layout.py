from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout, QComboBox,
    QStackedLayout, QTextEdit
)
from PySide6.QtCore import Qt
import sys


class LayoutGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Générateur de Layouts PySide6")
        self.resize(500, 300)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)

        self.combo = QComboBox()
        self.combo.addItems(["QVBoxLayout", "QHBoxLayout", "QGridLayout", "QFormLayout", "QStackedLayout"])
        self.combo.currentTextChanged.connect(self.generate_layout)

        self.preview_area = QWidget()
        self.preview_layout = QVBoxLayout()
        self.preview_area.setLayout(self.preview_layout)

        main_layout.addWidget(QLabel("Choisissez un type de layout :"))
        main_layout.addWidget(self.combo)
        main_layout.addWidget(self.preview_area)

        self.generate_layout(self.combo.currentText())

    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            widget = child.widget()
            if widget:
                widget.deleteLater()

    def generate_layout(self, layout_name):
        self.clear_layout(self.preview_layout)

        container = QWidget()

        if layout_name == "QVBoxLayout":
            layout = QVBoxLayout()
            layout.addWidget(QLabel("Nom:"))
            layout.addWidget(QLineEdit())
            layout.addWidget(QPushButton("Valider"))
        elif layout_name == "QHBoxLayout":
            layout = QHBoxLayout()
            layout.addWidget(QPushButton("Annuler"))
            layout.addWidget(QPushButton("OK"))
        elif layout_name == "QGridLayout":
            layout = QGridLayout()
            layout.addWidget(QLabel("Nom:"), 0, 0)
            layout.addWidget(QLineEdit(), 0, 1)
            layout.addWidget(QLabel("Âge:"), 1, 0)
            layout.addWidget(QLineEdit(), 1, 1)
        elif layout_name == "QFormLayout":
            layout = QFormLayout()
            layout.addRow("Email:", QLineEdit())
            layout.addRow("Mot de passe:", QLineEdit())
        elif layout_name == "QStackedLayout":
            layout = QStackedLayout()
            layout.addWidget(QLabel("Page 1"))
            layout.addWidget(QLabel("Page 2"))
            layout.setCurrentIndex(0)

        container.setLayout(layout)
        self.preview_layout.addWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LayoutGenerator()
    window.show()
    sys.exit(app.exec())
