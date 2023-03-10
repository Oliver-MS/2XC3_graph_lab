import itertools

from graph import MVC, Graph, approx1

experiments = 1
node_start = 5  
nodes = 20
edges = 10


mvcCovers=[]
a1Covers=[]
def generate_all_graphs(n):
    edges = []
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            edges.append([i,j])
    graphs = []
    for i in range(1,len(edges)+1):
        gEdges = [list(l) for l in itertools.combinations(edges,i)]
        for g in gEdges:
            print(g)
            gta = Graph(n)
            for edge in g:
                gta.add_edge(edge[0]-1,edge[1]-1)
            graphs.append(gta)
    return graphs

G = generate_all_graphs(5)
print(len(G))
i=0
for graph in G:
    mvcCovers.append(MVC(graph))
    a1Covers.append(approx1(graph))
countDiff=0
diffMag=[]
for i in range(0, len(mvcCovers)):
    if len(mvcCovers[i]) < len(a1Covers[i]):
        countDiff += 1
        diffMag.append(abs(len(a1Covers[i])-len(mvcCovers[i])))
print("Graph size: 5")
print("Total number of graphs: " + str(len(G)+1))
print("Max difference between MVC and approx1 vertex covers: " + str(max(diffMag)))
print("Number of differences between MVC and approx1 vertex covers: " + str(countDiff))