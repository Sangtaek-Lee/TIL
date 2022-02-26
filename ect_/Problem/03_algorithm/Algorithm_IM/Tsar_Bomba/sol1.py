import sys

sys.stdin = open('input.txt')

T = int(input())

def tsar_boomba(N, P, matrix):
    righ_angle = [[0, 1], [1, 0], [0, -1], [-1, 0]]             # 직각 : 우 하 좌 상
    opposite_angle = [[1, 1], [1, -1], [-1, -1], [-1, 1]]       # 대각 : 우하 좌하 좌상 우상
    max_val = 0

    for i in range(N):          # 2차 배열을 순회한다
        for j in range(N):
            sum_r = matrix[i][j]
            sum_o = matrix[i][j]
            sum_val = 0
            for p in range(1, P+1):             # Power 만큼 더해야 하니까 delta 에 power를 곱하여 표현
            # 직각의 Tsar boomba
                for di, dj in righ_angle:       # 방향 순회
                    row = i + di*p              # row delta 만큼 움직인다
                    col = j + dj*p              # col delta 만큼 움직인다.
                    if 0 <= row < N and 0 <= col < N:   # matrix 범위 안에서만 수행한다.
                        sum_r += matrix[row][col]      # 더해준다
            # 대각의 Tsar boomba
                for di, dj in opposite_angle:  # 방향 순회
                    row = i + di * p  # row delta 만큼 움직인다
                    col = j + dj * p  # col delta 만큼 움직인다.
                    if 0 <= row < N and 0 <= col < N:  # matrix 범위 안에서만 수행한다.
                        sum_o += matrix[row][col]  # 더해준다
            # print(sum_r, sum_o)
            if sum_o > sum_r:               # 최댓값 찾기
                if max_val < sum_o:
                    max_val = sum_o
            else:
                if max_val < sum_r:
                    max_val = sum_r
    return max_val

for tc in range(1, T + 1):
    N, P = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # print(N, P)
    # print(matrix)
    rlt = tsar_boomba(N, P, matrix)
    print(f'#{tc} {rlt}')

