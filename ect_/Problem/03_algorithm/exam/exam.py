import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    total_zero = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                total_zero += 1
            if arr[i][j] == 2:
                row = i
                col = j
    # print(total_zero)
    # print(row, col)
    cnt = 0
    d_rc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for i, j in d_rc:
        for k in range(1, N):
            di = row + i * k
            dj = col + j * k
            if 0 <= di < N and 0 <= dj < N and arr[di][dj] == 1:
                break
            elif 0 <= di < N and 0 <= dj < N:
                cnt += 1
    # print(cnt)
    rlt = total_zero - cnt
    print(f'#{tc} {rlt}')