import random

# Define the distance matrix representing distances between cities
# Example: distances[i][j] is the distance from city i to city j
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Parameters
num_ants = 5
alpha = 1  # Controls the importance of pheromone in decision making
beta = 2   # Controls the importance of distance in decision making
evaporation_rate = 0.5
pheromone_init = 1

# Initialize pheromone matrix
num_cities = len(distances)
pheromone = [[pheromone_init for _ in range(num_cities)] for _ in range(num_cities)]

# Define a function to calculate tour length
def tour_length(tour):
    total_distance = 0
    for i in range(len(tour)):
        total_distance += distances[tour[i]][tour[(i + 1) % num_cities]]
    return total_distance

# Define a function to update pheromone levels
def update_pheromone():
    global pheromone
    pheromone = [[(1 - evaporation_rate) * pheromone[i][j] for j in range(num_cities)] for i in range(num_cities)]
    for ant, tour in enumerate(tours):
        tour_distance = tour_length(tour)
        for i in range(num_cities):
            pheromone[tour[i]][tour[(i + 1) % num_cities]] += 1 / tour_distance

# Main loop
num_iterations = 100
for iteration in range(num_iterations):
    tours = [[] for _ in range(num_ants)]
    for ant in range(num_ants):
        current_city = random.randint(0, num_cities - 1)
        unvisited_cities = set(range(num_cities))
        unvisited_cities.remove(current_city)
        tours[ant].append(current_city)
        while unvisited_cities:
            probabilities = [((pheromone[current_city][next_city] ** alpha) *
                              ((1 / distances[current_city][next_city]) ** beta))
                             for next_city in unvisited_cities]
            total_prob = sum(probabilities)
            probabilities = [prob / total_prob for prob in probabilities]
            next_city = random.choices(list(unvisited_cities), probabilities)[0]
            unvisited_cities.remove(next_city)
            tours[ant].append(next_city)
            current_city = next_city
    update_pheromone()

# Find the best tour
best_tour = min(tours, key=tour_length)
best_distance = tour_length(best_tour)

# Print the best tour and its length
print(f"Best tour: {best_tour}")
print(f"Length of the best tour: {best_distance}")
