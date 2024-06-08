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


newborn_weight = random.randint(30, 40)  # 0 - 7
one_week_weight = random.randint(50, 100)  # 7 - 14 days
two_week_weight = random.randint(100, 150)  # 14 - 21 days
three_week_weight = random.randint(150, 200)  # 21-28 days
four_week_weight = random.randint(200, 300)  # 28+ days
adolescent_weight = random.randint(500, 1000)  # 8 weeks - 3 months old
adult_weight = random.randint(1000, 2500)  # 3+ months 
weight_through_age = [newborn_weight, one_week_weight, two_week_weight, three_week_weight, four_week_weight,'', '', '', adolescent_weight, '', '', '', adult_weight]

time_step = len(weight_through_age)

plt.figure(figsize=(10, 6))
plt.plot(range(time_step), weight_through_age, label='Rabbit weight by age')
plt.xlabel("week")
plt.ylabel("weight")
plt.title("Rabbit weight over time")
plt.legend()
plt.show()
