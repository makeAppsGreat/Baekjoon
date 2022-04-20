"""
    2738번: 행렬 덧셈
    Create by Kim Gayoun on 2022-04-15
"""
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N, M = map(int, input().split())
    m, result = list(), list()

    for _ in range(N * 2): m.append(list( map(int, input().split()) ))
    for i in range(N):
        result.append(list())
        for j in range(M): result[i].append(m[i][j] + m[i + N][j])
        print(*result[i])

