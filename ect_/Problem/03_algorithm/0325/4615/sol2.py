import sys
sys.stdin = open('input.txt')

T = int(input())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(x_y):
    pass

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    arr2 = [[0]*N for _ in range(N)]
    print(N, M)
    print(arr)
    for i in range(M):
        rlt = bfs(arr[i])

    print(f'#{tc} {rlt}')
