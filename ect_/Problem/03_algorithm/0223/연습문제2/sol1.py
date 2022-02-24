def powerset(idx, N, t):
    global cnt
    cnt += 1
    if idx == N:
        s = 0
        for j in range(N):
            if bit[j]:
                s += lst[j]

        if s == t:
            for j in range(N):
                if bit[j]:
                    print(lst[j], end=' ')
            print()


    else:
        bit[idx] = 0
        powerset(idx+1, N, t)
        bit[idx] = 1
        powerset(idx + 1, N, t)


lst = [x for x in range(1, 11)]
N = len(lst)              # 배열 길이
bit = [0] * N
s = 0
t = 10
cnt = 0
powerset(0, N, t)
print(cnt)