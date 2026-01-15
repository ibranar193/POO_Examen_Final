#
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
        self.array = np.array(self.entiers)

    def min(self) :
        minimum = self.entiers[0]
        for i in self.entiers :
            if i < minimum :
                minimum = i
        return minimum

    def max(self) :
        maximum = self.entiers[0]
        for i in self.entiers:
            if i >maximum:
                maximum = i
        return maximum

    def somme(self) :
        return self.array.sum()

    def moyenne(self) :
        return self.array.mean()

    def __str__(self):
        return f"{self.entiers}"