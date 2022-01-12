from moteur import Moteur


class Voiture:
    _moteur: Moteur = None
    _couleur: str = ""
    _marque: str = ""

    # #composition
    # def __init__(self, couleur, marque):
    #     """
    #     ceci est un exemple de composition car le moteur est instancié dans le constructeur de voiture
    #     il s'agit d'un couplage extrêmement fort entre le moteur et la voiture: si la voiture est détruite, le moteur l'est aussi
    #     """
    #     self._moteur = Moteur(150, "diesel")
    #     self._couleur = couleur
    #     self._marque = marque

    #agrégation
    def __init__(self, couleur, marque, moteur):
        """
        ceci est un exemple d'injection de dépendance par constructeur:
        le moteur est créé EN DEHORS de la classe voiture, et lui est passé par le constructeur.
        Si je détruis ma voiture, mon moteur existe toujours
        :param couleur:
        :param marque:
        :param moteur: le moteur passé par agrégation
        """
        self._moteur = moteur
        self._couleur = couleur
        self._marque = marque

    @property
    def couleur(self) -> str:
        return self._couleur

    @couleur.setter
    def couleur(self, value) -> None:
        self._couleur = value

    @property
    def marque(self) -> str:
        return self._marque

    @property
    def moteur(self) -> Moteur:
        return self._moteur

    def freiner(self) -> str:
        return "La voiture freine"

    def accelerer(self) -> str:
        return f"La voiture accelere et le moteur fait {self.moteur.augmenter_tour()}"

    def decrire(self) -> str:
        return f"La voiture est {self.couleur} et elle a {self.moteur.puissance} chevaux"
