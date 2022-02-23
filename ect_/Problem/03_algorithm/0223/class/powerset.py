
def powerset(idx, N):
    if idx == N:
        print(bit)
        return
    else:
        bit[idx] = 0
        powerset(idx+1, N)
        bit[idx] = 1
        powerset(idx + 1, N)


A = [1, 2, 3]           # 배열
N = len(A)              # 배열 길이
bit = [0] * N
powerset(0, N)