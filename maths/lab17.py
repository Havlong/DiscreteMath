from maths.lab14 import make_undirected, graph_from_matrix


def kruskal(graph):
    edges = []
    graph_size = len(graph)
    for i in range(graph_size):
        for j in range(graph_size):
            if graph[i][j] != 0:
                edges.append((graph[i][j], i, j))
    result = [[0 for j in range(graph_size)] for i in range(graph_size)]
    edges.sort()
    tree = [i for i in range(graph_size)]
    for edge in edges:
        if tree[edge[1]] != tree[edge[2]]:
            result[edge[1]][edge[2]] = edge[0]
            result[edge[2]][edge[1]] = edge[0]
            old_tree = tree[edge[2]]
            new_tree = tree[edge[1]]
            for v in range(len(tree)):
                if tree[v] == old_tree:
                    tree[v] = new_tree
    return result


if __name__ == '__main__':
    n = 7
    input_graph = make_undirected(list(map(lambda element: list(map(int, input().split())), range(n))))
    graph_from_matrix(input_graph, 'Входной граф', 'input17')

    print("Полученный по методу Крускала граф:")
    output_graph = kruskal(input_graph)
    print(*kruskal(input_graph), sep='\n')
    graph_from_matrix(output_graph, 'Остов', 'output17')

"""
0 1  1  0 4  0 3
1 0  0  0 89 0 1
1 0  0  9 0  0 10
0 0  9  0 0  0 2
4 89 0  0 0  1 1
0 0  0  0 1  0 3
3 1  10 2 1  3 0
"""
