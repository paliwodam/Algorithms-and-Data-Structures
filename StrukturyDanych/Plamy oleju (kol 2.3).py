# Michał Gniadek

# Rozwiązanie zachłanne. Jedziemy do przodu aż skończy nam sie
# paliwo. Wtedy zbieramy ropę z największej plamy którą już
# mineliśmy. Zebranie jakiejkolwiek innej plamy tylko skróci
# zasięg.

# Dodatkowo jeśli jedną plamę można zebrać w dwóch miejscach
# to zakładamy że jest tylko we wcześniejszym (bo jeśli chcieliśmy
# ją zebrać później to i tak możemy wcześniej)

# O(mlogm) - każde pole trasy (jeśli ma plamę) zostanie dodane
# maksymalnie raz do priority queue i maksymalnie raz wyjęte

# from zad3testy import runtests
from queue import PriorityQueue


def get_size(T, N, x, y):
    if not (0 <= x < N and 0 <= y < N) or T[x][y] == 0:
        return 0

    val = T[x][y]
    T[x][y] = 0

    for (x_off, y_off) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        val += get_size(T, N, x+x_off, y+y_off)

    return val


def plan(T):
    N = len(T[0])
    R = [0] * N

    # Upraszczamy mapę to tablicy jednowymiarowej
    for x in range(N):
        R[x] = get_size(T, N, 0, x)

    out = []
    q = PriorityQueue(N)
    fuel = 0

    for i in range(N-1):
        if R[i] != 0:
            # Pythonowska priority queue zwraca najmniejszy element
            # a my potrzebujemy największego
            q.put((-R[i], i))

        if fuel == 0:
            (f, x) = q.get()
            fuel += -f
            out.append(x)

        fuel -= 1

    out.sort()
    return out


# runtests(plan)