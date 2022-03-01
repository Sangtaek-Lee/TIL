import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_val = 0
    d_box = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]
    d_crs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for i in range(N):
        for j in range(N):
            sum_box = 0
            sum_crs = arr[i][j]
            for row, col in d_box:
                d_row, d_col = i + row, j + col
                if 0 <= d_row < N and 0 <= d_col < N:
                    sum_box += arr[d_row][d_col]
                else:
                    sum_box = 0
                    break

            for row, col in d_crs:
                for k in range(1, arr[i][j]):
                    d_row, d_col = i + row*k, j + col*k
                    if 0 <= d_row < N and 0 <= d_col < N:
                        sum_crs += arr[d_row][d_col]

            if sum_box > sum_crs:
                temp = sum_box
            else:
                temp = sum_crs
            if temp > max_val:
                # print(i, j)
                max_val = temp

    print(f'#{tc} {max_val}')