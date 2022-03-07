from math import inf


def dijkstra(G, s):
    n = len(G)
    d = [inf] * n
    visited = [False] * n
    parent = [None] * n

    d[s] = 0

    for _ in range(n):
        du = inf
        for i in range(n):
            if d[i] < du and not visited[i]:
                u = i
                du = d[i]
        visited[u] = True
        for v in range(n):
            if G[u][v] != 0 and not visited[v] and d[v] > d[u] + G[u][v]:
                d[v] = d[u] + G[u][v]
                parent[v] = u

