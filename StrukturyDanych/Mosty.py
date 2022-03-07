from math import inf


def Mosty(E):
    n = len(E)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    d = [inf] * n
    low = [inf] * n
    time = 0

    def DFSVisit(E, u):
        nonlocal time
        time += 1
        visited[u] = True
        d[u] = time
        low[u] = d[u]
        for v in range(n):
            if E[u][v] != 0 and not visited[v]:
                parent[v] = u
                DFSVisit(E, v)
                low[u] = min(low[u], low[v])
            if E[u][v] != 0 and visited[v] and parent[v] != u and parent[u] != v:
                low[u] = min(low[u], low[v])

    for u in range(n):
        if not visited[u]:
            DFSVisit(E, u)

    for i in range(n):
        if d[i] == low[i] and parent[i] is not None:
            print(i, parent[i], end="  ")


E = [[0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
     [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
     [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]

Mosty(E)
