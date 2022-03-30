
def powerset(idx, N):
    if idx == N:
        sum_number = 0
        for i in range(10):
            if bit[i] != 0:
                sum_number += A[i]
        if sum_number == 10:
            for i in range(10):
                if bit[i] != 0:
                    print(A[i], end=' ')
            print()
        return
    else:
        bit[idx] = 0
        powerset(idx+1, N)
        bit[idx] = 1
        powerset(idx + 1, N)

A = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]           # 배열
N = len(A)              # 배열 길이
bit = [0] * N
powerset(0, N)
