import sys

sys.stdin = open('input.txt')

T = int(input())

from pprint import pprint
# 빈 matrix에 색의 숫자를 채우고 중첩되면 색을 더하는 방식으로

for tc in range(1, T + 1):
    box_num = int(input())
    land = [[0] * 10 for _ in range(10)]                # 10x10 빈 매트릭스
    box_list = []
    cnt = 0
    for i in range(box_num):                            # box 크기와 색을 한 리스트에 받아온다.
        box_list += [list(map(int, input().split()))]
    # print(box_list)
    # print(box_list[0][1:4:2])

    for i in range(len(box_list)):                      # 박스 별 색칠
        for x in range(box_list[i][0], box_list[i][2] + 1):     # 행 변화
            for y in range(box_list[i][1], box_list[i][3] + 1): # 열 변화
                if land[x][y] != box_list[i][4]:                # 같은 색이 아니면 색칠
                    land[x][y] += box_list[i][4]

    for i in range(10):                                 # 겹쳐서 색칠 된 부분을 찾는다.
        for j in range(10):
            if land[i][j] == 3:                         # 1을 칠하고 2를 칠하면 겹치는 부분은 3이다.
                cnt += 1                                # 겹치는 부분 카운트
    # pprint(land)

    print(f'#{tc}', cnt)

