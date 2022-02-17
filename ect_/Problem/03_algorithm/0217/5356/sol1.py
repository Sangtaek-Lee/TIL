import sys

sys.stdin = open('input.txt')

T = int(input())


# 공백을 어떻게 처리 할까? ''로 처리?
# 제일 긴 문자열 길이를 구하고 나머지를 ''로 처리

for tc in range(1, T + 1):
    matrix = [list(input()) for _ in range(5)]
    print(matrix)
    # max 열 구하기
    max_col = 0
    for i in range(5):
        if max_col < len(matrix[i]):
            max_col = len(matrix[i])
    print(f'#{tc} ')

