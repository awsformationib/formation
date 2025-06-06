from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

app = QApplication([])

loader = QUiLoader()

admin=True
if admin:
    f = QFile("aeroportadmin.ui")
else:
    f = QFile("aeroportlambda.ui")

f.open(QFile.ReadOnly)
fenetre = loader.load(f)
fenetre.show()
app.exec()