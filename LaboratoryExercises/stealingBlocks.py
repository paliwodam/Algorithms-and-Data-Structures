def steal(towers):
    # biggest blocks on top of each tower
    towers = [sorted(t, reverse=True) for t in towers]

    # heights of each tower
    H = [sum(t) for t in towers]

    winning_height = max(H)
    my_height = H[0]

    delta = winning_height - my_height

    while delta >= 0:
        print("Missing", delta, "height")
        best_tower = None
        best_delta = delta
        for tower_i in range(1, len(towers)):
            if len(towers[tower_i]) == 0:
                continue

            # steal biggest block from tower i
            H[tower_i] -= towers[tower_i][0]
            my_height += towers[tower_i][0]

            new_winning_height = max(H[1:])
            new_delta = new_winning_height - my_height

            if new_delta < best_delta:
                best_tower = tower_i
                best_delta = new_delta

            # put back block
            my_height -= towers[tower_i][0]
            H[tower_i] += towers[tower_i][0]

        print("Stole block", towers[best_tower][0], "from tower", best_tower)
        H[best_tower] -= towers[best_tower][0]
        my_height += towers[best_tower][0]
        towers[best_tower].pop(0)
        delta = best_delta


W = [[1, 1],
     [8],
     [5, 4]]

steal(W)