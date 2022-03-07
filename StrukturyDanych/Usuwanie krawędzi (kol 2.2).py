# Michał Gniadek

# 1. Używając BFSa liczymy odłegłość od s do każdego wierzchołka

# 2. Używając DFSa który idzie od wierzchołka t i porusza się tylko
# wierzchołkami bliższymi o 1 (czyli poruszającego się najkrótszymi
# ścieżkami) liczy ilość wierzchołków z najkrótszych ścieżek o danej
# odległości (i zapisuje przykłąd takiego wierzchołka)

# 3. Jeśli istnieje odległość D, taka że jest tylko jeden wierzchołek
# o odległość D i jeden o odległość D+1 to każda najkrótsza ścieżka
# przechodzi przez krawędź między nimi

# O(V + E) (bfs, dfs, maksymalna odległość 😊 długość tablic) to V)

# from zad2testy import runtests
from collections import deque


def dfs(G, v, dist, visited, number_of_dist, exmple_of_dist):
    visited[v] = True

    number_of_dist[dist[v]] += 1
    exmple_of_dist[dist[v]] = v

    for u in G[v]:
        if not visited[u] and dist[u] == dist[v] - 1:
            dfs(G, u, dist, visited, number_of_dist, exmple_of_dist)


def enlarge(G, s, t):
    N = len(G)
    dist = [-1] * N

    q = deque()

    dist[s] = 0
    q.append(s)

    while len(q) > 0:
        v = q.popleft()

        for u in G[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                q.append(u)

    # Nie ma ścieżki między s i t
    if dist[t] == -1:
        return None

    dfs_visited = [False] * N
    dfs_visited[t] = True

    # Liczba wierzchołków z dowolnej najkrótszej ścieżki
    # o danej odległości od s i przykłady takich wierzchołków
    number_of_dist = [0] * N
    exmple_of_dist = [-1] * N

    dfs(G, t, dist, dfs_visited, number_of_dist, exmple_of_dist)

    for i in range(len(number_of_dist)-1):
        if number_of_dist[i] == 1 and number_of_dist[i+1] == 1:
            return (exmple_of_dist[i], exmple_of_dist[i+1])
    return None


G = [[1, 4],
     [2, 0],
     [1, 3],
     [2, 4],
     [0, 3]]

s = 0
t = 3
print(enlarge(G, s, t))

# runtests(enlarge)