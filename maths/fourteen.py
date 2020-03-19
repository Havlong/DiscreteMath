from random import randint

from graphviz import Graph


def make_undirected(matrix):
    for i in range(len(matrix)):
        for j in range(i):
            matrix[j][i] = max(matrix[i][j], matrix[j][i])
            matrix[i][j] = matrix[j][i]
    return matrix


def graph_from_matrix(matrix, name, filename):
    graph = Graph(name='G' + name, filename=filename, format='svg',
                  node_attr={'shape': 'circle', 'color': 'lightblue2', 'style': 'filled'})
    for i in range(len(matrix)):
        graph.node(str(i + 1))
    for i in range(len(matrix)):
        for j in range(i):
            if matrix[i][j] == 1 and i != j:
                graph.edge(str(i + 1), str(j + 1))
    graph.attr('graph', label=name, labelloc='t')
    graph.view(cleanup=True)


def unite_graphs(a, b):
    if len(a) < len(b):
        (a, b) = (b, a)
    answer = a
    for i in range(len(b)):
        for j in range(len(b)):
            answer[i][j] = max(answer[i][j], b[i][j])
    return answer


def intersect_graphs(a, b):
    if len(a) < len(b):
        (a, b) = (b, a)
    answer = b
    for i in range(len(b)):
        for j in range(len(b)):
            answer[i][j] = min(answer[i][j], a[i][j])
    return answer


if __name__ == '__main__':
    first_graph = make_undirected([
        [1, 0, 0, 1, 1],
        [0, 1, 0, 1, 1],
        [1, 1, 0, 0, 0],
        [1, 0, 0, 0, 1],
        [0, 0, 0, 0, 1]
    ])

    second_graph = make_undirected(list(map(lambda y: list(map(lambda x: randint(0, 1), range(7))), range(7))))
    third_graph = make_undirected(list(map(lambda y: list(map(lambda x: randint(0, 1), range(7))), range(7))))

    graph_from_matrix(first_graph, 'A', 'first14')
    graph_from_matrix(second_graph, 'B', 'second14')
    graph_from_matrix(third_graph, 'C', 'third14')

    answer_graph = intersect_graphs(unite_graphs(first_graph, second_graph), third_graph)

    graph_from_matrix(answer_graph, 'Результат (A || B) ^ C', 'result14')

    print(*first_graph, sep='\n')
    print()
    print(*second_graph, sep='\n')
    print()
    print(*third_graph, sep='\n')
    print()
    print(*answer_graph, sep='\n')
