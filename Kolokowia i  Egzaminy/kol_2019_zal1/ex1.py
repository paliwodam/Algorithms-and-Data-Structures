from math import inf
from queue import PriorityQueue


def jak_dojade(G, P, c, a, b):
    n = len(G)

    P2 = [0] * n
    for i in P:
        P2[i] = 1

    d = [[inf] * (c + 1) for _ in range(n)]
    visited = [[False] * (c + 1) for _ in range(n)]
    parent = [[None] * (c + 1) for _ in range(n)]

    Q = PriorityQueue()
    d[a][c] = 0
    Q.put((0, a, c))

    while not Q.empty():
        dis, u, fuel = Q.get()

        fuel2 = fuel
        if P2[u] == 1:
            fuel2 = c

        for v in range(n):
            f = fuel2 - G[u][v] # ilość paliwa z jaką przyjedziemy do wierzchołka v
            if G[u][v] != -1 and f >= 0 and not visited[v][f]:
                if d[v][f] > d[u][fuel] + G[u][v]:
                    d[v][f] = d[u][fuel] + G[u][v]
                    parent[v][f] = (u, fuel)
                    Q.put((dis+G[u][v], v, f))

    u = 0
    for i in range(c+1):
        if d[b][u] > d[b][i]:
            u = i

    if parent[b][u] is None:
        return None

    A = get_path(parent, u, a, b)
    A.append(b)
    return A


def get_path(parent, i, a, b):
    u, v = parent[b][i]
    if u != a:
        A = get_path(parent, v, a, u)
        A.append(u)
        return A
    return [a]


G = [[-1, 6, -1, 5, 2],
     [-1, -1, 1, 2, -1],
     [-1, -1, -1, -1, -1],
     [-1, -1, 4, -1, -1],
     [-1, -1, 8, -1, -1]]
P = [0, 1, 3]

print(jak_dojade(G, P, 6, 0, 2))
