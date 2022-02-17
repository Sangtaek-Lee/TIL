import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    p = input()
    t = input()
    rlt = 0
    for i in range(len(t)-len(p)):          # 인덱스를 늘려 가며
        temp_str = t[i:i+len(p)]            # 정해진 길이만큼 슬라이싱해서
        if p == temp_str:                   # 문자열 단위로 비교
            rlt = 1

    print(f'#{tc}', rlt)

