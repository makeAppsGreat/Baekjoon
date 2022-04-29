"""
    1406번: 에디터
    Create by Kim Gayoun on 2022-04-28
"""
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    note = input()[:-1]
    M = int(input())

    cur = len(note)
    for _ in range(M):
        cmd = input().split()

        if cmd[0] == "L":
            if cur > 0: cur -= 1
        elif cmd[0] == "D":
            if cur < len(note): cur += 1
        elif cmd[0] == "B":
            # print(cur, len(note), note[:cur], note[cur:], end='\t')
            if cur > 0:
                print(note[: cur - 1], note[cur:], end='\t')
                note = note[: cur - 1] + note[cur:]
                cur -= 1
        else:
            if cur == 0: note = cmd[1] + note
            else: note = note[:cur] + cmd[1] + note[cur:]
            cur += 1

        print(cmd[0], note)


    print(note)

