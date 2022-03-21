import sys
sys.stdin = open('input.txt')

T = 10

def postorder(node):
    if node:
        postorder(tree[node][0])
        postorder(tree[node][1])
        val = tree[node][2]
        temp_list.append(val)
        if temp_list[-1] in ['+', '-', '*', '/']:
            c = temp_list.pop()
            b = int(temp_list.pop())
            a = int(temp_list.pop())
            if c == '+':
                rlt = a + b
                temp_list.append(rlt)
            elif c == '-':
                rlt = a - b
                temp_list.append(rlt)
            elif c == '/':
                rlt = a / b
                temp_list.append(rlt)
            else:
                rlt = a * b
                temp_list.append(rlt)

for tc in range(1, T + 1):
    N = int(input())
    tree = [[0, 0, 0] for _ in range(N+1)]
    temp_list = []
    for n in range(N):
        temp = list(input().split())
        if len(temp) == 2:
            tree[int(temp[0])][2] = temp[1]
        else:
            tree[int(temp[0])][0] = int(temp[2])
            tree[int(temp[0])][1] = int(temp[3])
            tree[int(temp[0])][2] = temp[1]
    postorder(1)
    rlt = int(temp_list[0])
    print(f'#{tc} {rlt}')