import sys
sys.stdin = open('input.txt')

T = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(v, cnt):
    global rlt
    if v[0] == N and v[1] == N:
        if rlt > cnt:
            rlt = cnt
        return


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    start, end = [0, 0], [N-1, N-1]

    print(f'#{tc} {dfs(start, 0)}')