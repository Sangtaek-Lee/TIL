import sys
sys.stdin = open('input.txt')


def bfs(v):
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        print(v, end=' ')
        for adj in adjL[v]:
            if not visited[adj]:
                visited[adj] = 1
                q.append(adj)

T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    V = 7
    adjL = [[] for _ in range(V+1)]
    visited = [0]*(V+1)
    q = []
    # print(adjL)
    for i in range(0, len(arr), 2):
        adjL[arr[i]].append(arr[i+1])
        adjL[arr[i+1]].append(arr[i])
    # print(adjL)
    bfs(1)