import sys
sys.stdin = open('input.txt')
from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

TC = int(input())

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
            print(graph)
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
            print(time)
        print('##############')
    return 'KAKTUS'

for tc in range(1, TC + 1):
    R, C = map(int, input().split())
    graph = [list(input()) for _ in range(R)]     # . 비어있는 곳, * 물이 차있는 곳, X 돌, D 비버의 굴, S 고슴도치 위치
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
    print(f'{rlt}')      # 고슴도치가 비버의 굴로 이동할 수 있는 가장 빠른 시간 or KAKTUS