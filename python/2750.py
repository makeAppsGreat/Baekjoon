"""
    2750번: 수 정렬하기
    Create by Kim Gayoun on 2022-04-19
"""
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    array = list()

    for _ in range(N): array.append(int(input()))
    array.sort()

    
    result = ""
    for num in array: result += "{}\n".format(num)
    print(result)

