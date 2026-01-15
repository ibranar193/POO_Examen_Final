# Declaration de class.
class Outils :
    def __init__(self) :
        self.entiers = []

# Les fonctions.
    def saisir (self) :
        print("Veuiller saisir 10 nombre entiers : ")
        for i in range(10) :
            while True :
                try :
                    entier = int (input(f"Nombre {i+1} : "))
                    self.entiers.append(entier)
                    break
                except ValueError : print("Erreur : Veuiller saisir un entier valide.")

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
        somme = 0
        for i in self.entiers:
            somme += i
        return somme

    def moyenne(self) :
        return self.somme()/10

# fonction d'affichage.
    def __str__(self):
        return f"{self.entiers}"