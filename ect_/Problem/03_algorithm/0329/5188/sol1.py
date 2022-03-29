import sys
sys.stdin = open('input.txt')

dx = [0, 1]
dy = [1, 0]

def dfs(s, sum_num):
    global rlt
    sum_num += arr[s[0]][s[1]]      # 방문 값 더하기
    if rlt < sum_num:               # 런타임 에러로 아래 두 조건 추가, rlt 값이 현재까지 최종 결과 최솟값 보다 작다면 리턴하여 계산 종료
        return
    if [s[0], s[1]] == [N - 1, N - 1]:  # 2,2 도착하면 rlt에 값 써준다. 최솟값 조건은 위에서 걸러진다.
        rlt = sum_num
        return
    x = s[0]
    y = s[1]
    for i in range(2):      # 오른쪽, 아래 방문
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < N and ny < N:   # 범위 안에 들어오면 다시 dfs
            dfs([nx, ny], sum_num)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    rlt = 9999999           # min 값 찾기 위해 적당히 큰 수
    start = [0, 0]          # 시작점
    sum_num = 0             # 합
    dfs(start, sum_num)
    print(f'#{tc} {rlt}')