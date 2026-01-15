# Import le fichier Outils.py
from Outils import Outils

# main fonction
entier = Outils()
entier.saisir()
print("-------------------------------------------------------------")
print(entier)
print("-------------------------------------------------------------")
print(f"Minimum :{entier.min()}")
print(f"Maximum :{entier.max()}")
print(f"Somme :{entier.somme()}")
print(f"Moyenne :{entier.moyenne()}")
