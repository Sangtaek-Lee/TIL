import sys
sys.stdin = open('input.txt')
from pprint import pprint
N = int(input())                # 보드의 크기 2 <= N <= 100
K = int(input())                # 사과의 개수 0 <= K <= 100
board = [[0]*N for _ in range(N)]
visited = [[0]*N for _ in range(N)]
visited[0][0] = 1
for i in range(K):
    temp = list(map(int, input().split()))
    board[temp[0]][temp[1]] = 1
L = int(input())                # 뱀의 방향 변환 정보 1 <= L <= 100

## print
pprint(board)
print(snake_arr)

rlt = 0
cnt = 0
base = 0
direct = 'G'
x = 0
y = 0
for w in snake_arr:
    sec = int(w[0])
    # 우 하 좌 상
    if base == 0:
        x = x
        y = y
    elif base == 1:
        x = -y
        y = x
    for i in range(sec):
        if 0<= x < N or 0<= y < N:

            if direct == 'G':
                x += 1
            elif direct == 'L':

            else:


            if i == sec:
                direct = w[1]
        else:
            rlt = cnt
            break
    if rlt:
        break
