"""
    14681번: 사분면 고르기
    Create by Kim Gayoun on 2022-05-26
"""
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    x = int(input())
    y = int(input())

    if x > 0:
        if y > 0: print(1)
        else: print(4)
    else:
        if y > 0: print(2)
        else: print(3)

