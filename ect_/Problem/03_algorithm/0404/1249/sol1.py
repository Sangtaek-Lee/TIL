import sys
sys.stdin = open('input.txt')
from collections import deque

T = int(input())


for tc in range(1, T + 1):
    n = int(input())
    maps = [list(map(int, list(input()))) for _ in range(n)]
    answer = 0
    keys = [[99999] * n for _ in range(n)]
    keys[0][0] = 0
    q = deque()
    q.append((0, 0))

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if keys[x][y] + maps[nx][ny] < keys[nx][ny]:
                    keys[nx][ny] = keys[x][y] + maps[nx][ny]
                    q.append((nx, ny))

    answer = keys[-1][-1]

    print(f'#{tc} {answer}')
