import sys
from collections import deque
sys.stdin = open('input.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
cnt_list = []
def bfs():
    q = deque()
    q.append([0, 0])
    visited[0][0] = 1
    visited = [[0]*Y for _ in range(X)]
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < X and 0 <= ny < Y and visited[nx][ny] == 0:
                if graph[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = 1
                else:
                    graph[nx][ny] = 0
                    visited[nx][ny] = 1
                    cnt += 1
    cnt_list.append(cnt)
    return cnt

X, Y = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(X)]

time = 0
while True:
    temp = bfs()
    if temp == 0:
        break
    time += 1
print(time)
print(cnt_list[-2])