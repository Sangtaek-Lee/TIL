import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N, K = map(int, input().split())
    # print(N, K)
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    sum_list = []
    cnt = 0
    for i in range(1, 1 << N):
        sum_arr = []
        for j in range(N):
            if i & 1 << j:
                # print(j, end=' ')
                sum_arr.append(A[j])
        sum_list.append(sum_arr)

    for i in sum_list[1:]:
        total = 0
        for n in i:
            total += n
        if len(i) == N and total == K:
            cnt += 1

    print(f'#{tc}', cnt)

