import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    atom = [list(map(int, input().split())) for _ in range(n)]
    d = [(0, 0.5), (0, -0.5), (-0.5, 0), (0.5, 0)]
    result = 0

    while len(atom) >= 2:
        location = {}
        atom = []
        for i in range(len(atom)):
            atom[i][0] = atom[i][0] + d[atom[i][2]][0]
            atom[i][1] = atom[i][1] + d[atom[i][2]][1]
        for a in atom:
            try:
                location[(a[0], a[1])].append(a)
            except Exception:
                location[(a[0], a[1])] = [a]
        for l in location:
            if len(location[l]) >= 2:
                for at in location[l]:
                    result += at[3]
            else:
                if -1000 <= location[l][0][0] <= 1000 and -1000 <= location[l][0][1] <= 1000:
                    atom.append(location[l][0])

    print(f'#{tc} {result}')


