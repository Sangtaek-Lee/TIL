import sys
sys.stdin = open('input.txt')

TC = 10

def in_order(v):                    # 중위순회
    if v:                           # 비어있는 값인지 확인
        in_order(ch1[v])            # 왼쪽 먼저 방문
        print(word[v], end='')      # 현재 값 출력
        in_order(ch2[v])            # 오른쪽 방문

for tc in range(1, TC + 1):
    V = int(input())
    E = V - 1
    word = [0]*(V+1)                # 알파벳 담을 배열
    ch1 =[0]*(V+1)                  # 왼쪽 자식
    ch2 =[0]*(V+1)                  # 오른쪽 자식
    for i in range(V):
        tmp = list(input().split()) # 입력값을 받아와
        v1 = int(tmp[0])            # 첫번째 값은 부모 노드이거
        word[v1] = tmp[1]           # 두번째 값은 부모 노드의 값
        if len(tmp) == 3:           # 만약 3번째 값이 있다면 왼쪽 자식이 있다는 거
            ch1[v1] = int(tmp[2])   # 부모의 인덱스 값에 왼쪽 자식 을 써준다
        elif len(tmp) == 4:         # 만약 4번째 값이 있다면 오른쪽 자식이 있다는 거
            ch1[v1] = int(tmp[2])   # 왼쪽
            ch2[v1] = int(tmp[3])   # 오른쪽 써준다.

    print(f'#{tc} ', end='')        # 출력
    in_order(1)
    print()