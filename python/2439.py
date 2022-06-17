"""
    2439번: 별 찍기 - 2
    Create by Kim Gayoun on 2022-06-17
"""
N = int(input())
for i in range(1, N + 1): print("{:>{}}".format("*" * i, N))

