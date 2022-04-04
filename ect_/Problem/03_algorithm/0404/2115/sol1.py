import sys
sys.stdin = open('input.txt')

def comb(num, starting):
    global max_get_honey, selected_honey_idxs

    if num == 0:
        amount = 0
        value = 0
        for j in range(len(selected_honey_idxs)):
            amount += candidate_honey[selected_honey_idxs[j]]
            value += candidate_honey[selected_honey_idxs[j]]**2
        if amount <= C and max_get_honey < value:
            max_get_honey = value
    else:
        for i in range(starting, M):
            selected_honey_idxs[num-1] = i
            comb(num-1, i+1)

T = int(input())

for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    honey_map = [list(map(int, input().split())) for _ in range(N)]

    total_value = 0
    for r1 in range(N):
        for c1 in range(N):
            # 영역을 벗어나는 경우
            if c1+M-1 >= N:
                continue
            else:
                # 뭐가 최적인지 모르니 완전탐색을 해야함
                max_get_honey = 0
                candidate_honey = honey_map[r1][c1:c1+M]
                for i1 in range(1, M+1):
                    selected_honey_idxs = [0] * i1
                    comb(i1, 0)
                tmp_value1 = max_get_honey

                for r2 in range(r1, N):
                    c2_starting = 0
                    if r1 == r2:
                        c2_starting = c1+M

                    for c2 in range(c2_starting, N):
                        if c2+M-1 >= N:
                            continue
                        else:
                            max_get_honey = 0
                            candidate_honey = honey_map[r2][c2:c2+M]
                            for i2 in range(1, M+1):
                                selected_honey_idxs = [0] * i2
                                comb(i2, 0)
                            tmp_value2 = max_get_honey

                            if total_value < tmp_value1 + tmp_value2:
                                total_value = tmp_value1 + tmp_value2

    print(f'#{tc} {total_value}')