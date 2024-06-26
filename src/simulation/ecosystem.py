from src.entities.prey import Prey
from src.entities.predator import Predator


class Ecosystem:
    def __init__(self) -> None:
        self.preys = []
        self.predators = []
        self.dead = []
        self.prey_population = 0
        self.predator_population = 0

    def create_preys(self, num=1, name="Rabbit") -> None:
        for i in range(num):
            prey = Prey(i, name)
            prey.age = 91
            prey.update_mortality()
            print(prey.mortality_rate)
            self.preys.append(prey)
        self.update_population()

    def create_predators(self, num=1, name="Hawk") -> None:
        for i in range(num):
            predator = Predator(i, name)
            self.predators.append(predator)
        self.update_population()

    def roll(self):
        living_preys = []
        for prey in self.preys:
            if not prey.is_dead_today():
                living_preys.append(prey)
            else:
                self.dead.append(prey)
        self.preys = living_preys

    def update_population(self) -> None:
        self.prey_population = len(self.preys)
        self.predator_population = len(self.predators)

    def simulate_day(self):
        for prey in self.preys:
            if prey.is_pregnant:
                prey.gestation_timer -= 1
            prey.age += 1
            prey.update_mortality()
            prey.update_flee_rate()
            prey.update_detection_rate()
            prey.can_reproduce()
            if prey.can_give_birth(Prey):
                for child in prey.new_children:
                    self.preys.append(child)
        self.roll()
        self.update_population()
