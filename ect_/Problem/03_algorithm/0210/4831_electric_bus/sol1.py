import sys
sys.stdin = open('input.txt')

T = int(input())


#

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    charger_station = list(map(int, input().split()))
    station_bool = [0]*(N+1)


# 앞으로 정해진 숫자 만큼 전진 한 후 충전 소가 있으면 다시 전진 없다면 뒤로 한칸씩 가며 정해진 숫자만큼 뒤로가면 도착하지 못한 경우이다.

    for i in charger_station:
        station_bool[i] += 1
    station_bool[0] = 1

    current_status = 0
    charging_num = 0
    back_num = 0

    while True:
        # print(current_status)
        if station_bool[current_status] == 1:   # 현재 위치에 충전소가 있다면
            current_status += K                 # 현재 위치에서 k만큼 전진
            if current_status >= N:             # 도착하면 while문 빠져나온다.
                break
            charging_num += 1
        if station_bool[current_status] == 0:   # 현재 위치에 충전소가 없으면
            current_status -= 1                 # 뒤로 간다
            back_num += 1                       # 도착하지 못할경우를 알기 위해 뒤로 몇번간지 센다.
            if back_num == K:                   # k번 만큼 뒤로가면 도착하는 경우가 없기 때문에
                charging_num = 0                # 출력 0으로 설정
                break                           # 반복문 빠져 나온다.

    print(f'#{tc}', charging_num)











