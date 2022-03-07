def DFS(E):
    n = len(E)
    visited = [False for _ in range(n)]
    kolejnosc = []
    time = 0

    def DFSVisit(E, u):
        nonlocal time
        time += 1
        visited[u] = True
        for v in range(n):
            if E[u][v] == 2 and not visited[v]:
                DFSVisit(E, v)
        kolejnosc.append(u)
        time += 1

    for u in range(n):
        if not visited[u]:
            DFSVisit(E, u)

    return kolejnosc


def taskts(T):
    n = len(T)
    print(DFS(T))


T = [[0, 2, 1, 1],
     [1, 0, 1, 1],
     [2, 2, 0, 1],
     [2, 2, 2, 0]]

taskts(T)

G = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
taskts(G)