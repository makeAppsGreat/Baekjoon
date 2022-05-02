"""
    7576번: 토마토
    Created by Kim Gayoun on 2022-04-15
"""
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    M, N = map(int, input().split())
    T, G = list(), dict()
    goal = None

    for _ in range(N): T += list( map(int, input().split()) )
    goal = T.count(1) + T.count(0)


    G[-1] = list()
    for i, t in enumerate(T):
        if t == 1: G[-1].append(i)


    idx, last = -1, T.count(1)
    while last <= goal:
        for i in G[idx]:
            G[i] = list()

            if i >= M and T[i - M] == 0: # up
                T[i - M] = 1
                G[i].append(i - M)
            if i <= M * (N - 1) and T[i + M] == 0: # down
                T[i + M] = 1
                G[i].append(i + M)
            if (i + 1) % M == 0 and T[i - 1] == 0: # left
                T[i - 1] = 1
                G[i].append(i - 1)
            if i % M == 0 and T[i + 1] == 0: # right
                T[i + 1] = 1
                G[i].append(i + 1)

        if last == T.count(1): break
        else: last = T.count(1)
        break



    print(M, N)
    for i in range(N):
        for j in range(M): print("{:2}".format(T[M * i + j]), end=' ')
        print("")
    print("\n", G)
