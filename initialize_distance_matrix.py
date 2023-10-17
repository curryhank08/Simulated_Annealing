import math
import random

# Example Usage:
# Generate 10 random cities in 2D space
random.seed(10)  # For reproducibility
num_cities = 10
cities_2d = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(num_cities)]
print("Location of cities: ", cities_2d)

# distance of two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

distance_matrix = []
for city1 in cities_2d:
    distance_row = []
    for city2 in cities_2d:
        distance = euclidean_distance(city1, city2)
        distance_row.append(distance)
    distance_matrix.append(distance_row)
print("distance_martrix: ", distance_matrix)