import sys

sys.stdin = open('input.txt')

T = int(input())

def min_cnt(N, target):
    led = [0]*N
    cnt = 0
    if target[0] == 1:
        led[0] = 1
        cnt += 1
    for i in range(2, N+1):             # 0, 1의 배수는 해당사항 없으니 2의 배수 부터 (2, 3, 4, 5)
        if led[i - 1] != target[i - 1]:            # index 는(1, 2, 3, 4)
            print(f'i:{i}')
            k = i
            cnt += 1                    # cnt 증가
            if led[i - 1] == 0:
                while k < N + 1:
                    led[k - 1] = 1
                    k *= 2
            else:
                while k < N + 1:
                    led[k - 1] = 0
                    k *= 2
        # list와 비교하여 맞는지 비교하여 cnt 값 리턴
        if target == led:
            return cnt

for tc in range(1, T + 1):
    N = int(input())
    target = list(map(int, input().split()))
    rlt = min_cnt(N, target)
    print(f'#{tc} {rlt}')

