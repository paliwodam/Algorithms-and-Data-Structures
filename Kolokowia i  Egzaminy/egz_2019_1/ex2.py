def opt_sum(tab):
    n = len(tab)
    new_tab = [tab[i] for i in range(n)]
    res = []

    max_r = 0
    while len(new_tab) > 1:
        x = 0
        y = 1
        for i in range(2, len(new_tab)):
            if abs(new_tab[i-1] + new_tab[i]) < abs(new_tab[x] + new_tab[y]):
                x = i-1
                y = i
        if abs(new_tab[x] + new_tab[y]) > max_r:
            max_r = abs(new_tab[x] + new_tab[y])

        res.append((new_tab[x], new_tab[y]))
        new_tab[y] += new_tab[x]
        new_tab.pop(x)
    # print(res)
    return max_r


T = [-10, -9, 4, -4, 14, 3, -4, 2, 18, -19, 9]
opt_sum(T)
