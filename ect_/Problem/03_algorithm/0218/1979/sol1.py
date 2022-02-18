import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+1)]
    # print(matrix)
    cnt = 0
    cnt_row = 0
    cnt_col = 0

    for i in range(N+1):
        for j in range(N+1):
            if matrix[i][j] == 1:
                cnt_row += 1
            else:
                if cnt_row == K:
                    cnt += 1
                cnt_row = 0
            if matrix[j][i] == 1:
                cnt_col += 1
            else:
                if cnt_col == K:
                    cnt += 1
                cnt_col = 0

    print(f'#{tc}', cnt)

