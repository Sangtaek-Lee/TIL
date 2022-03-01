import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    l = [list(map(int, input().split())) for _ in range(3)]
    cnt_l = [0]*1001
    max_val = 0
    for i in range(N):
        A = l[i][1]
        B = l[i][2]
        if l[i][0] == 1:
            for j in range(A, B+1):
                cnt_l[j] += 1
            print(cnt_l)
        elif l[i][0] == 2:
            cnt_l[B] += 1
            k = 0
            while A+k < B:
                cnt_l[A+k] += 1
                k += 2
            print(cnt_l)
        else:
            cnt_l[A] += 1
            cnt_l[B] += 1
            k = 1
            while k < B:
                if A % 2 == 0 and A < 4*k < B:
                    cnt_l[4*k] += 1
                else:
                    if A + 3*k % 10 != 0 and A < 3*k < B:
                        cnt_l[3*k] += 1
                k += 1
            print(cnt_l)

        for i in range(1001):
            if max_val < cnt_l[i]:
                max_val = cnt_l[i]

    print(f'#{tc} {max_val}')