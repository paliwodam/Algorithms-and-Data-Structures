from math import inf
from queue import PriorityQueue


def letters(G, W):
    L = G[0]
    E = G[1]

    n = len(L)
    E2 = [[] for _ in range(n)]

    for u, v, w in E:
        E2[u].append((v, w))
        E2[v].append((u, w))

    n_w = len(W)

    d = [[inf]*n_w for _ in range(n)]
    parent = [[None]*n_w for _ in range(n)]
    visited = [[False]*n_w for _ in range(n)]

    Q = PriorityQueue()
    for i in range(n):
        if L[i] == W[0]:
            # (odległość, indeks wierzchołka, indeks litery)
            Q.put((0, i, 0))
            d[i][0] = 0

    while not Q.empty():
        dis, u, i_w = Q.get()
        visited[u][i_w] = True

        for v, w in E2[u]:
            if i_w + 1 < n_w and L[v] == W[i_w + 1] and not visited[v][i_w + 1]:
                if d[v][i_w + 1] > d[u][i_w] + w:
                    d[v][i_w + 1] = d[u][i_w] + w
                    parent[v][i_w + 1] = u
                    Q.put((dis + w, v, i_w + 1))

    u = 0
    for i in range(n):
        if d[i][n_w - 1] < d[u][n_w - 1]:
            u = i

    if d[u][n_w - 1] == inf:
        return None

    A = get_path(parent, n_w-1, u)
    print(A)


def get_path(parent, i, u):
    if i == 0:
        return [u]
    else:
        v = parent[u][i]
        A = get_path(parent, i-1, v)
        A.append(u)
        return A


L = ["k", "k", "o", "o", "t", "t"]
E = [(0, 2, 2), (1, 2, 1), (1, 4, 3), (1, 3, 2), (2, 4, 5), (3, 4, 1), (3, 5, 3)]
letters((L, E), "kto")
