from garage import Garage

#dependance
class Engin_motorise():

    def __init__(self,marque):
        self._marque = marque
    
    def avancer(self):
        pass


    def freiner(self):
        pass

    def display(self):
        return f"je suis une {self._marque}"
