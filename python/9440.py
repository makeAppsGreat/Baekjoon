"""
    9440번: 숫자 더하기
    Create by Kim Gayoun on 2022-04-01
"""
if __name__ == "__main__":
    while True:
        n = list(map(int, input().split()))
        if n[0] == 0: break
        else:
            n.remove(n[0])
            zero = 0

            try:
                while True:
                    n.remove(0)
                    zero = zero + 1
            except: pass
            n.sort()

            
            result, j = list(), (zero + 2)
            for _ in range(2):
                x = n[0]
                n.remove(x)
                result.append(str(x))
            for i in range(zero): result[i % 2] += "0"
            for i, __n in enumerate(n): result[(j + i) % 2] += str(__n)

            print(int(result[0]) + int(result[1]))

