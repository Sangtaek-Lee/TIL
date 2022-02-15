import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    list_random = list(map(int, input().split()))           # 입력값을 정수 리스트로 받아옴
    for i in range(1, 1 << len(list_random)):               # for 사용 부분 집합의 개수 (2^len) 만큼 i를 반복 (1부터 한 이유는 0 공집합 제외 시키려)
        sum_arr = 0                                         # 부분집합의 합을 구하기 위한 sum_arr 변수 선언
        for j in range(len(list_random)):                   # 부분 집합 비교를 위한 리스트 원소 만큼 반복문
            if i & 1 << j:                                  # 부분 집합의 각 비트가 1인지를 검사
                sum_arr += list_random[j]                   # sum_arr에 더한다.
        if sum_arr == 0:                                    # 합이 0일 때
            print(f'#{tc} ', '1')                           # 1 출력
            break                                           # 만족 시 계산 그만하고 반복문 빠져 나온다.
    if sum_arr != 0:                                        # 반복문 계산을 끝내도 0이 아닐 시 0 출력
        print(f'#{tc} ', '0')

