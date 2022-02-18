import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    A_list = [2, 3, 5, 7, 11]
    cnt_list = [0]*5
    i = 0
    while i < 5:
        if N % A_list[i] == 0:
            N = N / A_list[i]
            cnt_list[i] += 1
            continue
        else:
            i += 1
        # print(N)
    print(f'#{tc}', end=' ')
    for i in range(5):
        print(cnt_list[i], end=' ')
    print()



