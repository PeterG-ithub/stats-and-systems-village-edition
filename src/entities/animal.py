from src.event_simulator import Dice


class Animal:
    def __init__(self, id) -> None:
        self.id = id
        self.species = ""

    def __str__(self) -> str:
        return f"{self.species}#{self.id} rolled {self.roll()}"

    def roll(self):
        dice = Dice()
        return dice.roll()

    def eat(self, food):
        pass

    def reproduce(self, who):
        pass

    def die(self):
        pass
