import sys
sys.stdin = open('input.txt')

T = int(input())

def preorder(node):                 #preoder로 방문하여 노드 수를 셀 것
    global cnt                      # global로 cnt 변수 수정
    if node:                        # 값이 있는지
        cnt += 1                    # Visit
        preorder(tree[node][0])     # Left
        preorder(tree[node][1])     # Right

for tc in range(1, T + 1):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))
    V = E + 1
    tree = [[0]*2 for _ in range(V+1)]      # [왼쪽자식, 오른쪽자식] * 1~V 까지 idx
    cnt = 0                                 # node 개수 셀 cnt

    for i in range(0,len(edges)-1,2):       # edge의 수 만큼 반복 입력이 부모, 자식 순이므로 idx 2씩 증가 하도록
        v1 = edges[i]                       # 부모 노드
        v2 = edges[i+1]                     # 자식 노드
        if tree[v1][0] == 0:                # 왼쪽 자식 노드 값이 없다면
            tree[v1][0] = v2                # 왼쪽에 값 저장
        else:                               # 왼쪽에 값이 있다면
            tree[v1][1] = v2                # 오른쪽에 저장
    preorder(N)
    print(f'#{tc} {cnt}')