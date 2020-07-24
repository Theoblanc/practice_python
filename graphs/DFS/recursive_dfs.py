graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'G', 'H'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['E'],
         'G': ['C'],
         'H': ['C']}


def recursive_dfs(graph, start_node, visited=[]):
    visited.append(start_node)

    for node in graph[start_node]:
        if node not in visited:
            recursive_dfs(graph, node, visited)

    return visited
