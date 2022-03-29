import sys
sys.stdin = open('input.txt')

def dfs(s, sum_num, cnt):
    global rlt
    if cnt == N-1:                  # 종료 조건으로 cnt가 마지막 노드에서 1로 가는 경우를 제외한 N-1과 같을 때 종료
        sum_num += arr[s][1]        # 마지막 노드에서 시작 노드로 갈때 값
        if sum_num < rlt:           # 최솟값 찾기 위한 조건
            rlt = sum_num
            return

    if sum_num > rlt:               # 계산 중간 현재 min 값 보다 더 크다면 바로 계산 종료
        # print('over')
        return

    for i in range(2, N+1):         # 시작점 1 제외 2부터 N까지
        if s != i and visited[i] == 0:  # 대각선 요소 값은 0이므로 계산 제외, 방문하지 않은 곳
            visited[i] = 1              # 방문 표시
            # print(cnt, ':', [s,i], sum_num + arr[s][i])
            dfs(i, sum_num + arr[s][i], cnt + 1)    # 다음 노드로 가며, 현재까지 더해진 값에 다음 노드 값 더해 준다, cnt 1 증가
            visited[i] = 0              # 다음 경우를 생각 현재 노드 visited 초기화

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]   # 문제와 동일하게 인덱스 사용하기 위해 0채워줌
    visited = [0] * (N+1)   # 방문 표시
    rlt = 99999             # min 값 구하기 위해 적당히 큰값
    dfs(1,0,0)              # (node, 탐색하면 더해지는 값, 종료하기 위해 몇번 째 방문인지 cnt)
    print(f'#{tc} {rlt}')