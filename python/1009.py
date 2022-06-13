"""
    1009번: 분산처리
    Create by Kim Gayoun on 2022-06-13
"""
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        A, B = map(int, input().split())
        # com = A ** B % 10
    
        buff, index = [ A % 10 ], 2
        while index <= B:
            buff.append(A ** index % 10)
            if buff[0] == buff[-1]:
                buff.pop()
                break

            index += 1

        com = buff[B % len(buff) - 1]
        if com == 0: print(10)
        else: print(com)
    
