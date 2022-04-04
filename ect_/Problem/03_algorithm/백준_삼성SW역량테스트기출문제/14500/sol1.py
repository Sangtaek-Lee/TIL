import sys
sys.stdin = open('input.txt')

def dfs(r, c, cnt, cal):
    global rlt
    # cnt += 1
    # cal += arr[r][c]

    if rlt >= cal + arr_max_val * (4 - cnt):
        return

    if cnt == 4:
        # print(cal)
        if cal > rlt:
            rlt = cal
            return
        return

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
            if cnt == 2:
                visited[nr][nc] = 1
                dfs(r, c, cnt + 1, cal + arr[nr][nc])
                visited[nr][nc] = 0
            visited[nr][nc] = 1
            dfs(nr, nc, cnt + 1, cal + arr[nr][nc])
            visited[nr][nc] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
dr = [0, 1, 0, -1]                      # 우 하 좌 상
dc = [1, 0, -1, 0]
rlt = 0
arr_max_val = max(map(max, arr))
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 0, 0)
        visited[i][j] = 0
print(rlt)

