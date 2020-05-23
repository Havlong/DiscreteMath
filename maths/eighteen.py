from maths.fourteen import make_undirected


def paint(graph, color, graph_size, cur):
    min_color = 1
    for i in sorted(map(lambda x: color[x] if graph[cur][x] != 0 else 0, range(graph_size))):
        if i == min_color:
            min_color += 1
    color[cur] = min_color
    for i in range(graph_size):
        if graph[cur][i] != 0 and color[i] == 0:
            paint(graph, color, graph_size, i)


if __name__ == '__main__':
    n = 8
    input_graph = make_undirected(list(map(lambda element: list(map(int, input().split())), range(n))))
    painting = [0 for i in range(n)]
    paint(input_graph, painting, n, 0)
    print(*range(1, n + 1))
    print(*painting)

"""
0 1 1 0 0 1 0 0
1 0 0 1 1 0 1 0
1 0 0 0 0 1 0 0
0 1 0 0 1 0 1 0
0 1 0 1 0 0 0 0
1 0 1 0 0 0 1 0
0 1 0 1 0 1 0 1
0 0 0 0 0 0 1 0

graph G {
    node[style=filled]
    1[color="red"]
    2[color="green"]
    3[color="blue"]
    4[color="red"]
    5[color="blue"]
    6[color="green"]
    7[color="blue"]
    8[color="red"]
    1 -- 2
    1 -- 3
    1 -- 6
    2 -- 4
    2 -- 5
    2 -- 7
    3 -- 6
    4 -- 5
    4 -- 7
    6 -- 7
    7 -- 8
}
"""
