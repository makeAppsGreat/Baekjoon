"""
    2480번: 주사위 세개
    Create by Kim Gayoun on 2022-06-22
"""
if __name__ == "__main__":
    A, B, C = map(int, input().split())

    if A == B and A == C: print(10000 + A * 1000)
    elif A != B and A != C and B != C:
        dice = [A, B, C]
        print(max(dice) * 100)
    else:
        if A == B or A == C: print(1000 + A * 100)
        else: print(1000 + B * 100)

