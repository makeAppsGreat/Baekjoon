"""
    1712번: 손익분기점
    Create by Kim Gayoun on 2022-03-25
"""
import time


if __name__ == "__main__":
    A, B, C = map(int, input().split())


    if B >= C: print(-1)
    else:
        BEP, i = 0, 1

        while True:
            x = A + B * BEP
            y = C * BEP


            # print("{}\t{}".format(i , BEP))
            if x < y: # down
                i = i // 2
                BEP = BEP - i
            elif x > y: # up
                i = i * 2
                BEP = BEP + i
            else:
                BEP = BEP + 1
                break


        print(BEP)

