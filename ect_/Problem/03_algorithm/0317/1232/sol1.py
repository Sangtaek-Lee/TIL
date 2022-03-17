import sys
sys.stdin = open('input.txt')

T = 10

def inorder(node):
    if node:
        inorder(tree[node][0])
        val = tree[node][2]
        temp_list.append(val)
        if len(temp_list) == 3:
            a = int(temp_list[0])
            b = int(temp_list[2])
            c = temp_list[1]
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
        inorder(tree[node][1])


for tc in range(1, T + 1):
    N = int(input())                #정점의 개수 v
    # 정점번호, 해당 양의 정수
    # 정점이 연산자이면 정점번호, 연산자, 해당 정점의 왼쪽 자식, 오른쪽 자식의 정점번호
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
    inorder(1)
    print(temp_list)

    print(f'#{tc}')