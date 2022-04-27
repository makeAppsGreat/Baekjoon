"""
    2484번: 주사위 네개
    Create by Kim Gayoun on 2022-04-22
"""
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    top = -1

    for _ in range(N):
        dice = list( map(int, input().split()) )
        mem, prize = dict(), None

        for d in dice:
            if not d in mem: mem[d] = 1
            else: mem[d] = mem[d] + 1

        keys = list(mem.keys())
        if len(mem) == 1: prize = 50000 + keys[0] * 5000
        elif len(mem) == 2:
            if mem[keys[0]] == 1 or mem[keys[1]] == 1:
                if keys[0] == 3: prize = 10000 + keys[0] * 1000
                else: prize = 10000 + keys[1] * 1000
            else: prize = 2000 + keys[0] * 500 + keys[1] * 500
        elif len(mem) == 3:
            if mem[keys[0]] == 2: prize = 1000 + keys[0] * 100
            elif mem[keys[1]] == 2: prize = 1000 + keys[1] * 100
            else: prize = 1000 + keys[2] * 100
        else: prize = max(keys) * 100

        print(prize)
        if prize > top: top = prize


    print(top)

