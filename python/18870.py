"""
    18870번: 좌표 압축
    Create by Kim Gayoun on 2022-04-08
"""
if __name__ == "__main__":
    N = input()
    X, result = list( map(int, input().split()) ), ""


    __X, dic = list( set(X) ), dict()
    __X.sort()
    for i, x in enumerate(__X): dic[x] = i
    for x in X: result += "{} ".format(dic[x])


    print(result)

