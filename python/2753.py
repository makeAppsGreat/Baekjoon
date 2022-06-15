"""
    2753번: 윤년
    Create by Kim Gayoun on 2022-06-15
"""
if __name__ == "__main__":
    year = int(input())

    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0): print(1)
    else: print(0)

