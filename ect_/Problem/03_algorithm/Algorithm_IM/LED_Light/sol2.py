import sys

sys.stdin = open('input.txt')

T = int(input())

def min_cnt(N, target):
    global cnt
    target = [0] + target
    if target[1] == 1:
        led = [0] + [1] * (N)
        cnt += 1
    else:
        led = [0] * (N+1)
    for i in range(2, N+1):
        if target[i] != led[i]:
            for j in range(i, N+1):
                if j % i == 0:
                    if led[j]:
                        led[j] = 0
                    else:
                        led[j] = 1
            cnt += 1
        if led == target:
            return cnt

for tc in range(1, T + 1):
    N = int(input())
    target = list(map(int, input().split()))
    cnt = 0
    rlt = min_cnt(N, target)
    print(f'#{tc} {rlt}')

