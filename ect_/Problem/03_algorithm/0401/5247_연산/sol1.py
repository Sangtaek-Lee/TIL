import sys
sys.stdin = open('input.txt')

T = int(input())

def dfs(v):
    global rlt
    print(v, M)
    if v == M:
        print('return')
        if rlt > visited[v]:
            rlt = visited[v]
        return

    for i in range(1, 5):
        if not visited[i]:
            visited[i] = visited[v] + 1
            if i == 1:


            dfs(i)


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    M_max = 1000000
    rlt = 999999
    visited = [0]*(M_max+1)
    dfs(0)
    print(f'#{tc} {rlt}')