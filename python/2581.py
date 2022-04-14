

if __name__ == "__main__":
    M = int(input())
    N = int(input())
    p = list()

    if M == 1: M = 2
    for i in range(M, N + 1): p.append(i)
    print(len(p), p)
    for i in range(2, int(N ** (1/2)) + 1):
        print("\n\n")
        j = M // i
        if j == 0: j = 1

        try:
            print(j, p.index(j * i))
            if j < 2 and p.index(j * i) >= 0: j = 2
        except: pass

        while True:
            k = i * j
            
            print(i, j, k, N)
            if k > N: break
            else:
                try: p.remove(k)
                except: pass
                j = j + 1
                print(len(p), p)
        if len(p) == 0: break


    if len(p) > 0: print("{}\n{}".format(sum(p), p[0]))
    else: print("-1")
        

