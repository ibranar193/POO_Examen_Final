class Triangle :
    def __init__(self, n):
        self.n = n
    def les_lignes (self) :
        lignes = []
        for i in range(1,self.n+1) :
            espaces = " " * (self.n-i)
            etoiles = "*" * i
            lignes.append(espaces + etoiles)
        return lignes

class Affichage :
    def __init__(self, triangle):
        self.triangle = triangle

    def affichage (self) :
        lignes = self.triangle.les_lignes()
        print (f"\nAffichage pour n = {self.triangle.n} : \n")
        for i in lignes :
            print(f"{i} {i}")

try:
    entier = int(input("Veuiller saisir un nombre entiers :"))
    triangle = Triangle(entier)
    affichage = Affichage(triangle)
    affichage.affichage()
except ValueError:
    print("Erreur : Veuiller saisir un entier valide.")
