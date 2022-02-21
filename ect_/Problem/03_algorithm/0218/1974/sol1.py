import sys

sys.stdin = open('input.txt')

T = int(input())

def check_list(N, matrix):
    for i in range(N):
        for t in range(1, N+1):
            cnt = 0
            for j in range(N):
                if matrix[i][j] == t:
                    cnt += 1
            if cnt != 1:
                return 0
    return 1

for tc in range(1, T + 1):
    N = 9
    matrix = [list(map(int, input().split())) for _ in range(N)]
    matrix_col = list(map(list, zip(*matrix)))
    matrix_box = []
    for r in range(0,N,3):
        for c in range(0,N,3):
            temp_list = []
            for i in range(3):
                for j in range(3):
                    temp_list.append(matrix[i+r][j+c])
            matrix_box += [temp_list]
    rlt = 1
    row_check, col_check, box_check = 0, 0, 0

    row_check += check_list(N, matrix)
    col_check += check_list(N, matrix_col)
    box_check += check_list(N, matrix_box)

    error_cnt = row_check + col_check + box_check
    if error_cnt != 3:
        rlt = 0

    print(f'#{tc} {rlt}')

