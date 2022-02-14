import sys
sys.stdin = open('input.txt')

T = 10


for tc in range(1, T + 1):
    number = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    max_value = 0
    sum_diag_r = 0
    sum_diag_l = 0

    #행의 합
    for i in range(100):
        sum_row = 0
        for j in range(100):
            sum_row += matrix[i][j]
        if sum_row > max_value:
            max_value = sum_row
    #열의 합
    for i in range(100):
        sum_col = 0
        for j in range(100):
            sum_col += matrix[j][i]
        if sum_col > max_value:
            max_value = sum_col
    #우 대각 합
    for i in range(100):
        sum_col += matrix[i][i]
    if sum_diag_r > max_value:
        max_value = sum_diag_r
    #좌 대각 합
    for i in range(100):
        sum_col += matrix[i][i]
    if sum_diag_l > max_value:
        max_value = sum_diag_l

    print(f'#{tc}', max_value)

