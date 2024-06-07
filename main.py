from src.simulation.ecosystem import Ecosystem
import matplotlib.pyplot as plt

# Simulate population data
ecosystem = Ecosystem()
ecosystem.create_preys(100, "Rabbit")
ecosystem.create_predators(10, "Hawk")
time_steps = 1000

prey_population = []
predator_population = []

for i in range(time_steps):
    print(f"Day #{i}")
    prey_population.append(ecosystem.prey_population)
    ecosystem.simulate_day()
    print(len(ecosystem.preys))
# ecosystem.preys[0].give_birth()

plt.figure(figsize=(10,6))
plt.plot(range(time_steps), prey_population, label='Total Rabbit Population', color='green')
plt.xlabel('Day of the Year')
plt.ylabel('Population')
plt.title('Rabbit population over time')
plt.legend()
plt.show()
