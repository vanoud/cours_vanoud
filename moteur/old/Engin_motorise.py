class Engin_motorise:
    def __init__(self, marque):
        self._marque = marque

    def set_marque(self, marque):
        self._marque = marque

    def get_marque(self):
        return self._marque

    def presenter(self):
        return f"La marque est {self.get_marque()}"

