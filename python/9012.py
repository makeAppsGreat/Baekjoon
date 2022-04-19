"""
    9012번: 괄호
    Create by Kim Gayoun on 2022-04-15
"""
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        line, cur = list( input().strip() ), 0

        for char in line:
            if char == "(": cur += 1
            else: cur -= 1

            if cur < 0: break

        if cur == 0: print("YES")
        else: print("NO")




