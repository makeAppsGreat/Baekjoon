"""
    1260번: DFS와 BFS
    Create by Kim Gayoun on 2022-06-20
"""
import sys
input = sys.stdin.readline


def doDFS(G, V):
    result, stack = list(), list()
    cnode = pnode = V
    
    result.append(cnode)
    G[0][cnode] = 1

    while True:
        for i in range(1, N + 1):
            if G[0][i] == 0 and G[cnode][i] == 1:
                result.append(i)
                G[0][i] = 1

                stack.append(cnode)
                cnode = i
                break


        if len(stack) == 0: break
        else:
            if pnode == cnode:
                cnode = stack.pop()
                pnode = cnode
            else: pnode = cnode


    print(*result)


def doBFS(G, V):
    result, queue = list(), list()
    p = 0 # pointer of queue
    cnode = pnode = V

    queue.append(cnode)
    while len(queue) > p:
        cnode = queue[p]; p += 1

        if cnode not in result:
            result.append(cnode)
            G[0][cnode] = 1

        for i in range(1, N + 1):
            if G[0][i] == 0 and G[cnode][i] == 1: queue.append(i)


    print(*result)



if __name__ == "__main__":
    N, M, V = map(int, input().split())
    G = [ [ 0 ] * (N + 1) for _ in range(N + 1) ]


    for _ in range(M):
        A, B = map(int, input().split())
        G[A][B] = 1
        G[B][A] = 1


    doDFS(G, V); G[0] = [ 0 ] * (N + 1)
    doBFS(G, V)

    

