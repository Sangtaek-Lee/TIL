import sys

sys.stdin = open('input.txt')

T = int(input())

# 버블 소트를 짝수 인덱스와 홀수 인덱스 조건으로 나누어 실행

for tc in range(1, T + 1):
    num_ea = int(input())
    num_list = list(map(int, input().split()))

    for i in range(num_ea):
        # 짝수 인덱스 일 때 큰값을 제일 앞으로 오게
        if i % 2 == 0:                      # 2로 나머지가 0이면 짝수
            for j in range(i, num_ea-1):
                if num_list[j] > num_list[j+1]: # 앞 값과 비교하여 크면 자리 바꿈
                    num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
            num_list[i], num_list[num_ea-1] = num_list[num_ea-1], num_list[i]   # 뒤로 가 있는 큰 값을 앞 값과 자리 바꿔줌
        # 홀수 인덱스 일 때 큰값을 제일 앞으로 오게
        if i % 2 != 0:                      # 2로 나머지가 1이면 홀수
            for j in range(i, num_ea-1):
                if num_list[j] < num_list[j+1]: # 앞 값과 비교하여 작으면 자리 바꿈
                    num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
            num_list[i], num_list[num_ea-1] = num_list[num_ea-1], num_list[i]   # 뒤로 가 있는 작은 값을 앞 값과 자리 바꿔줌

    print(f'#{tc} ', end='')
    for i in range(10):
        print(num_list[i], end=' ')
    print()

