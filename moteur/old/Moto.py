from Engin_motorise import Engin_motorise


class Moto(Engin_motorise):
    def __init__(self, marque, carburant):
        super().__init__(marque)
        self._carburant = carburant

    def set_carburant(self, carburant):
        self._carburant = carburant

    def get_carburant(self):
        return self._carburant

    # redéfinition
    def presenter(self):
        return f"VROOOUUUUUUMMMMMMMMMM BAM PIMPON"
