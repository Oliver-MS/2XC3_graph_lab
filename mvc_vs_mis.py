from graph import MIS, MVC, create_random_graph

# create random graphs with n nodes and sum the size of MIS and MVC and print them
def compare(n):
    G = create_random_graph(n, n-1)
    print("MIS size: " + str(len(MIS(G))))
    print("MVC size: " + str(len(MVC(G))))

for i in range(5, 20):
    print("test for " + str(i) + " nodes")
    compare(i)