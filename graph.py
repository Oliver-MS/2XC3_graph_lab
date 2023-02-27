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

def create_random_graph(i, j):
    G = Graph(i)
    edges = []
    #j = num edges
    for _ in range(j):
        while True:
            node1 = random.randint(0, i)
            node2 = random.randint(0, i)
            #ensure no duplicates
            while node2 == node1:
                node2 = random.randint(0, i)
            if {node1, node2} in edges:
                pass
            else:
                G.add_edge(node1, node2)
                edges.append({node1, node2})
                break
    return G

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
    G_temp=G
    while not is_vertex_cover(G_temp, C):
        max_degree = 0
        max_node = None
        for node in G_temp.adj:
            if len(G_temp.adj[node]) > max_degree:
                max_degree = len(G_temp.adj[node])
                max_node = node
        C.append(max_node)
        G_temp.remove_node(max_node)

    return C

graph_test = create_random_graph(8, 5)
print(MVC(graph_test))
print(approx1(graph_test))


