import matplotlib.pyplot as plt
from graph import Graph, create_random_graph, has_cycle

experiments = 500
max_nodes = 100
min_edges, max_edges = 3, max_nodes - 1

edges = []
cycle_perc = []

for i in range(min_edges, max_edges + 1):
    total_cycles = 0
    for _ in range(experiments):
        temp = create_random_graph(max_nodes, i)
        if has_cycle(temp):
            total_cycles += 1
    edges.append(i)
    cycle_perc.append((total_cycles / experiments) * 100) 
    
plt.plot(edges, cycle_perc)
plt.xlabel("number of edges in graph")
plt.ylabel("percent chance to contain a cycle")
plt.title(f"Finding the Chances for Randomly Generated Graphs\nWith {max_nodes} Nodes to Contain a Cycle")
plt.show()