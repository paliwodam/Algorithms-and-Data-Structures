

def partition(T, l, r):
    x = T[r]
    i = l
    for j in range(l, r):

        if T[j] <= x:
            T[i], T[j] = T[j], T[i]
            i += 1

    T[i], T[r] = T[r], T[i]
    return i


def quickSelect(T, l, r, k):

    if 0 < k <= r - l + 1:
        index = partition(T, l, r)

        if index - l == k - 1:
            return T[index]

        if index - l > k - 1:
            return quickSelect(T, l, index - 1, k)

        return quickSelect(T, index + 1, r, k - index + l - 1)


def soilder(T, p, q):
    n = len(T)
    pth = quickSelect(T, 0, n-1, p+1)
    qth = quickSelect(T, 0, n-1, q+1)

    T2 = [0] * (q - p + 1)
    k = 0
    for i in T:
        if pth <= i <= qth:
            T2[k] = i
            k += 1

    return T2


A = [195, 185, 173, 188, 199, 200, 210, 201, 154, 163]

print(soilder(A, 3, 7))
