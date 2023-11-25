import random
import numpy as np

# Define the cities and their coordinates
cities = {
    "A": (0, 0),
    "B": (1, 3),
    "C": (2, 2),
    "D": (3, 1),
    "E": (4, 4)
}

# Parameters
population_size = 100
generations = 100
mutation_rate = 0.02

# Function to calculate the distance between two cities
def distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return np.sqrt((x1 - x2)*2 + (y1 - y2)*2)

# Initialize the population with random routes
def initialize_population(cities, population_size):
    population = []
    city_list = list(cities.keys())
    for _ in range(population_size):
        route = city_list[:]
        random.shuffle(route)
        population.append(route)
    return population

# Calculate the total distance of a route
def route_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance(cities[route[i]], cities[route[i + 1]])
    return total_distance + distance(cities[route[-1]], cities[route[0]])

# Select parents for crossover using tournament selection
def tournament_selection(population, k=5):
    tournament = random.sample(population, k)
    return min(tournament, key=route_distance)

# Perform crossover to create a new route
def crossover(parent1, parent2):
    start = random.randint(0, len(parent1) - 1)
    end = random.randint(start, len(parent1))
    child = [None] * len(parent1)

    for i in range(start, end):
        child[i] = parent1[i]

    j = 0
    for i in range(len(parent1)):
        if child[i] is None:
            while parent2[j] in child:
                j += 1
            child[i] = parent2[j]

    return child

# Apply mutation to a route
def mutate(route, mutation_rate):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(route)), 2)
        route[idx1], route[idx2] = route[idx2], route[idx1]

# Genetic algorithm
def genetic_algorithm(cities, population_size, generations, mutation_rate):
    population = initialize_population(cities, population_size)
    for _ in range(generations):
        new_population = []

        while len(new_population) < population_size:
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate)
            new_population.append(child)

        population = new_population

    best_route = min(population, key=route_distance)
    return best_route, route_distance(best_route)

# Run the genetic algorithm
best_route, best_distance = genetic_algorithm(cities, population_size, generations, mutation_rate)
print("Best Route:", best_route)
print("Best Distance:", best_distance)
