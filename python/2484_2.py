"""
    2484번: 주사위 네개
    Create by Kim Gayoun on 2022-04-27
"""
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    top = -1

    for _ in range(N):
        dice = list( map(int, input().split()) )
        mem, prize = dict(), 0

        for d in dice:
            if not d in mem: mem[d] = 1
            else: mem[d] = mem[d] + 1

        
        keys = list(mem.keys())
        if len(mem) == 1: prize = 50000 + 5000 * keys[0]
        elif len(mem) == 2:
            if mem[keys[0]] != 2:
                if mem[keys[0]] == 3: prize = 10000 + 1000 * keys[0]
                else: prize = 10000 + 1000 * keys[1]
            else: prize = 2000 + 500 * keys[0] + 500 * keys[1]
        elif len(mem) == 3:
            if mem[keys[0]] == 2: prize = 1000 + 100 * keys[0]
            elif mem[keys[1]] == 2: prize = 1000 + 100 * keys[1]
            else: prize = 1000 + 100 * keys[2]
        else: prize = 100 * max(keys)

        if prize > top: top = prize
        print(mem, keys, prize)


    print(top)





