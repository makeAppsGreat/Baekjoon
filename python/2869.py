"""
    2869번: 달팽이는 올라가고 싶다
    Create by Kim Gayoun on 2022-03-27
"""
import math


if __name__ == "__main__":
    A, B, V = map(int, input().split())
    print(math.ceil((V - B) / (A - B)))

