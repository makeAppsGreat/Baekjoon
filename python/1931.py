"""
    1931번: 회의실 배정
    Create by Kim Gayoun on 2022-04-05
"""
if __name__ == "__main__":
    N = int(input())
    ml, g = list(), [ (0, 0) ]
    

    for _ in range(N):
        m = input().split()
        ml.append((int(m[0]), int(m[1])))

    ml.sort(key=lambda k:(k[1], k[0]))


    for m in ml:
        if m[0] >= g[len(g) - 1][1]: g.append(m)


    print(len(g) - 1)
