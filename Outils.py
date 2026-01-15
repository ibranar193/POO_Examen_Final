class Outils :
    def __init__(self) :
        self.entiers = []

    def saisir (self) :
        print("Veuiller saisir 10 nombre entiers :")
        for i in range(10) :
            entier = int (input(f"Nombre {i+1} : "))
            self.entiers.append(entier)

