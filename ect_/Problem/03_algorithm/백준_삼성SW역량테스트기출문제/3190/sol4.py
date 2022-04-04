


import sys
sys.stdin = open('input.txt')
# input = sys.stdin.readline
from pprint import pprint



dx = [0, 1, 0, -1]          # 우 하 좌 상
dy = [1, 0, -1, 0]

def dummy():
    direction = 0
    time = 1
    x, y = 0, 0
    board[x][y] = 2
    visited = []
    visited.append([x, y])
    while True:
        x, y = x + dx[direction], y + dy[direction]
        # print(time-1)
        # pprint(board)
        # print(x, y)
        if 0 <= x < N and 0 <= y < N and board[x][y] != 2:
            if board[x][y] != 1:
                temp = visited.pop(0)
                lx, ly = temp[0], temp[1]
                board[lx][ly] = 0
            visited.append([x, y])
            board[x][y] = 2
            if time in times.keys():
                temp = times[time]
                if temp == 'D':
                    direction += 1
                else:
                    direction -= 1
                if direction >= 0:
                    direction = direction % 4
                else:
                    direction = 3
            time += 1
        else:
            return time


# N*N 행열에 사과가 놓여져 있다
N = int(input())                # 보드의 크기 2 <= N <= 100
K = int(input())                # 사과의 개수 0 <= K <= 100
board = [[0]*N for _ in range(N)]
for i in range(K):
    temp = list(map(int, input().split()))
    board[temp[0]-1][temp[1]-1] = 1
# pprint(board)
L = int(input())                # 뱀의 방향 변환 정보 1 <= L <= 100
times = {}
for _ in range(L):
    X, C = input().split()
    times[int(X)] = C

rlt = dummy()
print(f'{rlt}')