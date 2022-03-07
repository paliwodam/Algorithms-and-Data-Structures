from math import inf


# żleeeeeeeeeeeeeeeeed

def mnozenie_macierzy(A):
    n = len(A)
    F = [[inf] * n for _ in range(n)]
    for i in range(n):
        F[i][i] = 0

    for i in range(n):
        for j in range(i+1, n):
            for k in range(i+1, n-1):
                F[i][j] = min(F[i][j], F[i][k] + F[k+1][j] + A[i][0] * A[k][1] * A[j][1])