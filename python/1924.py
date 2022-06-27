"""
    1924번: 2007년
    Create by Kim Gayoun on 2022-06-27
"""
import datetime
DAY = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]


if __name__ == "__main__":
    M, D = map(int, input().split())
    print(DAY[datetime.date(2007, M, D).weekday()])


