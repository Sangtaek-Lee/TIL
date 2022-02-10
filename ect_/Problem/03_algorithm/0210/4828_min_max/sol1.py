import sys

sys.stdin = open('input.txt')

T = int(input())                                            # Test Case 선언

for tc in range(1, T + 1):                                  # case 별 계산
    numbers_length = int(input())                           # 숫자 개수 선언
    numbers_list = list(map(int, input().split()))          # 숫자 값들 리스트 선언
    max_val = numbers_list[0]                               # max 초기 값을 리스트 첫번 째 값으로 선언
    min_val = numbers_list[0]                               # min 초기 값을 리스트 첫번 째 값으로 선언
    for i in range(1, numbers_length):                      # min max 값 찾기 위한 for
        if numbers_list[i] > max_val:                       # max 조건 만족 시
            max_val = numbers_list[i]                       # max 값 재설정
        if numbers_list[i] < min_val:                       # min 조건 만족 시
            min_val = numbers_list[i]                       # min 값 재설정
    delta_max_min = max_val - min_val                       # delta 값 선언
    print(f'#{tc} ', delta_max_min)