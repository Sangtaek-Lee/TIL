result = "6528-*2/+"
stack = []

for token in result:
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

ans = stack.pop()
print(ans)