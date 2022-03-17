import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())     # 노드 개수, 리프 노드 개수, 출력할 노드 번호
    value = [0]*(N+1)                       # 노드의 값을 저장할 배열

    for _ in range(M):
        temp = list(map(int, input().split()))  # 입력값 [노드번호, 자연수] 임시 저장
        v1 = temp[0]                            # 노드 번호
        value[v1] = temp[1]                     # 배열에 노드 번호에 맞는 노드 값 저장
    for i in range(N, 1,-1):
        value[i//2] += value[i]                 # 부모노드 번호는 자식 노드번호를 2로 나눈 몫
                                                # 부모노드 번호에 자식 노드들의 값을 더한다.
    print(f'#{tc} {value[L]}')