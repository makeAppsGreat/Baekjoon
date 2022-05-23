"""
    10845번: 큐
    Create by Kim Gayoun on 2022-05-23
"""
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    queue, p = list(), 0

    for _ in range(N):
        cmd = input().split()

        if cmd[0] == "push": queue.append(cmd[1])
        elif cmd[0] == "pop":
            if p < len(queue):
                print(queue[p])
                p += 1
            else: print(-1)
        elif cmd[0] == "size": print(len(queue) - p)
        elif cmd[0] == "empty":
            if p < len(queue): print(0)
            else: print(1)
        elif cmd[0] == "top":
            if p < len(queue): print(queue[-1])
            else: print(-1)
        else:
            if p < len(queue):
                if cmd[0] == "front": print(queue[p])
                elif cmd[0] == "back": print(queue[-1])
            else: print(-1)

