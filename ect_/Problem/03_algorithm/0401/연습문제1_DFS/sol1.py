import sys
sys.stdin = open('input.txt')

def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for adj in adjL[v]:
        if not visited[adj]:
            dfs(adj)
    # visited[v] = 0

T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    V = 7
    adjL = [[] for _ in range(V+1)]
    visited = [0]*(V+1)
    # print(adjL)
    for i in range(0, len(arr), 2):
        adjL[arr[i]].append(arr[i+1])
        adjL[arr[i+1]].append(arr[i])
    # print(adjL)
    dfs(1)