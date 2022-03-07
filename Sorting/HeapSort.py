def left(i):
    return 2*i + 1


def right(i):
    return 2*i + 2


def parent(i):
    return (i-1) // 2


def heapify(A, n, i):
    l = left(i)
    r = right(i)
    m = i
    if l < n and A[l] > A[m]:
        m = l
    if r < n and A[r] > A[m]:
        m = r
    if m != i:
        A[i], A[m] = A[m], A[i]
        heapify(A, n, m)


def buildheap(A):
    n = len(A)
    for i in range(parent(n-1), -1, -1):
        heapify(A, n, i)
        # heapify_reversed(A, n, i)


def heapsort(A):
    n = len(A)
    buildheap(A)
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)
        # heapify_reversed(A, i, 0)


def add(A, x):
    A.append(x)
    n = len(A)
    i = n - 1
    j = (i - 1) // 2
    while i > 0 and A[j] <= x:
        A[i], A[j] = A[j], A[i]
        i = j
        j = parent(i)
    return A


def remove_max(A):
    n = len(A)
    A[0], A[n-1] = A[n-1], A[0]

    heapify(A, n-1, 0)


# to reverse heapsort stays the same, we change heapify only


def heapify_reversed(A, n, i):
    l = left(i)
    r = right(i)
    m = i
    if l < n and A[l] < A[m]:
        m = l
    if r < n and A[r] < A[m]:
        m = r
    if m != i:
        A[i], A[m] = A[m], A[i]
        heapify_reversed(A, n, m)


T = [-10, -9, 4, -4, 14, 3, -4, 2, 18, -19, 9]
buildheap(T)
print(T)
T.insert(8, 0)
heapify_reversed(T, len(T), 0)
print(T)
heapsort(T)
print(T)
