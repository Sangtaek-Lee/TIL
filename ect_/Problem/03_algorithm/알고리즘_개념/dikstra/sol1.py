# 시작 점과 목표 지점 사이의 최소 가중치의 합을 구할 수 있는 알고리즘
# 1. D 리스트 안에 시작점에서 목표 지점 사이의 가중치를 쭉 써준다.
# 2. 후 D 리스트 안에 가장 작은 가중치 값을 찾아
# 3. 최솟값 가중치를 기준으로 비교하여 작은 값을 D 리스트에 써준다.
#       최솟값 가중치 + 최솟값 가중치 지점에서 다음 지점 VS 시작 점에서 목표 지점
# 4. 이를 전체 노드 수 만큼 반복한다. (2~3 을 반복)
# 5. 그렇게 되면 D 리스트 안에는 시작점에서 각 지점까지 가는데 최솟 가중치 값들의 합이 나타내어져 있다.
# 6. O(n^2) 의 계산시간 이지만 가장 작은 가중치 값을 찾는 것(정렬)을
#    Min heap 자료구조로 구현하여 O(log(n)) 으로 나타 낼 시 O(nlog(n))이 된다.

import sys
sys.stdin = open("input.txt")


def dijkstra(s, V):
    visited = [0] * (V + 1)

    visited[s] = 1
    for i in range(V + 1):
        D[i] = adj[s][i]  # 초기 D 리스트 만들기

    for _ in range(V):
        minV = INF  # 선택된 목적지까지 가는 가중치
        w = 0  # 이번에 선택된 목적지

        # 방문하지 않은 노드 중에서, 가장 비용이 적은 노드 선택
        for i in range(V + 1):
            if not visited[i] and minV > D[i]:
                w = i
                minV = D[i]

        visited[w] = 1  # 방문 표시
        for i in range(V + 1):
            if 0 < adj[w][i] < INF:  # 연결되어있으면
                D[i] = min(D[i], D[w] + adj[w][i])

T = int(input())
for tc in range(1, 1+T):
    INF = 987654321
    V, E = map(int, input().split())
    adj = [[INF] * (V + 1) for _ in range(V + 1)]

    for i in range(V + 1):
        adj[i][i] = 0

    for _ in range(E):
        u, v, w = map(int, input().split())
        adj[u][v] = w

    D = [0] * (V + 1)
    dijkstra(0, V)

    print(D)
