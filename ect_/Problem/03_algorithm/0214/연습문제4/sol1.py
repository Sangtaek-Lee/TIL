import sys
sys.stdin = open('input.txt')

T = 10


for tc in range(1, T + 1):
    number = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]  # 입력을 matrix 형태로 받아옴
    max_value = 0                                                   # max값 찾기 위해 변수 선언
    sum_diag_r = 0                                                  # 오른쪽 대각선 합을 위한 변수
    sum_diag_l = 0                                                  # 왼쪽 대각선 합을 위한 변수


    for i in range(100):            # 행의 합, 행
        sum_row = 0                 # 행의 합을 구하기 위한 변수
        for j in range(100):        # 열
            sum_row += matrix[i][j] # i행 0~100열 합을 구함
        if sum_row > max_value:     # i행의 합과 최댓값 비교
            max_value = sum_row     # 만족시 값 교체

    for i in range(100):            # 열의 합, 열
        sum_col = 0                 # 행의 합을 구하기 위한 변수
        for j in range(100):        # 행
            sum_col += matrix[j][i] # j행 0~100열 합을 구함
        if sum_col > max_value:     # i열 합과 최댓값 비교
            max_value = sum_col     # 만족 시 값 교체

    for i in range(100):            # 우 대각 합
        sum_col += matrix[i][i]     # 우 대각은 행열 값이 같다
    if sum_diag_r > max_value:      # 비교하여 만족 시 최댓값 교체
        max_value = sum_diag_r

    for i in range(100):            # 좌 대각 합
        for j in range(99, -1, -1): # 좌 대각은 행열 인덱스 값이 반대로 증가 감소한다.
           sum_col += matrix[i][j]  # 0,99 ~ 99,0 까지 합
        if sum_diag_l > max_value:  # 최댓값 비교
            max_value = sum_diag_l  # 만족시 값 교체

    print(f'#{tc}', max_value)

