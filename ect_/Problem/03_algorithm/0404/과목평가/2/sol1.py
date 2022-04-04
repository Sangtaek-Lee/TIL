import sys
sys.stdin = open('algo2_sample_in.txt')

T = int(input())

dx = [0, 1, 0, -1]      # 우 하 좌 상
dy = [1, 0, -1, 0]

def bfs(s, arr):
    global rlt
    visited = [[0]*N for _ in range(N)]
    visited[s[0]][s[1]] = 1
    q.append(s)
    # print('bfs start',arr)
    # print(q)
    while q:
        x, y = q.pop(0)
        # print("x,y",x, y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and arr[nx][ny] != 1:
                # print(nx, ny)
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])
                # print(q)
                if arr[nx][ny] == 3:
                    # print('xxxxxxxxxxxxxxxxxxx')
                    # print(rlt)
                    # print(visited[nx][ny])
                    if rlt > visited[nx][ny]:
                        rlt = visited[nx][ny]






for tc in range(1, T+1):
    N = int(input())
    arr = []
    wall_list = []
    q = []
    rlt = 99999
    # arr 만들고 출발점, 도착점 위치 찾기
    for i in range(N):
        temp = input()
        temp_list = []
        for j in range(N):
            box = int(temp[j])
            temp_list.append(box)
            if box == 2:
                start = [i, j]
            elif box == 3:
                end = [i, j]
            elif box == 1:
                wall_list.append([i, j])
        arr.append(temp_list)
    # print(arr)
    # print(wall_list)
    # print(start, end)

    # 조합으로 벽 제거 후 bfs

    # 조합을 만들자
    wall = [0, 0]
    rlt_list = [0, 1]
    for i in range(len(wall_list)):
        for j in range(i+1, len(wall_list)):
            wall[0] = wall_list[i]
            wall[1] = wall_list[j]
            arr[wall[0][0]][wall[0][1]] = 0
            arr[wall[1][0]][wall[1][1]] = 0
            bfs(start, arr)
            arr[wall[0][0]][wall[0][1]] = 1
            arr[wall[1][0]][wall[1][1]] = 1
    if rlt == 99999:
        rlt = -1
    print(f'#{tc} {rlt}')