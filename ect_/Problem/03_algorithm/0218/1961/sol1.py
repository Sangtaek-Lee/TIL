import sys

sys.stdin = open('input.txt')

T = int(input())

def right_90(N, arr):
    rlt_matrix = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rlt_matrix[i][j] = arr[N-1-j][i]
    return rlt_matrix

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    arr_90 = right_90(N, matrix)
    arr_180 = right_90(N, arr_90)
    arr_270 = right_90(N, arr_180)

    print(f'#{tc}')
    for i in range(N):
        print(''.join(map(str, arr_90[i])), end=' ')
        print(''.join(map(str, arr_180[i])), end=' ')
        print(''.join(map(str, arr_270[i])), end=' ')
        print()

