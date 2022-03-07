def getMaxLengh(T):
    max_n = 0
    for i in T:
        if i > max_n:
            max_n = i

    max_l = 0
    while max_n > 0:
        max_n //= 10
        max_l += 1
    return max_l


def getDigit(num, idx):
    d = num % (10 ** idx) // (10 ** (idx-1))
    return d


def radixSort(T):
    L = getMaxLengh(T)
    for i in range(1, L+1):
        countSort(T, i)


def countSort(T, idx):
    digits = [0]*10

    for i in range(len(T)):
        d = getDigit(T[i], idx)
        digits[d] += 1

    for i in range(1, len(digits)):
        digits[i] += digits[i-1]

    T2 = [0] * len(T)

    for i in range(len(T)-1, -1, -1):
        d = getDigit(T[i], idx)
        digits[d] -= 1
        T2[digits[d]] = T[i]

    for i in range(len(T)):
        T[i] = T2[i]


A = [5, 3, 1, 7, 2, 92, 11, 91]
radixSort(A)
print(A)