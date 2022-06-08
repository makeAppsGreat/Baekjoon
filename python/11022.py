"""
    11022번: A+B - 8
    Create by Kim Gayoun on 2022-06-08
"""
N = int(input())
for i in range(N):
    A, B = map(int, input().split())
    print("Case #{}: {} + {} = {}".format(i + 1, A, B, A + B))

