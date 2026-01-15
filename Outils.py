import numpy as np
class Outils :
    def __init__(self) :
        self.entiers = []
        self.array = np.array(self.entiers)
    def saisir (self) :
        print("Veuiller saisir 10 nombre entiers : ")
        for i in range(10) :
            entier = int (input(f"Nombre {i+1} : "))
            self.entiers.append(entier)

    def min(self) :
        return self.array.min()

    def max(self) :
        return self.array.max()

    def somme(self) :
        return self.array.sum()

    def moyenne(self) :
        return self.array.mean()