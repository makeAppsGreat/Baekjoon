"""
    1085번: 직사각형에서 탈출
    Create by Kim Gayoun on 2022-05-12
"""
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    x, y, w, h = map(int, input().split())
    __min = x

    if __min > y: __min = y
    if __min > (w - x): __min = w - x
    if __min > (h - y): __min = h - y


    print(__min)

