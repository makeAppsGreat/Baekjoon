"""
    2588번: 곱셈
    Create by Kim Gayoun on 2022-04-23
"""
A = int(input())
B = int(input())
print(A *(B % 10))
print(A * (B // 10 % 10))
print(A * (B // 100))
print(A * B)

