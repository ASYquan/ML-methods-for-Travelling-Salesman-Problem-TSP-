"""
Utility functions for loading data and calculating TSP tour length.
"""

import csv
import numpy as np

def load_city_data(path):
    with open(path) as f:
        data = list(csv.reader(f, delimiter=';'))
    return data[0], np.array(data[1:], dtype=float)

def route_distance(route, cities, dist_matrix):
    """Compute total length of a TSP tour."""
    total = 0
    for i in range(len(route)):
        idx1 = cities.index(route[i])
        idx2 = cities.index(route[(i+1) % len(route)])
        total += dist_matrix[idx1, idx2]
    return total
