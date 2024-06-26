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
        self.attributes = {
            "Speed": 0,
            "Perception": 0,
            "Stealth": 0
        }
        self.experiences = {
            "Hunting": 0.0,
            "Hiding": 0.0,
            "Escaping": 0.0
        }
        self.chances = {
            "Eating": 0.0,
            "Sleeping": 0.0,
            "Resting": 0.0,
            "Exploring": 0.0,
            "Hunting": 0.0,
            "Escaping": 0.0,
            "Guarding": 0.0,
            "FindingFood": 0.0,
            "Hiding": 0.0
        }

        self.calorie = 4000  # kCalories / energy the animal has or has eaten
        self.hungry_threshold = 2000
        self.satiety_threshold = 5000

        self.fatigue_threshold = 30
        self.energy = 100

    def update_all_chances(self):
        self.update_chance_of_eating()
        self.update_chance_of_sleeping()
        self.update_chance_of_exploring()
        self.update_chance_of_escaping()
        self.update_chance_of_guarding()
        self.update_chance_of_hunting()
        self.update_chance_of_resting()

    def check_sleeping(self):
        self.update_chance_of_sleeping()
        if self.roll() < self.chance_of_sleeping:
            self.state = "Sleeping"
            self.sleep()

    def update_chance_of_eating(self):
        if self.calorie <= self.hungry_threshold:
            self.chances["Eating"] = 0.9
        elif self.calorie >= self.satiety_threshold:
            self.chances["Eating"] = 0.2
        else:
            proportion = (self.calorie - self.hungry_threshold) / (self.satiety_threshold - self.hungry_threshold)
            self.chances["Eating"] = 0.9 - (proportion * (0.9 - 0.2))

    def update_chance_of_sleeping(self):
        if self.energy > 100:
            self.energy = 100
        if self.energy <= self.fatigue_threshold:
            self.chances["Sleeping"] = 0.8
        else:
            proportion = self.energy / 100
            self.chances["Sleeping"] = 0.8 - (proportion * 0.7)
    
    def update_chance_of_resting(self):
        if self.energy <= self.fatigue_threshold:
            self.chances["Resting"] = 0.5
        else:
            proportion = self.energy / 100
            self.chances["Resting"] = 0.5 - (proportion * 0.4)

    def update_chance_of_exploring(self):
        pass

    def update_chance_of_hunting(self):
        pass

    def update_chance_of_escaping(self):
        pass

    def update_chance_of_guarding(self):
        pass

    def update_state(self):
        self.update_all_chances()
        total_chance = sum(self.chances.values())

        # Scale the roll to the total chance
        roll = self.roll() * total_chance
        cumulative_chance = 0.0

        for state, chance in self.chances.items():
            cumulative_chance += chance
            if roll < cumulative_chance:
                self.state = state
                break

    def check_state(self):
        self.update_state()
        if self.state == "Idle":
            pass
        elif self.state == "Hunting":
            self.hunt()  # Call the hunt method
        elif self.state == "Eating":
            self.eat(500)  # Call the eat method
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

    def hunt(self):
        # Behavior for hunting state
        pass

    def convert_calorie_to_energy(self, rate):
        calories_taken = 500 * rate
        convertion_rate = 30 / 1000
        self.energy += (calories_taken * convertion_rate)
        self.calorie -= calories_taken

    def eat(self, food_calories):
        print(f"{self} is now eating")
        self.calorie += food_calories

    def rest(self):
        print(f"{self} is now resting")
        self.convert_calorie_to_energy(.7)
        pass

    def sleep(self):
        print(f"{self} is now sleeping")
        self.convert_calorie_to_energy(1)

    def explore(self):
        # Behavior for exploring state
        pass

    def escape(self):
        # Behavior for escaping state
        pass

    def guard(self):
        # Behavior for guarding state
        pass

    def grow(self):
        # Grow base on weight %
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
