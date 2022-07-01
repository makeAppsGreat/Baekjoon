"""
    7569번: 토마토
    Create by Kim Gayoun on 2022-07-01
"""
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    M, N, H = map(int, input().split())
    G, Q, p = list(), list(), 0 # graph, queue, point of queue

    for _ in range(N * H): G += list( map(int, input().split()) )
    for i, T in enumerate(G):
        if T == 1: Q.append(i)


    # do travel
    if len(Q) == 0: print(-1)
    else:
        level, pnode = -1, Q[-1]
        while len(Q) > p:
            print(Q[p], level, pnode, Q, "\n")
            for k in range(H):
                for j in range(N):
                    for i in range(M): print(G[i + M * j + M * N * k], end=" ")
                    print("")
                print("")

            i = Q[p]
            p += 1
            
            # upper
            # if i + M * N < M * N * H and G[i + M * N] == 0:
            if i < M * N * (H - 1) and G[i + M * N] == 0:
                G[i + M * N] = 1
                Q.append(i + M * N)
            # lower
            if i >= M * N and G[i - M * N] == 0:
                G[i - M * N] = 1
                Q.append(i - M * N)
            # up
            if (i % (M * N)) < M * (N - 1) and G[i + M] == 0:
                G[i + M] = 1
                Q.append(i + M)
            # down
            if (i % (M * N)) >= M and G[i - M] == 0:
                G[i - M] = 1
                Q.append(i - M)
            # left
            if ((i % (M * N)) + 1) % M != 0  and G[i + 1] == 0:
                G[i + 1] = 1
                Q.append(i + 1)
            # right
            if (i % (M * N)) % M != 0  and G[i - 1] == 0:
                G[i - 1] = 1
                Q.append(i - 1)
            

            if i == pnode:
                level += 1
                pnode = Q[-1]
            print(i, level, pnode, Q)
            print("=" * 80)


        """
        if 0 in G: print(-1, Q, end="\n\n")
        else: print(level, Q, end="\n\n")
        for k in range(H):
            for j in range(N):
                for i in range(M): print(G[i + M * j + M * N * k], end=" ")
                print("")
            print("")
        """
        if 0 in G: print(-1)
        else: print(level)

