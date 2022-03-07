from math import inf


def jumper(G, s, w):
    n = len(G)
    d = [[inf] * 2 for _ in range(n)]
    visited = [[False] * 2 for _ in range(n)]
    # parent = [[None] * 2 for _ in range(n)]

    d[s][0] = 0

    for _ in range(2 * n):
        u = -1
        du = inf
        veh = -1
        for i in range(n):
            for j in range(2):
                if d[i][j] < du and not visited[i][j]:
                    u = i
                    du = d[i][j]
                    veh = j

        visited[u][veh] = True

        for v in range(n):
            if G[u][v] != 0:
                if not visited[v][0] and d[v][0] > d[u][veh] + G[u][v]:
                    d[v][0] = d[u][veh] + G[u][v]
                    # parent[v][0] = (u, veh)

                if veh == 0:
                    for z in range(n):
                        if G[v][z] != 0 and not visited[z][1] and d[z][1] > d[u][0] + max(G[u][v], G[v][z]):
                            d[z][1] = d[u][0] + max(G[u][v], G[v][z])
                            # parent[z][1] = (u, 0)

    # print(d)
    return min(d[w][0], d[w][1])


G = [[0, 4, 0, 0, 0, 0, 0],
     [4, 0, 1, 5, 0, 0, 0],
     [0, 1, 0, 2, 0, 0, 0],
     [0, 5, 2, 0, 4, 3, 0],
     [0, 0, 0, 4, 0, 2, 0],
     [0, 0, 0, 3, 2, 0, 1],
     [0, 0, 0, 0, 0, 1, 0]]

print(jumper(G, 0, 6))

G2 = [[0, 2, 6, 0, 0],
      [2, 0, 3, 0, 0],
      [6, 3, 0, 0, 6],
      [0, 0, 0, 0, 0],
      [0, 0, 6, 0, 0]]

print(jumper(G2, 0, 4))

G3 = [[0, 8, 0, 0, 0, 0, 0, 0],
      [8, 0, 7, 0, 0, 0, 0, 0],
      [0, 7, 0, 1, 0, 0, 0, 0],
      [0, 0, 1, 0, 1, 0, 0, 0],
      [0, 0, 0, 1, 0, 1, 0, 0],
      [0, 0, 0, 0, 1, 0, 6, 0],
      [0, 0, 0, 0, 0, 6, 0, 6],
      [0, 0, 0, 0, 0, 0, 6, 0]]

print(jumper(G3, 0, 7))

G4 = [[0, 1, 200, 200, 200, 200],
      [1, 0, 2, 200, 200, 200],
      [200, 2, 0, 40, 200, 200],
      [200, 200, 40, 0, 40, 200],
      [200, 200, 200, 40, 0, 117],
      [200, 200, 200, 200, 117, 0]]

print(jumper(G4, 0, 5))