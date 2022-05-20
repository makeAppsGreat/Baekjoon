"""
    11055번: 가장 큰 증가 부분 수열
    Create by Kim Gayoun on 2022-04-12
"""
if __name__ == "__main__":
    N = int(input())
    A = list( map(int, input().split()) )
    dp = [ 0 for _ in range(N) ]
    dp.append(0)

    for i in range(len(A)):
        __max = -1

        for j in range(i):
            if A[i] > A[j] and dp[__max] <= dp[j]: __max = j

        dp[i] = dp[__max] + A[i]

    l = "["
    for k in dp: l += "{:2}, ".format(k)
    l = l[0 : -4] + "0]"
    print(l)

    print(A)
    print(max(dp))

