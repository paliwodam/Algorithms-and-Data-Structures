from math import log


def fast_sort(tab, a):
    n = len(tab)
    rng = 1/n

    buckets = [[] for _ in range(n)]
    for i in tab:
        b = int(log(i, a) / rng)
        buckets[b].append(i)

    for b in buckets:
        b.sort()

    res = []
    for b in buckets:
        for i in b:
            res.append(i)

    print(res)


T = [1, 1.01, 1.4, 1.2, 1.31]
a = 2
fast_sort(T, a)
