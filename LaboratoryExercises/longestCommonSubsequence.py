def longest_substring(A, B):
    n = len(A)

    F = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if A[i-1] == B[j-1]:
                F[i][j] = F[i-1][j-1] + 1
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1], F[i-1][j-1])

    print(F[n][n])
    for i in F:
        print(i)


A = [0, 3, 15, 2, 7, 3, 12, 7, 9]
B = [3, 4, 6, 7, 3, 11, 12, 18, 9]

# 3, 7, 3, 12, 9
longest_substring(A, B)
