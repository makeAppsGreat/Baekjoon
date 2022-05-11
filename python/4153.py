"""
    4153번: 
    Create by Kim Gayoun on 2022-05-11
"""
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    while True:
        l = list( map(int, input().split()) )

        if sum(l) == 0: break
        else:
            l.sort()
            if l[2] ** 2 == l[0] ** 2 + l[1] ** 2: print("right")
            else: print("wrong")


