from src.event_simulator import Dice
import random


class Animal:
    def __init__(self, id, species="") -> None:
        self.id = id
        self.species = species
        self.age = 0  # Age in days
        self.weight = 0  # Grams
        self.state = "Idle"
        self.mortality_rate = 0
        self.is_female = random.choice([True, False])
        self.is_pregnant = False
        self.gestation_timer = 0
        self.is_alive = True
        self.children = []
        self.new_children = []

        self.calorie = 4000  # kCalories / energy the animal has or has eaten
        self.hungry_threshold = 2000
        self.satiety_threshold = 5000
        self.chance_of_eating = 0.5

        self.fatigue_threshold = 30
        self.energy = 100
        self.chance_of_sleeping = 0.1

    def check_sleeping(self):
        self.update_chance_of_sleeping()
        if self.roll() < self.chance_of_sleeping:
            self.state = "Sleeping"
            self.sleep()

    def update_chance_of_sleeping(self):
        if self.energy <= self.fatigue_threshold:
            self.chance_of_sleeping = 0.8
        else:
            proportion = self.energy / 100
            self.chance_of_sleeping = 0.8 - (proportion * 0.7)

    def update_chance_of_eating(self):
        if self.calorie <= self.hungry_threshold:
            self.chance_of_eating = 0.9
        elif self.calorie >= self.satiety_threshold:
            self.chance_of_eating = 0.2
        else:
            proportion = (self.calorie - self.hungry_threshold) / (self.satiety_threshold - self.hungry_threshold)
            self.chance_of_eating = 0.9 - (proportion * (0.9 - 0.2))

    def check_hunger(self):
        self.update_chance_of_eating()
        if self.roll() < self.chance_of_eating:
            self.state = "Eating"

    def grow(self):
        # Grow base on weight %
        pass

    def check_state(self):
        if self.state == "Idle":
            pass
        elif self.state == "Hunting":
            self.hunt()  # Call the hunt method
        elif self.state == "Eating":
            self.eat()  # Call the eat method
        elif self.state == "Resting":
            self.rest()  # Call the rest method
        elif self.state == "Sleeping":
            self.sleep()  # Call the sleep method
        elif self.state == "Exploring":
            self.explore()  # Call the explore method
        elif self.state == "Escaping":
            self.escape()  # Call the escape method
        elif self.state == "Guarding":
            self.guard()  # Call the guard method
        else:
            print(f"Unknown state: {self.state}")

    def hunt(self):
        # Behavior for hunting state
        pass

    def eat(self, food_calories):
        print(f"{self} is now eating")
        self.calorie += food_calories

    def rest(self):
        # Behavior for resting state
        pass

    def sleep(self):
        print(f"{self} is now sleeping")
        self.energy += 30

    def explore(self):
        # Behavior for exploring state
        pass

    def escape(self):
        # Behavior for escaping state
        pass

    def guard(self):
        # Behavior for guarding state
        pass

    def __str__(self) -> str:
        return f"{self.species}#{self.id}"

    def roll(self):
        dice = Dice(100)
        return dice.roll() / 100

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
