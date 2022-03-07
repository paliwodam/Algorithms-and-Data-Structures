def countsort(A, k):
    n = len(A)
    C = [0]*k
    B = [0]
    for i in range(n):
        C[A[i]] += 1

    for i in range(1, k):
        C[i] += C[i-1]

    for i in range(n-1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]

    for i in range(n):
        A[i] = B[i]