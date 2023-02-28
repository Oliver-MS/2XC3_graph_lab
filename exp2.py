import matplotlib.pyplot as plt

from graph import create_random_graph, is_connected

experiments = 500
nodes = 100
edges = 200

chance_of_connection = []
edge = []

for j in range(99, edges):
    connected = 0
    for _ in range(experiments):
        G = create_random_graph(nodes, j)
        if is_connected(G):
            connected += 1
    chance_of_connection.append(connected/experiments * 100)
    edge.append(j)


plt.plot(edge, chance_of_connection, label = "Chance of Connection")
plt.xlabel("number of edges in graph")
plt.ylabel("chance to be connected (%)")
plt.title("Number of Edges vs. Connection Probability")
plt.show()