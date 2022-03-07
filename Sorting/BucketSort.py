def bucketsort(A):
    n = len(A)
    a = max(A)
    b = min(A)
    rng = (a+b)/n

    buckets = [[] for _ in range(n)]
    for i in A:
        b = int((i-b)/rng)
        buckets[b].append(i)

    for b in buckets:
        b.sort()

    res = []
    for b in buckets:
        for i in b:
            res.append(i)

    print(res)


A = [0.3, 0.21, 0.11, 0.08, 0.32, 0.67, 0.53, 0.876, 0.9]
bucketsort(A)
