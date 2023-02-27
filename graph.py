from collections import deque
import random

#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes(self):
        return len(self.adj)

    def remove_node(self, node):
        for node1 in self.adj[node]:
            self.adj[node1].remove(node)
        del self.adj[node]

    def copy(self):
        G = Graph(len(self.adj))
        for node1 in self.adj:
            for node2 in self.adj[node1]:
                G.add_edge(node1, node2)
        return G

    #function that removes all edges incident to node
    def remove_incident_edges(self, node):
        if self.adj[node] == []:
            return
        for node1 in self.adj[node]:
            self.adj[node1].remove(node)
        self.adj[node] = []

def create_random_graph(i, j):
    G = Graph(i)
    edges = []
    #j = num edges
    for _ in range(j):
        while True:
            node1 = random.randint(0, i - 1)
            node2 = random.randint(0, i - 1)
            #ensure no duplicates
            while node2 == node1:
                node2 = random.randint(0, i - 1)
            if {node1, node2} in edges:
                pass
            else:
                G.add_edge(node1, node2)
                edges.append({node1, node2})
                break
    return G


#function that selects random node from graph
def random_node(G):
    return random.choice(list(G.adj.keys()))
#Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    #initialize nodes to not marked
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False

#returns a path from node1 to node2
def BFS2(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    #track parent of each node searched
    parent = {node1 : None}
    #initialize nodes to not marked
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                #reconstruct path from parents
                path = [node]
                while current_node != node1:
                    path = [current_node] + path
                    current_node = parent[current_node]
                path = [node1] + path
                return path
            if not marked[node]:
                Q.append(node)
                marked[node] = True
                parent[node] = current_node
    return []

#return whole predecessor dictionary
def BFS3(G, node1):
    Q = deque([node1])
    marked = {node1 : True}
    #track parent of each node searched
    parent = {}
    #initialize nodes to not marked
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if not marked[node]:
                Q.append(node)
                marked[node] = True
                parent[node] = current_node
    return parent

#Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False

#returns a path from node1 to node2
def DFS2(G, node1, node2):
    S = [node1]
    marked = {}
    parent = {node1 : None}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        #print(f"queue: {S}\nparent: {parent}\nmarked: {marked}\n")
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if not marked[node]:
                    parent[node] = current_node
                if node == node2:
                    path = [node]
                    while node != node1:
                        node = parent[node]
                        path = [node] + path
                    return path
                S.append(node)
    return []

#return whole predecessor dictionary
def DFS3(G, node1):
    S = [node1]
    marked = {}
    parent = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if not marked[node]:
                    parent[node] = current_node
                S.append(node)
    return parent

#returns true if a cycle exists in graph G
def has_cycle(G):
    for node in G.adj:
        parent1 = BFS3(G, node)
        parent2 = DFS3(G, node)
        for i in parent1:
            if parent1[i] != parent2[i]:
                return True
    return False

#returns true if a connection exists in graph G
def is_connected(G):
    for node in G.adj:
        if DFS3(G, node):
            return True
    return False

#Use the methods below to determine minimum vertex covers

def add_to_each(sets, element):
    copy = sets.copy()
    for set in copy:
        set.append(element)
    return copy

def power_set(set):
    if set == []:
        return [[]]
    return power_set(set[1:]) + add_to_each(power_set(set[1:]), set[0])

def is_vertex_cover(G, C):
    for start in G.adj:
        for end in G.adj[start]:
            if not(start in C or end in C):
                return False
    return True

def MVC(G):
    nodes = [i for i in range(G.number_of_nodes())]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover

def approx1(G):
    C = []
    #create copy of G to remove nodes from
    G_temp = G.copy()
    while not is_vertex_cover(G_temp, C):
        max_degree = 0
        max_node = None
        for node in G_temp.adj:
            if len(G_temp.adj[node]) > max_degree:
                max_degree = len(G_temp.adj[node])
                max_node = node
        C.append(max_node)
        G_temp.remove_incident_edges(max_node)

    return C

def approx2(G):
    C = []
    while not is_vertex_cover(G, C):
        rand_vertex = random.choice(list(G.adj.keys()))
        while rand_vertex in C:
            rand_vertex = random.choice(list(G.adj.keys()))
        C.append(rand_vertex)
    return C


def approx3(G):
    C = []
    G_temp = G.copy()
    while not is_vertex_cover(G_temp, C):
        while True:
            u = random.choice(list(G_temp.adj.keys()))
            while len(G_temp.adj[u]) == 0:
                u = random.choice(list(G_temp.adj.keys()))
            v = random.choice(G_temp.adj[u])
            if not u in C and not v in C:
                break
        C.append(u)
        C.append(v)
        G_temp.remove_incident_edges(u)
        G_temp.remove_incident_edges(v)
    return C

    
graph_test = create_random_graph(8, 5)
print(MVC(graph_test))
print(approx1(graph_test))
print(approx2(graph_test))
print(approx3(graph_test))


