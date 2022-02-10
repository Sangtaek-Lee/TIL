import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    charger_station = list(map(int, input().split()))
    station_bool = [0]*(N+1)
    for i in charger_station:
        station_bool[i] += 1
    station_bool[0] = 1

    current_status = 0
    charging_num = 0
    back_num = 0
    while True:
        # print(current_status)
        if station_bool[current_status] == 1:
            current_status += K
            if current_status >= N:
                break
            charging_num += 1
        if station_bool[current_status] == 0:
            current_status -= 1
            back_num += 1
            if back_num == K:
                charging_num = 0
                break

    print(f'#{tc}', charging_num)











