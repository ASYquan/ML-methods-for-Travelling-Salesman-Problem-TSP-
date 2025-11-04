# Traveling Salesman Problem (TSP) — Evolutionary Techniques

This project implements multiple strategies to solve the Traveling Salesman Problem (TSP) and compares their performance:

- Exhaustive Search (baseline)
- Hill Climbing
- Genetic Algorithm (PMX crossover, inversion mutation, tournament selection)

The project loads real inter-city distance data and visualizes example tours on a map.  
Plots are automatically generated for:

- Best paths found
- Algorithm performance curves
- Population size comparison (for GA)

## Unfortunately, due to copyright the data used the ML-algorithms cannot be published. However, it is data-agnostic. Meaning, it runs on all data sets as longs as there is .img to plot on, and a .csv-file to pull from:) 
---

## Project Goals

- Demonstrate search vs heuristic approaches
- Compare exact vs stochastic optimization
- Explore GA behavior and convergence trends
- Visualize tours on map of Europe

---

## Running

```bash
python main.py
