from src.entities.animal import Animal


class Hawk(Animal):
    def __init__(self, id, species="Hawk") -> None:
        super().__init__(id, species)

    def set_hawk_attributes(self):
        pass