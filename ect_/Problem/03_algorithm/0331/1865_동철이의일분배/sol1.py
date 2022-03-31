import sys
sys.stdin = open('input.txt')

def dfs(s, cal):
    global rlt
    if cal < rlt:
        return
    if s == N:
        rlt = cal
        return

    for i in range(N):
        if visited[i] == 0 and arr[s][i]:                     # 방문 안했으면 계산 진행
            visited[i] = 1                      # 방문 처리
            dfs(s + 1, cal*arr[s][i] / 100)                          # 다음 사람 진행
            visited[i] = 0

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    rlt = 0
    dfs(0, 1)
    # print(f'#{tc}', end=' ')
    # print(format(round(rlt*100, 7), '.6f'))
    print('#{} {:.6F}'.format(tc, rlt*100))