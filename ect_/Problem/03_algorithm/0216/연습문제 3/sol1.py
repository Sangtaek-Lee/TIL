import sys

sys.stdin = open('input.txt', encoding='utf-8')

T = 10


for tc in range(1, T + 1):
    case_num = int(input())
    p = input()
    t = input()
    i = 0
    j = 0
    cnt = 0

    while i < len(t) - len(p) + 2:         # 검색을 p의 길이에서 t르 뺀만큼만 수행할 것이다.
        if t[i] == p[j]:                # 같다면
            i += 1
            j += 1
            if j == len(p):
                i = i - (j - 1)
                j = 0
                cnt += 1
        elif t[i] != p[j]:
            i = i - (j - 1)
            j = 0

    print(f'#{tc}', cnt)

