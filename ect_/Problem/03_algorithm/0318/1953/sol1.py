import sys
sys.stdin = open('input.txt')
from pprint import pprint

T = int(input())

dx = [[0], [-1, 1, 0, 0], [-1, 1, 0, 0], [0, 0, 0, 0], [-1, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [-1, 0, 0, 0]]
dy = [[0], [0, 0, -1, 1], [0, 0, 0, 0], [0, 0, -1, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, -1, 0], [0, 0, -1, 0]]
match = [[0], [1, 2, 3, 4], [1, 2, 0, 0], [0, 0, 3, 4], [0, 2, 3, 0], [1, 0, 3, 0], [1, 0, 0, 4], [0, 2, 0, 4]]


def bfs(ci, cj, L):
    q = []
    q.append([ci, cj])
    visited = [[0]*M for _ in range(N)]
    visited[ci][cj] = 1
    cnt = 1
    while q:
        x, y= q.pop(0)
        i = 0
        if visited[x][y] == L:
            break
        while i < len(dx[arr[x][y]]):
            nx = x + dx[arr[x][y]][i]
            ny = y + dy[arr[x][y]][i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and arr[nx][ny] and (dx[arr[x][y]][i] or dy[arr[x][y]][i])  and match[arr[nx][ny]][i]:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
                cnt += 1
            i += 1
    return cnt


for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    rlt = bfs(R, C, L)

    print(f'#{tc} {rlt}')