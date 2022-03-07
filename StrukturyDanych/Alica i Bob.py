from math import inf
from queue import PriorityQueue
from random import seed, randint


def rozwiazanie(G, start, end):
    ALICE = 0
    BOB = 1

    N = len(G)
    q = PriorityQueue()
    # dist[ALICE][v] = najmniejszy dystans (który przejechała Alicja) od startu do v tak że do v dojechała Alicja
    # dist[BOB][v] = najmniejszy dystans (który przejechała Alicja) od startu do v tak że do v dojechał Bob
    dist = ([inf for _ in range(N)], [inf for _ in range(N)])
    parent = ([-1 for _ in range(N)], [-1 for _ in range(N)])

    dist[ALICE][start] = 0
    dist[BOB][start] = 0
    q.put((0, ALICE, start))
    q.put((0, BOB, start))

    while not q.empty():
        d, who, u = q.get()

        # Do u dojechał Bob
        if who == BOB:
            # Czy u już było odwiedzone przez Boba?
            if d > dist[BOB][u]:
                continue

            for v, e_w in G[u]:
                # Następna jedzie Alicja więc dodajemy odległość
                if dist[ALICE][v] > d + e_w:
                    dist[ALICE][v] = d + e_w
                    q.put((dist[ALICE][v], ALICE, v))
                    parent[ALICE][v] = u

        else:  # Do u dojechała Alicja
            if d > dist[ALICE][u]:
                continue

            for v, e_w in G[u]:
                # Następny jedzie Bob więc nie dodajemy odległości
                if dist[BOB][v] > d:
                    dist[BOB][v] = d
                    q.put((dist[BOB][v], BOB, v))
                    parent[BOB][v] = u

    # Kto dojechał do ostatniego wierzchołka
    ends_with = -1
    if dist[ALICE][end] < dist[BOB][end]:
        ends_with = ALICE
    else:
        ends_with = BOB

    final_dist = dist[ends_with][end]
    final_path = []

    # Tworzymy ścieżkę z tablicy parent naprzemiennie
    v = end
    while v != start:
        final_path.append(v)
        v = parent[ends_with][v]
        ends_with = 1-ends_with

    final_path.append(start)

    final_path.reverse()

    return final_dist, final_path


# A --100-- B --100-- E
#          / \
#         1   1
#        /     \
#       C --1-- D
G1 = [
    [(1, 100)],
    [(0, 100), (2, 1), (3, 1), (4, 100)],
    [(1, 1), (3, 1)],
    [(2, 1), (1, 1)],
    [(1, 100)],
]
answ1 = rozwiazanie(G1, 0, 4)
print("G1: długość:", answ1[0], "trasa:", answ1[1])

# A --7-- C --9-- D
#  \     /
#   9   6
#    \ /
#     B
G2 = [
    [(1, 9), (2, 7)],
    [(0, 9), (2, 6)],
    [(0, 7), (1, 6), (3, 9)],
    [(2, 9)],
]
answ2 = rozwiazanie(G2, 0, 3)
print("G2: długość:", answ2[0], "trasa:", answ2[1])


# Testowanie losowych grafów brute forcem
def print_graph(G):
    for v in range(len(G)):
        print(v, end=" -> ")
        for u, d in G[v]:
            print(u, "[", d, "]", sep="", end="   ")
        print()


def generate_graph(number_of_v):
    M = [([-1] * number_of_v) for _ in range(number_of_v)]

    for i in range(1, number_of_v):
        d = randint(0, 9)
        M[i-1][i] = d
        M[i][i-1] = d

    for _ in range(number_of_v):
        a = randint(0, number_of_v-1)
        b = randint(0, number_of_v-1)
        d = randint(0, 9)
        M[a][b] = d
        M[b][a] = d

    E = [[] for _ in range(number_of_v)]

    for v in range(number_of_v):
        for u in range(number_of_v):
            if u != v and M[v][u] != -1:
                E[v].append((u, M[v][u]))

    return E


def brute_force(G, v, target, visited, who, dist):
    if v == target:
        return dist

    mn = 9999999
    if not visited[who][v]:
        visited[who][v] = True
        for u, d in G[v]:
            mn = min(mn, brute_force(G, u, target,
                                     visited, 1-who, dist + d * who))
        visited[who][v] = False

    return mn


def check_with_brute(G):
    visited = ([False] * len(G), [False] * len(G))
    ans = min(brute_force(G, 0, len(G)-1, visited, 0, 0),
              brute_force(G, 0, len(G)-1, visited, 1, 0))

    ans2 = rozwiazanie(G, 0, len(G)-1)[0]

    if ans != ans2:
        print(ans, ans2)
        print_graph(G)


check_with_brute(G1)
check_with_brute(G2)

for _ in range(50):
    # seed(42)
    G = generate_graph(10)
    check_with_brute(G)