from math import inf


def merge_p(p):
    new_p = []
    prev_x = p[0][0]
    prev_y = p[0][1]

    for i in range(1, len(p)):
        x = p[i][0]
        y = p[i][1]
        if prev_y == x:
            prev_y = y
        else:
            new_p.append((prev_x, prev_y))
            prev_x = x
            prev_y = y

    new_p.append((prev_x, prev_y))
    return new_p


def tower(T):
    n = len(T)
    T2 = [None] * n

    for i in range(n):
        T2[i] = (T[i][0], T[i][1], i)

    T2 = sorted(T2, key=lambda t: t[1], reverse=True)
    T2 = sorted(T2, key=lambda t: t[0])

    #  tablica indeksów
    res = []
    # ilość pozostałych do położenia klocków
    k = n
    p = [(-inf, inf)]

    while k > 0:
        # koniec ostatniego klocka
        end = 0
        # nowe przedziały
        p2 = []
        # czy cokolwiek zmieniliśmy
        tmp = False

        for i in range(n):
            for j in range(len(p)):
                x, y = p[j][0], p[j][1]
                if T2[i] is not None and T2[i][0] >= end and T2[i][0] >= x and T[i][1] <= y:
                    # położyliśmy klocek
                    tmp = True
                    res.append(T2[i][2] + 1)
                    # dodajemy przedział do nowej wysokości
                    p2.append((T2[i][0], T2[i][1]))
                    end = T2[i][1]
                    # oznaczamy, że klocek wzięty
                    T2[i] = None
                    k -= 1
        if not tmp:
            break
        # sumujemy przedziały
        p = merge_p(p2)

    if len(res) != n:
        return False
    else:
        return res


T = [(2, 4), (5, 7), (3, 6), (4, 5)]
print(tower(T))