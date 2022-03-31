import sys
sys.stdin = open('input.txt')

T = int(input())

def binary_search(arr, t, l, r):
    global a
    m = (l+r) // 2
    # print(f'l:{l} m:{m}, r:{r}, visit:{arr[m]}, target:{t}, a:{a}')
    if arr[m] == t:
        return t
    elif l == r:
        return 0
    elif arr[m] > t:
        a -= 1
        return binary_search(arr, t, l, m-1)
    elif arr[m] < t:
        a += 1
        return binary_search(arr, t, m+1, r)

    if a not in [-1, 0, 1]:
        return 0
    return 0

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr_A = sorted(list(map(int, input().split())))
    arr_B = list(map(int, input().split()))
    rlt = 0
    cnt = 0
    a = 0
    for target in arr_B:
        # print(f'target:{target}')
        rlt = binary_search(arr_A, target, 0, N-1)
        # print(f"rlt:{rlt}")
        if rlt != 0:
            cnt += 1

    print(f'#{tc} {cnt}')