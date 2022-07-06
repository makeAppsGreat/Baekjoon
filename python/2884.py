"""
    2884번: 알람 시계
    Create by Kim Gayoun on 2022-03-21
"""
if __name__ == "__main__":
    input = input().split()
    h = int(input[0]) * 60
    m = int(input[1])

    if (h + m - 45) < 0: m += 24 * 60

    x = int( (h + m - 45) / 60 )
    y = (h + m - 45) % 60


    print("{} {}".format(x, y))

