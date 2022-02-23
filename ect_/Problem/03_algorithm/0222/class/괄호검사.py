A = '()()((()))((()((((()()((()())((())))))'
len_A = len(A)
stack = []
top = -1
rlt = True
for i in range(len_A):
    if A[i] == '(':
        stack.append(A[i])
        top += 1
    else:
        if top == -1:
            rlt = False
        stack.pop()
        top -= 1
if top != -1:
    rlt = False
print(stack)
print(rlt)
# ((((