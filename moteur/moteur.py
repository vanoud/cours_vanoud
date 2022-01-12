class Moteur:
    """
    Le moteur est destiné à être ajoute à une voiture. Il détermine la puissance et le carburant
    """
    _puissance: int = 0
    _carburant: str = ""

    def __init__(self, puissance: int, carburant: str):
        self._puissance = puissance
        self._carburant = carburant

    @property
    def puissance(self) -> int:
        return self._puissance

    @puissance.setter
    def puissance(self, value) -> None:
        self._puissance = value

    @property
    def carburant(self) -> str:
        return self._carburant

    @carburant.setter
    def carburant(self, value) -> None:
        self._carburant = value

    def augmenter_tour(self) -> str:
        return "VROUUUMMMM"

    def __str__(self) -> str:
        return f"Le moteur a une puissance de {self.puissance} et consomme ce carburant: {self.carburant}"

    def afficher_description(self):
        print(self)
