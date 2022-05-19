"""
    10814번: 나이순 정렬
    Create by Kim Gayoun on 2022-05-19
"""
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    __dict = dict()

    for _ in range(N):
        age, name = map(str, input().split())
        age = int(age)

        if age in __dict: __dict[age].append(name)
        else:
            __dict[age] = list()
            __dict[age].append(name)

    keys = list(__dict.keys())
    keys.sort()

    result = ""
    for k in keys:
        for name in __dict[k]:
            result += "{} {}\n".format(k, name)


    print(result)

