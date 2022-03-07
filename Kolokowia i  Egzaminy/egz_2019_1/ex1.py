from math import inf
from queue import PriorityQueue


def islands(G, a, b):
    n = len(G)
    d = [[inf] * 3 for _ in range(n)]
    visited = [[False] * 3 for _ in range(n)]
    parent = [[None] * 3 for _ in range(n)]

    M = (0, 1)
    P = (1, 5)
    S = (2, 8)

    d[a][0], d[a][1], d[a][2] = 0, 0, 0
    Q = PriorityQueue()

    Q.put((0, a, M))
    Q.put((0, a, P))
    Q.put((0, a, S))

    while not Q.empty():
        dis, u, veh = Q.get()
        visited[u][veh[0]] = True

        for v in range(n):
            if G[u][v] != 0:
                veh2 = (-1, -1)
                if G[u][v] == 1:
                    veh2 = M
                if G[u][v] == 5:
                    veh2 = P
                if G[u][v] == 8:
                    veh2 = S
                if veh2 != veh and not visited[v][veh2[0]]:
                    if d[v][veh2[0]] > dis + G[u][v]:
                        d[v][veh2[0]] = dis + G[u][v]
                        parent[v][veh2[0]] = (u, veh[0])
                        Q.put((d[v][veh2[0]], v, veh2))

    u = 0
    for i in range(1, 3):
        if d[b][u] > d[b][i]:
            u = i

    if d[b][u] == inf:
        return -1
    else:
        A = get_path(parent, b, u)
        print(d[b][u])
        print(A)


def get_path(parent, a, b):
    if parent[a][b] is None:
        return[a]
    else:
        x, y = parent[a][b]
        A = get_path(parent, x, y)
        A.append(a)
        return A


G1 = [[0, 5, 1, 8, 0, 0, 0],
      [5, 0, 0, 1, 0, 8, 0],
      [1, 0, 0, 8, 0, 0, 8],
      [8, 1, 8, 0, 5, 0, 1],
      [0, 0, 0, 5, 0, 1, 0],
      [0, 8, 0, 0, 1, 0, 5],
      [0, 0, 8, 1, 0, 5, 0]]

islands(G1, 5, 2)
