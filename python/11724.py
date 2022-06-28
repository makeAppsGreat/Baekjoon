"""
    11724번: 연결 요소의 개수
    Create by Kim Gayoun on 2022-06-28
"""
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N, M = map(int, input().split())
    G = [ [ 0 ] * (N + 1) for _ in range(N + 1) ]
    link = list()

    for _ in range(M):
        u, v = map(int, input().split())
        G[u][v] = 1
        G[v][u] = 1

    
    # do travel
    q, p = list(), 0 # queue, point of queue
    while True:
        if len(q) == p and len(q) < N:
            for i in range(G[0][0] + 1, N + 1):
                if i not in q:
                    q.append(i)
                    G[0][0] = i
                    break
        elif len(q) == p and len(q) == N: break


        cnode = q[p]; p += 1
        if cnode == G[0][0] and cnode not in link: link.append(cnode)
        for i in range(1, N + 1):
            if G[cnode][i] == 1 and i not in q:
                q.append(i)



    print(len(link))

