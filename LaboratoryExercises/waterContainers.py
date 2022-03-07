def containers(T, V):
    n = len(T)
    Y = [0] * (2 * n)

    for i in range(n):
        Y[i] = T[i][1]
        Y[i + n] = T[i][3]

    Y.sort()

    tmp_container = 0
    l = 0
    r = 2 * n - 1
    while l <= r:
        m = (l + r) // 2
        y = Y[m]
        V2 = 0
        container = 0
        for x1, y1, x2, y2 in T:
            if y1 < y and y2 <= y:
                V2 += (x2 - x1) * (y2 - y1)
                container += 1
            elif y1 < y:
                V2 += (x2 - x1) * (y - y1)

        if V2 < V:
            tmp_container = container
            l = m + 1
        elif V2 > V:
            r = m - 1
        else:
            tmp_container = container
            break
    return tmp_container


T = [(0, 4, 4, 10), (5, 0, 8, 3), (9, 2, 12, 5), (6, 5, 8, 7)]
V = 46
# dla V = 47 res 4
# dla V = 37 res 3
# dla V = 22 res 2
# dla V = 13 res 1
# dla V = 12 res 1
# dla V = 11 res 0

print(containers(T, V))
