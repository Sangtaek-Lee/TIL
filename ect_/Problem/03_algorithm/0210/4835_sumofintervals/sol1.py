import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    list_length, sum_num = map(int, input().split())
    # print(list_length, sum_num)
    numbers_list = list(map(int, input().split()))

    sum_list = [0]*(list_length - sum_num + 1)
    for i in range(0,list_length-sum_num+1):
        for j in range(sum_num):
            sum_list[i] += numbers_list[i+j]
    # print(sum_list)
    max_val = sum_list[0]
    min_val = sum_list[0]
    for i in range(len(sum_list)):
        if sum_list[i] > max_val:
            max_val = sum_list[i]
        if sum_list[i] < min_val:
            min_val = sum_list[i]
    delta_max_min = max_val - min_val

    print(f'#{tc} ', delta_max_min)

