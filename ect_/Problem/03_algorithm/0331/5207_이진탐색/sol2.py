import sys
sys.stdin = open('input.txt')

T = int(input())

# 재귀로 풀다 런타임 에러 난다...
# a 를 처음에 a +=1, a -= 1 로 제어 하다 보니까 + - - 이런 경우가 발생해서 틀렸던 거다.
def binary_search(arr, t, l, r):
    a = 0
    while l <= r:
        m = (l + r) // 2
        if arr[m] == t:
            return t
        elif arr[m] > t:
            if a == -1:
                return 0
            r = m - 1
            a = -1
        elif arr[m] < t:
            if a == 1:
                return 0
            l = m + 1
            a = 1
        else:
            return t

    return 0

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr_A = list(map(int, input().split()))
    arr_B = list(map(int, input().split()))
    arr_A.sort()
    rlt = 0
    cnt = 0
    # a = 0
    for target in arr_B:
        # print(f'target:{target}')
        rlt = binary_search(arr_A, target, 0, N-1)
        # print(f"rlt:{rlt}")
        if rlt:
            cnt += 1

    print(f'#{tc} {cnt}')