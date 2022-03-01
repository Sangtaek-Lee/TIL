import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    rlt = 0

    for row in range(1,N):          # 절단 row
        for col in range(1,N):      # 절단 col
            box1, box2, box3, box4 = 0, 0, 0, 0
            for i in range(N):      # 행
                for j in range(N):  # 열
                    if i < row and j < col:         # 좌상단
                        box1 += arr[i][j]
                    elif i >= row and j < col:      # 우상단
                        box2 += arr[i][j]
                    elif i < row and j >= col:      # 좌하단
                        box3 += arr[i][j]
                    elif i >= row and j >= col:     # 우하단
                        box4 += arr[i][j]

            if box1 == box2 == box3 == box4:
                # print(row, col)
                # print(box1, box2, box3, box4)
                rlt = 1

    print(f'#{tc} {rlt}')