"""
    10828번: 스택
    Create by Kim Gayoun on 2022-05-21
"""
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    stack = list();

    for _ in range(N):
        cmd = input().split()

        if cmd[0] == "push": stack.append(cmd[1])
        elif cmd[0] == "pop":
            if len(stack) > 0: print(stack.pop())
            else: print(-1)
        elif cmd[0] == "size": print(len(stack))
        elif cmd[0] == "empty":
            if len(stack) > 0: print(0)
            else: print(1)
        elif cmd[0] == "top":
            if len(stack) > 0: print(stack[-1])
            else: print(-1)

