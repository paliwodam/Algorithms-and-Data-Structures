from math import inf


def zbigniew(A):
    n = len(A)
    max_e = 0
    for i in A:
        max_e += i
    F = [[inf] * (max_e + 1) for _ in range(n)]

    F[0][A[0]] = 0

    for i in range(n):
        for e in range(max_e + 1):
            if F[i][e] != inf:
                for r in range(1, e + 1):
                    if i + r >= n:
                        break
                    F[i+r][e - r + A[i+r]] = min(F[i+r][e - r + A[i+r]], F[i][e] + 1)

    for i in F:
        print(i)
    print(min(F[n-1]))

    #
    # T = [[inf] * (max_e + 1) for _ in range(n)]
    #
    # def f(i, y):
    #     print(i, y)
    #     if 0 > i or i > max_e or 0 > y or y >= n:
    #         return inf
    #
    #     if T[i][y] != inf:
    #         return T[i][y]
    #     if i == n-1:
    #         T[i][y] = 0
    #         return 0
    #     if y == 0:
    #         T[i][y] = inf
    #         return inf
    #
    #     min_l = f(i+1, y + A[i+1] - 1) + 1
    #
    #     for j in range(2, y+1):
    #         curr = f(i+j, y + A[i+j]-j) + 1
    #         if curr < min_l:
    #             min_l = curr
    #
    #     T[i][y] = min_l
    #     return min_l
    #
    # # m = inf
    # # for e in range(max_e):
    # #     print(f(n-1, e))
    # print(f(0, A[0]))
    # for i in T:
    #     print(i)


A = [2, 2, 1, 0, 0, 0]
zbigniew(A)

