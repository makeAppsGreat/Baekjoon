"""
    15552번: 빠른 A+B
    Create by Kim Gayoun on 2022-03-22
"""
import sys


if __name__ == "__main__":
    result = ""

    T = int(sys.stdin.readline())
    for x in range(T):
        i = sys.stdin.readline().split()
        result += "{}\n".format(int(i[0]) + int(i[1]))


    print(result)
