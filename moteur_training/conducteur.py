#dependance de Garage
from person import Person


class Conducteur(Person):

    def __init__(self, nom, age):
        super().__init__(nom, age)
    
    def conduire(self): # conduire(engin_motorise)
        pass

    def presenter_garage(self):
        pass
    #surcharge de methode pour appeler methode parent
    def display_pres(self):
        return f"je suis le conducteur {super().display_pres()}"