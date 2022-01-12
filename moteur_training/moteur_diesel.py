from moteur_thermique import Moteur_thermique

class moteur_diesel(Moteur_thermique):
    
    def __init__(self,carburant):
        super().__init__()
        self._carburant = carburant

    def type_moteur(self):

        return f"je suis un moteur {self._carburant}"