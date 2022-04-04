import sys
sys.stdin = open('algo1_sample_in.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    d_list = [[0, 0], [0, K-1], [K-1, 0], [K-1, K-1]]
    for i in range(1, K-1):
        d_list.append([0, i])
        d_list.append([i, 0])
        d_list.append([K-1, i])
        d_list.append([i, K-1])
    rlt = 0
    for i in range(N):
        for j in range(M):
            cal = 0
            for d in d_list:
                nr = i + d[0]
                nc = j + d[1]
                if 0 <= nr < N and 0<= nc < M:
                    cal += arr[nr][nc]
                else:
                    break
            if rlt < cal:
                rlt = cal

    print(f'#{tc} {rlt}')