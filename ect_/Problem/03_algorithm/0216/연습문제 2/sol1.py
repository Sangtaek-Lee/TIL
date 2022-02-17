import sys

sys.stdin = open('input.txt')

T = 6


for tc in range(1, T + 1):
    number = int(input())
    number_str = ''

    while number > 0:                                   # 양수 일 때
        number_digit = number % 10                      # 나머지로 한자리 수를 받아 온다
        number_str = chr(number_digit+48) + number_str  # ASCII 코드 0이 48이므로 + 48 해준다음 빈 문자열 앞에 추가한다.
        number = number // 10                           # 몫으로 자리 수 제거
    if number < 0:                                              # 음수 일 때
        number = -1 * number                                    # 양수로 바꾼 후
        while number > 0:                                       # 양수 조건과 동일
            number_digit = number % 10                          # 양수와 같은 과정 반복
            number_str = chr(number_digit+48) + number_str
            number = number // 10
        number_str = '-' + number_str                           # -기호를 추가한다.
    print(f'#{tc}', number_str, type(number_str))
