import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    row_column = int(input())
    matrix = [list(map(int, input().split())) for _ in range(row_column)]

    rd = [0, -1, 0, +1]  # 우 하 좌 상
    cd = [1, 0, -1, 0]
    sum_d = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            for k in range(4):
                row_d = r + rd[k]
                col_d = c + cd[k]
                if 0 <= row_d < len(matrix) and 0 <= col_d < len(matrix[0]):
                    if matrix[r][c] < matrix[row_d][col_d]:
                        sum_d -= matrix[r][c] - matrix[row_d][col_d]
                    else:
                        sum_d += matrix[r][c] - matrix[row_d][col_d]

    print(f'#{tc} ', sum_d)

