from _collections import deque


def BFS(E, s):
    n = len(E)

    Q = deque()
    visited = [False for _ in range(n)]
    d = [-1 for _ in range(n)]
    parent = [None for _ in range(n)]

    d[s] = 0
    visited[s] = True
    Q.append(s)

    while len(Q) != 0:
        u = Q.pop()
        for v in range(n):
            if E[u][v] != 0 and not visited[v]:
                visited[v] = True
                d[v] = d[u] + 1
                parent[v] = u
                Q.append(v)
    print(d)
    return visited, d, parent


E = [[0, 1, 0, 0, 0],
     [0, 0, 1, 0, 1],
     [0, 0, 0, 0, 1],
     [0, 1, 0, 0, 0],
     [0, 0, 0, 1, 0]]
v, d, p = BFS(E, 0)

print(v, d, p)