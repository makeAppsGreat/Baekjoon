"""
    4948번: 베르트랑 공준
    Create by Kim Gayoun on 2022-04-04
"""
if __name__ == "__main__":
    n = 123_456 * 2
    l = [ True for i in range(n * 2 + 1) ]
    l[0] = False
    l[1] = False

    for i in range(2, int((n * 2) ** 0.5) + 1):
        if l[i] == False: continue
        else:
            j = 2

            while True:
                if i * j > n * 2: break
                else:
                    l[i * j] = False
                    j = j + 1


    while True:
        n = int(input())

        if n == 0: break
        else:
            result = 0
            for i in range(n + 1, n * 2 + 1):
                if l[i] == True: result += 1
            print(result)
