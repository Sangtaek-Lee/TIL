import sys
sys.stdin = open('input.txt')

T = int(input())

def postorder(node):
    if node:
        preorder(tree[node][0])
        preorder(tree[node][1])
        cnt += 1

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())     # 노드 개수, 리프 노드 개수, 출력할 노드 번호
    value = [0]*(N+1)                       # 노드의 값을 저장할 배열
    temp = [list(map(int, input().split())) for _ in range(M)]  # 입력값 [노드번호, 자연수] 임시 저장
    tree = [0]*(N+1)
    for i in range(1, N+1):
        tree[i] = [i*2, i*2 + 1]
    print(temp)

    print(f'#{tc} {value[L]}')