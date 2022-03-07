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


def neighbours_to_list(E):
    n = len(E)

    K = []

    for i in range(n):
        for j in range(n):
            if E[i][j] != -1:
                K.append((E[i][j], i, j))
    return K


def Kruskal(E):
    n = len(E)

    W = [Node(i) for i in range(n)]
    K = neighbours_to_list(E)
    K.sort()
    # print(K)
    # K = sorted(K, key=lambda x: x[2])

    A = []

    for i in range(len(K)):
        u = K[i][1]
        v = K[i][2]
        x = find(W[u])
        y = find(W[v])
        if x != y:
            A.append((K[i][1], K[i][2]))
            union(x, y)

    print(A)


#      1
#    0----4
#  1 |    | 3
#    1-3--3
#   4 \  / 5
#      \/
#      2

G = [[-1, 2, -1, -1, 1],
     [2, -1, 4, 1, -1],
     [-1, 4, -1, 5, -1],
     [-1, 1, 5, -1, 3],
     [1, -1, -1, 3, -1]]

V = [0, 1, 2, 3, 4]
Kruskal(G)


# 0 - 1       6
#    / \     / \
#   2   4 - 5 - 7
#    \ /
#     3 - 8 - 9

E2 = [
    [1],        # 0
    [0, 2, 4],  # 1
    [1, 3],     # 2
    [2, 4, 8],  # 3
    [1, 3, 5],  # 4
    [4, 6, 7],  # 5
    [5, 7],     # 6
    [5, 6],     # 7
    [3, 9],     # 8
    [8],        # 9
]
