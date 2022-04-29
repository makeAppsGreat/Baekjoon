"""
    1406번: 에디터
    Create by Kim Gayoun on 2022-04-29
"""
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    note, buff = list( input()[:-1] ), list()
    M = int(input())

    cur = len(note)
    for _ in range(M):
        cmd = input().split()

        if cmd[0] == "L":
            if len(note) > 0: buff.append(note.pop())
        elif cmd[0] == "D":
            if len(buff) > 0: note.append(buff.pop())
        elif cmd[0] == "B":
            # print(cur, len(note), note[:cur], note[cur:], end='\t')
            if len(note) > 0: note.pop()
        else:
            # if cur == 0: note = cmd[1] + note
            if len(note) == 0: note.append(cmd[1])
            # else: note = note[:cur] + cmd[1] + note[cur:]
            else: note.append(cmd[1])

        buff.reverse()
        print(cmd[0], note, buff)
        buff.reverse()


    buff.reverse()
    note.extend(buff)
    print("".join(note))

