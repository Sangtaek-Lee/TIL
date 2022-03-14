import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
d_list = [[1, 1],[1, -1],[-1, -1],[-1, 1]]
cnt_list = []
cnt = 0
arr_one = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            arr_one.append([i, j])
len = len(arr_one)
for n in range(len):
    b = 0
    while b < len:
        num = n % len
        i = arr_one[num][0]
        j = arr_one[num][1]
        if arr[i][j] == 1:
            a = 0
            for k in range(1, N):
                for d in d_list:
                    d_row = i + d[0]*k
                    d_col = j + d[1]*k
                    if 0 <= d_row <5 and 0 <= d_col <5:
                        if arr[d_row][d_col] == 2:
                            a += 1
            if a == 0:
                arr[i][j] = 2
                cnt += 1
        n += 1
        b += 1
    cnt_list.append(cnt)
print(max(cnt_list))
