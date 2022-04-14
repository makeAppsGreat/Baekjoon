""" 2022-03-22 """


if __name__ == "__main__":
    alpha = [ 0 ] * 26
    word = list(input().upper())


    for w in word:
        i = ord(w) - 65
        alpha[i] = alpha[i] + 1


    m = max(alpha)
    i = alpha.index(m)
    alpha.remove(m)

    if m == max(alpha): print("?")
    else: print(chr(i + 65))

