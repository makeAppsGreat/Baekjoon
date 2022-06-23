"""
    10871번: X보다 작은 수
    Create by Kim Gayoun on 2022-06-23
"""
if __name__ == "__main__":
    N, X = map(int, input().split())
    A = list( map(int, input().split()) )

    for i in range(N):
        if A[i] < X: print(A[i], end=" ")

