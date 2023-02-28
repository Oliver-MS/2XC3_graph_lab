from graph import MIS, MVC, create_random_graph

def compare(n):
    G = create_random_graph(n, n-1)
    print("length of MIS: " + str(len(MIS(G))))
    print("length of MVC: " + str(len(MVC(G))))

for i in range(2, 15):
    print("for n = " + str(i))
    compare(i)