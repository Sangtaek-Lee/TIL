import sys
sys.stdin = open('input.txt')

# 목표 : 전체 제품의 최소 생산 비용

def dfs(s):
    global cost, rlt

    if rlt < cost:
        return
    if s == N:
        if rlt > cost:
            rlt = cost
            return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            cost += arr[s][i]
            # print(f's: {s}, i: {i}, cost: {cost}')
            dfs(s+1)
            visited[i] = 0
            cost -= arr[s][i]







T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [0] * N
    rlt = 99999
    cost = 0
    dfs(0)
    print(f'#{tc} {rlt}')