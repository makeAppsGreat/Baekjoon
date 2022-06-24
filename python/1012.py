"""
    1012번: 유기통 배추
    Create by Kim Gayoun on 2022-06-24
"""
import sys
input = sys.stdin.readline


def pGraph(M, N, G):
    for j in range(N):
        print("{}\t".format(N - (j + 1)), end="")
        for i in range(M): print(G[i + M * (N - (j + 1))], end=" ")
        print("")

    print("\n \t", end="")
    for i in range(M): print(i, end=" ")
    print("")

def pQueue(M, N, q):
    for i in range(len(q)): print("({}, {})".format(q[i] % M, q[i] // M), end=" ")
    print("")

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        M, N, K = map(int, input().split())
        G = [ 0 ] * (M * N)
        q, p = list(), 0 # queue, pointer of queue

        for _ in range(K):
            X, Y = map(int, input().split())
            G[X + M * Y] = 1


        # main
        i, pnode, cnt = 0, -1, 0
        while i < M * N:
            """
            print("\n{}\t({}, {})\t({}, {})".format(i, pnode % M, pnode // M, i % M, i // M))
            print("{} {}".format(p, len(q)), end="\t")
            pQueue(M, N, q)
            pGraph(M, N, G)
            """

            if G[i] == 1:
                G[i] = 0
                if pnode < 0:
                    pnode = i
                    cnt += 1

                # up
                if i + M < M * N and G[i + M] == 1 and (i + M) not in q: q.append(i + M)
                # down
                if i - M >= 0 and G[i - M] == 1 and (i - M) not in q: q.append(i - M)
                # left
                if (i + 1) % M != 0 and G[i + 1] == 1 and (i + 1) not in q: q.append(i + 1)
                # right
                if i % M != 0 and G[i - 1] == 1 and (i - 1) not in q: q.append(i - 1)
                
                if p < len(q):
                    i = q[p]
                    p += 1
                else:
                    i = pnode + 1
                    pnode = -1
            else: i += 1


        print(cnt)

