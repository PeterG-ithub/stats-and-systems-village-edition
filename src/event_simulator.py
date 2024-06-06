import numpy as np


class Dice:
    def __init__(self, sides=100):
        self.sides = sides

    def roll(self):
        return np.random.randint(1, self.sides + 1)
