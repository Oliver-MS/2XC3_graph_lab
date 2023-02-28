import matplotlib.pyplot as plt

from graph import create_random_graph, has_cycle

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
plt.ylabel("chance to contain a cycle (%)")
plt.title("Number of Edges vs. Cycle Probability")
plt.show()