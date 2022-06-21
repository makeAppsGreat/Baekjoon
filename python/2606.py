"""
    2606번: 바이러스
    Create by Kim Gayoun on 2022-06-21
"""
import sys
input = sys.stdin.readline


def doBFS(G, V):
    result, queue = list(), list()
    p = 0 # pointer of queue
    cnode = V

    queue.append(cnode)
    while len(queue) > p:
        cnode = queue[p]; p += 1

        if cnode not in result:
            result.append(cnode)
            G[0][cnode] = 1

        for i in range(1, N + 1):
            if G[0][i] == 0 and G[cnode][i] == 1: queue.append(i)


    # print(*result)
    print(len(result) - 1)


if __name__ == "__main__":
    N = int(input())
    M = int(input())
    G = [ [ 0 ] * (N + 1) for _ in range(N + 1) ]


    for _ in range(M):
        A, B = map(int, input().split())
        G[A][B] = 1
        G[B][A] = 1


    doBFS(G, 1)

