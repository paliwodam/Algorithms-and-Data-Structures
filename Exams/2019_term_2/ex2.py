from math import ceil, sqrt, inf


class Node:
    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent = self


def find(x):
    if x is not x.parent:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            if x.rank == y.rank:
                y.rank += 1


def get_dis(T):
    n = len(T)
    A = []
    for i in range(n):
        for j in range(i+1, n):
            x1 = T[i][0]
            y1 = T[i][1]
            x2 = T[j][0]
            y2 = T[j][1]
            # if x1 != x2 or y1 != y2:
            w = ceil(sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))
            A.append((w, i, j))
    return A


def Kruskal(K, s, n):
    W = [Node(i) for i in range(n)]
    n2 = len(K)
    A = []
    for i in range(s, n2):
        u = K[i][1]
        v = K[i][2]
        x = find(W[u])
        y = find(W[v])
        if x != y:
            A.append((K[i][0], K[i][1], K[i][2]))
            union(x, y)

    if len(A) != n-1:
        return inf
    else:
        return A[n-2][0] - A[0][0]


def highway(T):
    n = len(T)
    K = get_dis(T)
    K.sort()

    n2 = len(K)

    min_d = inf

    for i in range(n2):
        a = Kruskal(K, i, n)
        if a < min_d:
            min_d = a

    print(min_d)


A = [(10, 10), (15, 25), (20, 20), (30, 40)]
highway(A)