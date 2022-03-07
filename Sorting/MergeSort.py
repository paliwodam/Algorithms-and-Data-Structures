from random import randint, seed


def mergesort_rec(T, l, r):
    if abs(l - r) < 2:
        return [T[l]]

    m = (l + r) // 2

    left = mergesort_rec(T, l, m)
    right = mergesort_rec(T, m, r)

    out = [0] * (len(left) + len(right))
    l_index, r_index = 0, 0

    for i in range(len(out)):
        if r_index >= len(right) or (l_index < len(left) and left[l_index] < right[r_index]):
            out[i] = left[l_index]
            l_index += 1
        else:
            out[i] = right[r_index]
            r_index += 1

    return out


def mergesort(T):
    if len(T) == 0:
        return T
    return mergesort_rec(T, 0, len(T))


seed(42)

n = 10
T = [randint(1, 10) for i in range(10)]

print("Before sorting: T =", T)
T = mergesort(T)
print("After sorting    : T =", T)

for i in range(len(T)-1):
    if T[i] > T[i+1]:
        print("Sort error!")
        exit()

print("OK")
