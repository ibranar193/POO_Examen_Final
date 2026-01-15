# Importer la bibliotheque
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton


def calculator () :
    try :
        n = float(lineEditN.text())
        result = n * 2
        lineEditD.setText(str(result))
    except ValueError :
        lineEditD.setText("Nombre non valid")

app = QApplication([])
fen = QWidget()
fen.setWindowTitle("Doubleure")
fen.setGeometry(100, 100, 375, 150)

text1 = QLabel("Entrer la valeur de N :", fen)
text1.setGeometry(25, 25, 150, 20)

lineEditN = QLineEdit(fen)
lineEditN.setGeometry(150, 25, 200, 20)

text2 = QLabel("Voici le double :", fen)
text2.setGeometry(25, 50, 150, 20)

lineEditD = QLineEdit(fen)
lineEditD.setGeometry(150, 50, 200, 20)

btn = QPushButton("Valider l'operation",fen)
btn.setGeometry(150, 75, 200, 40)
btn.clicked.connect(calculator)


fen.show()
app.exec()