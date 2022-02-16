import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))

    cnt = 1
    max_cnt = 1

    for i in range(N-1):
        if num_list[i+1] > num_list[i]:
            cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
        else:
            cnt = 1


    print(f'#{tc}', max_cnt)

