class Personne:
    _age: int = 0
    _nom: str = ""

    def __init__(self, age, nom):
        self._age = age
        self._nom = nom

    @property
    def nom(self):
        return self._nom

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value) -> None:
        self._age = value

    def se_presenter(self):
        return f"Je m'appelle {self.nom} et j'ai {self.age} ans"
