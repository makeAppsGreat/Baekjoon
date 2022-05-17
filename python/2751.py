"""
    2751번: 수 정렬하기 2
    Create by Kim Gayoun on 2022-05-17
"""
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    nums = list()

    for _ in range(N): nums.append(int(input()))
    nums.sort()

    result = ""
    for n in nums: result += "{}\n".format(n)


    print(result)

