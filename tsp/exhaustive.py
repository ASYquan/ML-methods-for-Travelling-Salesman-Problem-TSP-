"""
Exhaustive brute-force TSP solver (baseline reference solution).
"""

from itertools import permutations
from .utils import route_distance

def exhaustive_tsp(cities, dist_matrix, n):
    best_route, best_dist = None, float("inf")
    for perm in permutations(cities[:n]):
        dist = route_distance(list(perm), cities, dist_matrix)
        if dist < best_dist:
            best_dist, best_route = dist, list(perm)
    return best_route, best_dist