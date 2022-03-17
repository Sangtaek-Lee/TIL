#13
#1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

def pre_oder(v):
    if v:
        print(v)
        pre_oder(ch1[v])
        pre_oder(ch2[v])

V = int(input())
E = V-1
arr = list(map(int, input().split()))
ch1 = [0]*(V+1)
ch2 = [0]*(V+1)

for i in range(E):
    v1, v2 = arr[i*2], arr[i*2 + 1]
    if ch1[v1] == 0:
        ch1[v1] = v2
    else:
        ch2[v1] = v2

pre_oder(1)