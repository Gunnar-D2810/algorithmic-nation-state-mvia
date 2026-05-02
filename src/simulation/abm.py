import networkx as nx
import numpy as np
import random

def run_abm(num_agents=50, steps=100):
    G = nx.random_geometric_graph(num_agents, 0.3)
    resources = {n: 10 for n in G.nodes()}

    for _ in range(steps):
        new_resources = {}

        for n in G.nodes():
            neighbors = list(G.neighbors(n))
            if neighbors:
                avg = np.mean([resources[k] for k in neighbors])
                new_resources[n] = avg
            else:
                new_resources[n] = resources[n] * 0.99

            if random.random() < 0.1:
                new_resources[n] += random.uniform(-2, 0)

            new_resources[n] = max(0, new_resources[n])

        resources = new_resources

    return resources