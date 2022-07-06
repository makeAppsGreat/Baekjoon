"""
    4673번: 셀프 넘버
    Create by Kim Gayoun on 2022-04-14
"""
if __name__ == "__main__":
    l = [ i for i in range(1, 10000 + 1) ]


    for i in range(1, 2 ** 32):
        __sum = i

        while True:
            __sum += i % 10
            i = i // 10
            if i == 0: break
        
        try: l.remove(__sum)
        except: pass
        if __sum >= 20000: break


    result = ""
    for j in l: result += "{}\n".format(j)
    print(result)

