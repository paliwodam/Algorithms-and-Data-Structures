from _collections import deque
from math import inf


def longest_path(E, s):
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
        for v in E[u]:
            if not visited[v]:
                visited[v] = True
                d[v] = d[u] + 1
                parent[v] = u
                Q.append(v)
    return max(d), d


def best_root(L):
    n = len(L)
    min_max_d, parent, distance = inf, None, None
    for i in range(n):
        m_d, d = longest_path(L, i)
        if m_d < min_max_d:
            min_max_d = m_d
            distance = d

    for i in range(n):
        if distance[i] == 0:
            return i


L = [[2],
     [2],
     [0, 1, 3],
     [2, 4],
     [3, 5, 6],
     [4],
     [4]]
print(best_root(L))