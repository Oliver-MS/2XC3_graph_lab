import matplotlib.pyplot as plt

from graph import MVC, approx1, approx2, approx3, create_random_graph

experiments = 10
node_start = 5  
nodes = 20
edges = 10

mvcAvg = 0
a1Avg = 0
a2Avg = 0
a3Avg = 0
sumsMVC = []
sumsA1 = []
sumsA2 = []
sumsA3 = []
numEdges = []

for j in range(node_start, nodes):
    for i in range(experiments):
        G = create_random_graph(j, edges)
        mvcAvg += (len(MVC(G)))
        a1Avg += (len(approx1(G)))
        a2Avg += (len(approx2(G)))
        a3Avg += (len(approx3(G)))

    numEdges.append(j)

    sumsMVC.append(mvcAvg/experiments)
    sumsA1.append(a1Avg/experiments)
    sumsA2.append(a2Avg/experiments)
    sumsA3.append(a3Avg/experiments)

plt.plot(numEdges, sumsMVC, label="MVC")
plt.plot(numEdges, sumsA1, label="approx1")
plt.plot(numEdges, sumsA2, label="approx2")
plt.plot(numEdges, sumsA3, label="approx3")
plt.title("Number of Nodes vs. Number of Nodes in Vertex Covers")
plt.ylabel("Number of Nodes in Vertex Covers")
plt.xlabel("Number of Nodes in Graph")
plt.legend()
plt.show()