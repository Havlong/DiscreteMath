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
            old_tree = tree[edge[2]]
            new_tree = tree[edge[1]]
            for v in tree:
                if tree[v] == old_tree:
                    tree[v] = new_tree
    return result


if __name__ == '__main__':
    n = 7
    input_graph = make_undirected(list(map(lambda element: list(map(int, input().split())), range(n))))
    start = int(input())
    graph_from_matrix(input_graph, 'Входной граф', 'input17')

    print("Полученный по методу Крускала граф:")
    print(*kruskal(input_graph))
