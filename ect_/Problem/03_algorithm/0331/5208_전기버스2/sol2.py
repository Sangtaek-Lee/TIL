import sys
sys.stdin = open('input.txt')

# 목표 : 최소한의 교환횟수

def dfs(s):
    global rlt, cnt
    if s >= N:
        if cnt < rlt:
            rlt = cnt
        return
    elif rlt <= cnt:
        return
    for i in tree[s]:
        cnt += 1
        # print(f'visit {s}->{i}')
        # print(f'cnt: {cnt}')
        dfs(i)
        cnt -= 1



T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = arr[0]
    tree = [0]*(N)
    rlt = 1000
    cnt = 0
    for i in range(1, N):
        child = [x+i+1 for x in range(arr[i]) if x+i+1 <= N]
        tree[i] = child
    # print(f'tree:{tree}')
    dfs(1)
    print(f'#{tc} {rlt-1}')