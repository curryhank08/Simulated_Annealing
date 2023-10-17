#### Step1: Initialize a distance matrix by initialize_distance_matrix.py or give a existed distance matrix
#### Step2: Set parameters for Simulated Annealing function
SA(distance_matrix, initial_temperature, cooling_rate, max_iterations, stagnation_limit)
```{r}
distance_matrix : a nested list containg the distances between city1 and city2
initial_temperature : Cooling from this teperature
cooling_rate : used in each iteration within SA function to get its temperature(shown as below)
# temperature = initial_temperature / (1 + cooling_rate * iteration)
max_iterations : max number of the iteration finding a new path within SA function
stagnation_limit : max number of not accepting a new path (not shorter and not accepted under the probability from acceptance_probability(current_distance, new_distance, temperature))
```
#### Example:
```{r}
import time
start_time = time.time()

initial_temperature = 1000.0
cooling_rate = 1
max_iterations = 1000000  # Adjust as needed
stagnation_limit = num_cities * 20

min_distance_path, min_distance = SA(
    distance_matrix, initial_temperature, cooling_rate, max_iterations, stagnation_limit)

end_time = time.time()
running_time = end_time - start_time

print(f"Minimum Total Distancee: {min_distance}")
print(f"Corresponding Path: {min_distance_path}")
print(f"Running Time: {running_time:.6f} seconds")
-------------------------------------------------------------------------------------------------------------------
Minimum Total Distancee: 305.9292632050412
Corresponding Path: [0, 4, 8, 1, 3, 6, 7, 2, 5, 9, 0]
Running Time: 0.004587 seconds
```


