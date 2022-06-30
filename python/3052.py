"""
    3052번: 나머지
    Create by Kim Gayoun on 2022-06-30
"""
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    D = dict()
    for _ in range(10): D[int(input()) % 42] = None


    print(len(list(D.keys())))

