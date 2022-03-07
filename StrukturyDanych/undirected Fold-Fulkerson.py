from math import inf
from queue import PriorityQueue


def BFS(G, s, t, parent):
    V = G[0]
    E = G[1]

    n = len(V)

    visited = [False for _ in range(n)]

    Q = PriorityQueue()
    Q.put(s)
    visited[s] = True

    while not Q.empty():
        u = Q.get()
        for v in range(n):
            if visited[v] is False and E[u][v] > 0:
                visited[v] = True
                Q.put(v)
                parent[v] = u
                if v == t:
                    return True

    return False


def FordFulkerson(G, source, sink):
    V = G[0]
    E = G[1]

    n = len(V)
    F = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            F[i][j] = E[i][j]

    parent = [-1 for _ in range(n)]

    max_float = 0

    while BFS((V, F), source, sink, parent):
        path_flow = inf
        s = sink

        while s != source:
            path_flow = min(path_flow, F[parent[s]][s])
            s = parent[s]

        max_float += path_flow

        v = sink
        while v != source:
            u = parent[v]
            F[u][v] -= path_flow
            F[v][u] += path_flow
            v = parent[v]

    for i in range(n):
        for j in range(n):
            if F[i][j] < E[i][j]:
                F[i][j] = E[i][j] - F[i][j]
            else:
                F[i][j] = 0

    for v in F:
        print(v)

    return max_float


V = [0, 1, 2, 3, 4, 5]
E = [[0, 16, 13, 0, 0, 0],
         [16, 0, 10, 12, 0, 0],
         [13, 10, 0, 9, 14, 0],
         [0, 12, 9, 0, 7, 20],
         [0, 0, 14, 7, 0, 4],
         [0, 0, 0, 20, 4, 0]]

source = 0
sink = 5

print(FordFulkerson((V, E), source, sink))