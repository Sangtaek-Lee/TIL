import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    decimal = input()
    f_to_i = int(float(decimal)*10**(len(decimal)-2))
    x = 1*10**(len(decimal)-2)
    binary = ''
    while f_to_i != 0:
        x = x / 2
        if f_to_i >= x:
            f_to_i = f_to_i - x
            binary += '1'
        else:
            binary += '0'
        if len(binary) > 12:
            binary = 'overflow'
            break

    print(f'#{tc} {binary}')