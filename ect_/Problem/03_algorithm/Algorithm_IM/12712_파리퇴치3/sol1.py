import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    d_a = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    d_b = [[-1, -1], [-1, 1], [1, 1], [1, -1]]
    max_val = 0
    for i in range(N):
        for j in range(N):
            s_a = s_b = arr[i][j]
            for k in range(1, M):
                for m in range(4):
                    ai = i + d_a[m][0]*k
                    aj = j + d_a[m][1]*k
                    if 0 <= ai < N and 0 <= aj < N:
                        s_a += arr[ai][aj]
                    bi = i + d_b[m][0]*k
                    bj = j + d_b[m][1]*k
                    if 0 <= bi < N and 0 <= bj < N:
                        s_b += arr[bi][bj]

                    if s_a > s_b:
                        if max_val < s_a:
                            max_val = s_a
                    else:
                        if max_val < s_b:
                            max_val = s_b

    print(f'#{tc} {max_val}')