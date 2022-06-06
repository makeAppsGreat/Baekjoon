"""
    11021번: A+B - 7
    Create by Kim Gayoun on 2022-06-06
"""
N = int(input())
for i in range(N):
    A, B = map(int, input().split())
    print("Case #{}: {}".format(i + 1, A + B))

