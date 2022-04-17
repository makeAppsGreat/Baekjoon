"""
    10809번: 알파벳 찾기
    Create by Kim Gayoun on 2022-04-18
"""


if __name__ == "__main__":
    line, result = input(), list()
    for i in range(97, 123): result.append(line.find(chr(i)))
    print(*result)
    
