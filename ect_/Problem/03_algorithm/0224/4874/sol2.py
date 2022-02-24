import sys

sys.stdin = open('input.txt')

T = int(input())

def forth(eq):
    stack = []                              # 계산을 위한 스택
    N = len(eq)
    i = 0                                   #
    while eq[i] != '.' :                    # . 이 나올 때 계산 끝난다.
        if eq[i].isdigit():                 # 숫자라면
            stack.append(int(eq[i]))        # stack에 정수로 push

        elif len(stack) > 1:                # 연산자라면, stack 2개 이상 숫자가 들어 있으면
            # print(stack, len(stack))
            p2 = stack.pop()                # 숫자 꺼낸다
            p1 = stack.pop()                # 숫자 꺼낸다
            if eq[i] == '+':                # + 연산
                stack.append(p1 + p2)
            elif eq[i] == '-':              # - 연산
                stack.append(p1 - p2)
            elif eq[i] == '*':              # * 연산
                stack.append(p1 * p2)
            elif eq[i] == '/':              # / 연산
                stack.append(p1 // p2)
        else:                               # 연산자인데 숫자가 1개 이하이면 error
            return 'error'
        i += 1

    if len(stack) == 1:                     # .을 만나 반복문 빠져나왔을 때 stack 값이 1개이면
        return stack[0]
    else:                                   # 2개 이상이면 error
        return 'error'

for tc in range(1, T + 1):
    eq = list(map(str, input().split()))
    rlt = forth(eq)
    print(f'#{tc} {rlt}')