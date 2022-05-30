"""
    1946번: 신입 사원
    Create by Kim Gayoun on 2022-04-06
"""
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, rank       = int(input()), list()
        __min, result = 200_000, 0


        for _ in range(N):
            x, y = map(int, input().split())
            rank.append((x, y))

        rank.sort(key=lambda k:k[0])
    
        for r in rank:
            if r[1] < __min:
                result += 1
                __min = r[1]

        
        print(result)

