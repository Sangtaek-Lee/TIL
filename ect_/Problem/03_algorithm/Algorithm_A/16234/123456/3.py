import sys
sys.setrecursionlimit(10**5)
# 입력 받기
N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]
# 인접행렬
adj = [[] for _ in range(2*(2*N-1))]
# 이분 매칭 정보 저장
matched = [-1] * 2 * (2*N-1)

# 이분 그래프 만들기
for r in range(N):
    for c in range(N):
        # 비숍을 놓을 수 있는 자리라면, 대각선 노드 정보 갱신
        if array[r][c] == 1:
            adj[r-c+N-1].append(r+c+2*N-1)
            adj[r+c+2*N-1].append(r-c+N-1)

# dfs 탐색
def dfs(start):
    if visited[start]:
        return False
    visited[start] = True

    for node in adj[start]:
        # 대상 노드가 연결되어있지 않거나,
        # 연결되어있을 경우 연결된 노드의 재연결이 가능하다면
        if matched[node] == -1 or dfs(matched[node]):
            matched[start] = node
            matched[node] = start
            return True
    return False

cnt = 0
# 좌상단 방향 대각선 노드에 대해 DFS 수행
for i in range(2*N-1):
    visited = [False] * (2*N-1)
    # 비숍 개수 +1
    if dfs(i):
        cnt += 1

print(cnt)