import sys

sys.stdin = open('input.txt')

T = int(input())

def forth(eq):
    stack = []
    N = len(eq)


    for i in range(N-1):
        if eq[i].isdigit():
            stack.append(int(eq[i]))
        else:
            if len(stack) < 2:
                return 'error'
            else:
                p2 = stack.pop()
                p1 = stack.pop()
            if eq[i] == '+':
                stack.append(p1 + p2)
            elif eq[i] == '-':
                stack.append(p1 - p2)
            elif eq[i] == '*':
                stack.append(p1 * p2)
            elif eq[i] == '/':
                stack.append(p1 / p2)

    if len(stack) == 1:
        return stack.pop()
    else:
        return 'error'

for tc in range(1, T + 1):
    eq = list(map(str, input().split()))
    rlt = forth(eq)
    print(f'#{tc} {rlt}')