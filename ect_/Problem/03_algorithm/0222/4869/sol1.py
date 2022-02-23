import sys

sys.stdin = open('input.txt')

T = int(input())

def check(area):
    i = area // 10                                      # 가로를 index로 사용하기 위해 10으로 나눔
    stack = [0, 1, 3] + [0]*(i -2)                      # 초기값 설정
    for k in range(3, i + 1):
        stack[k] = stack[k - 2] * 2 + stack[k - 1]      # 값들을 구해보니 점화식이 f[n] = f[n-2]*2 + f[n-1] 이였다.
    return stack[i]                                     # 끝 값 리턴

for tc in range(1, T + 1):
    N = int(input())
    rlt = check(N)
    print(f'#{tc} {rlt}')