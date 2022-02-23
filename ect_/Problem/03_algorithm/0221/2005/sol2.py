import sys

sys.stdin = open('input.txt')

T = int(input())

def pascal(N):
    stack = [[0]*i for i in range(1, N+1)]  # 계단식 2차 배열
    stack[0][0] = 1                         # 초기 값 설정
    print(stack[0][0])                      # 초기 값 출력
    for i in range(1, N):
        for j in range(i+1):                # 배열을 1씩 늘려가며 push할 것이다.
            x = 0
            if j < len(stack[i-1]) and j > 0:         # 왼쪽 위 조건
                x += stack[i-1][j]          # 왼쪽 위 더한다
                x += stack[i - 1][j - 1]
            # if j > 0:                       # 오른쪽 위 조건
            #     x += stack[i-1][j-1]        # 오른쪽 위 더한다
            stack[i][j] = x                 # 더한값을 배열에 써준다.
            print(x, end=' ')                # 출력한다.
        print()

for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')
    pascal(N)

