"""
    1929번: 소수 구하기
    Create by Kim Gayoun on 2022-04-02

    # 시간 초과
"""
if __name__ == "__main__":
    M, N = map(int, input().split())
    p = list()

    if M == 1: M = 2 # 1 <= M <= N <= 1,000,000
    for i in range(M, N + 1): p.append(i)
    for i in range(2, int(N ** (1/2)) + 1):
        j = 2

        while True:
            k = i * j

            
            print(i, j, k, N, p)
            if k > N: break
            else:
                try: p.remove(k)
                except: pass
                j = j + 1

    result = ""
    for i in p: result += "{}\n".format(i)
    print(result)

