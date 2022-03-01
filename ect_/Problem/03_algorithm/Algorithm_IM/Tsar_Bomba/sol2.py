import sys

sys.stdin = open('input.txt')

# IM 차르봄바 정답 예시 코드
T = int(input())

for tc in range(1, T+1):
    N,P = map(int, input().split())
    base = [list(map(int, input().split())) for i in range(N)]

    virus = 0
    for i in range(N):
        for j in range(N):
            row, cro = base[i][j], base[i][j]
            for k in range(-P, P+1):
                if k:
                    if 0 <= i+k < N:
                        row += base[i+k][j]
                        if 0 <= j+k < N:
                            cro += base[i+k][j+k]
                        if 0 <= j-k < N:
                            cro += base[i+k][j-k]
                    if 0 <= j+k < N:
                        row += base[i][j+k]
            if not virus or virus < max(row, cro):
                virus = max(row, cro)
    print('#{} {}'.format(tc, virus))