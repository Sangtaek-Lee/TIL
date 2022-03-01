import sys

sys.stdin = open('input.txt')

T = int(input())

def min_cnt(N, target):
    cnt = 0
    if target[0] == 1:
        led = [1] * N
        cnt += 1
    else:
        led = [0] * N
    for i in range(2, N+1):
        k = i - 1
        if led[k] != target[k]:
            cnt += 1
            while i < N + 1:
                if led[k-1] == 0:
                    led[k-1] = 1
                else:
                    led[k-1] = 0
                i *= 2
            print(led)
        if target == led:
            return cnt

for tc in range(1, T + 1):
    N = int(input())
    target = list(map(int, input().split()))
    rlt = min_cnt(N, target)
    print(f'#{tc} {rlt}')

