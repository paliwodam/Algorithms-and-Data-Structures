from math import inf
from queue import PriorityQueue


def jumper(G, s, w):
    n = len(G)
    d = [[inf] * 2 for _ in range(n)]
    visited = [[False] * 2 for _ in range(n)]

    Q = PriorityQueue()
    Q.put((0, s, 0))
    d[s][0] = 0

    while not Q.empty():
        dis, u, veh = Q.get()
        # print(dis, u, veh)
        if visited[u][veh]:
            continue
        visited[u][veh] = True

        for v in range(n):
            if G[u][v] != 0:
                if d[v][0] > d[u][veh] + G[u][v]:
                    d[v][0] = d[u][veh] + G[u][v]
                    Q.put((d[v][0], v, 0))

                if veh == 0:
                    for x in range(n):
                        if G[v][x] != 0 and d[x][1] > d[u][0] + max(G[u][v], G[v][x]):
                            d[x][1] = d[u][0] + max(G[u][v], G[v][x])
                            Q.put((d[x][1], x, 1))
    print(d[w])
    # return get_path(parent, w)
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
