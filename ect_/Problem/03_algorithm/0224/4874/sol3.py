import sys

sys.stdin = open('input.txt')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    eq = list(input().split())
    stack = []
    result = 0

def forth(eq):
    rlt = 0
    for i in eq:
        if i == '.':
            if len(stack) == 1:
                break
            else:
                rlt = 'error'
                break
        if i.isdigit():  # 숫자는 스택에 넣기
            stack.append(int(i))
        else:
            try:
                if i == '+':
                    result = sum(stack[-2:])
                elif i == '-':
                    result = stack[-2] - stack[-1]
                elif i == '*':
                    result = stack[-2] * stack[-1]
                elif i == '/':
                    result = stack[-2] // stack[-1]
                stack[-2] = result
                stack.pop()
            except:
                print(f"#{test_case} error")
                break