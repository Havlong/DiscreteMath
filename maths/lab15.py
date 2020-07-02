from maths.lab14 import graph_from_matrix
from maths.lab14 import make_undirected


def dfs(x, visited_vertices, component, graph):
    for i in range(len(visited_vertices)):
        if graph[x][i] == 1 and not visited_vertices[i]:
            component.append(i)
            visited_vertices[i] = True
            dfs(i, visited_vertices, component, graph)


def is_euler(graph_to_check):
    for i in range(len(graph_to_check)):
        count = sum(graph_to_check[i]) + graph_to_check[i][i]
        if count % 2 != 0:
            return False
    return True


def is_gamilton(graph_to_check):
    if len(graph_to_check) < 3:
        return True
    for i in range(len(graph_to_check)):
        for j in range(i):
            if not graph_to_check[i][j]:
                count_a = sum(graph_to_check[i]) - graph_to_check[i][i]
                count_b = sum(graph_to_check[j]) - graph_to_check[j][j]
                if count_a + count_b < len(graph_to_check):
                    return False
    return True


if __name__ == '__main__':
    n = 7
    input_graph = make_undirected(list(map(lambda element: list(map(int, input().split())), range(n))))
    graph_from_matrix(input_graph, 'Входной граф', 'input15')
    components = []
    visited = [False for i in range(n)]
    for i in range(n):
        if not visited[i]:
            components.append([])
            dfs(i, visited, components[-1], input_graph)
    if len(components) == 1:
        print("Граф связный")
        edges_count = 0
        for i in input_graph:
            for v in i:
                edges_count += v
        print("Граф является деревом" if edges_count == 2 * n - 2 else "Граф не является деревом")
        print("Граф является Эйлеровым" if is_euler(input_graph) else "Граф не является Эйлеровым")
        print("Граф является Гамильтоновым по условию Оре" if is_gamilton(
            input_graph) else "Граф не является Гамильтоновым по условию Оре")
    else:
        print("Граф несвязный")
        print("Всего компонент:", len(components))
