import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    temp_list = [list(map(int,input().split())) for _ in range(Q)]
    rlt_list = [0]*N
    # print(temp_list)
    for i in range(Q):
        for j in range(temp_list[i][0]-1,temp_list[i][1]):
            rlt_list[j] = i + 1
    print(f'#{tc}', *rlt_list[:])

    # print(f'#{tc}', end=' ')
    # for i in range(N):
    #     print(rlt_list[i], end=' ')

