import sys

sys.stdin = open('input.txt')


def pizza(N, M, arr):
    # 화덕 준비
    Q = []
    # 화덕의 크기만큼 피자를 채워요 (N개만큼 채울 수 있음)
    for i in range(1, N + 1):
        Q.append(i)
    print(Q)
    idx = N + 1  # 이 다음에 들어갈 피자 번호
    pizza_num = 0  # 피자 번호가 저장될 곳

    # 화덕에 피자가 있는 동안 반복
    while Q:
        # 화뎍에서 가장 앞에 있는 피자를 꺼내요 ( 가장 앞 = 입구에 있는 피자)
        pizza_num = Q.pop(0)

        # 1. 지금 꺼낸 피자에 치즈가 남았으면
        if arr[pizza_num] // 2 != 0:
            # 치즈 녹여요
            arr[pizza_num] //= 2
            # 다시 화덕의 맨 뒤에 넣어요
            Q.append(pizza_num)

        # 2. 더 들어갈 피자가 있으면
        elif idx <= M:
            # 이거 화덕에 넣자
            Q.append(idx)
            # 다음 피자 준비
            idx += 1

    return pizza_num


T = int(input())
for tc in range(1, T + 1):

    # N : 화덕의 크기, M : 피자 개수
    N, M = map(int, input().split())
    arr = [0] + list(map(int, input().split()))

    rlt = pizza(N, M, arr)
    print(f'#{tc} {rlt}')