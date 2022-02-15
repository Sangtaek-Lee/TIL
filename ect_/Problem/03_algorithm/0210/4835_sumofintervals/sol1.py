import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    list_length, sum_num = map(int, input().split())    # list 길이, 연속하여 더할 개수
    # print(list_length, sum_num)
    numbers_list = list(map(int, input().split()))      # list

    sum_list = [0]*(list_length - sum_num + 1)          # 더한 값들의 개수만큼 빈 리스트
    for i in range(0,list_length-sum_num+1):            # 
        for j in range(sum_num):                        # sum_num 개씩 더한다
            sum_list[i] += numbers_list[i+j]            # i 번째 인덱스를 기준으로 더한다.
    # print(sum_list)
    max_val = sum_list[0]
    min_val = sum_list[0]
    for i in range(len(sum_list)):                      # 반복문으로 최댓값 최솟값 찾음
        if sum_list[i] > max_val:
            max_val = sum_list[i]
        if sum_list[i] < min_val:
            min_val = sum_list[i]
    delta_max_min = max_val - min_val                   # delta 값 선언

    print(f'#{tc} ', delta_max_min)

