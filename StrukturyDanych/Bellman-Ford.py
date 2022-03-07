from math import inf


def BellmanFord(E, s):
    n = len(E)
    d = [inf for _ in range(n)]
    parent = [None for _ in range(n)]

    d[s] = 0

    def Relax(u, v):
        if d[v] > d[u] + E[u][v]:
            d[v] = d[u] + E[u][v]
            parent[v] = u

    for i in range(n - 1):
        for u in range(n):
            for v in range(n):
                if E[u][v] != inf:
                    Relax(u, v)

    for u in range(n):
        for v in range(n):
            if E[u][v] != inf and d[v] > d[u] + E[u][v]:
                return False
    print(d)
    print(parent)
    return True


E = [[inf, 2, inf, inf, inf],
     [inf, inf, 4, -1, inf],
     [inf, inf, inf, 5, inf],
     [inf, inf, inf, inf, 3],
     [1, inf, inf, inf, inf]]

print(BellmanFord(E, 0))