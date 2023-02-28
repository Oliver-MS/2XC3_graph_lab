import matplotlib.pyplot as plt

from graph import MVC, approx1, approx2, approx3, create_random_graph

experiments = 100
nodes = 8
edges = 30

sumsMVC = []
sumsA1 = []
sumsA2 = []
sumsA3 = []
numEdges = []

for j in range(1, edges, 5):

    for _ in range(experiments):
        G = create_random_graph(nodes, j)

        sumsMVC.append(len(MVC(G)))
        sumsA1.append(len(approx1(G)))
        sumsA2.append(len(approx2(G)))
        sumsA3.append(len(approx3(G)))

    numEdges.append(j)

finalMVC = sum(sumsMVC)
finalA1 = sum(sumsA1)
finalA2 = sum(sumsA2)
finalA3 = sum(sumsA3)
#create a bar graph
plt.bar(0, height=finalMVC, label = "MVC")
plt.bar(1, height=finalA1, label = "Approximation 1")
plt.bar(2, height=finalA2, label = "Approximation 2")
plt.bar(3, height=finalA3, label = "Approximation 3")

plt.ylabel = "MVC"
plt.xlabel = "Approximations"
plt.legend()
plt.show()