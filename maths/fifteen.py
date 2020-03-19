from maths.fourteen import graph_from_matrix
from maths.fourteen import make_undirected


def dfs(x, visited_vertices, component, graph):
    for i in range(len(visited_vertices)):
        if graph[x][i] == 1 and not visited_vertices[i]:
            component.append(i)
            visited_vertices[i] = True
            dfs(i, visited_vertices, component, graph)


def is_euler(graph_to_check):
    for i in range(len(graph_to_check)):
        count = 0
        for j in range(len(graph_to_check)):
            count += graph_to_check[i][j]
            if i == j:
                count += 1
        if count % 2 != 0:
            return False
    return True


def is_gamilton(graph_to_check):
    if len(graph_to_check) < 3:
        return True
    for i in range(len(graph_to_check)):
        for j in range(len(graph_to_check)):
            if i != j:
                count_a = 0
                count_b = 0
                for x in range(len(graph_to_check)):
                    count_a += graph_to_check[i][x]
                    count_b += graph_to_check[j][x]
                    if i == x:
                        count_a += 1
                    if j == x:
                        count_b += 1
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
        print("Граф является деревом" if edges_count == n - 1 else "Граф не является деревом")
        print("Граф является Эйлеровым" if is_euler(input_graph) else "Граф не является Эйлеровым")
        print("Граф является Гамильтоновым" if is_gamilton(input_graph) else "Граф не является Гамильтоновым")
    else:
        print("Граф несвязный")
        print("Всего компонент:", len(components))
