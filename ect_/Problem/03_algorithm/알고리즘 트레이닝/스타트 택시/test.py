import sys
sys.stdin = open('input.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M, F = map(int, input().split())
arr_1 = [list(map(int, input().split())) for _ in range(N)]
row, col = map(int, input().split())
arr_2 = [list(map(int, input().split())) for _ in range(M)]

def taxi_bfs():
    return 0

def pass_bfs():
    return 0

for _ in range(M):
    F = F - taxi_bfs() - pass_bfs()
    if F < 0:
        F = -1
        break
    F = F * 2

print(F)
