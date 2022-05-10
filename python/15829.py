"""
    15829번: Hashing
    Create by Kim Gayoun on 2022-05-10
"""
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    L = int(input())
    line = list( input() )

    result = 0
    for i in range(L): result += (ord(line[i]) - 96) * (31 ** i)


    print(result % 1234567891)

