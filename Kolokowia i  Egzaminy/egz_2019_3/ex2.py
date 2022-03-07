def tower(A):
    n = len(A)
    F = [1] * n
    P = [-1] * n
    for i in range(1, n):
        for j in range(i):
            if A[j][0] <= A[i][0] and A[j][1] >= A[i][1] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j

    print(P)
    return max(F)


A = [(1, 4), (0, 5), (1, 5), (2, 6), (2, 4)]
A2 = [(10, 15), (8, 14), (1, 6), (3, 10), (8, 11), (6, 15)]
print(tower(A))
