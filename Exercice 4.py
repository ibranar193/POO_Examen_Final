# Class Etudiant
class Etudiant:
    def __init__(self, nom):
        self.nom = nom
        self.notes = [15, 18, 12]
        self.identite = (nom, "2025-H")
        self.resultats = {"POO": 90, "Cisco": 85}

    def afficher_infos(self):
        print(f"Étudiant: {self.identite[0]} (Session: {self.identite[1]})")
        print(f"Liste des notes: {self.notes}")
        print(f"Score Python: {self.resultats['Python']}%")

# main
eleve = Etudiant("Mouad")
eleve.afficher_infos()

