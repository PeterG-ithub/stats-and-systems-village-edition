from src.entities.prey import Prey
from src.entities.predator import Predator


class Ecosystem:
    def __init__(self) -> None:
        self.rabbits = []
        self.hawks = []
        self.create_rabbits()
        self.create_hawks()

    def create_rabbits(self, num=10) -> None:
        for i in range(num):
            rabbit = Prey(i, "Rabbit")
            self.rabbits.append(rabbit)

    def create_hawks(self, num=5) -> None:
        for i in range(num):
            hawk = Predator(i, "Hawk")
            self.hawks.append(hawk)

    def roll(self) -> None:
        for rabbit in self.rabbits:
            rabbit.roll()
            print(rabbit)
        for hawk in self.hawks:
            hawk.roll()
            print(hawk)
