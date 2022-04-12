import sys
sys.stdin = open('input.txt')
from pprint import pprint





def dfs(x, y, cnt, cal):
    global rlt
    if cnt == 4:
        if rlt < cal**2:
            # pprint(visited)
            # print(cal**2)
            rlt = cal**2
        return
    if y % 2 == 0:
        dx = [-1, 0, 1, 0, -1, -1]
        dy = [1, 1, 0, -1, -1, 0]
    else:
        dx = [0, 1, 1, 1, 0, -1]
        dy = [1, 1, 0, -1, -1, 0]

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < H and 0<= ny < W and visited[nx][ny] == 0:
            # print(cnt)
            # print(x, y)

            cnt += 1
            visited[nx][ny] = 1
            # print(nx, ny)
            dfs(nx, ny, cnt, cal + arr[nx][ny])
            cnt -= 1
            visited[nx][ny] = 0





T = int(input())

for tc in range(1, T+1):
    W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    rlt = 0
    W, H = W, H
    # print(W,H,arr)
    for i in range(H):
        for j in range(W):
            if j % 2 == 0:
                dx = [-1, -1, 0, 1, 0, -1]
                dy = [0, 1, 1, 0, -1, -1]
            else:
                dx = [0, 1, 1, 1, 0, -1]
                dy = [1, 1, 0, -1, -1, 0]
            visited = [[0] * W for _ in range(H)]
            # print('start########', i, j)
            visited[i][j] = 1
            temp = dfs(i, j, 1, arr[i][j])


    print(f'#{tc} {rlt}')