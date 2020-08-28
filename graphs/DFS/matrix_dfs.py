adjacency_matrix = [[0, 1, 1, 1],
                    [1, 0, 0, 1],
                    [1, 0, 0, 1],
                    [1, 1, 1, 0]]


def dfs(start_node):
    to_visit = list()

    for c in range(len(adjacency_matrix[start_node])):
        if adjacency_matrix[start_node][c] == 1 and (c not in to_visit):
            dfs(start_node+1)
