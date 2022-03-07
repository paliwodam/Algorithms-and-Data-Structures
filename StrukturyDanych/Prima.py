from math import inf
from queue import PriorityQueue


def Prima(G, s):
    V = G[0]
    E = G[1]

    n = len(V)

    d = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]

    Q = PriorityQueue()
    d[s] = 0
    Q.put((0, s))

    min_cycl = inf

    def get_cycl_lengh(u, v):
        print(u, v, parent[u], parent[v])
        if parent[u] == parent[v]:
            return 0
        if parent[u] is None or parent[v] is None:
            return inf
        return min(get_cycl_lengh(u, parent[v]) + E[v][parent[v]], get_cycl_lengh(parent[u], v) + E[u][parent[u]], get_cycl_lengh(parent[u], parent[v]) + E[v][parent[v]] + E[u][parent[u]])

    while Q.qsize() > 0:
        u = Q.get()
        visited[u[1]] = True

        for v in range(len(E[u[1]])):
            if E[u[1]][v] != -1 and d[v] > E[u[1]][v]:
                if d[v] != inf:
                    print(get_cycl_lengh(u[1], v))
                d[v] = E[u[1]][v]
                parent[v] = u[1]
                Q.put((d[v], v))
    print(d)


V = [0, 1, 2, 3, 4]
E = [[-1, 2, -1, -1, 1],
     [2, -1, 4, 1, -1],
     [-1, 4, -1, 5, -1],
     [-1, 1, 5, -1, 3],
     [1, -1, -1, 3, -1]]

Prima((V, E), 2)
