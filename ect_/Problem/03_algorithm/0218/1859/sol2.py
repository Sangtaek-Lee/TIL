import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    days = int(input())
    day_price = list(map(int, input().split()))
    gain = 0

    max_price = day_price[days-1]
    for i in range(days-2, -1, -1):
        if max_price < day_price[i]:
            max_price = day_price[i]
        else:
            gain += max_price - day_price[i]

    print(f'#{tc}', gain)

