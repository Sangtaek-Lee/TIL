def permutation(i, N):              # i는 시작 N 은 끝
    if len(temp) == 7:
        return print(temp)
    if i >= N:
        return
    else:
        print(i)
        temp.append(A[i])
        permutation(i+1, N)
        temp.pop()
        permutation(i+1, N)

A = [7, 5, 9, 7, 5, 9, 5, 4, 0, 2, 8, 7]
temp = []
N = len(A)
Permutation(0, N)