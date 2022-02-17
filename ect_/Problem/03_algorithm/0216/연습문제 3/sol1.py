import sys

sys.stdin = open('input.txt', encoding='utf-8')

T = 10


for tc in range(1, T + 1):
    case_num = int(input())
    p = input()                             # 검사용  
    t = input()                             # 텍스트
    i = 0                                   # 텍스트의 인덱스로 사용
    j = 0                                   # 검사용의 인덱스로 사용
    cnt = 0                                 # 일치하는 개수

    while i < len(t) - len(p) + 2:          # 텍스트 길이에서 검사용 길이만큼 뺀 값을 돌면 종료
        if t[i] == p[j]:                    # 같다면
            i += 1                          # 다음 알파벳 검사
            j += 1                          # 다음 알파벳 검사
            if j == len(p):                 # 검사용 텍스트를 다 검사하여서 일치하게 된다면
                i = i - (j - 1)             # i는 검사를 처음 시작한 인덱스에서 1만큼 증가한 위치로 다시 돌아가고
                j = 0                       # j는 0으로 초기화
                cnt += 1                    # 카운트 해준다.
        elif t[i] != p[j]:                  # 만약 다르다면
            i = i - (j - 1)                 # i는 검사를 시작한 인데스에서 1만큼 증가한 위치로 간다.
            j = 0                           # j는 0으로 초기화

    print(f'#{tc}', cnt)
