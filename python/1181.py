"""
    1181번: 단어 정렬
    Create by Kim Gayoun on 2022-05-16
"""
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    __dict = dict()


    for _ in range(N):
        line = input()[:-1]
        __len = len(line)

        if not __len in __dict:
            __dict[__len] = set()
            __dict[__len].add(line)
        else: __dict[__len].add(line)

    keys = list(__dict.keys())
    keys.sort()
    for k in keys:
        values = list(__dict[k])
        values.sort()

        for v in values: print(v)


