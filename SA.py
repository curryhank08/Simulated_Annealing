# -*- coding: utf-8 -*-
import math
import random

def SA(distance_matrix, initial_temperature, cooling_rate, max_iterations, stagnation_limit):

    ### Necessary functions for SA function
    def total_distance(tour, distance_matrix):
        distance = 0
        num_cities = len(tour)
        # path = []
        for i in range(num_cities):
            if i != (num_cities -1):
              # path.append([tour[i], tour[i+1]])
              distance += distance_matrix[tour[i]][tour[i+1]]
            else:
              # path.append([tour[i], tour[0]])
              distance += distance_matrix[tour[i]][tour[0]]

        return distance

    def acceptance_probability(current_distance, new_distance, temperature):
        p = math.exp(-abs(current_distance - new_distance) / temperature)
        return min(1, p)

    def generate_initial_solution(num_cities):
        # return random.sample(range(num_cities), num_cities)
        return list(range(num_cities))
    ###

    num_cities = len(distance_matrix)
    current_tour = generate_initial_solution(num_cities)
    current_distance = total_distance(current_tour, distance_matrix)

    # Track consecutive iterations without improvement
    no_improvement_count = 0

    for iteration in range(max_iterations):
        temperature = initial_temperature / (1 + cooling_rate * iteration)
        current_distance = total_distance(current_tour, distance_matrix)

        new_tour = current_tour.copy()
        # randomly select 2 cities to exchange for creating a new tour path
        index1, index2 = random.sample(range(num_cities), 2)
        new_tour[index1], new_tour[index2] = new_tour[index2], new_tour[index1]
        new_distance = total_distance(new_tour, distance_matrix)

        # Case of finding a path with shorter distance
        if new_distance < current_distance:
            current_tour = new_tour
            current_distance = new_distance
            # Reset no_improvement_count if finding a path with shorter distance
            no_improvement_count = 0

        # Case of not finding a better path but accepting the new path under a probability
        else:
          acceptance_prob = acceptance_probability(current_distance, new_distance, temperature)
          if acceptance_prob > random.random():
              current_tour = new_tour
              current_distance = new_distance
              # Reset no_improvement_count if accepting a new path
              no_improvement_count = 0

          # Consider the number of iterations without improvement and quit the for loop to find a new path if exceed a limit
          else:
              no_improvement_count += 1  # Track consecutive iterations without improvement
              if no_improvement_count > stagnation_limit:
                break

    # Adjust min_distance_path to begin from 0 and end at 0
    min_distance = current_distance
    min_distance_path = current_tour
    index_0 = min_distance_path.index(0)
    min_distance_path_part1 = list(min_distance_path[i] for i in range(index_0, num_cities))
    min_distance_path_part2 = list(min_distance_path[j] for j in range(0, index_0))
    min_distance_path = min_distance_path_part1 + min_distance_path_part2
    min_distance_path.append(min_distance_path[0])

    return min_distance_path, min_distance