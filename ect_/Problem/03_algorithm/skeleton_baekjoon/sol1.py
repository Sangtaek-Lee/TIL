import sys
sys.stdin = open('input.txt')

def dfs(cnt, cal):
    for i in range(M):
        for j in range(N):
            pass
    pass




N, M = map(int, input().split())
print(N, M)

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

rlt = dfs(0, 0)
print(rlt)

