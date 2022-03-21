import sys
sys.stdin = open('input.txt')

T = 10

def bfs(start):
    visited = [0]*101
    q = []
    q.append(start)
    rlt = []
    print(q)
    while q:
        c = q.pop(0)
        for i in range(len(graph[c])):
            if graph[c] and visited[graph[c][i]] == 0:
                q.append(graph[c][i])
                visited[c] = 1
                rlt.append(graph[c][i])

    print(rlt)


for tc in range(1, T + 1):
    N, start = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    for i in range(0, N, 2):
        graph[arr[i]].append(arr[i+1])
    # print(graph)
    bfs(start)


    print(f'#{tc}')