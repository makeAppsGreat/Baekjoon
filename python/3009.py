

if __name__ == "__main__":
    # min : 2, max : 999
    x_max, x_min, y_max, y_min = -1, 1000, -1, 1000
    p, sq = list(), [False, False, False, False]



    for i in range(3):
        p.append(list(map(int, input().split())))
        if x_max < p[i][0]: x_max = p[i][0]
        if x_min > p[i][0]: x_min = p[i][0]
        if y_max < p[i][1]: y_max = p[i][1]
        if y_min > p[i][1]: y_min = p[i][1]

    for __p in p:
        if x_min == __p[0] and y_min == __p[1]: sq[0] = True
        if x_min == __p[0] and y_max == __p[1]: sq[1] = True
        if x_max == __p[0] and y_max == __p[1]: sq[2] = True
        if x_max == __p[0] and y_min == __p[1]: sq[3] = True

    i = sq.index(False)
    if i == 0: print("{} {}".format(x_min, y_min))
    elif i == 1: print("{} {}".format(x_min, y_max))
    elif i == 2: print("{} {}".format(x_max, y_max))
    else: print("{} {}".format(x_max, y_min))

