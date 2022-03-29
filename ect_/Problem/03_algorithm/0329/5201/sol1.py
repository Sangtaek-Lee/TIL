import sys
sys.stdin = open('input.txt')

T = int(input())

def wt():
    rlt = 0
    i = 0
    for t in T:                 # Truck 앞에서 부터 넣을 수 있는 값 찾을 거다
        while i < len(W):       # Truck 값 하나 당 배열 전체를 최대 1번만 돌거다. 내림차순 정렬이므로 앞에서 부터 찾으면 된다.
            if t >= W[i]:       # Truck 값이 컨테이너 무게 보다 크다면
                rlt += W[i]     # 결과 값에 더해 주고
                i += 1          # 인덱스는 한칸 앞으로
                break           # 다음 트럭으로 넘어가자
            i += 1              # 만족 값을 못 찾았다면 다음 값으로 넘어 가자
    return rlt

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    T = list(map(int, input().split()))
    W.sort(reverse=True)                    # 내림차순 정렬
    T.sort(reverse=True)                    # 내림차순 정렬
    rlt = wt()

    print(f'#{tc} {rlt}')