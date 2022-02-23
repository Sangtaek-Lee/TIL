import sys

sys.stdin = open('input.txt')

T = 10

def infix(N, exp):              # 후위 표기법으로
    operator = []               # 연산자 더할 stack
    rlt = ''                    # 후위표기법 나타낼 문자열

    for i in range(len(exp)):   # 한 글자씩 받아와 상황에 맞추어 계산하자.
        if exp[i] == '+':       # + 일때
            pass
        elif exp[i] == '*':     # * 일때
            pass
        else:   #숫자일때는
            rlt += exp[i]
    print(rlt)
        # print(int(equation[i]))
        # if equation[i]

def calculation(str):           # 후위 표기법 계산
    pass

for tc in range(1, T + 1):
    N = int(input())
    exp = list(input())
    rlt = infix(N, exp)
    print(f'#{tc} {rlt}')