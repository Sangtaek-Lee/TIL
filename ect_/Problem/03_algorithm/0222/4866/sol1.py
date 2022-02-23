import sys

sys.stdin = open('input.txt')

T = int(input())

def check(S):
    tmp_l = []                          # stack list
    for i in range(len(S)):             # 문자열 전체 검사
        if S[i] == '(' or S[i] == '{':  # 여는 괄호 면 push
            tmp_l.append(S[i])
        elif S[i] == '}':               # 닫는괄호 } 면 pop
            if len(tmp_l) != 0 and tmp_l[len(tmp_l)-1] == '{':
                tmp_l.pop()
            else:                       # 닫는 괄호 } 지만 스택이 비어 있거나 top 값이 {가 아니면 false
                return 0
        elif S[i] == ')':               # 닫는괄호 ) 면 pop
            if len(tmp_l) != 0 and tmp_l[len(tmp_l)-1] == '(':
                tmp_l.pop()
            else:                       # 닫는 괄호 ) 지만 스택이 비어 있거나 top 값이 {가 아니면 false
                return 0
    if len(tmp_l) != 0:                 # 스택이 비어있지 않으면 false
        return 0
    else:                               # 아니라면 True
        return 1

for tc in range(1, T + 1):
    S = input()
    rlt = check(S)
    print(f'#{tc} {rlt}')

