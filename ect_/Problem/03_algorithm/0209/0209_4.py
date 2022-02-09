import sys
sys.stdin = open('input_4.txt')

T = int(input())

for tc in range(1, T + 1):

    num = int(input())
    c = [0] * 12  # run 조건에 대한 index Error 방지 12 칸
    for i in range(6):
        c[num % 10] += 1
        num //= 10


    i = 0
    tri = run = 0
    while i < 10:                                           # 0~9 까지 triplet과 run 조건을 검사하기 위한 반복문
        if c[i] >= 3:                                       # triplet 조건
            c[i] -= 3
            tri += 1
            continue
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:       # run 조건
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            run += 1
            continue
        i += 1

    if run + tri == 2:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')

