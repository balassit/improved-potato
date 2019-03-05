"""
Adjacency Matrix:
 - E is edge and V is vertex
 - always space of |V|^2 
 - better for dense graphs (when V^2 is close to E)
 - simplier for weighted edges
 - uses more space
Adjacency List: 
 - faster and less space for sparse graphs
 - slower for dense graphs 
"""
# undirected graph using adjacency matrix
class Vertex:
    def __init__(self, n):
        self.name = n

    def __str__(self):
        return "{}({})".format(self.__class__.__name__, self.name)

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self.name)


class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []
        self.edge_indices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges) + 1))
            self.edge_indices[vertex.name] = len(self.edge_indices)
            return True
        return False

    def add_edge(self, u, v, weight=1):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
            return True
        return False

    def print_graph(self):
        print("   ", end="")
        for v in sorted(self.edge_indices.keys()):
            print(v, end=" ")
        print("")
        for v, i in sorted(self.edge_indices.items()):
            print(v + " ", end="|")
            for j in range(len(self.edges)):
                print(self.edges[i][j], end=" ")
            print(" ")

    def __str__(self):
        return "{}({})".format(self.__class__.__name__, dict(self.vertices))


g = Graph()
a = Vertex("A")
g.add_vertex(a)
g.add_vertex(Vertex("B"))

for i in range(ord("A"), ord("K")):
    g.add_vertex(Vertex(chr(i)))

edges = ["AB", "AE", "BF", "CG", "DE", "DH", "EH", "FG", "FI", "FJ", "GJ", "HI"]
for edge in edges:
    g.add_edge(edge[:1], edge[1:])

g.print_graph()
