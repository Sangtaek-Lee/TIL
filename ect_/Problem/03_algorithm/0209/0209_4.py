import sys
sys.stdin = open('input_4.txt')

T = int(input())                        # Test case 선언

for tc in range(1, T + 1):              # case 하나씩 진행

    num = int(input())                  # input 값 선언
    c = [0] * 12                        # 각 정수의 개수를 카운트 할 리스트 생성, run 조건에 대한 index Error 방지 12 칸
    for i in range(6):                  # 0 ~ 9 각 개수를 카운트 한다.
        c[num % 10] += 1                # 예시) input 값 111456을 10으로 나눈 나머지인 6을 인덱스로 c 리스트에 카운트 1 증가
        num //= 10                      # 1의 자리를 10으로 나눈 몫으로 제거


    i = 0                               # while 문을 제어하기 위한 i선언
    tri = run = 0                       # triplet과 run 개수를 세기 위해 선언언
    while i < 10:                       # 0~9 까지 c 리스트의 인덱스를 증가 시켜가며 triplet과 run 조건을 검사하기 위한 반복문
        if c[i] >= 3:                   # triplet 조건 : 중복 값이 3개 이상일 때,
            c[i] -= 3                   # cnt 값 3개 제거
            tri += 1                    # triplet 1 카운트
            continue                    # triplet이 중복 될 수 있으므로 continue를 통해 index 유지 후 조건 재 검사
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:       # run 조건 : 연속되는 인덱스에 값이 존재하는지 and로 조건문
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1                 # 연속되는 카운트 값 하나씩 제거
            run += 1                    # run 값 1 카운트
            continue                    # run 또한 중복 될 수 있으므로 continue 사용 index 유지
        i += 1                          # 첫번째 인덱스 값 검사 후 다음 인덱스로 넘어간다.

    if run + tri == 2:                  # baby gin 경우의 수 (2,0),(1,1),(0,2) 조건을 만족하는지 조건문
        print(f'#{tc} 1')               # 만족할 시 #tc_number 1 출력
    else:
        print(f'#{tc} 0')               # 불만족 시 #tc_number 0 출력

## 이문제는 수업 중 이미 들은 내용이라 생각하는게 제한적이였다...