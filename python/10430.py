"""
    10430번: 나머지
    Create by Kim Gayoun on 2022-04-24
"""
A, B, C = map(int, input().split())
print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)

