"""
Genetic Algorithm (PMX crossover, inversion mutation, tournament selection).
"""

import numpy as np
import random
from .utils import route_distance

def pmx(p1, p2):
    n = len(p1)
    a, b = sorted(np.random.choice(n, 2, replace=False))
    c1, c2 = p1.copy(), p2.copy()

    c1[a:b], c2[a:b] = p2[a:b], p1[a:b]
    m1 = {p2[i]: p1[i] for i in range(a,b)}
    m2 = {p1[i]: p2[i] for i in range(a,b)}

    for c, m in ((c1, m1),(c2, m2)):
        for i in list(range(0,a))+list(range(b,n)):
            while c[i] in c[a:b]:
                c[i] = m[c[i]]
    return c1, c2

def mutate(route):
    i, j = sorted(np.random.choice(len(route), 2, replace=False))
    route[i:j] = reversed(route[i:j])

def select(pop, k=10):
    return min(random.sample(pop, k), key=lambda x: x[1])

def genetic_tsp(cities, dist_matrix, n, pop_size=100, generations=500):
    pop = []
    for _ in range(pop_size):
        r = list(np.random.permutation(cities[:n]))
        pop.append((r, route_distance(r, cities, dist_matrix)))

    for _ in range(generations):
        pop.sort(key=lambda x: x[1])
        elite = pop[:2]
        children = []

        while len(children) < pop_size - 2:
            p1 = select(pop)[0]
            p2 = select(pop)[0]
            c1, c2 = pmx(p1, p2)
            if np.random.rand() < 0.1: mutate(c1)
            if np.random.rand() < 0.1: mutate(c2)
            children += [(c1, route_distance(c1,cities,dist_matrix)),
                         (c2, route_distance(c2,cities,dist_matrix))]

        pop = elite + children

    return min(pop, key=lambda x:x[1])