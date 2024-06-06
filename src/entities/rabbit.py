from src.event_simulator import Dice


class Rabbit:
    def __init__(self, id) -> None:
        self.id = id

    def __str__(self) -> str:
        return f"id: {self.id} roll: {self.roll()}"

    def roll(self):
        dice = Dice()
        return dice.roll()