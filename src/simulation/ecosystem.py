from src.entities.prey import Prey
from src.entities.predator import Predator


class Ecosystem:
    def __init__(self) -> None:
        self.preys = []
        self.predators = []
        self.prey_population = 0
        self.predator_population = 0

    def create_preys(self, num=1, name="Rabbit") -> None:
        for i in range(num):
            prey = Prey(i, name)
            self.preys.append(prey)
        self.update_population()

    def create_predators(self, num=1, name="Hawk") -> None:
        for i in range(num):
            predator = Predator(i, name)
            self.predators.append(predator)
        self.update_population()

    def roll(self) -> None:
        for prey in self.preys:
            prey.roll()
            print(prey)
        for predator in self.predators:
            predator.roll()
            print(predator)

    def update_population(self) -> None:
        self.prey_population = len(self.preys)
        self.predator_population = len(self.predators)
