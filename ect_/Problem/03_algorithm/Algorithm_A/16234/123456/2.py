# 색종이를 붙일 기본 배열
array = [list(map(int, input().split())) for _ in range(10)]
papers = {}

# 종이 개수 저장
for i in range(1, 6):
    papers[i] = 5

# 정답을 저장할 변수
cnt_min = 30


# 해당 위치에서 붙일 수 있는 종이의 최대 크기 리턴
def check(r, c):
    for n in range(2, 6):
        for i in range(r, r + n):
            for j in range(c, c + n):
                if not (0 <= i < 10) or not (0 <= j < 10) or array[i][j] != 1:
                    return n - 1
    return 5


# 종이를 붙이거나 떼기
# state == 1이면 붙이고, state == 0이면 뗀다
def stickUnstick(r, c, n, state):
    for i in range(r, r + n):
        for j in range(c, c + n):
            array[i][j] = (state + 1) % 2


# dfs 함수 구현
# 인덱스는 r,c 이용
def dfs(r, c, cnt):
    global cnt_min
    # 탐색의 끝에 도달하면 cnt_min 갱신
    if r >= 9 and c > 9:
        cnt_min = min(cnt_min, cnt)
    # cnt가 cnt_min보다 크면 확인할 필요 없음
    if cnt >= cnt_min: return
    # c가 9를 넘어가면, r에 1을 더하고 c는 0으로 초기화 후 dfs
    if c > 9:
        dfs(r + 1, 0, cnt);
        return

    # 해당 칸이 1이라면 종이를 붙여야함
    if array[r][c] == 1:
        # 어느 크기의 종이 까지 붙일 수 있는지 판단
        n = check(r, c)
        # 가능한 종이를 모두 붙이고, 떼보며 dfs 반복
        for i in range(1, n + 1):
            if papers[i] >= 1:
                # 종이 붙이기
                stickUnstick(r, c, i, 1)
                papers[i] -= 1
                dfs(r, c + 1, cnt + 1)
                # 종이 떼기
                stickUnstick(r, c, i, 0)
                papers[i] += 1
    # 해당사항 없으면 다음 열에 대해 반복
    else:
        dfs(r, c + 1, cnt)


# 0,0의 위치부터 dfs 시작
dfs(0, 0, 0)

# cnt_min이 초기화 되지 않았으면, 가능한 경우가 없으므로 -1 출력
# 그렇지 않다면 cnt_min 출력
if cnt_min == 30:
    print(-1)
else:
    print(cnt_min)