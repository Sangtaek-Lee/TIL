import sys

sys.stdin = open('input.txt')

T = int(input())

def remove_s(s):
    stack = ''                          # 빈 문자열 스택
    for i in range(len(s)):             # 입력 하나씩 push
        stack += s[i]                   # i번째 입력 push
        if len(stack) > 1:              # 문자열이 2 이상일때만 검사
            if stack[len(stack)-1] == stack[len(stack)-2]:      # 끝에 두 문자가 같다면
                stack = stack[0:len(stack)-2]                   # 두문자 제외시킨다
    return stack                        # stack 값 리턴

for tc in range(1, T + 1):
    s = input()
    rlt = remove_s(s)
    s_length = len(rlt)
    print(f'#{tc} {s_length}')
