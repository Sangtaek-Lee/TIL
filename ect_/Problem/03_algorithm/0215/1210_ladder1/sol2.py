import sys

sys.stdin = open('input.txt')

T = 10


for tc in range(1, T + 1):
    tc_num = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    row = 99
    # 하단 2값 위치 찾기
    for i in range(100):
        if matrix[row][i] == 2:
            col = i
            break

    # 상, 하 좌 우 중 하나의 값이 1 이면 그쪽으로 이동 (상, 하, 좌, 우 우선순위를 둔다)
    while row > 0:                      # row 가 0이면 도착 결과 도출된다.

        if matrix[row-1][col] == 1:     # 상단이 1이면 한칸 위로
            row -= 1

        while col > 0 and matrix[row][col-1] == 1:  # 좌측이 1이면 0이나올때 까지 쭉간다.
            col -= 1
            if matrix[row][col-1] == 0:             # 쭉 가다 0 만나면
                row -= 1                            # 한칸 위로 보내준다. 밑에 우측 반복문 만나서 다시 오른쪽으로 갈 수 있기 때문에

        while col < 99 and matrix[row][col+1] == 1: # 우측이 1이면 0이 나올때 까지 쭉 간다.
            col += 1                                # 위로 가서 상단으로 올라가는 조건문 만날거기에 한칸 위로 안 보내 줘도 된다.

    print(f'#{tc}', col)

