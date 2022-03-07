def dominace(P):
    n = len(P)
    P2 = [None] * n
    for i in range(n):
        P2[i] = (P[i][0], P[i][1], i)

    # posortuj po dwóch współrzędnych
    S = []

    for i in range(n):
        if P2[i] is not None:
            S.append(P2[i][2])
            for j in range(i + 1, n):
                if P2[j] is not None and P2[i][0] <= P2[j][0] and P2[i][1] <= P2[j][1]:
                    P2[j] = None
    return S


P = [(2, 2), (1, 1), (2.5, 0.5), (3, 2), (0.5, 3)]
print(dominace(P))
