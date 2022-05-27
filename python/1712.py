"""
    1712번: 손익분기점
    Create by Kim Gayoun on 2022-03-24
    
    $ time echo 2100000000 9 10 | python3 1712_1.py
    2100000001
    echo 2100000000 9 10  0.00s user 0.00s system 35% cpu 0.002 total
    python3 1712_1.py  785.75s user 0.01s system 99% cpu 13:09.71 total
"""
if __name__ == "__main__":
    A, B, C = map(int, input().split())
    BEP = 0

    while True:
        BEP = BEP + 1
        if (A + B * BEP) < (C * BEP): break

    print(BEP)

