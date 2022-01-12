

class Moteur():

    def __init__(self,essence) -> None:
        self._essence = essence

    def bruit(self):
        
        self._essence = self._essence - 1
        print(self._essence)
        return f"Vrrrouuuummmmmmmmm"
    