"""
    2562번: 최댓값
    Create by Kim Gayoun on 2022-04-10
"""
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    l = list()
    for _ in range(9): l.append(int(input()))

    print(max(l))
    print(l.index(max(l)) + 1)
