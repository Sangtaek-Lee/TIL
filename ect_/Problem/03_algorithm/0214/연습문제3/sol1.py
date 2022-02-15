import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())                                # 행열
    limit = N*N                                     # 반복문 제어를 위한 limit
    matrix = [[0]*N for _ in range(N)]              # 빈 matrix
    # matrix[0][0] = 1
    num = 1                                         # 1 부터 시작 이므로 1로 선언
    row = 0                                         # 행
    col = -1                                        # 열 반복문 시잓 시 col + 1을 하고 시작하여 -1로 선언

   while num <= limit:                              # 우하좌상 칸수만큼 반복 되게 N*N 을 조건으로 둠
        for right in range(N):                      # 오른쪽 방향으로 이동
            # print(row, col)
            col += 1                                # 오른쪽으로 1칸 옮긴 후
            matrix[row][col] = num                  # 값을 채운다.
            num += 1                                # 다음 채울 값을 위해 num +1
        N -= 1                                      # 제일 윗행을 채웠으므로 행 하나 지워준다.
        for down in range(N):                       # 아래 바향으로 이동
            row += 1                                # 아래 방향으로 1칸 옮긴 후
            matrix[row][col] = num                  # 값을 채운다.
            num += 1                                # 다음 채울 값을 위해 num + 1
                                                    # 이미 위에서 행값을 하나 지워져 있기에 이를 그대로 사용한다. (행열 값 공용 사용)
        for left in range(N):                       # 왼쪽 방향으로 이동
            col -= 1                                # 왼쪽으로 한칸 옮긴 후
            matrix[row][col] = num                  # 값을  채운다.
            num += 1                                # 다음 채울 값을 위해 num + 1
        N -= 1                                      # 아리 행 값이 채워졌으므로 행 하나 지운다.
        for up in range(N):                         # 윗방향으로 이동
            row -= 1                                # 위로 한칸 옮긴 후
            matrix[row][col] = num                  # 값 채우기
            num += 1                                # 다음 값
    # print(matrix)
    print(f'#{tc} ')
    for i in range(len(matrix)):                    # matrix를 주어진 출력 형태로 출력하기 위한 반복문
        for j in range(len(matrix)):
            print(matrix[i][j], end=' ')
        print()