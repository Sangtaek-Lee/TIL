import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    card_num = int(input())                         # 카드가 총 몇장인지
    card = int(input())                             # 카드 값
    card_num_list = [0]*10                          # 값의 개수를 세기 위한 빈 리스트
    for i in range(card_num):                       # 카드 값 세기 위한 반복문
        card_num_list[card % 10] += 1               # 카드 값을 10으로 나눈 나머지 값을 인덱스로 하여 빈리스트에 카운트 (+1)
        card //= 10                                 # 카운트한 카드값 제거를 위해 10으로 나눈 몫
    max_num = 0                                     # max 카드 개수
    max_val = 0                                     # max 값
    for i in range(10):                             # 0~9 까지 값
        if card_num_list[i] >= max_num:             # 반복문을 돌며 카드 개수 최댓값을 찾는다.
            max_num = card_num_list[i]               
            max_val = i                             # car_num_list 의 인덱스 값은 카드의 숫자, value 는 카드 개수

    print(f'#{tc}', max_val, max_num)

