import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs():
    visited = [[0]*N for _ in range(N)]
    visited[start[0]][start[1]] = 1
    q = deque()
    q.append(start)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx,ny])
                elif graph[nx][ny] == 3:
                    return visited[x][y] - 1
    return 0

for tc in range(1, 1+ T):
    N = int(input())
    graph = [list(map(int,input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2:
                start = [i, j]

    print(f'#{tc} {bfs()}')