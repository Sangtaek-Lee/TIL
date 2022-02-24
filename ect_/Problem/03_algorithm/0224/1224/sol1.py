import sys

sys.stdin = open('input.txt')

T = 10



def infix(infix):
    stack = []  # 변환을 위해 사용할 스택
    result = []  # 결과가 담길 스택
    # 1. 중위 표현식을 순회
    for token in infix:
        # 2. 만약에, 너 숫자면 결과에 push
        if token.isdigit():
            result.append(token)
        else:  # 연산자라면
            if not stack:  # 스택이 비어있다면
                stack.append(token)
            else:  # 스택이 비어있지 않다면(icp, isp 비교후 push)
                # icp == 3
                if token == "(":
                    stack.append(token)
                elif token == ")":
                    temp = stack.pop()
                    while temp != "(":
                        result.append(temp)
                        temp = stack.pop()
                # icp == 2
                elif token == "*":
                    while stack and stack[-1] == "*":
                        result.append(stack.pop())
                    stack.append(token)
                # icp == 1
                elif token == "+":
                    while stack and stack[-1] != "(":
                        result.append(stack.pop())
                    stack.append(token)

    # stack에 남아있다면, 모두 꺼내서 push
    for token in range(len(stack)):
        result.append(stack.pop())


    return stack

def cal(stack):
    stack = []

    for token in stack:
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
    # print(X)
    print(f'#{tc} ', cal(infix(X)))

