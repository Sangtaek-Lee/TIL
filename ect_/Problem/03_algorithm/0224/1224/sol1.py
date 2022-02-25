import sys

sys.stdin = open('input.txt')

T = 10

def infix(infix):
    stack = []                              # 연산자를 담을 스택
    result = []                             # 결과를 담을 리스트
    for token in infix:                     # 중위 표현식을 순회하며 숫자, 연사자 별 조건
        if token.isdigit():                 # 숫자일때, 결과에 push
            result.append(token)
        else:                               # 연산자일때,
            if not stack:                   # 스택이 비여있다면
                stack.append(token)         # 스택에 연산자 push
            else:                           # 스택이 비어있지 않다면 (icp 들어올 연산자의 운선순위, isp 들어있는 연산자 우선순위 비교)
                if token == "(":            # ( icp 우선순위는 3
                    stack.append(token)     # 무조건 stack 에 push
                elif token == ")":          # ) 일때, stack 안에 있는 연산자를 ( 가 나올때 까지 result 에 추가한다.
                    temp = stack.pop()      # stack 에서 하나를 꺼내서
                    while temp != "(":      # 닫는 괄호가 나올때 까지
                        result.append(temp) # result 에 추가한다.
                        temp = stack.pop()  # ( 가 나올때 까지 pop 하다 ( 이 나오게 되면 stack에서 제거되면서 while 문 중단
                # icp == 2
                elif token == "*":          # icp가 2인 *, / 는 조건문 순서에 따라 우선순위 선정
                    while stack and stack[-1] == "*":   # stack 이 비어 있지 않고 stack 의 top 값이 * 또는 / 일때까지 연산자를 result 에 추가한다.
                        result.append(stack.pop())      # stack에서 pop하여 result에 추가
                    stack.append(token)                 # stack에 추가한다
                # icp == 1
                elif token == "+":          # icp가 1인 +, - 는 조건문 순서에 따라 우선순위 선정
                    while stack and stack[-1] != "(":   # stack 이 비어 있지 않고 stack 의 top 값이 ( 일 때 까지 stack에서 pop 하여 result에 추가한다.
                        result.append(stack.pop())      #
                    stack.append(token)                 # stack 에 token 추가한다

    for token in range(len(stack)):                     # stack에 남아있다면, 모두 꺼내서 push
        result.append(stack.pop())

    return ''.join(result)                              # 계산을 위해 str으로 리턴

def cal(A):
    stack = []
    for token in A:
        if token.isdecimal():
            stack.append(int(token))

        else:  # 연산자를 만난경우
            p2 = stack.pop()
            p1 = stack.pop()

            if token == "+":
                rlt = p1 + p2
                stack.append(rlt)
            elif token == "-":
                rlt = p1 - p2
                stack.append(rlt)
            elif token == "*":
                rlt = p1 * p2
                stack.append(rlt)
            elif token == "/":
                rlt = p1 / p2
                stack.append(rlt)

    return stack.pop()

for tc in range(1, T + 1):
    N = int(input())
    X = input()
    A = infix(X)
    B = cal(A)

    print(f'#{tc} {B}')

