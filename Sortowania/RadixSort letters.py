def get_max_lengh(T):
    L = 0
    for i in T:
        if len(i) > L:
            L = len(i)
    return L


def radixSort(T):
    L = get_max_lengh(T)
    for i in range(L-1, -1, -1):
        countSort(T, i)


def countSort(T, idx):
    letters = [0]*26
    start = 0
    T2 = [0] * len(T)

    for i in range(len(T)):
        if len(T[i]) - 1< idx:
            T2[start] = T[i]
            start += 1
        else:
            L = ord(T[i][idx]) - 97
            letters[L] += 1

    letters[0] += start
    for i in range(1, len(letters)):
        letters[i] += letters[i-1]

    for i in range(len(T)-1, -1, -1):
        if len(T[i]) - 1 >= idx:
            L = ord(T[i][idx])-97
            letters[L] -= 1
            T2[letters[L]] = T[i]

    for i in range(len(T)):
        T[i] = T2[i]


T = ["abc", "a", "abbb", "abc", "abd"]

radixSort(T)

print(T)