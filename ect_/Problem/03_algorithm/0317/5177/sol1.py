import sys
sys.stdin = open('input.txt')

T = int(input())
# 노드를 새로 만들고 만들어진 노드들을 최소 힙을 만족하도록 다시 정렬하는 방법
def enq(n):                 # 노드를 추가 시켜 줄거다
    global last             # last 변수 global 지정
    last += 1               # last 1 증가
    tree[last] = n          # tree의 last 번호 node에 현 재 들어온 값을 써준다
    c = last                # 자식 번호를 last로
    p = c//2                # 부모 번호를 last//2 로
    while p > 0 and tree[p] > tree[c]:      # p 가 root가 아니면서, 최소 힙 만족을 위해 (부모 노드 값이 더 크면 while 실행)
        tree[p], tree[c] = tree[c], tree[p] # 부모 값과 자식 값을 바꿔 준다.
        c = p                               # 조상 노드를 순차적으로 실행하기 위해 부모 노드 번호를 자식으로
        p = c//2                            # 변경 된 자식 노드 번호로 부모 노드 번호를 찾는다

for tc in range(1, T + 1):
    N = int(input())                            # 완전 이진 트리 = 노드 개수
    last = 0                                    # 마지막 노드의 번호, 노드를 처음부터 생성하여 채워갈 것이기에 last = 0
    tree = [0]*(N+1)                            # tree 값 배열
    for n in list(map(int,input().split())):    # 주어진 정수 입력 받아 enq 반복
        enq(n)                                  # 새로운 노드를 생성하고 최소 힙으로 정렬 해 줄 함수

    idx = N                 # 마지막 노드의 번호
    rlt = 0                 # 합을 담기 위한 변수
    while idx > 0:          # 조상 노드 합을 구하기 위해 부모 노드 번호가 0이 되게 되면 종료
        idx = idx // 2      # 부모 노드의 번호
        rlt += tree[idx]    # 부모 노드의 결과 값을 더한다

    print(f'#{tc} {rlt}')