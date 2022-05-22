"""
    1920번: 수 찾기
    Create by Kim Gayoun on 2022-05-22
"""
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = input()
    A = dict()

    __input = list( map(int, input().split()) )
    for a in __input: A[a] = None


    M = input()
    __input = list( map(int, input().split()) )

    result = ""
    for i in __input:
        if i in A: result += "1\n"
        else: result += "0\n"


    print(result)

