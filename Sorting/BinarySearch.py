def binsearch(A, x):
    n = len(A)
    l = 0
    r = n - 1
    while l <= r:
        m = (l+r)//2
        if A[m] < x:
            l = m + 1
        elif A[m] > x:
            r = m - 1
        else:
            return m
    print("The list does not contain", x)
    return -1
