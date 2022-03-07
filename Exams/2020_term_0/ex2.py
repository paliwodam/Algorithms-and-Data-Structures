from math import inf


class Node:
    def __init__(self):
        self.left = None # lewe poddrzewo
        self.leftval = 0 # wartość krawędzi do lewego poddrzewa jeśli istnieje
        self.right = None # prawe poddrzewo
        self.rightval = 0 # wartość krawędzi do prawego poddrzewa jeśli istnieje
        self.values = []


def f(T, k):
    if k == 0:
        return 0

    if T is None:
        return -inf

    if T.values[k] != -inf:
        return T.values[k]

    max_s = max(f(T.left, k-1) + T.leftval, f(T.right, k-1) + T.rightval)

    for i in range(k-1):
        max_s = max(max_s, f(T.left, i) + T.leftval + f(T.right, k-2 - i) + T.rightval)

    T.values[k] = max_s
    return max_s


def f2(T, k):
    if T is None:
        return -inf
    return max(f(T, k), f2(T.left, k), f2(T.right, k))


def fill_with_arr(T, k):
    if T is not None:
        T.values = [-inf] * (k+1)
        fill_with_arr(T.left, k)
        fill_with_arr(T.right, k)


def valuableTree(T, k):
    fill_with_arr(T, k)
    return f2(T, k)


A = Node()
B = Node()
C = Node()
E = Node()
D = Node()
F = Node()
G = Node()

A.left = B
A.leftval = 1
A.right = E
A.rightval = 5
B.left = D
B.leftval = 6
B.right = C
B.rightval = 2
C.left = F
C.leftval = 8
C.right = G
C.rightval = 10

print(valuableTree(A, 6))