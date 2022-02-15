import sys

sys.stdin = open('input.txt')

T = 10

for tc in range(1, T + 1):
    limit = int(input())                                # 덤프 할 수 있는 숫자
    box_num_list = list(map(int, input().split()))      # 입력값 list에 담는다



# 최댓값 최솟값을 찾은 후 덤프를 한 후 그것을 정해진 덤프 수 만큼 반복 해 주면 된다. 제일 큰 값에서 작은 값을 빼고 출력한다.

    for i in range(limit+1):                            #
        max_val = box_num_list[0]
        max_idx = 0
        min_val = box_num_list[0]
        min_idx = 0
        for j in range(1, len(box_num_list)):           # 가장 높은 상자와 가장 낮은 상자를 반복문을 통해 찾음
            if box_num_list[j] > max_val:
                max_val = box_num_list[j]
                max_idx = j
            if box_num_list[j] < min_val:
                min_val = box_num_list[j]
                min_idx = j

        if i == limit:                                  # 덤프
            print(f'#{tc} ', max_val-min_val)
                                                # 마지막 덤프 후 최댓값

        box_num_list[max_idx] -= 1                      # 높은 상자에서 낮은 상자로 덤프 한다
        box_num_list[min_idx] += 1
