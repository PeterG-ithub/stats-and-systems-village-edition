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

    def set_adult_attributes(self):
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
    rabbit.set_adult_attributes()
    state_counter = {"Sleeping": 0, "Eating": 0, "Resting": 0}
    for i in range(24):
        rabbit.check_state()
        print(f"Hour {i}: {rabbit.state}")
        if rabbit.state in state_counter:
            state_counter[rabbit.state] += 1
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



#simulate_rabbit_sleeping()
# simulate_rabbit_eating()
simulate_rabbit_hourly()

# newborn_weight = random.randint(30, 40)  # 0 - 7
# one_week_weight = random.randint(50, 100)  # 7 - 14 days
# two_week_weight = random.randint(100, 150)  # 14 - 21 days
# three_week_weight = random.randint(150, 200)  # 21-28 days
# four_week_weight = random.randint(200, 300)  # 28+ days
# adolescent_weight = random.randint(500, 1000)  # 8 weeks - 3 months old
# adult_weight = random.randint(1000, 2500)  # 3+ months 
# weight_through_age = [newborn_weight, one_week_weight, two_week_weight, three_week_weight, four_week_weight,'', '', '', adolescent_weight, '', '', '', adult_weight]

# time_step = len(weight_through_age)

# plt.figure(figsize=(10, 6))
# plt.plot(range(time_step), weight_through_age, label='Rabbit weight by age')
# plt.xlabel("week")
# plt.ylabel("weight")
# plt.title("Rabbit weight over time")
# plt.legend()
# plt.show()
