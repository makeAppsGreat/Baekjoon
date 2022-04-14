

if __name__ == "__main__":
    i = input().split()
    i.append(input())


    h = int(i[0]) * 60
    m = int(i[1])
    t = int(i[2])


    x = (h + m + t) / 60 % 24
    y = (h + m + t) % 60


    print("{} {}".format(x, y))




