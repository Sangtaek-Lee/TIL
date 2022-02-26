import sys

sys.stdin = open('input.txt')

T = int(input())

def min_cnt(N, target):
    led = [0]*N
    for i in range(2, N+1):           # 1의 배수는 해당사항 없으니 2의 배수 부터
        # print(i)
        while i < N + 1:
            print(i)

            i = i + i
            # print(i)

        # list와 비교하여 맞는지 비교하여 cnt 값 리턴
        if target == led:
            return cnt

for tc in range(1, T + 1):
    N = int(input())
    target = list(map(int, input().split()))
    rlt = min_cnt(N, target)
    print(f'#{tc} {rlt}')

