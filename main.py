import matplotlib.pyplot as plt
from tsp.utils import load_city_data
from tsp.exhaustive import exhaustive_tsp
from tsp.hillclimb import hill_climb
from tsp.genetic import genetic_tsp
import os

os.makedirs("plots", exist_ok=True)

cities, dist = load_city_data("data/european_cities.csv")

# --- Run algorithms ---
route6, dist6 = exhaustive_tsp(cities, dist, 6)
route10, dist10 = hill_climb(cities, dist, 10)
ga_route, ga_dist = genetic_tsp(cities, dist, 10)

# --- Plot distances ---
plt.bar(["Exhaustive(6)", "HillClimb(10)", "GA(10)"], [dist6, dist10, ga_dist])
plt.title("Algorithm Comparison (Lower is better)")
plt.ylabel("Distance (km)")
plt.savefig("plots/algorithm_comparison.png")
plt.close()

print("Run complete! — plots saved in /plots/")