import sys
sys.stdin = open('input.txt')
from collections import deque

TC = int(input())

dz = [0,0,0,0,1,-1]
dx = [0,1,0,-1,0,0]
dy = [1,0,-1,0,0,0]
def bfs():
    day = 0
    while q:
        for _ in range(len(q)):
            z, x, y = q.popleft()
            for i in range(6):
                nz = z + dz[i]
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nz<H and 0<=nx<N  and 0<=ny<M:
                    if graph[nz][nx][ny] == 0:
                        graph[nz][nx][ny] = 1
                        q.append([nz,nx,ny])
        day += 1
    return day - 1

for tc in range(1, TC + 1):
    M, N, H = map(int, input().split())
    graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
    # print(graph)
    q = deque()
    for z in range(H):
        for x in range(N):
            for y in range(M):
                if graph[z][x][y] == 1:
                    q.append([z, x, y])
    rlt = bfs()
    for z in range(H):
        for x in range(N):
            for y in range(M):
                if graph[z][x][y] == 0:
                    rlt = -1
                    break
    print(rlt)