from Laitue import Laitue
from Tomate import Tomate


class Salade_composee:

    def __init__(self, tomate, laitue):
        self.tomate = tomate
        self.laitue = laitue

    def afficher_date_peremption_tomate(self):
        print(f"La tomate contenue dans la salade sera périmée dans {self.tomate.date_peremption} jours")

    def afficher_couleur_tomate(self):
        print(f"La couleur de la tomate dans la salade composée est {self.tomate.couleur}")
