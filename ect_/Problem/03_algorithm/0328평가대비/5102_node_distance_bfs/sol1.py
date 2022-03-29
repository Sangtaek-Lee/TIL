# 출력 출발 노드에서 최소 몇 개 간선을 지나면 도착 노드에 갈 수 있는지
# 입력을 그래피로 정리
# bfs 로 도착 노드 찾기

import sys
from pprint import pprint
sys.stdin = open('input.txt')

def bfs():
    visited = [0] * (V+1)
    Q = []
    Q.append(S)
    visited[S] = 1
    while Q:
        node = Q.pop(0)
        for i in range(V+1):
            if graph[node][i] == 1 and visited[i] == 0:
                visited[i] = visited[node] + 1
                Q.append(i)
    if visited[G]:
        return visited[G] - 1
    else:
        return 0

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    graph = [[0]*(V+1) for _ in range(V+1)]
    for edge in arr:
        graph[edge[0]][edge[1]] = 1
        graph[edge[1]][edge[0]] = 1

    rlt = bfs()
    print(f'#{tc} {rlt}')