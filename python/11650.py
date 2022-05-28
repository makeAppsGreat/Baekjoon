"""
    11650번: 좌표 정렬하기
    Create by Kim Gayoun on 2022-05-28
"""
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    __dict = dict()

    for _ in range(N):
        x, y = map(int, input().split())

        if not x in __dict:
            __dict[x] = list()
            __dict[x].append(y)
        else: __dict[x].append(y)

    
    __list = list(__dict.keys())
    __list.sort()
    result = ""
    for x in __list:
        __dict[x].sort()

        for y in __dict[x]: result += "{} {}\n".format(x, y)


    print(result)


