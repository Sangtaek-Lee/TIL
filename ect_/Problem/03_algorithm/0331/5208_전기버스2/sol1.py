import sys
sys.stdin = open('input.txt')

# 목표 : 최소한의 교환횟수
# 최단거리 이므로 bfs로 풀자
# bfs 로 1 에서 충전 지 용량까지 idx 더해 주면서 queue에 넣어 주고 목표 거리 도착 시 종료 해 주자

def dfs(s):
    global rlt
    stack.append(s)
    if s == N:
        if rlt > visited[s]:
            rlt = visited[s]
            return
        else:
            return
    elif rlt < visited[s]:
        return
    else:
        node = stack.pop()
        for i in range(len(tree[node])):
            visited[i] = visited[s] + 1
            dfs(tree[node][i])
            print(f'append {tree[node][i]} node')



T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = arr[0]
    tree = [0]*(N)
    stack = []
    visited = [0]*(N+1)
    rlt = 1000
    for i in range(1, N):
        child = [x+i+1 for x in range(arr[i]) if x+i+1 <= N]
        tree[i] = child
    print(f'tree:{tree}')
    dfs(1)
    print(f'#{tc} {rlt}')