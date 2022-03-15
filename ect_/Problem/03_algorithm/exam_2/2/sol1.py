import sys
sys.stdin = open('input.txt')
from collections import deque

T = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(start):




    # 시작점 몬스터 확인
    if graph[start[0]][start[1]] > 0:
        catch_list.append(graph[start[0]][start[1]])
        graph[start[0]][start[1]] = 0
    visited = [[0]*N for _ in range(N)]
    visited[start[0]][start[1]] = 1
    q = deque()
    q.append(start)
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
                q.append([nx, ny])
                visited[nx][ny] = 1

                if graph[nx][ny] > 0:
                    catch_list.append(graph[nx][ny])
                    graph[nx][ny] = 0
                    bfs([nx, ny])
                elif -graph[nx][ny] in catch_list:
                    npc_list.append(graph[nx][ny])
                    if len(npc_list) == max_val:
                        print("#####")
                        return
        cnt += 1
    print(f'cnt:{cnt}')
    pass

for tc in range(1, 1+T):
    N = int(input())
    graph = [list(map(int,input().split())) for _ in range(N)]
    catch_list = []
    npc_list = []
    max_val = 0
    start = [0, 0]
    for i in range(N):
        for j in range(N):
            if max_val < graph[i][j]:
               max_val = graph[i][j]
    print(f'max_val:{max_val}')
    print(bfs(start))

    print(f'#{tc}')