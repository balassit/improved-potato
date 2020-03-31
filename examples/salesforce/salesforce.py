import sys


class Vertex:
    def __init__(self, n):
        self.name = n

    def __str__(self):
        return "{}".format(self.name)

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self.name)


class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []
        self.edge_indices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph if it is not present
        :param vertex:
        :return:
        """
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges) + 1))
            self.edge_indices[vertex.name] = len(self.edge_indices)
            return True
        return False

    def add_edge(self, u, v, weight=1):
        """
        Adds an edge to the graph between the 2 components.
        If v has edges that u does not, add those to u to indicate the dependencies.
        If associate already exist, print message and do not update
        :param u: origin component
        :param v: component to associate to origin
        :param weight: value to indicate association (1)
        :return: True of association was made, False otherwise
        """
        if u in self.vertices and v in self.vertices:
            # get the associated links from v and add those to u as well
            # find the one that is already 1 that is from
            #  DNS -> TCPIP -> NETCARD

            for key, (a, b) in enumerate(
                zip(self.edges[self.edge_indices[u]], self.edges[self.edge_indices[v]])
            ):
                self.edges[self.edge_indices[u]][key] = a | b
            if self.edges[self.edge_indices[u]][self.edge_indices[v]] == 1:
                print(f"{u} depends on {v}, ignoring command")
                return False
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
            # print(f"{u}: {self.edges[self.edge_indices[u]]}")
            # print(f"{v}: {self.edges[self.edge_indices[v]]}")
            return True
        return False

    def get_neighbors(self, name):
        """
        Lookup the names of the components that are associated to the named component from the set of edges
        :param name: name of component to get associated components
        :return: associated components
        """
        component_names = set()
        index = 0
        for key in self.edge_indices.keys():
            if self.edges[self.edge_indices[name]][index]:
                component_names.add(key)
            index += 1

        return component_names

    def remove_edges(self, name):
        """
        If any components on graph have a dependency on the vertex, it cannot be deleted so return False
        Otherwise, delete the component.
        :param name:
        :return:
        """
        print(g.vertices[name])
        return True

    def print_graph(self):
        """
        Print the graph representation of the components and what they are associated to
        :return:
        """
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


# DEPEND TELNET TCPIP NETCARD
# DEPEND TCPIP NETCARD
# DEPEND NETCARD TCPIP
# DEPEND DNS TCPIP NETCARD
# DEPEND BROWSER TCPIP HTML

n = 3  # int(input())
# used to ensure that depend is done only at the beginning
depend = True
valid_commands = {"DEPEND", "INSTALL", "REMOVE", "LIST"}
terminate_command = "END"
g = Graph()
installed = set()

for _ in range(n):
    # parse input
    line = input().split()
    print(" ".join(line))
    command = line[0]
    items = []
    # validate command

    if command == "DEPEND" and depend:
        items = line[1:]
        # add vertexes
        for i in items:
            g.add_vertex(Vertex(i))
        # add edges
        for edge in items[1:]:
            g.add_edge(items[0], edge)
    elif command == "INSTALL":
        # install items and those that it is dependent on
        items = line[1:]
        depend = False
        if len(items) != 1:
            raise ValueError("Only Install 1 component at a time")
        installed.add(items[0])
        # get the associated things from the other components
        installed |= g.get_neighbors(items[0])

    elif command == "LIST":
        # list the names of all currently installed components
        depend = False
        for item in installed:
            print(f"{item}")
    elif command == "REMOVE":
        items = line[1:]
        depend = False
        if len(items) != 1:
            raise ValueError("Only Install 1 component at a time")
        if items[0] in installed:
            if g.remove_edges(items[0]):
                installed.remove(items[0])
    elif command == "END":
        exit()
    else:
        raise ValueError(
            f"Invalid input. First string in input must be one of {valid_commands} or {terminate_command}"
        )

    # g.print_graph()

    # validate that all depends are first and not after anything else
