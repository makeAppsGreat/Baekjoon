"""
    2839번: 설탕 배달
    Create by Kim Gayoun on 2022-03-28
"""
# import time


if __name__ == "__main__":
    N = int(input())
    l, k = list(), 0


    try:
        while True:
            w = l.count(3) * 3 + l.count(5) * 5

            if w == N: break
            elif w < N:
                l.append(5)
            else:
                if l.pop() == 5:
                    k = 0
                    l.append(3)
                else:
                    k = k + 1

                    for i in range(k): l[len(l) - (k + 1)] = 3
                    l.append(3)

            # print("{}\t{}".format(w, l))
            # time.sleep(0.4)



        print(len(l))
    except:
        print(-1)
