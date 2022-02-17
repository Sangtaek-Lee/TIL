import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    str1 = list(input())
    str2 = input()

    max_cnt = 0
    # 일단 str1 의 중복 제거 부터 하자
    # 먼저 나온 알파벳이 뒤에 있으면 0으로 바꿔준다.
    for i in range(len(str1)-1):
        for j in range(i+1,len(str1)):
            if str1[i] == str1[j]:
                str1[j] = 0
    # print(str1)

    # 각 알파벳 개수 카운트
    for i in range(len(str1)):
        cnt = 0
        for j in range(len(str2)):
            if str2[j] == str1[i]:
                # print(i,j)
                cnt += 1
        if max_cnt < cnt:           # max 값 찾기
            max_cnt = cnt

    print(f'#{tc}', max_cnt)

