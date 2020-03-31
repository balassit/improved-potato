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
# undirected graph using adjacency list
class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = []

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)

    def __str__(self):
        return "{}({})".format(self.__class__.__name__, self.name)

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self.name)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.vertices[v].add_neighbor(u)
            self.vertices[u].add_neighbor(v)
            return True
        return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors))

    def __str__(self):
        return "{}({})".format(self.__class__.__name__, dict(self.vertices))

    def dfs(self, start):
        visited, stack = set(), [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(set(self.vertices[vertex].neighbors) - visited)
                print(visited)
        return visited

    def bfs(self, start):
        visited, queue = set(), [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(set(self.vertices[vertex].neighbors) - visited)
                print(visited)
        return visited

    def bfs_paths(self, start, goal):
        queue = [(start, [start])]
        while queue:
            (vertex, path) = queue.pop(0)
            for next_node in set(self.vertices[vertex].neighbors) - set(path):
                if next_node == goal:
                    yield path + [next_node]
                else:
                    queue.append((next_node, path + [next_node]))

    def shortest_path(self, start, goal):
        try:
            return next(self.bfs_paths(start, goal))
        except StopIteration:
            return None

    def dfs_paths(self, start, goal, path=None):
        """
        All paths from start to goal possible
        """
        if path is None:
            path = [start]
        if start == goal:
            yield path
        for next_node in set(self.vertices[start].neighbors) - set(path):
            yield from self.dfs_paths(next_node, goal, path + [next_node])


# breadth-first search and depth-first search.

g = Graph()
for i in range(ord("A"), ord("G")):
    g.add_vertex(Vertex(chr(i)))

edges = ["AB", "AC", "BA", "BD", "BE", "CA", "CF", "DB", "EB", "EF", "FC", "FE"]
for edge in edges:
    g.add_edge(edge[:1], edge[1:])

# g.print_graph()
# print('bfs', g.bfs('C')) # {'B', 'C', 'A', 'F', 'D', 'E'}
print(list(g.bfs_paths("A", "F")))  # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
# print("shortest", g.shortest_path("A", "F"))  # ['A', 'C', 'F']
# print("dfs", g.dfs("C"))  # {'E', 'D', 'F', 'A', 'C', 'B'}
# print(list(g.dfs_paths('C', 'F'))) # [['C', 'F'], ['C', 'A', 'B', 'E', 'F']]
