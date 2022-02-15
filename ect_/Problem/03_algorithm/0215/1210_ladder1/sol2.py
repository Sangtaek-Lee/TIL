import sys

sys.stdin = open('input.txt')

T = 10


for tc in range(1, T + 1):
    tc_num = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    row = 99
    for i in range(100):
        if matrix[row][i] == 2:
            col = i
            break

    cnt = 0
    while row > 0:

        if col > 0:
            while col > 0 and matrix[row][col-1] == 1:
                col -= 1
            row -= 1

        # if matrix[row-1][col] == 1:
        #     row -= 1
        if col < 99:
            while col < 99 and matrix[row][col+1] == 1:
                col += 1
            row -= 1

        # if col < 99:
        #     if matrix[row][col + 1] == 1:
        #         while matrix[row][col + 1] == 1 and col < 99:

        if matrix[row-1][col] == 1:
            row -= 1
        cnt += 1
    print(f'#{tc} ', row, col)

