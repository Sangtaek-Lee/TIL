import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    days = int(input())
    day_price = list(map(int, input().split()))
    gain = 0

    # 오늘 기준으로 뒤에 가격을 쭉 보고 오늘 가격 보다 크면 사고 큰가격에서 오늘 가격을 빼서 더한다.
    for day in range(days):         # 하루
        max_price = 0
        for i in range(days-1, day-1, -1):
            if max_price < day_price[i]:
                max_price = day_price[i]
        if max_price > day_price[day]:
            gain += max_price - day_price[day]

    print(f'#{tc}', gain)

