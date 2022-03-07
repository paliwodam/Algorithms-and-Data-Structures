def DFS(E):
    n = len(E)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    time = 0

    def DFSVisit(E, u):
        nonlocal time
        time += 1 # czas odwiedzenia
        visited[u] = True
        for v in range(n):
            if E[u][v] != 0 and not visited[v]:
                parent[v] = u
                DFSVisit(E, v)
        time += 1 # czas przetworzenia

    for u in range(n):
        if not visited[u]:
            DFSVisit(E, u)


