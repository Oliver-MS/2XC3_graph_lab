from graph import MIS, MVC, create_random_graph


def compare(n):
    G = create_random_graph(n, n-1)
    print(f"for {n} vertices: length of MIS: {len(MIS(G))} + length of MVC: {len(MVC(G))} = {len(MIS(G)) + len(MVC(G))}")

for i in range(2, 15):
    compare(i)