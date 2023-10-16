# -*- coding: utf-8 -*-
"""BF.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SKTIWu0OQ4wI_Wt0hBUFCxJbsCi-o6LY
"""

def BF(distance_matrix):

    # Generate all permutations of cities
    def generate_all_permutations(num_cities):
        # Initialize the list to store all permutations
        all_permutations = []

        # Helper function for recursive permutation generation
        def permute(current_path):
            # Base case: If the current path is of length num_cities, add it to the list of permutations
            if len(current_path) == num_cities:
                all_permutations.append(current_path.copy())
                return
            # Recursive case: Try adding each city to the current path
            for city in range(num_cities):
                if city not in current_path:
                    current_path.append(city)
                    permute(current_path)
                    current_path.pop()

        # Start the recursive permutation generation with an empty path
        permute([])
        # Return the list of all permutations
        return all_permutations


    # Calculate total distance for a given path
    def calculate_total_distance(path, distance_matrix):
        total_distance = 0
        for i in range(len(path) - 1):
            total_distance += distance_matrix[path[i]][path[i + 1]]
        # Return to the starting city
        total_distance += distance_matrix[path[-1]][path[0]]
        return total_distance

    # Amount of cities
    num_cities = len(distance_matrix)
    # Generate all possible paths
    all_paths = generate_all_permutations(num_cities)

    # Calculate total distance for all paths
    min_distance = float('inf')
    min_distance_path = None

    for path in all_paths:
        total_distance = calculate_total_distance(path, distance_matrix)
        if total_distance < min_distance:
            min_distance = total_distance
            min_distance_path = path

    # Adjust min_distance_path to begin from 0 and end at 0
    index_0 = min_distance_path.index(0)
    min_distance_path_part1 = list(min_distance_path[i] for i in range(index_0, num_cities))
    min_distance_path_part2 = list(min_distance_path[j] for j in range(0, index_0))
    min_distance_path = min_distance_path_part1 + min_distance_path_part2
    min_distance_path.append(min_distance_path[0])

    return min_distance_path, min_distance