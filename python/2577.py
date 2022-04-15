"""
    2577번: 숫자의 개수
    Create by Kim Gayoun on 2022-04-16
"""


if __name__ == "__main__":
    A, B, C = int(input()), int(input()), int(input())
    x = A * B * C
    num = [ 0 for _ in range(10) ]

    while x > 0:
        num[x % 10] += 1
        x = x // 10


    for n in num: print(n)

