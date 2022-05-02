"""
    7576번: 토마토
    Created by Kim Gayoun on 2022-04-19
"""
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    M, N = map(int, input().split())
    T, q = list(), list() # tree, queue
    goal, cnt = 0, 0

    for _ in range(N): T += list( map(int, input().split()) )

    for i, t in enumerate(T):
        if t == 0: goal = goal + 1
        elif t == 1:
            q.append(i)
            cnt = cnt + 1
    # goal = T.count(1) + T.count(0)
    # goal = cnt + T.count(0)
    goal = goal + cnt


    if len(q) > 0:
        level, fnode, lnode = 0, q[0], q[-1]
        while goal > cnt:
            # i = q.pop(0)
            i = q[0]
            del q[0]
    
            if i >= M and T[i - M] == 0: # up
                T[i - M] = 1
                q.append(i - M)
                cnt = cnt + 1
            if i < M * (N - 1) and T[i + M] == 0: # down
                T[i + M] = 1
                q.append(i + M)
                cnt = cnt + 1
            if i % M != 0 and T[i - 1] == 0: # left
                T[i - 1] = 1
                q.append(i - 1)
                cnt = cnt + 1
            if (i + 1) % M != 0 and T[i + 1] == 0: # right
                T[i + 1] = 1
                q.append(i + 1)
                cnt = cnt + 1

            if i == fnode: level = level + 1
            if len(q) == 0:
                level = -1
                break
            elif i == lnode:
                fnode = q[0]
                lnode = q[-1]

            for i in range(N):
                for j in range(M): print("{:2}".format(T[M * i + j]), end=' ')
                print("")
            print("\n")


        print(level)
    else: print(-1)

