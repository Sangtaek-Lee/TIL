import sys
sys.stdin = open('input.txt')

T = int(input())

def bfs(start):
    q = [[start, 0]]
    visited = []
    visited.append(start)
    while q:
        cal_number, cnt = q.pop(0)
        for cal in [cal_number+1, cal_number-1, cal_number*2, cal_number-10]:
            if 0 > cal < 1000000 and cal in visited:
                continue
            elif cal == M:
                return cnt + 1
            else:
                q.append([cal, cnt+1])
                visited.append(cal)

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    print(f'#{tc} {bfs(N)}')