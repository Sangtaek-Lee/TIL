import sys

sys.stdin = open('input.txt')

T = 10

for tc in range(1, T + 1):
    limit = int(input())
    box_num_list = list(map(int, input().split()))

    for i in range(limit+1):
        max_val = box_num_list[0]
        max_idx = 0
        min_val = box_num_list[0]
        min_idx = 0
        for j in range(1, len(box_num_list)):
            if box_num_list[j] > max_val:
                max_val = box_num_list[j]
                max_idx = j
            if box_num_list[j] < min_val:
                min_val = box_num_list[j]
                min_idx = j

        if i == limit:
            print(f'#{tc} ', max_val-min_val)
            continue

        box_num_list[max_idx] -= 1
        box_num_list[min_idx] += 1
