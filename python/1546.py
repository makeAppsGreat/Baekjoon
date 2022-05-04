"""
    1546번: 평균
    Create by Kim Gayoun on 2022-05-04
"""
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    ss = list( map(int, input().split()) )
    sum_s, base = 0, max(ss)

    for s in ss: sum_s += s / base * 100


    print(sum_s / N)

