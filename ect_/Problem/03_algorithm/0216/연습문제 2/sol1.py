import sys

sys.stdin = open('input.txt')

T = 6


for tc in range(1, T + 1):
    number = int(input())
    number_str = ''

    while number > 0:
        number_digit = number % 10
        number_str = chr(number_digit+48) + number_str
        number = number // 10
    while number < 0:
        number_str = number_str + '-'
        number = -1 * number
        number_digit = number % 10
        number_str = number_str + chr(number_digit+48)
        number = number // 10

    print(f'#{tc}', number_str, type(number_str))
