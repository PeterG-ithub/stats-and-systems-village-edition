from src.entities.animal import Animal


class Prey(Animal):
    def __init__(self, id, species) -> None:
        super().__init__(id, species)

    def evade_predator(self):
        # Do something with chances of getting spotted
        pass

    def flee(self):
        # Do something here base on the chances of fleeing 
        # when getting hunted
        pass
