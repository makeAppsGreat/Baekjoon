

if __name__ == "__main__":
    N = int(input())
    p = list(map(int, input().split()))


    try:
        p.remove(1)
        N = N - 1
    except: pass


    for x in p:
        for y in range(2, int(x ** (1/2)) + 1):
            # print("{} {} {} {}".format(x, y, x / y, x % y))
            if (x % y) == 0:
                N = N - 1
                break


    print(N)


