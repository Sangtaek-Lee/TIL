import sys
sys.stdin = open('input_3.txt')

T = int(input())
for tc in range(1, T+1):
    columns = int(input())
    row_val_list = list(map(int, input().split()))
    # print(row, columns)
    a = 0
    max_drop = 0
    i = 0
    for row in row_val_list:
        cnt = 0
        for col in range(i, columns):
            if row > row_val_list[col]:
                cnt += 1
        i += 1
        if cnt > max_drop:
            max_drop = cnt
    print(f'#{tc}', max_drop)









    # print(f'#{i} ')


