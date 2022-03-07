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
    F = [[0] * n for _ in range(n)]
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

    # for v in F:
    #     print(v)

    return max_float


# directed
V = [0, 1, 2, 3, 4, 5]
E = [[0, 16, 13, 0, 0, 0],
     [0, 0, 10, 12, 0, 0],
     [0, 0, 0, 0, 14, 0],
     [0, 0, 9, 0, 0, 20],
     [0, 0, 0, 7, 0, 4],
     [0, 0, 0, 0, 0, 0]]

source = 0
sink = 5

print(FordFulkerson((V, E), source, sink))

# undirected
V2 = [0, 1, 2, 3, 4, 5]
E2 = [[0, 16, 13, 0, 0, 0],
      [16, 0, 10, 12, 0, 0],
      [13, 10, 0, 9, 14, 0],
      [0, 12, 9, 0, 7, 20],
      [0, 0, 14, 7, 0, 4],
      [0, 0, 0, 20, 4, 0]]

print(FordFulkerson((V2, E2), source, sink))


def FordFulkerson2(G, source, sink):
    V = G[0]
    E = G[1]

    n = len(V)
    F = [[0]*(n+2) for _ in range(n+2)]

    for i in source:
        F[0][i] = inf

    for i in sink:
        F[i][n+1] = inf

    for i in range(n):
        for j in range(n):
            F[i + 1][j+1] = E[i][j]

    parent = [-1 for _ in range(n + 2)]

    max_float = 0

    while BFS((V, F), 0, n + 1, parent):
        path_flow = inf
        s = 0

        while s != n + 1:
            path_flow = min(path_flow, F[parent[s]][s])
            s = parent[s]

        max_float += path_flow

        v = 0
        while v != n + 1:
            u = parent[v]
            F[u][v] -= path_flow
            F[v][u] += path_flow
            v = parent[v]

    return max_float


def matchingInTree(G, s):
    V = G[0]
    E = G[1]

    n = len(V)

    # build_graph
    E2 = [[0] * (n + 2) for _ in range(n + 2)]
    V2 = [0]*(n+2)

    visited = [False for _ in range(n)]

    def DFSVisit(G, u, k):
        visited[u] = True
        if k == 0:
            E2[0][u] = 1
            E2[u][0] = 1
            k = 1
        else:
            E2[u][n + 1] = 1
            E2[n + 1][u] = 1
            k = 0

        for v in range(n):
            if not visited[v] and E[u][v] != 0:
                E2[u][v] = 1
                DFSVisit(G, v, k)

    DFSVisit(G, s, 0)

    return FordFulkerson((V2, E2), 0, n + 1)


e = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]
v = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#          0
#         / \
#        /   \
#       /     \
#      1       2
#     / \     /|\
#    /   \   / | \
#   3    4  5  6  7
#  / \   |
# 8   9  10

print(matchingInTree((v, e), 0))
