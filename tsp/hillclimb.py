"""
Hill climbing solver for TSP.
"""

import numpy as np
from .utils import route_distance

def neighbors(route):
    """Generate neighbor tours by 2-opt swaps."""
    nbrs = []
    for _ in range(len(route)):
        a, b = sorted(np.random.choice(len(route), 2, replace=False))
        new = route.copy()
        new[a:b] = reversed(new[a:b])
        nbrs.append(new)
    return nbrs

def hill_climb(cities, dist_matrix, n, iters=10000):
    route = list(np.random.permutation(cities[:n]))
    best = route_distance(route, cities, dist_matrix)

    for _ in range(iters):
        for nb in neighbors(route):
            d = route_distance(nb, cities, dist_matrix)
            if d < best:
                route, best = nb, d
                break

    return route, best