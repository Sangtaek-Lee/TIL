import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, 1 + T):
    N, M = map(int, input().split())
    q = list(map(int, input().split()))
    idx = M % N
    rlt = q[idx]
    print(f'#{tc} {rlt}')