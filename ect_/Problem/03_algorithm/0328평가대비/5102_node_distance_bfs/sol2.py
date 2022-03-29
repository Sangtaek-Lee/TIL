import sys

sys.stdin = open('input.txt')


def bfs(v):
    Q = []
    Q.append(v)

    # 방문 했어요 표시
    visited[v] = 1

    while Q:
        w = Q.pop(0)  # 다음 나오세요

        for i in range(V + 1):
            if field[w][i] == 1 and visited[i] == 0:
                Q.append(i)  # 연결된 다음 번호 큐에 넣기

                # 이전 방문 정보에 +1 == 이동한 거리
                visited[i] = visited[w] + 1

    if visited[G]:
        return visited[G] - 1
    else:
        return visited[G]


T = int(input())
for tc in range(1, T + 1):

    V, E = map(int, input().split())
    line = [(list(map(int, input().split()))) for _ in range(E)]
    S, G = map(int, input().split())

    # print(line)

    # 방문 정보
    visited = [0] * (V + 1)

    # 인접 행렬 만들기
    # 0으로 초기화된 인접 행렬
    field = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
    # 연결된 곳 1로 만들기
    for each in line:
        start = each[0]
        end = each[1]

        field[start][end] = 1
        field[end][start] = 1

    rlt = bfs(S)
    print(f'#{tc} {rlt}')