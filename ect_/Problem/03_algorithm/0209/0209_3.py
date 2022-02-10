import sys
sys.stdin = open('input_3.txt')

T = int(input())                                    # Test Case 선언
for tc in range(1, T+1):                            # Case 별 진행
    columns = int(input())                          # 열의 개수를 받아옴
    row_val_list = list(map(int, input().split()))  # 칸 당 상자의 개수를 리스트로 받아옴
    # print(row, columns)                           #
    # a = 0
    max_drop = 0                                    # 최대값 초기값 선언
    i = 0                                           # 계산 진행 했던 열을 제외하기 위한 인덱스 선언
    for row in row_val_list:                        # 비교 기준이 되는 상자 값을 받아오기 위한 for
        cnt = 0                                     # 카운트 값 선언 및 초기화
        for col in range(i+1, columns):             # 빈 칸을 카운트 하기 위한 반복 문 인덱스 1~8, 2~8, 3~8, ... 진행
            if row > row_val_list[col]:             # 현재 열의 상자 값과 다음 열들의 상자 값을 비교하여 현재 열이 크다면
                cnt += 1                            # 카운트 1 증가
        i += 1                                      # 계산 진행된 열 제외 위한 인덱스 +1
        if cnt > max_drop:                          # 낙차가 가장 큰 값을 찾기 위한 조건 문
            max_drop = cnt
    print(f'#{tc}', max_drop)                       # 결과 출력









    # print(f'#{i} ')


