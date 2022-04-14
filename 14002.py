

if __name__ == "__main__":
    N = int(input())
    A = list( map(int, input().split()) )
    dp = [ 1 for _ in range(N) ]

    A.append(0);
    dp.append(0)
    for i in range(len(A) - 1):
        __max = -1

        for j in range(i):
            if A[i] > A[j] and dp[__max] <= dp[j]: __max = j
        dp[i] = dp[__max] + 1

    
    dp2 = dict()
    for k in range(N):
        index = N - (k + 1)

        if not dp[index] in dp2: dp2[dp[index]] = A[index]
        elif dp[index] + 1 in dp2 and dp2[dp[index] + 1] > A[index]: dp2[dp[index]] = A[index]



    l = "["
    for x in dp: l += "{:2}, ".format(x)
    l = l[0 : -4] + "0]"
    print(dp2)
    print(l)

    print(A)
    print(max(dp))
    for x in range(1, max(dp) + 1):
        print("{} ".format(dp2[x]), end='')
