from src.entities.prey import Prey
import matplotlib.pyplot as plt
import random


class Rabbit(Prey):
    def __init__(self, id, species) -> None:
        super().__init__(id, species)
        newborn_weight = random.randint(30, 40)
        self.weight = newborn_weight
        self.maintenance_calorie = 2150  # 2100 - 2200 kCal/kg
        self.growth_calorie = 400  # 300 - 500  kCal/kg
        self.set_daily_food_intake()

    def set_daily_food_intake(self):
        self.daily_food_intake = self.weight * 0.03  # 2% - 4% of their body weight in food per day

    def set_adult_rabbit(self):
        self.age = 91  # Days
        self.weight = 1750  # Grams
        self.calorie = 4000


def simulate_rabbit_reproduction():
    rabbit = Rabbit(1, 'rabbit')
    rabbit.is_female = True
    rabbit.age = 91
    rabbit.can_reproduce()
    rabbit.gestation_timer = 0
    rabbit.can_give_birth(Rabbit)


def simulate_rabbit_hourly():
    rabbit = Rabbit(1, 'rabbit')
    rabbit.set_adult_rabbit()
    state_counter = {"Sleeping": 0, "Eating": 0, "Resting": 0}
    for i in range(24):
        rabbit.check_state()
        print(f"Hour {i}: {rabbit.state}")
        if rabbit.state in state_counter:
            state_counter[rabbit.state] += 1

        rabbit.energy -= 10
    plot_state_counter(state_counter)


def simulate_rabbit_eating():
    rabbit = Rabbit(1, 'rabbit')
    rabbit.check_hunger()
    print(rabbit.calorie)


def simulate_rabbit_sleeping():
    rabbit = Rabbit(1, 'rabbit')
    rabbit.energy = 10
    rabbit.check_sleeping()
    print(rabbit.energy)


def plot_state_counter(state_counter):
    activities = list(state_counter.keys())
    counts = list(state_counter.values())
    plt.figure(figsize=(8, 5))
    plt.bar(activities, counts, color=['blue', 'orange', 'green'])
    plt.xlabel("Activities")
    plt.ylabel("Count")
    plt.title("State Counts over 24 Hours")
    plt.show()



# simulate_rabbit_sleeping()
# simulate_rabbit_eating()
simulate_rabbit_hourly()
