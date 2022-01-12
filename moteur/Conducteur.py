from Personne import Personne
from Voiture import Voiture


class Conducteur(Personne):
    _voiture: Voiture = None

    def __init__(self, age, nom, voiture):
        super().__init__(age, nom)
        self._voiture = voiture

    @property
    def voiture(self) -> Voiture:
        return self._voiture

    @voiture.setter
    def voiture(self, value: Voiture) -> None:
        self._voiture = value

    def se_presenter(self) -> str:
        return f"{super().se_presenter()} et {self.voiture.decrire()}"

    def __str__(self):
        return self.se_presenter()
