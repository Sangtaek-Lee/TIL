import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_val = 0
    for i in range(N):
        num_sum = 0
        for j in range(K):
            if i + j < N:
                num_sum += arr[i][i+j]
            if max_val < num_sum:
                max_val = num_sum


    print(f'#{tc} {max_val}')