"""
    1076번: 저항
    Create by Kim Gayoun on 2022-06-10
"""
def c2v( color ): # color to value
    if color == "black": return 0
    elif color == "brown": return 1
    elif color == "red": return 2
    elif color == "orange": return 3
    elif color == "yellow": return 4
    elif color == "green": return 5
    elif color == "blue": return 6
    elif color == "violet": return 7
    elif color == "grey": return 8
    elif color == "white": return 9


A = input()
B = input()
C = input()
print((c2v(A) * 10 + c2v(B)) * 10 ** c2v(C))

