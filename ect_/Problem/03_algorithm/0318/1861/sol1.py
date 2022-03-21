import sys
sys.stdin = open('input.txt')

T = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(si, sj):
    q = []
    q.append([si, sj])
    visited = [[0]*N for _ in range(N)]
    visited[si][sj] = 1
    rlt = 1
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and arr[nx][ny] == arr[x][y] + 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])
                if visited[nx][ny] > rlt:
                    rlt = visited[nx][ny]
    return rlt

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_val = 0
    start_num = 0
    for i in range(N):
        for j in range(N):
            rlt = bfs(i, j)
            if max_val < rlt:
                max_val = rlt
                start_num = arr[i][j]
            elif max_val == rlt:
                if start_num > arr[i][j]:
                    start_num = arr[i][j]

    print(f'#{tc} {start_num} {max_val}')