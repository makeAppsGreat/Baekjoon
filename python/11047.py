"""
    11047번: 동전 0
    Create by Kim Gayoun on 2022-04-09
"""
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N, K = map(int, input().split())
    A, result = list(), 0

    for _ in range(N): A.append( int(input()) )
    
    for i in range(N):
        if K == 0: break

        s = K // A[len(A) - (i + 1)]
        if s > 0:
            K      -= s * A[len(A) - (i + 1)]
            result += s


    print(result)

