from Conducteur import Conducteur
from Voiture import Voiture
from moteur import Moteur

moteur = Moteur(150, "électricité")
voiture = Voiture("rouge", "tesla", moteur)
thomas = Conducteur(25, "thomas", voiture)

print(thomas)
