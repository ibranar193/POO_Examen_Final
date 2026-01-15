# Importer la bibliotheque
from PyQt6.QtWidgets import QApplication, QWidget


app = QApplication([])
fen = QWidget()
fen.setWindowTitle("Doubleure")
fen.setGeometry(100, 100, 400, 200)

fen.show()
app.exec()