import sys

sys.stdin = open('input.txt')

T = int(input())

def check_list(N, matrix):
    for i in range(1, N+1):
        for j in range(N):
            if matrix[]


for tc in range(1, T + 1):
    N = 9
    matrix = [list(map(int, input().split())) for _ in range(N)]
    matrix_col = []
    matrix_box = []
    rlt = 1
    row_check, col_check, box_check = 0, 0, 0

    for i in range(N):
        row_check += check_list(N, matrix[i])
        col_check += check_list(N, matrix_col[i])
        box_check += check_list(N, matrix_box[i])

    error_cnt = row_check + col_check + box_check
    if error_cnt != 0:
        rlt = 0

    print(f'#{tc} {rlt}')

