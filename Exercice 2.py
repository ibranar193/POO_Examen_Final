# Importer la bibliotheque
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton

# Fonctions
def calculateur () :
    try :
        n = int(lineEditN.text())
        result = n * 2
        lineEditD.setText(str(result))
    except ValueError :
        lineEditD.setText("Nombre non valid")

def sauvegarder () :
    res = lineEditD.text()
    if res != "":
        fichier = open ("resultats.txt", "w")
        fichier.write(res)
        fichier.close()

def charger () :
    try :
        fichier = open ("resultats.txt", "r")
        contenu = fichier.read()
        fichier.close()
        lineEditD.setText(contenu)
        nombre = int(int(contenu)/2)
        lineEditN.setText(str(nombre))
    except FileExistsError :
        lineEditN.setText("Erreur : Fichier introuvable")
        lineEditD.setText("Erreur : Fichier introuvable")
    except ValueError :
        lineEditN.setText("Erreur : Contenu introuvable")
        lineEditD.setText("Erreur : Contenu introuvable")

# Interface Graphique
app = QApplication([])
fen = QWidget()
fen.setWindowTitle("Doubleure")
fen.setGeometry(100, 100, 375, 200)

text1 = QLabel("Entrer la valeur de N :", fen)
text1.setGeometry(25, 25, 150, 20)

lineEditN = QLineEdit(fen)
lineEditN.setGeometry(150, 25, 200, 20)

text2 = QLabel("Voici le double :", fen)
text2.setGeometry(25, 50, 150, 20)

lineEditD = QLineEdit(fen)
lineEditD.setGeometry(150, 50, 200, 20)

btnD = QPushButton("Valider l'operation",fen)
btnD.setGeometry(150, 75, 200, 40)
btnD.clicked.connect(calculateur)

btnS = QPushButton("sauvegarder",fen)
btnS.setGeometry(25, 125, 160, 40)
btnS.clicked.connect(sauvegarder)

btnC = QPushButton("charger",fen)
btnC.setGeometry(190, 125, 160, 40)
btnC.clicked.connect(charger)

fen.show()
app.exec()