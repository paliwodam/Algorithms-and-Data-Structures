from cmath import inf


def czolgi_b1(L, S, P, t):
    n = len(S)
    T = [inf] * (n + 1)

    T[n] = 0
    P.append(0)
    S.append(t)

    for i in range(n-1, -1, -1):
        T[i] = T[i+1] + P[i+1] * (S[i+1] - S[i])
        k = i + 2
        while k <= n and S[k] - S[i] <= L:
            T[i] = min(T[i], T[k] + P[k] * (S[k] - S[i]))
            k += 1

    wyn = T[0] + P[0] * S[0]
    k = 1
    while k <= n and S[k] <= L:
        wyn = min(wyn, T[k] + P[k]*S[k])
        k += 1

    print(wyn)


def czolgi2(S, P, L, t):
    n = len(S)
    T = [[inf] * L for _ in range(n+1)]

    def f(i, y):
        if T[i][y] != inf:
            return T[i][y]

        if i == n - 1:
            if y < 0 or t - S[n-1] > L:
                T[i][y] = inf

            elif t - S[n-1] > y:
                T[i][y] = P[n-1] * (L - y)

            else:
                T[i][y] = 0

            return T[i][y]

        if y - (S[i+1]-S[i]) < 0:
            T[i][y] = f(i+1, L-(S[i+1] - S[i])) + P[i]*(L-y)

        else:
            T[i][y] = min(f(i+1, y - (S[i+1] - S[i])), f(i+1, L - (S[i+1]-S[i])) + P[i]*(L-y))

        return T[i][y]

    result = f(0, L-S[0])
    print(result)


S = [1, 3, 4, 6, 10]
P = [1, 5, 1, 2, 1]
czolgi2(S, P, 4, 13)



