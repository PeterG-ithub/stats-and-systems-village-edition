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
        self.is_alive = True
        self.children = []

    def __str__(self) -> str:
        return f"{self.species}#{self.id}"

    def roll(self):
        dice = Dice(100)
        return dice.roll()

    def eat(self, food):
        pass

    def reproduce(self, who):
        pass

    def die(self):
        print(f"{self.species}#{self.id} is dead")
        self.is_alive = False

    def is_dead_today(self) -> bool:
        if self.roll() < self.mortality_rate:
            self.die()
            return True
        return False
