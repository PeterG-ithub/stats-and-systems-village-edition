from src.event_simulator import Dice
import random


class Animal:
    def __init__(self, id, species="") -> None:
        self.id = id
        self.species = species
        self.age = 0  # Age in days
        self.mortality_rate = 0
        self.is_female = random.choice([True, False])
        self.is_pregnant = False
        self.gestation_timer = 0

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
