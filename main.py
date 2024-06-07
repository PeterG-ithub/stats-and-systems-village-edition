from src.simulation.ecosystem import Ecosystem

# Simulate population data
ecosystem = Ecosystem()
ecosystem.create_preys(100, "Rabbit")
ecosystem.create_predators(10, "Hawk")
time_steps = 365

prey_population = []
predator_population = []

ecosystem.roll()
print(len(ecosystem.dead))