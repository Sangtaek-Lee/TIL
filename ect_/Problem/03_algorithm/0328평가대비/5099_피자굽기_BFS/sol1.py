import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    pizza = [0] + list(map(int, input().split()))
    rlt = 0
    Q = []
    for i in range(N):
        Q.append(i)
    pizza_number = 0
    idx = N
    while Q:
        pizza_number = Q.pop(0)
        if pizza[pizza_number]//2 != 0:
            pizza[pizza_number] = pizza[pizza_number]//2
            Q.append(pizza_number)
        elif idx <= M:
            Q.append(idx)
            idx += 1

    rlt = pizza_number

    print(f'#{tc} {rlt}')