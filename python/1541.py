

if __name__ == "__main__":
    __input, result = input().split('-', maxsplit=1), 0

    result += sum( list(map(int, __input[0].split('+'))) )
    if len(__input) > 1:
        __input[1] = __input[1].replace('-', '+')
        result -= sum( list(map(int, __input[1].split('+'))) )


    print(result)

