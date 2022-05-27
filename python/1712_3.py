"""
    1712번: 손익분기점
    Create by Kim Gayoun on 2022-03-26
"""
if __name__ == "__main__":
    A, B, C = map(int, input().split())

    if B >= C: print(-1)
    else:
        BEP = int(A / (C - B)) + 1
        print(BEP)
