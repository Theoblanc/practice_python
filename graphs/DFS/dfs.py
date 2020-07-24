graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'G', 'H'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['E'],
         'G': ['C'],
         'H': ['C']}


def dfs(graph, start_node):
    stack = list()
    to_visit = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()

        if node not in to_visit:
            to_visit.append(node)
            stack.extend(graph[node])

        return to_visit
