import sys

sys.stdin = open('input.txt')

T = 3


for tc in range(1, T + 1):
    N = int(input()) + 1
    limit = N*N
    matrix = [[0]*N for _ in range(N)]
    matrix[0][0] = 1
    num = 1
    row = 0
    col = -1

    while num <= limit:           #우하좌상 반복 되게
        for right in range(N):
            # print(row, col)
            col += 1
            matrix[row][col] = num
            num += 1
        N -= 1
        for down in range(N):
            row += 1
            matrix[row][col] = num
            num += 1
        for left in range(N):
            col -= 1
            matrix[row][col] = num
            num += 1
        N -= 1
        for up in range(N):
            row -= 1
            matrix[row][col] = num
            num += 1
    # print(matrix)
    print(f'#{tc} ')
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end=' ')
        print()

