def countSort(T, i):
    n = len(T)
    counters = [0] * 11
    for j in range(n):
        counters[T[j][i]] += 1

    for j in range(1, 11):
        counters[j] += counters[j-1]

    T2 = [None] * n
    for j in range(n-1, -1, -1):
        counters[T[j][i]] -= 1
        T2[counters[T[j][i]]] = T[j]

    for j in range(n):
        T[j] = T2[j]


def radix_sort(T):
    countSort(T, 1)
    countSort(T, 0)


def count_single_multi(i):
    single = 0
    multi = 10

    digits = [0] * 10
    while i > 0:
        k = i % 10
        digits[k-1] += 1
        i //= 10

    for j in digits:
        if j == 1:
            single += 1
        if j > 1:
            multi -= 1

    return single, multi


def pretty_sort(T):
    n = len(T)
    C = [[0, 0, 0] for _ in range(n)]
    for i in range(n):
        C[i][0], C[i][1] = count_single_multi(T[i])
        C[i][2] = T[i]

    radix_sort(C)

    for i in range(n-1, -1, -1):
        print(C[i][2], end=" ")


T = [123, 114577, 67333, 455, 1266, 2344]
pretty_sort(T)