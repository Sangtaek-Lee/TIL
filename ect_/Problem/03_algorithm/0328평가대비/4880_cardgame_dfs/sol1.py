import sys
sys.stdin = open('input.txt')

T = int(input())


def rsp(a, b):
    if (a - b) % 2 == 0:
        return


def fn(S, N):
    mid = (1 + N) // 2




    pass

for tc in range(1, T + 1):
    N = int(input())
    arr = [0] + list(map(int, input().split()))

    # 1 ~ (1+N) // 2
    # (1+N) // 2 + 1 ~ N
    rlt = fn(1, N)

    print(f'#{tc} {rlt}')