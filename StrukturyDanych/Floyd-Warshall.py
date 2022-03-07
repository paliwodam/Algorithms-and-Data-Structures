def Floyd_Warshall(E):
    n = len(E)
    S = E

    for t in range(n):
        for u in range(n):
            for w in range(n):
                S[u][w] = min(S[u][w], S[u][t] + S[t][w])

    return S