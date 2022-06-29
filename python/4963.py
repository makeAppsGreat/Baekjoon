"""
    4963번: 섬의 개수
    Create by Kim Gayoun on 2022-06-29
"""
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    while True:
        w, h = map(int, input().split())

        if w == 0 and h == 0: break
        else:
            G, cnt = list(), 0
            for _ in range(h): G += list( map(int, input().split()) )


            # do travel
            cnode, pnode = 0, -1
            q, p = list(), 0 # queue, point of queue
            while cnode < w * h:
                # print(cnode, p, q)

                if G[cnode] == 1:
                    G[cnode] = 0
                    if pnode < 0:
                        pnode = cnode
                        cnt += 1

                    # North
                    if cnode + w < w * h and G[cnode + w] == 1:
                        q.append(cnode + w)
                    # NE
                    if cnode + w + 1 < w * h and (cnode + 1) % w != 0 and G[cnode + w + 1] == 1:
                        q.append(cnode + w + 1)
                    # East
                    if (cnode + 1) % w != 0 and G[cnode + 1] == 1:
                        q.append(cnode + 1)
                    # SE
                    if cnode - w >= 0 and (cnode + 1) % w != 0 and G[cnode - w + 1] == 1:
                        q.append(cnode - w + 1)
                    # South
                    if cnode - w >= 0 and G[cnode - w] == 1:
                        q.append(cnode - w)
                    # SW
                    if cnode - w >= 0 and cnode % w != 0 and G[cnode - w - 1] == 1:
                        q.append(cnode - w - 1)
                    # West
                    if cnode % w != 0 and G[cnode - 1] == 1:
                        q.append(cnode - 1)
                    # NW
                    if cnode + w < w * h and cnode % w != 0 and G[cnode + w - 1] == 1:
                        q.append(cnode + w - 1)


                if len(q) > p:
                    cnode = q[p]
                    p += 1
                elif pnode >= 0:
                    cnode = pnode + 1
                    pnode = -1
                else: cnode += 1


            print(cnt)

