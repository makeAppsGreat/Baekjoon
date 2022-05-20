"""
    11399번: ATM
    Create by Kim Gayoun on 2022-04-06
"""
if __name__ == "__main__":
    N = input()
    P = list(map(int, input().split()))
    P.sort()

    result = 0
    for i, p in enumerate(P): result += p * (len(P) - i)


    print(result)

