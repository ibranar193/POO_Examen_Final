# Importer la bibliotheque
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit

app = QApplication([])
fen = QWidget()
fen.setWindowTitle("Doubleure")
fen.setGeometry(100, 100, 400, 200)

text1 = QLabel("Entrer la valeur de N :", fen)
text1.setGeometry(25, 25, 150, 20)

lineEditN = QLineEdit(fen)
lineEditN.setGeometry(150, 25, 200, 20)

fen.show()
app.exec()