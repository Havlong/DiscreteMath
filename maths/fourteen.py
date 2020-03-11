from random import randint


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
    first_graph = [
        [1, 0, 0, 1, 1],
        [0, 1, 0, 1, 1],
        [1, 1, 0, 0, 0],
        [1, 0, 0, 0, 1],
        [0, 0, 0, 0, 1]
    ]

    second_graph = list(map(lambda y: list(map(lambda x: randint(0, 1), range(7))), range(7)))
    third_graph = list(map(lambda y: list(map(lambda x: randint(0, 1), range(7))), range(7)))
    answer_graph = intersect_graphs(unite_graphs(first_graph, second_graph), third_graph)
    print(*first_graph, sep='\n')
    print()
    print(*second_graph, sep='\n')
    print()
    print(*third_graph, sep='\n')
    print()
    print(*answer_graph, sep='\n')
