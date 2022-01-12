
class Person():

    def __init__(self,nom,age): 
        self._age = age
        self._nom = nom

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,value):
        self._age = value

    @property
    def nom(self):
        return self._nom
    @nom.setter
    def nom(self,value):
        self._nom = value


    def display_pres(self):
        return f"bonjour je m'appel {self._nom} j'ai {self._age} ans"

