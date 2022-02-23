import sys

sys.stdin = open('input.txt')

T = 10

def infix(N, equation):
    operator = []
    rlt = ''
    icp = {'+': 1, '*': 2, '(': 3}
    isp = {'(': 0, '+': 1, '*': 2}

    for i in range(len(equation)):
        if equation[i] == '+':
            pass
        elif equation[i] == '*':
            pass
        else:   #숫자
            rlt += equation[i]
    print(rlt)
        # print(int(equation[i]))
        # if equation[i]





for tc in range(1, T + 1):
    N = int(input())
    in_eq = list(input())
    rlt = infix(N, in_eq)
    print(f'#{tc} {rlt}')

