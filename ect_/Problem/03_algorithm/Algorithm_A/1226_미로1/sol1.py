import sys
sys.stdin = open('input.txt')

T = 10

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs():
    idx_1 = 0
    idx_2 = 0
    q = [0]*1000
    q[0] = start
    visited = [[0]*16 for _ in range(16)]
    visited[start[0]][start[1]] = 1
    while q[idx_1]:
        x = q[idx_1][0]
        y = q[idx_1][1]
        idx_1 += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<16 and 0<=ny<16 and visited[nx][ny] != 1:
                if graph[nx][ny] == 0:
                    idx_2 += 1
                    q[idx_2] = [nx, ny]
                    visited[nx][ny] = 1
                elif graph[nx][ny] == 3:
                    return 1
    return 0

for tc in range(1, 1+ T):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if graph[i][j] == 2:
                start = [i,j]

    print(f'#{tc} {bfs()}')