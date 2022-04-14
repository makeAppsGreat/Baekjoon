"""
    1316번: 그룹 단어 체커 
    Create by Kim Gayoun on 2022-04-15
"""
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    result = N

    for _ in range(N):
        line = input()[:-1]
        alpha, last = [ 0 for _ in range(27) ], -1


        for i in range(len(line)):
            A = ord(line[i:i + 1]) - 97

            if A != last:
                if alpha[A] == 0:
                    alpha[last] = -1
                    last = A
                else:
                    result = result - 1
                    break

    
    print(result)

