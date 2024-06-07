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
        self.new_children = []

    def __str__(self) -> str:
        return f"{self.species}#{self.id}"

    def roll(self):
        dice = Dice(100)
        return dice.roll() / 100

    def eat(self, food):
        pass

    def can_reproduce(self):
        if self.is_female and not self.is_pregnant and self.age > 90:
            self.reproduce()
            return True
        return False

    def reproduce(self):
        self.is_pregnant = True
        self.gestation_timer = random.randint(28, 31)
        print(f"Rabbit#{self.id} is now pregnant")

    def can_give_birth(self, cls):
        if self.is_pregnant and self.gestation_timer == 0:
            self.give_birth(cls)
            return True
        return False

    def give_birth(self, cls):
        self.new_children = []
        children = random.randint(4, 12)
        for child in range(children):
            child = cls(f"{self.id}-{child}", self.species)  # Got to figure out what to do with the id
            self.children.append(child)
            self.new_children.append(child)
            print(f"Rabbit#{self.id} gave birth to Rabbit#{child.id}")
        self.is_pregnant = False

    def update_mortality(self):
        # Mortality based on a rabbit age cycle
        if self.age < 30:  # 1 month
            self.mortality_rate = 1 - (1 - 0.9)**(1 / 30)  # (1 - D)^30 = 1 - M where D is daily mortality rate and M is monthly mortality rate 
        elif self.age < 90:  # 3 months
            self.mortality_rate = 1 - (1 - 0.5)**(1 / 60)
        else:
            self.mortality_rate = 1 - (1 - 0.1)**(1 / 90)
 
    def die(self):
        print(f"{self.species}#{self.id} is dead")
        self.is_alive = False

    def is_dead_today(self) -> bool:
        if self.roll() < self.mortality_rate:
            self.die()
            return True
        return False
