class DirectedGraph(object):

    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, source, destination):
        if source not in self.adjacency_list:
            self.adjacency_list[source] = set()

        self.adjacency_list[source].add(destination)

    def get_vertex(self):

        for v in self.adjacency_list:
            yield v

    def get_neighbor(self, vertex):
        if vertex in self.adjacency_list:
            for u in self.adjacency_list[vertex]:
                yield u

    def dfs(self):
        parents = {}
        components = set()
        to_visit = []

        for vertex in self.get_vertex():
            if vertex not in parents:
                components.add(vertex)
            else:
                continue

            to_visit.append(vertex)

            while to_visit:
                v = to_visit.pop()

                for neighbor in self.get_neighbor(v):
                    if neighbor not in parents:
                        parents[neighbor] = v
                        to_visit.append(neighbor)

            return components, parents
