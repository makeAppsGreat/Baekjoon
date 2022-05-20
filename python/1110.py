"""
    1110번: 더하기 사이클
    Create by Kim Gayoun on 2022-03-22
"""
if __name__ == "__main__":
    x = int(input())
    i, k = 0, x

    while True:
        a = k // 10
        b = k % 10
        k = b * 10 + (a + b) % 10
        i = i + 1

        if x == k: break


    print(i)

