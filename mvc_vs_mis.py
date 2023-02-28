from graph import MIS, MVC, create_random_graph

# create random graphs with n nodes and sum the size of MIS and MVC and print them
def compare(n):
    G = create_random_graph(n, n*(n-1)//2)
    if len(MVC(G)) + len(MIS(G)) == n:
        print(True)
    else:
        print(False)

for i in range(2, 20):
    print("n = " + str(i))
    compare(i)