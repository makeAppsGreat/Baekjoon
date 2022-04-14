

if __name__ == "__main__":
    i = input().split()
    i.append(input())


    h = int(i[0]) * 60
    m = int(i[1])
    t = int(i[2])


    x = int( (h + m + t) / 60 )
    y = (h + m + t) % 60


    print("{} {}".format(x if x < 24 else (x - 24), y))




