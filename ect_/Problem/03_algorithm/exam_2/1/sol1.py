import sys
sys.stdin = open('input.txt')

T = int(input())

def dfs(s, p, N):
    # 처음 오면 어떻게 해야 될까
    if 1 > s > 10:
        return
    distance = 0
    if block[s] == 0:
        block[s] = 1
        distance += 1
    print(block)
    # 오른쪽 넣었다가
    dfs(s+1, p, N)


    # 빼고

    # 다시 왼쪽 넣자



    return [0]      # 임시 값

for tc in range(1, 1+T):
    #입력값 받아오자
    N = int(input())    # 낚시터 개수
    gate = 3            # 게이트는 항상 3개
    #[gate 위치, 낚시꾼]
    data_list = [list(map(int, input().split())) for _ in range(gate)]
    print(N, data_list)
    tmp_list = []
    for i in range(3):
        block = [1] + [0] * N
        tmp_list += dfs(data_list[i][0], data_list[i][1], N)
    rlt = min(tmp_list)

    print(f'#{tc} {rlt}')