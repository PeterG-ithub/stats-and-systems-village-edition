from src.simulation.ecosystem import Ecosystem
import matplotlib.pyplot as plt
import random

# Simulate population data
ecosystem = Ecosystem()
ecosystem.create_preys(50, "Rabbit")
ecosystem.create_predators(10, "Hawk")
time_steps = 365

prey_population = []
predator_population = []


prey_population.append(ecosystem.prey_population)
predator_population.append(ecosystem.predator_population)


# This population is not actually connected to ecosystem populations
for t in range(1, time_steps):
    prey_population.append(prey_population[-1] + random.randint(-5, 10))
    predator_population.append(predator_population[-1] + random.randint(-3, 5))

# Plot the data
plt.figure(figsize=(10, 6))

plt.plot(range(time_steps), prey_population, label='Prey Population', color='blue')
plt.plot(range(time_steps), predator_population, label='Predator Population', color='red')

plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Prey and Predator Population over Time')
plt.legend()

plt.show()
