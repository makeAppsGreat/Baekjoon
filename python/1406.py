"""
    1406번: 에디터
    Create by Kim Gayoun on 2022-04-19
"""
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    note = input().strip()
    N = int(input())


    cur = len(note)
    for _ in range(N):
        cmd = input().split()

        print("{} {}\t{}\t{}\t".format(len(note), cur, cmd[0], note), end="")
        if len(cmd) > 1:
            note = note[:cur] + cmd[1] + note[cur:]
            cur += 1
        elif cmd[0] == "D" and len(note) > cur: cur += 1
        elif cmd[0] in [ "L", "B" ] and cur != 0:
            if cmd[0] == "B": note = note[:cur - 1] + note[cur:]
            cur -= 1

        print(cur, note[:cur], note[cur:])





    print("\n\n", note)


