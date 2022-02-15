import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = 10


for tc in range(1, T + 1):
    tc_num = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    # row_legnth = len(matrix)
    # col_legnth = len(matrix[0])
    # print(row_legnth,col_legnth)

    # 하단 2값 위치 찾기
    x_rc = [99, 0]
    for i in range(100):
        if matrix[99][i] == 2:
            x_rc[1] = i
            break


    # print(x_rc)
    row = x_rc[0]
    col = x_rc[1]
    cnt = 0
    print(row,col)
    # 상, 하 좌 우 중 하나의 값이 1 이면 그쪽으로 이동 (상, 하, 좌, 우 우선순위를 둔다)

    # row = 95
    # if col < 99:
    #     if matrix[row][col + 1] == 1:  # 우
    #         col += 1
    # elif row > 0:
    #     if matrix[row][col - 1] == 1:  # 좌
    #         col -= 1
    # elif matrix[row - 1][col] == 1:  # 상
    #     row -= 1
    # print(f'#{tc}', col)




    while cnt <= 10:                # 상단에서 시작 시 2를 만나면 break? or 하단에서 시작하면 값이 없으면 break?)
        if col < 99:
            if matrix[row][col+1] == 1:         # 우
                col += 1
        elif col > 0:
            if matrix[row][col-1] == 1:         # 좌
                col -= 1
        elif matrix[row-1][col] == 1:         # 상
            row = row - 1
        # col += 1
        cnt += 1
        # print(row, col)
        print(matrix[row-1][col])
        print(f'#{tc}', row, col)

