from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs():
    while q:
        for r in range(len(wq)):
            x, y = wq.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] == '.':
                    graph[nx][ny] = '*'
                    wq.append([nx, ny])
        for r in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx = x +dx[i]
                ny = y +dy[i]
                if 0 <= nx < R and 0 <= ny < C:
                    if graph[nx][ny] == '.' and time[nx][ny] == 0:
                        time[nx][ny] = time[x][y] + 1
                        q.append([nx, ny])
                    elif graph[nx][ny] == 'D':
                        return time[x][y] + 1
    return 'KAKTUS'

R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
time = [[0]*C for _ in range(R)]
q = deque()
wq = deque()
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'S':
            q.append([i, j])
        elif graph[i][j] == '*':
            wq.append([i, j])

rlt = bfs()
print(f'{rlt}')