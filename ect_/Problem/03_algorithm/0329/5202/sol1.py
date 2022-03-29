import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 정렬을 해서 풀고 싶은데 두개 원소로 이루어진 원소를 하나의 원소 기준으로 정렬하는 방법은?
    # 시작시간 기준으로 내림 차순 하면 배열을 순서대로 훑으면 항상 시작값이 고정이 되버리네?
    # 빨리 끝나는데 최대한 늦게 시작하는게 best case?
    # 그럼 end 값 기준으로 오름 차순, start 값 기준으로 내림 차순 정렬
    # 그러면 sort로 안되네? 조건줘서 정렬해야 되네? lambda?
    # 코드 작성 결과 시작 시간 정렬은 의미 없다.
    arr.sort(key = lambda x: (x[1], -x[0]))
    # print(arr)
    i = 0                       # 시작 시간을 나타내기 위한 idx
    j = 1                       # 종료 시간을 나타내기 위한 idx
    cnt = 1                     # 이용 횟 수
    while j < len(arr):
        start, end = arr[i]             # 현재 시간
        next_start, next_end = arr[j]   # 다음 시간
        if end <= next_start:           # 현재 종료 시간이 다음 시작시간 보다 같거나 작아야 다음 작업을 할 수 있다.
            cnt += 1                    # 만족시 cnt + 1
            # print(f'cnt:{cnt} [{start}, {end}], [{next_start}, {next_end}]')
            i = j                       # 다음 시간을 현재 시간으로 바꿔 준다.
        j += 1                          # 다음 시간의 idx 증가


    print(f'#{tc} {cnt}')