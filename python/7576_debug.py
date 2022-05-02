"""
    7576번: 토마토
    Created by Kim Gayoun on 2022-04-18
"""
import sys
import time
input = sys.stdin.readline


if __name__ == "__main__":
    timer = time.time()
    M, N = map(int, input().split())
    T, q = list(), list()
    goal, cnt = None, 0
    
    t = time.time()
    print("1\t{:0.3f}".format((t - timer) * 1000 * 1000))
    timer = t

    for _ in range(N): T += list( map(int, input().split()) )

    t = time.time()
    print("2\t{:0.3f}".format((t - timer) * 1000 * 1000))
    timer = t

    for i, t in enumerate(T):
        if t == 1:
            q.append(i)
            cnt = cnt + 1
    # goal = T.count(1) + T.count(0)
    goal = cnt + T.count(0)

    t = time.time()
    print("3\t{:0.3f}\n".format((t - timer) * 1000 * 1000))
    timer = t



    if len(q) > 0:
        level, fnode, lnode = 0, q[0], q[-1]
        t1, t2, t3 = 0, 0, 0
        while goal > cnt:
            """
            print("\n\n", level, fnode, lnode, q)
            for i in range(N):
                for j in range(M): print("{:2}".format(T[M * i + j]), end=' ')
                print("")
            """
            tt = time.time()
            # i = q.pop(0)
            i = q[0]
            del q[0]
            t1 += time.time() - tt
    
            tt = time.time()
            if i >= M and T[i - M] == 0: # up
                T[i - M] = 1
                q.append(i - M)
                q += [ i - M ]
                cnt = cnt + 1
            if i < M * (N - 1) and T[i + M] == 0: # down
                T[i + M] = 1
                q.append(i + M)
                q += [i + M]
                cnt = cnt + 1
            if i % M != 0 and T[i - 1] == 0: # left
                T[i - 1] = 1
                q.append(i - 1)
                q += [ i - 1 ]
                cnt = cnt + 1
            if (i + 1) % M != 0 and T[i + 1] == 0: # right
                T[i + 1] = 1
                q.append(i + 1)
                q += [i + 1]
                cnt = cnt + 1
            t2 += time.time() - tt


            tt = time.time()
            if i == fnode: level = level + 1
            if len(q) == 0:
                level = -1
                break
            elif i == lnode:
                fnode = q[0]
                lnode = q[-1]
            t3 += time.time() - tt

        print("3.1\t{:10.3f}".format(t1 * 1000 * 1000))
        print("3.2\t{:10.3f}".format(t2 * 1000 * 1000))
        print("3.3\t{:10.3f}\n".format(t3 * 1000 * 1000))
        print("3.10\t{:10.3f}\n".format((t1+ t2+ t3) * 1000 * 1000))
    
        """
        print("\n", M, N)
        for i in range(N):
            for j in range(M): print("{:2}".format(T[M * i + j]), end=' ')
            print("")
        print("\n", q) """
        print(level)
    else: print(-1)


    t = time.time()
    print("\n4\t{:0.3f}\n".format((t - timer) * 1000 * 1000))
    timer = t

