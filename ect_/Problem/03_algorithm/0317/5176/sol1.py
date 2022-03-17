import sys
sys.stdin = open('input.txt')

T = int(input())

def inorder(node):                  # inorder 방식으로 값을 1씩 증가 시키며 값을 써줄거다.
    global num                      # 변수 num을 global 지정
    if node:                        # node 값이 있는지 있다면
        inorder(tree[node][0])      # 왼쪽 자식
        value[node] = num           # value idx가 node 번호에 num 값을 써준다
        num += 1                    # num 값 1 증가
        inorder(tree[node][1])      # 오른쪽 자식

for tc in range(1, T + 1):
    N = int(input())                        # 완전 이진 트리 = 1~N까지 key 값은 node 의 번호
    tree = [[0]*2 for _ in range(N+1)]      # [왼쪽, 오른쪽] 자식을 담을 tree 배열
    value = [0]*(N+1)                       # node의 번호를 idx 로 하여 key 값을 담을 배열
    num = 1                                 # 1 ~ N 까지 증가시킬 변수
    for i in range(1, N):                   # 완전 이진 트리의 node 번호를 만들어 줌
        j = (i+1) // 2                      # 부모는 2개의 자식을 가질 수 있으므로
        if (i+1) % 2 == 0:                  # 나머지가 0이면 왼쪽 자식
            tree[j][0] = j*2                # j 노드의 왼쪽 자식 번호 저장
        else:                               # 나머지가 1이면 오른쪽 자식
            tree[j][1] = j*2+1              # j 노드의 오른쪽 자식 번호 저장
    inorder(1)                              # inorder 방식으로 값을 써준다.
    print(f'#{tc} {value[1]} {value[N//2]}')# 1번 노드는 root 노드, N//2 노드 값 출력