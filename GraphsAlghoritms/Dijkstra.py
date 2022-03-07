from math import inf
from queue import PriorityQueue


def Dijkstra(G, s):
    V = G[0]
    E = G[1]

    n = len(V)

    d = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]

    Q = PriorityQueue()
    d[s] = 0
    Q.put((0, s))

    def relax(u, v):
        if d[v] > d[u] + E[u][v]:
            d[v] = d[u] + E[u][v]
            parent[v] = u
            Q.put((d[v], v))

    while not Q.empty():
        u = Q.get()
        visited[u[1]] = True

        for v in range(len(E[u[1]])):
            if E[u[1]][v] != -1 and not visited[v]:
                relax(u[1], v)
    print(d)


V = [0, 1, 2, 3, 4]
E = [[-1, 2, -1, -1, 1],
     [2, -1, 4, 1, -1],
     [-1, 4, -1, 5, -1],
     [-1, 1, 5, -1, 3],
     [1, -1, -1, 3, -1]]

Dijkstra((V, E), 0)

