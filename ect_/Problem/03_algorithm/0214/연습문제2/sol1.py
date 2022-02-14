import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    list_random = list(map(int, input().split()))
    for i in range(1, 1 << len(list_random)):
        sum_arr = 0
        for j in range(len(list_random)):
            if i & 1 << j:
                sum_arr += list_random[j]
        if sum_arr == 0:
            print(f'#{tc} ', '1')
            break
    if sum_arr != 0:
        print(f'#{tc} ', '0')

