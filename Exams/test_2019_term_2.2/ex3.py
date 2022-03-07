from math import log10, inf, floor
from queue import PriorityQueue


def comm_digit(a, b):
    n = floor(log10(a) + 1)
    n2 = floor(log10(b) + 1)

    T = [0] * 10
    for i in range(n):
        T[(a % 10**(i+1)) // 10**i] += 1

    for j in range(n2):
        if T[(b % 10**(j+1)) // 10**j] > 0:
            return True
    return False


def min_sum(T):
    n = len(T)
    a = 0
    b = 0

    for i in range(n):
        if T[i] < T[a]:
            a = i
        if T[i] > T[b]:
            b = 1

    G = [[-1]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j and comm_digit(T[i], T[j]):
                G[i][j] = abs(T[i] - T[j])

    d = Dikstra(G, a)
    if d[b] == inf:
        return -1
    else:
        return d[b]


def Dikstra(E, s):
    n = len(E)

    d = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]

    Q = PriorityQueue()
    d[s] = 0
    Q.put((0, s))

    def relax(u, v):
        if d[v] > d[u] + E[u][v]:
            d[v] = d[u] + E[u][v]
            parent[v] = u
            Q.put((d[v], v))

    while not Q.empty():
        u = Q.get()
        visited[u[1]] = True

        for v in range(len(E[u[1]])):
            if E[u[1]][v] != -1 and not visited[v]:
                relax(u[1], v)
    return d


T = [123, 890, 688, 587, 257, 246]
T2 = [587, 990, 257, 246, 668, 132]

print(min_sum(T), min_sum(T2))