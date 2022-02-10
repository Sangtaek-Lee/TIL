import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    card_num = int(input())
    card = int(input())
    card_num_list = [0]*10
    for i in range(card_num):
        card_num_list[card % 10] += 1
        card //= 10
    max_num = 0
    max_val = 0
    for i in range(10):
        if card_num_list[i] >= max_num:
            max_num = card_num_list[i]
            max_val = i

    print(f'#{tc}', max_val, max_num)

