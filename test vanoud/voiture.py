from moteur import Moteur

class Voiture(Moteur):

    def __init__(self,essence) -> None:
        super().__init__(essence)

    def accelerer(self):
        return f"on accélére {super().bruit()}"