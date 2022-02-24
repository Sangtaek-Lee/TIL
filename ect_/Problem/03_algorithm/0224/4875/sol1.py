import sys

sys.stdin = open('input.txt')

T = int(input())

def maze(row, col, arr):
    stack = [[row, col]]
    top = 0
    d_row = [0, 1, 0, -1] # 우 하 좌 상
    d_col = [1, 0, -1, 0]
    i = 0
    while True:
        print(i)
        if 0 <= row + d_row[i] < N and 0 <= col + d_col[i] < N:             # arr 범위
            if arr[row + d_row[i]][col + d_col[i]] == 0:                    # 우 하 좌 상 중 0 이라면
                arr[row][col] = 1                                           # 지나 온 길 1로 표시
                stack.append([row + d_row[i], col + d_col[i]])              # 스택에 좌표 추과
                row = row + d_row[i]                                        # 현재 row 위치 변경
                col = col + d_col[i]                                        # 현재 col 위치 변경
                # print(stack)
            elif arr[row + d_row[i]][col + d_col[i]] == 3:
                arr[row][col] = 1                                           # 지나 온 길 1로 표시
                stack.append([row + d_row[i], col + d_col[i]])              # 스택에 좌표 추과
                return 1

                # tmp = stack.pop()
                # row = tmp[0]
                # col = tmp[1]
        print(stack)
        i = (i+1) % 4
        break

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]
    # print(arr)

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                current_row = i
                current_col = j
    # print(current_row, current_col, arr)

    rlt = maze(current_row, current_col, arr)

    print(f'#{tc} {rlt}')


