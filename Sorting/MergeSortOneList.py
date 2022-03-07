def mergesort(A, left, right, tmp):
    if abs(left-right) < 2:
        return left, right

    mid = (left + right) // 2

    left_1, left_2 = mergesort(A, left, mid, tmp)
    right_1, right_2 = mergesort(A, mid, right, tmp)

    i, j, k = left_1, right_1, left_1
    while i < left_2 and j < right_2:
        if A[i] <= A[j]:
            tmp[k] = A[i]
            i += 1
        else:
            tmp[k] = A[j]
            j += 1
        k += 1

    while i < left_2:
        tmp[k] = A[i]
        k += 1
        i += 1

    while j < right_2:
        tmp[k] = A[j]
        k += 1
        j += 1

    for i in range(left_1, right_2):
        A[i] = tmp[i]

    return left_1, right_2


T = [7, 19, 9, 15, 16, 14, 10, 19, 3, 14, 12]
tmp = [0]*len(T)
mergesort(T, 0, len(T), tmp)
print(T)
