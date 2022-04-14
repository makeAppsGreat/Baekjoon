import sys
input = sys.stdin.readline


if __name__ == "__main__":
    l = list()
    for _ in range(9): l.append(int(input()))

    print(max(l))
    print(l.index(max(l)) + 1)
