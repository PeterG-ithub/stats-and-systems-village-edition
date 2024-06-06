from src.entities.animal import Animal


class Predator(Animal):
    def __init__(self, id, species) -> None:
        super().__init__(id, species)

    def seek_prey(self):
        # Do something here with chance of finding prey
        pass

    def hunt_prey(self):
        # When hunting, do something here that depends on
        # the chances of succesfully hunting
        pass