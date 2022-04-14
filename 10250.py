

if __name__ == "__main__":
    T = int(input())
    
    for t in range(T):
        H, W, N = map(int, input().split())
        h, w = 0, 0

        if (N % H) == 0:
            h = H
            w = N // H
        else:
            h = N % H
            w = N // H + 1


        print("{}{:02}".format(h, w))

