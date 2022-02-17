import sys

sys.stdin = open('input.txt')

T = int(input())

# 처음 시도 한 방법은 레퍼런스 리스트를 만들고 그걸 기준으로 숫자로 만들었다 다시 문자로 만드는 과정을 하였는데 시간이 오래 소요되어 아래 방법을 하게 됨
# 레퍼런스를 만들고 레퍼런스의 인덱스와 문자값은 동일한 의미를 가지므로 동일한 문자가 몇번있는지를 카운트한다.
for tc in range(1, T + 1):
    case_num = input()
    num_list = list(input().split())
    ref_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]   # 레퍼런스 선언
    cnt_list = [0]*10                           # 입력값 중 각 문자가 몇개 있는지 세기 위한 빈 리스트
    for i in range(len(num_list)):              # 반복문을 통해 레퍼런스와 입력 리스트를 비교 해 각 자리에 개수를 카운트한다.
        for j in range(len(ref_list)):
            if num_list[i] == ref_list[j]:
                cnt_list[j] += 1

    print(f'#{tc}')
    for i in range(len(cnt_list)):              # 출력할 숫자의 개수를 가지고 있으므로 바로 출력한다.
        for cnt in range(cnt_list[i]):
            print(ref_list[i], end=' ')
    print()

