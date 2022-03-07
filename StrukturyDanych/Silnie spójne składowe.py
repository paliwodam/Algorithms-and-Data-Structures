def Silnie_spojne_skladowe(E):
    n = len(E)
    visited = [False for _ in range(n)]
    d = [None] * n
    res = []
    time = 0

    def DFSVisit(E, u):
        nonlocal time
        visited[u] = True
        res.append(u)
        for v in range(n):
            if E[u][v] != 0 and not visited[v]:
                DFSVisit(E, v)
        d[u] = (time, u)
        time += 1

    for u in range(n):
        if not visited[u]:
            DFSVisit(E, u)

    for i in range(n):
        for j in range(i + 1, n):
            E[i][j], E[j][i] = E[j][i], E[i][j]

    d = sorted(d, reverse=True)
    order = [d[i][1] for i in range(n)]
    visited = [False for _ in range(n)]
    res = []

    for u in order:
        if not visited[u]:
            DFSVisit(E, u)
            print(res)
            res = []


E = [[0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0]]


Silnie_spojne_skladowe(E)