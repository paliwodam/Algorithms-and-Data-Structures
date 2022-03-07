def suma_podciągu(A, t):
    n = len(A)
    F = [[False] * (t+1) for _ in range(n)]

    for i in range(n):
        F[i][0] = True

    for i in range(1, n):
        for s in range(1, t+1):
            if s - A[i] >= 0:
                F[i][s] = F[i-1][s-A[i]] or F[i-1][s]
            else:
                F[i][s] = F[i-1][s]

    print(F[n-1][t])


T = [6, 3, 8, 2, 9, 3]
s = 14
# s = 14 #true
# s = 7 #false

suma_podciągu(T, 7)
suma_podciągu(T, 14)