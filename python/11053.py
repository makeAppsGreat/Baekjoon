"""
    11053번: 가장 긴 증가하는 부분 수열
    Create by Kim Gayoun on 2022-04-11
"""
if __name__ == "__main__":
    N = int(input())
    A = list( map(int, input().split()) )
    dp = [ 1 for _ in range(N) ]

    A.append(0); print(A)
    dp.append(0)
    for i in range(len(A) - 1):
        __max = -1

        for j in range(i):
            print(A[i], A[j])
            if A[i] > A[j] and dp[__max] <= dp[j]: __max = j

        print(A[i], A[__max], __max, "\n")
        dp[i] = dp[__max] + 1

    l = "["
    for k in dp: l += "{:2}, ".format(k)
    l = l[0 : -4] + "0]"
    print(l)

    print(A)
    print(max(dp))
