import sys
sys.stdin = open('input.txt')

def infix(equation):
    l = len(equation)
    stack = []
    for i in range(l):
        if equation[i] == '+' or equation[i] == '-' or equation[i] == '*' or equation[i] == '/':
            stack.append(equation[i])
        else:
            print(equation[i], end='')
    for i in range(len(stack)-1,-1,-1):
        if stack[i]:
            print(stack.pop(),end='')

T = int(input())

for tc in range(1, T + 1):
    in_eq = list(input())
    # print(in_eq)
    print(f'#{tc} ', end='')
    rlt = infix(in_eq)
    print()
