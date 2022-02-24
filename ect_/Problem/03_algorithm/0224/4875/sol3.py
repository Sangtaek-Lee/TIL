import sys

sys.stdin = open('input.txt')

TC = int(input())

def maze(row, col):
    arr[row][col] = 1
    for i in range(4):
        row_c = d_row[i] + row
        col_c = d_col[i] + col
        if (0 <= col_c < N) and (0 <= row_c < N):
            if arr[row_c][col_c] == 0:
                maze(row_c, col_c)
            if arr[row_c][col_c] == 3:
                return 1

for tc in range(1, TC + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    d_row = [0, 0, 1, -1]
    d_col = [1, -1, 0, 0]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                row = i
                col = j
    rlt = maze(row, col)

    print(f'{tc} {rlt}')