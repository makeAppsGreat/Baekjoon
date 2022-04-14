

if __name__ == "__main__":
    N = int(input())
    l = list(map(int, input().split()))
    w = list(map(int, input().split()))
    w.pop()
    
    result, w_min, last = 0, min(w), 1_000_000_000
    for i, __w in enumerate(w):
        if __w == w_min:
            for j in range(i, N - 1): result += w_min * l[j]
            break
        elif __w < last: last = __w

        result += last * l[i]


    print(result)

