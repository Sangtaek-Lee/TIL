import sys

sys.stdin = open('input.txt')

def sum_box(M, i, j, matrix):
    sum_val = 0
    for row in range(M):
        for col in range(M):
            sum_val += matrix[row+i][col+j]
    return  sum_val

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_val = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_box_val = sum_box(M, i, j, matrix)
            if max_val < sum_box_val:
                max_val = sum_box_val
    print(f'#{tc}', max_val)

    #
    # # print(matrix)
    # for row in range(N-1):
    #     cnt = 0
    #     for col in range(N-1):
    #         cnt = matrix[row][col] + matrix[row][col+1] + matrix[row+1][col] +matrix[row+1][col+1]
    #         print(cnt)
    #     if cnt > max_val:
    #         max_val = cnt
    #

