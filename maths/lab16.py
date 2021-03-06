from maths.lab14 import make_undirected, graph_from_matrix

INF = 2000000000000000000


def dijkstra(s, distance, graph):
    my_n = len(graph)
    visited = [False for i in range(my_n)]
    distance[s] = 0
    for times in range(my_n):
        v_from = -1
        for v_new in range(my_n):
            if (not visited[v_new]) and (v_from == -1 or distance[v_new] < distance[v_from]):
                v_from = v_new
        if v_from == -1 or distance[v_from] == INF:
            break
        visited[v_from] = True

        for v_to in range(my_n):
            d = graph[v_from][v_to]
            if d != 0 and distance[v_from] + d < distance[v_to]:
                distance[v_to] = distance[v_from] + d


if __name__ == '__main__':
    n = 7
    input_graph = make_undirected(list(map(lambda element: list(map(int, input().split())), range(n))))
    start = int(input())
    graph_from_matrix(input_graph, 'Входной граф', 'input16')
    way = [INF for i in range(n)]
    dijkstra(start, way, input_graph)
    print(*range(1, n + 1))
    print(*way)

"""
0 1  1  0 4  0 3
1 0  0  0 89 0 1
1 0  0  9 0  0 10
0 0  9  0 0  0 2
4 89 0  0 0  1 1
0 0  0  0 1  0 3
3 1  10 2 1  3 0
"""
